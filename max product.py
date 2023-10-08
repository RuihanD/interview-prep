"""
 一个朋友关系和company，找最大的set，类似于island那题。
 输入是{[1,2, 1], [2,3,1]}前两个是朋友id，最后一个是companyID
 meaning 在company1下，1和2是朋友，2和3也是朋友，所以这个集合就是1，2，3在company1下。
 同一个人可以在多个company下，求最大的这个集合

白人大哥，input是一组数字每组三个数，分别代表friendId, friendId, companyId，
问你max product of two friendIds in the same company with longest graph. 需要主语的是如果friend1和friend2connect然后friend2和friend3 connect，friend1也会算是friend3的friend。

can we have more than one set that have greatest number of friends?
group friends by company
max friend group size
maintain a list of list (max friends set)
create a djs for each company
    friends pair list of list
    hashmap friendAndCenter: centerFriend
    hashmap all friend In ACenter: all friends
    a function to connect friend
        update the center of one p to center of another p
        move all friends of one group to another
    a function to find center friend of a person
"""
from collections import defaultdict
class Solution:
    @staticmethod
    def maxProductFriendsGroup(friendsInACompany):
        company_to_friends = defaultdict(list)
        for id1, id2, company in friendsInACompany:
            company_to_friends[company].append([id1, id2])

        def dfs(cur):
            if cur in visited:
                return False
            visited.add(cur)
            path.append(cur)
            for nei in neibors[cur]:
                dfs(nei)
            return True

        res = []
        for key in company_to_friends:
            neibors = defaultdict(list)
            visited = set()
            for id1, id2 in company_to_friends[key]:
                neibors[id1].append(id2)
                neibors[id2].append(id1)
            for cur in neibors:
                path = []
                if dfs(cur):
                    res.append(path)

        res.sort(key = len, reverse = True)
        maxLen = len(res[0])
        maxLen_res = [i for i in res if len(i) == maxLen]
        maxRes = 0
        for cur in maxLen_res:
            cur.sort()
            if maxLen >= 2:
                maxRes = max(maxRes, cur[-1] * cur[-2])
        return maxRes

if __name__ == "__main__":
    fp1 = [1, 2, 1]
    fp2 = [2, 7, 1]
    fp3 = [4, 1, 1]
    fp4 = [1, 4, 2]
    fp5 = [3, 4, 2]
    friends = [fp1, fp2, fp3, fp4, fp5]
    print(Solution.maxProductFriendsGroup(friends))
