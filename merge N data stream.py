"""
Given n sorted stream, and a constant number k. The stream type is like iterator
and it has two functions, move() and getValue(), find a list of numbers that each
of them appears at least k times in these streams. Duplicate numbers in a stream
should be counted as once.

Note: In the interview, we should use min heap method

follow up是如果一个stream特别长其他的短怎么办

有n个排好序的int stream，只能用iterator access。 iterator有 peek（）， next（）， hasNext（）三个方法。
要找出在至少m个stream中出现过的int， 做成list输出。
例子：
stream：
1) 0, 0, 1, 1, 2, 3, 3, 4, 5, 6, 7, 10...
2) 2, 3, 4, 5, 5, 6, 7, 10 ....
3) 0, 1, 2, 3, 4, 4, 4, 4, 11....
4) 5, 6, 8, 9, 10 ...
if m = 3, return: [2, 3, 4, 5, 6, 10,.... ]
"""
import heapq

class Stream:
    def __init__(self, nums):
        self.it = iter(nums)

    def hasNext(self):
        try:
            next(self.it)
            return True
        except StopIteration:
            return False

    def nextVal(self):
        return next(self.it)

def mergeK(streams, k):
    def cmp(a, b):
        return a[0] > b[0]

    pq = []
    res = []
    for s in streams:
        if s.hasNext():
            val = s.nextVal()
            heapq.heappush(pq, (val, s))
    flag = True
    cnt = 0
    lastVal = None
    while len(pq) >= k:
        val, s = heapq.heappop(pq)
        tmpVal = val
        while s.hasNext() and tmpVal == val:
            tmpVal = s.nextVal()
        if tmpVal != val:
            heapq.heappush(pq, (tmpVal, s))
        if flag:
            lastVal = val
            flag = False
        if lastVal == val:
            cnt += 1
        else:
            if cnt >= k:
                res.append(lastVal)
            lastVal = val
            cnt = 0
    return res

if __name__ == "__main__":
    nums0 = [0, 0, 1, 1, 2, 3, 3, 4, 5, 6, 7, 10]
    nums1 = [2, 3, 5, 5, 6, 7, 10]
    nums2 = [0, 1, 2, 3, 4, 4, 4, 4, 10]
    nums3 = [0, 1, 2, 3, 4, 4, 4, 4, 10]
    nums4 = [5, 2]
    streams = [Stream(nums0), Stream(nums1), Stream(nums2), Stream(nums3), Stream(nums4)]
    result = mergeK(streams, 3)
    print(result)
