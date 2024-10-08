from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
import json
from typing import Dict, List, Optional

import redis
import shortuuid

import settings

redis_db = redis.Redis.from_url(settings.CACHE_REDIS_URL or "redis://localhost:6379/0")

CACHE_EXPIRATION_MINUTES = 1
search_queue = "search_queue"


@dataclass
class Search:
    id: str = field(init=False)
    query: dict = field(default_factory=dict)
    results: Optional[List] = field(default_factory=list)
    meta: Optional[Dict] = field(default_factory=dict)
    is_ready: bool = False
    timestamp: str = field(init=False)

    def __post_init__(self):
        self.id = self.short_uuid()
        self.timestamp = datetime.now(timezone.utc).isoformat()

    def short_uuid(self) -> str:
        return shortuuid.uuid()

    def save(self):
        print(f"Saving search {self.id} to cache with {self.to_dict()}")
        redis_db.set(self.id, json.dumps(self.to_dict()))
        # add to queue for processing
        redis_db.rpush(search_queue, self.id)

    def to_dict(self):
        return asdict(self)


def get_existing_search(id: str) -> Optional[Dict]:
    existing_search_json = redis_db.get(id)
    if not existing_search_json:
        return None
    existing_search = json.loads(existing_search_json)
    return existing_search
