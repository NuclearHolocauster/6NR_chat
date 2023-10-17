from dependency_injector import containers, providers

from services import ChatService, SqlService, WebsocketService


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    sql_service = providers.Singleton(SqlService, connection_str=config.db_connection_string)
    websocket_service = providers.Singleton(WebsocketService)

    chat_service = providers.Factory(
        ChatService, 
        sql_service=sql_service,
        websocket_service=websocket_service
    )
