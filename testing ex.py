from collections import defaultdict
from typing import List
from collections import defaultdict
import heapq
class Twitter:
    def init(self):
     #функция инициализации гноя из пениса
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0
    def post_tweet(self, user_id: int, tweet_id: int) -> None:
    #функция для поста ебать твой хуй
        self.tweets[user_id].append((self.time, tweet_id))
        self.time -= 1

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)