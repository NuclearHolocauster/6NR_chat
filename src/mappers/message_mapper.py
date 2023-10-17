from models import Message
from schemas.message import MessageScheme


def message_data_to_message_scheme_mapper(data: Message):
    
    return MessageScheme(
        text=data.text
    )