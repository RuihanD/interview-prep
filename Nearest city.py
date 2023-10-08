"""
give a list of cities names, x coor of cities, y corr of cities, and a city to look for,
find nearest city of the city having same x or y coor as the city
if nearest city more than one, return the city name with largest alphabetical value

put city with same x into a hashmap x: list of cities with x coor the same [x,y, index]
sor the list of cities in the mapper
for each city to find its neighbor
    generate a min distance value
    generate a result list
    find the neighboring cities(left and right if exists) as potential candidates
        binary search for closest city
        add left right return list
    add all potential candidates together
    set a min distance value
    build result list of indexes of cities based on min distance
    get the name of cities  from index and put into list then sort
"""
from collections import defaultdict

class Solution:
    @staticmethod
    def nearestStone(names, cityX, cityY, nameCity):
        sameX = defaultdict(list)
        sameY = defaultdict(list)
        cityId = defaultdict()
        for i in range(len(names)):
            cityId[i] = names[i]
            sameX[cityX[i]].append([cityY[i],i])
            sameY[cityY[i]].append([cityX[i],i])
            if names[i] == nameCity:
                targetX = cityX[i]
                targetY = cityY[i]
                targetId = i
        minCoor = float('inf')
        distance = defaultdict(list)
        for nx, id in sameY[targetY]:
            if targetId == id:
                continue
            distance[abs(nx - targetX)].append(id)
            minCoor = min(minCoor, abs(nx - targetX))
        for ny, id in sameX[targetX]:
            if targetId == id:
                continue
            distance[abs(ny - targetY)].append(id)
            minCoor = min(minCoor, abs(ny - targetY))
        result = [cityId[id] for id in distance[minCoor]]
        result.sort()
        # print(distance[minCoor], result, targetId)
        return result[0]

    @staticmethod
    def main():
        citieNames = ["c1", "c2", "c3", "c4", "c5"]
        cityX = [0, 0, 1, 1, 2]
        cityY = [0, 1, 0, 1, 2]
        print(Solution.nearestStone(citieNames, cityX, cityY, "c2"))

if __name__ == "__main__":
    Solution.main()
