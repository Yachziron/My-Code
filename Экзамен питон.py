from typing import List
from collections import defaultdict
import heapq
class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0
    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        self.tweets[user_id].append((self.time, tweet_id))
        self.time -= 1
    def get_news_feed(self, user_id: int) -> List[int]:
        tweets = heapq.merge(*(self.tweets[u] for u in self.following[user_id] | {user_id}))
        return [t for _, t in heapq.nsmallest(10, tweets)]
    def follow(self, follower_id: int, followee_id: int) -> None:
        self.following[follower_id].add(followee_id)
    def unfollow(self, follower_id: int, followee_id: int) -> None:
        self.following[follower_id].discard(followee_id)

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
