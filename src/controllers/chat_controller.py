from fastapi.templating import Jinja2Templates
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Request, Depends, WebSocket, WebSocketDisconnect

from di_container import Container
from schemas.message import MessageListResponseScheme
from services.chat_service import ChatService


router = APIRouter(tags=['chat'])

templates = Jinja2Templates(directory='templates')


@router.websocket('/ws/{client_id}')
@inject
async def websocket_endpoint(
    websocket: WebSocket,
    client_id: int,
    chat_service: ChatService = Depends(Provide[Container.chat_service])
):  
    await chat_service.broadcast(client_id=client_id, websocket=websocket)
        

@router.get('/chat')
def get_chat_page(request: Request):
    
    return templates.TemplateResponse('chat.html', {'request': request})

@router.get('/chat_history', response_model=MessageListResponseScheme)
@inject
async def get_chat_history(chat_service: ChatService = Depends(Provide[Container.chat_service])):

    return await chat_service.get_chat_history()
