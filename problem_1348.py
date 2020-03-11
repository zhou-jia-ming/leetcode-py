# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-22


# 请你实现一个能够支持以下两种方法的推文计数类 TweetCounts：
#
# 1. recordTweet(string tweetName, int time)
#
# 记录推文发布情况：用户 tweetName 在 time（以 秒 为单位）时刻发布了一条推文。
# 2. getTweetCountsPerFrequency(string freq, string tweetName, int startTime, int endTime)
#
# 返回从开始时间 startTime（以 秒 为单位）到结束时间 endTime（以 秒 为单位）内，每 分 minute，时 hour 或者 日 day （取决于 freq）内指定用户 tweetName 发布的推文总数。
# freq 的值始终为 分 minute，时 hour 或者 日 day 之一，表示获取指定用户 tweetName 发布推文次数的时间间隔。
# 第一个时间间隔始终从 startTime 开始，因此时间间隔为 [startTime, startTime + delta*1>,  [startTime + delta*1, startTime + delta*2>, [startTime + delta*2, startTime + delta*3>, ... , [startTime + delta*i, min(startTime + delta*(i+1), endTime + 1)>，其中 i 和 delta（取决于 freq）都是非负整数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/tweet-counts-per-frequency
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
from collections import defaultdict


class TweetCounts:

    def __init__(self):
        self.data = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.data[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        step = {'hour': 60 * 60, 'minute': 60, 'day': 24 * 60 * 60}.get(freq)

        result = [0 for _ in range((endTime - startTime) // step + 1)]
        for i in self.data[tweetName]:
            if startTime <= i <= endTime:
                result[(i - startTime) // step] += 1
        return result


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)


if __name__ == "__main__":
    tweetCounts = TweetCounts()
    tweetCounts.recordTweet("tweet3", 0)
    tweetCounts.recordTweet("tweet3", 60)
    tweetCounts.recordTweet("tweet3", 10)

    print(tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59))
    print(tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60))
    tweetCounts.recordTweet("tweet3", 120)
    print(tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210))
