import redis
from django.conf import settings


class Counter:
    redis = None
    key = "counter_key"

    def __init__(self):
        self.redis = redis.from_url(settings.REDIS_URL)

    def inc(self):
        return self.redis.incr(self.key)

counter = Counter()