import json
import time
from typing import List
from enum import IntEnum
from hashlib import sha256

class EventKind(IntEnum):
    SET_METADATA = 0
    TEXT_NOTE = 1
    RECOMMEND_RELAY = 2
    CONTACTS = 3
    ENCRYPTED_DIRECT_MESSAGE = 4
    DELETE = 5

class Event:
    def __init__(
            self, 
            id: str=None,
            pubkey: str='', 
            kind: int=EventKind.TEXT_NOTE, 
            tags: List[List[str]]=[], 
            content: str='',
            sig: str=None) -> None:

        self.pubkey = pubkey 
        self.created_at = int(time.time())
        self.kind = kind
        self.tags = tags
        self.content = content
        self.sig = sig

        if not id:
            id = Event.create_id(self.pubkey, self.created_at, self.kind, self.tags, self.content)

        self.id = id

    @staticmethod
    def create_id(pubkey: str, created_at: int, kind: int, tags: List[List[str]], content: str) -> str:
        data = [0, pubkey, created_at, kind, tags, content]
        data_str = json.dumps(data, separators=(',', ':'), ensure_ascii=False).encode()

        return sha256(data_str).hexdigest()

    def to_json_object(self) -> dict:
        return {
            "id": self.id,
            "pubkey": self.pubkey,
            "kind": self.kind,
            "tags": self.tags,
            "content": self.content,
            "sig": self.sig
        }

    
    def __str__(self):
        return json.dumps(self.to_json_object())
        

