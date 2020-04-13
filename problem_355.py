# coding:utf-8
# Created at: 2020-04-13
# Created by: jiaming

# 设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个功能：
#
# postTweet(userId, tweetId): 创建一条新的推文
# getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
# follow(followerId, followeeId): 关注一个用户
# unfollow(followerId, followeeId): 取消关注一个用户
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/design-twitter
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Twitter:
    class Node:
        def __init__(self):
            self.followee = set()
            self.tweet = list()

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.recentMax = 10
        self.tweetTime = dict()
        self.user = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.user:
            self.user[userId] = Twitter.Node()
        self.user[userId].tweet.append(tweetId)
        self.time += 1
        self.tweetTime[tweetId] = self.time

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.user:
            return list()
        else:
            # 取出自己最近10条推文
            ans = self.user[userId].tweet[-10:][::-1]
            # 取出自己followee
            for followeeId in self.user[userId].followee:
                if followeeId in self.user:
                    # follow人的最近十条推文
                    opt = self.user[followeeId].tweet[-10:][::-1]
                    i, j, combined = 0, 0, list()
                    while i < len(ans) and j < len(opt):
                        if self.tweetTime[ans[i]] > self.tweetTime[opt[j]]:
                            combined.append(ans[i])
                            i += 1
                        else:
                            combined.append(opt[j])
                            j += 1
                    combined.extend(ans[i:])
                    combined.extend(opt[j:])
                    ans = combined[:10]
            return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            if followerId not in self.user:
                self.user[followerId] = Twitter.Node()
            self.user[followerId].followee.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            if followerId in self.user:
                self.user[followerId].followee.discard(followeeId)


if __name__ == '__main__':
    # Your Twitter object will be instantiated and called as such:
    obj = Twitter()
    userId = 1
    tweetId = 2
    followerId = 3
    followeeId = 4
    obj.postTweet(userId, tweetId)
    param_2 = obj.getNewsFeed(userId)
    obj.follow(followerId, followeeId)
    obj.unfollow(followerId, followeeId)
