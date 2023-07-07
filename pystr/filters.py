from typing import List
from events import EventKind

class Filter:
    def __init__ (
            self,
            ids: List[str]=None,
            authors: List[str]=None,
            kinds: List[EventKind]=None,
            e: List[str]=None,
            p: List[str]=None,
            since: int=None,
            until: int=None,
            limit: int=None) -> None:

        self.ids = ids
        self.authors = authors
        self.kinds = kinds
        self.e = e
        self.p = p
        self.since = since
        self.until = until
        self.limit = limit

    def to_json_object(self) -> dict:
        obj = {}

        if self.ids is not None:
            obj['ids'] = ids
        if self.authors is not None:
            obj['authors'] = authors
        if self.kinds is not None:
            obj['kinds'] = kinds
        if self.e is not None:
            obj['e'] = e 
        if self.p is not None:
            obj['p'] = p 
        if self.since is not None:
            obj['since'] = since
        if self.until is not None:
            obj['until'] = until
        if self.limit is not None:
            obj['limit'] = limit

        return obj
