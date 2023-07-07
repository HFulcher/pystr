import json
from typing import List
from filters import Filter

class Request:
    def __init__ (
            self,
            subscription_id: str,
            filters: Filter) -> None:

        self.subscription_id = subscription_id
        self.filters = filters

    def to_json_object(self) -> dict:
        return {
            "subscription_id": self.subscription_id,
            "filters": self.filters.to_json_object()
        }

    def __str__(self):
        return json.dumps(self.to_json_object())
