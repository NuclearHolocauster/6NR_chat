from sqlalchemy.future import select
from fastapi import WebSocket, WebSocketDisconnect

from models import Message
from services import SqlService
from schemas.message import MessageListResponseScheme
from mappers.message_mapper import message_data_to_message_scheme_mapper


class ChatService:
    
    def __init__(
        self, 
        sql_service: SqlService,
        websocket_service: WebSocket
    ) -> None:
        self.__sql_service = sql_service
        self.__websocket_service = websocket_service

    async def broadcast(self, client_id, websocket: WebSocket) -> None:
        await self.__websocket_service.create_connetion(websocket)
        try:
            while True:
                data = await websocket.receive_text()
                await self.__websocket_service.broadcast(f'Client #{client_id} -> {data}')
                await self.__sql_service.insert_one(Message(text=data, user_id=str(client_id)))
        except WebSocketDisconnect:
            await self.__websocket_service.disconnect(websocket)
    
    async def get_chat_history(self):
        chat_history_query = select(Message)
        result = await self.__sql_service.execute(chat_history_query)
        result = result.scalars().all()

        return MessageListResponseScheme(
            messages=[
                message_data_to_message_scheme_mapper(message)
                for message in result
            ]
        )
