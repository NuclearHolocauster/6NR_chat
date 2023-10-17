from pydantic import BaseModel, Field


class MessageScheme(BaseModel):
    text: str = Field(..., description='Text of message')


class MessageListResponseScheme(BaseModel):
    messages: list[MessageScheme] = Field(..., description='List of messages')