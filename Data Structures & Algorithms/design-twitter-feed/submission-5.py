from collections import defaultdict
class Twitter:

    def __init__(self):
        self.tweets_by_id = defaultdict(list)
        self.followers_by_id = defaultdict(set)
        self.ordered_id = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.ordered_id += 1
        self.tweets_by_id[userId].append((tweetId,self.ordered_id))

    def getNewsFeed(self, userId: int) -> List[int]:
        all_feeds = []
        feed_users = self.followers_by_id[userId]
        feed_users.add(userId)
        for user_id in feed_users :
            all_feeds.extend(self.tweets_by_id[user_id])
        all_feeds.sort(key=lambda x : x[1], reverse=True)
        res = []
        for feed in all_feeds[:10] :
            res.append(feed[0])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers_by_id[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers_by_id[followerId].discard(followeeId)
