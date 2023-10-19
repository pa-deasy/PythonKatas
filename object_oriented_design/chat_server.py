from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict, List


# 7.7 - Chat Server: Explain how you would design a chat server.In particular, provide details about the various backend components, classes and methods.
# What would be the hardest problems to solve?
class Status(Enum):
    ONLINE = 'online'
    OFFLINE = 'offline'


@dataclass
class User:
    id: int
    status: Status
    alias: str
    contacts: Dict[int, 'User']
    invites_sent: List['User']
    invites_received: List['User']
    

class UserManager:
    all_users: Dict[int, User]
    
    def add():
        return
    
    def remove():
        return
    
    def authenticate(user: User):
        return
    
    def set_status(status: Status, user: User) -> None:
        user.status = status
        
    def send_request(from_user: User, to_user: User) -> bool:
        return False
    
    def get_requests():
        return
    
    def accept_request():
        return
    
    def decline_request():
        return
    

class Message:
    id: int
    timestamp: datetime
    content: str
    from_id: User


class Chat:
    id: int
    members: Dict[int, User]
    messages: Dict[int, Message]


class ChatManager:
    def get_chats_for(user: User) -> List[Chat]:
        return []
    
    def add_message_to_chat(chat_id: int, message: Message) -> None:
        return
    
    def delete_message_from_chat(chat_id: int, message_id: int) -> None:
        return
    
    def create_new_chat(members: Dict[int, User]) -> Chat:
        return Chat()
    
    def delete_chat(chat_id: int) -> Chat:
        return Chat()
    
    
class ChatServer:
    user: User
    
    def login(self):
        self.user.status = Status.ONLINE
    
    def logout(self):
        self.user.status = Status.OFFLINE
    
    def get_chats():
        return
    
    def open_chat():
        return
    
    