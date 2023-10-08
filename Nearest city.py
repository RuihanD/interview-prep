"""
give a list of cities names, x coor of cities, y corr of cities, and a city to look for,
find nearest city of the city having same x or y coor as the city
if nearest city more than one, return the city name with largest alphabatical value

put city with same x into a hashmap x: list of cities with x coor the same [x,y, index]
sor the list of cities in the mapper
for each city to find its neibor
    generate a min dianstance value
    generate a result list
    find the neiboring cities(left and right if exists) as potential candidates
        binary search for cloest city
        add left right return list
    add all potential candidates together
    set a mindistance value
    build result list of indexes of cities based on mindistance
    get the name of cities  from index and put into list then sort
"""
from collections import defaultdict

class Solution:
    @staticmethod
    def nearestStone(citieNames, cityX, cityY, cityToFind):
        sameX = defaultdict(list)
        sameY = defaultdict(list)
        names = {}

        for i in range(len(cityX)):
            c1 = [cityX[i], cityY[i], i]
            names[citieNames[i]] = i

            if cityX[i] not in sameX:
                sameX[cityX[i]] = []
            sameX[cityX[i]].append(c1)

            if cityY[i] not in sameY:
                sameY[cityY[i]] = []
            sameY[cityY[i]].append(c1)

        for mapper in sameX.values():
            mapper.sort(key=lambda x: x[1])

        for mapper in sameY.values():
            mapper.sort(key=lambda x: x[0])

        cityIndex = names[cityToFind]
        minDistance = float('inf')
        citySameX = sameX[cityX[cityIndex]]
        citySameY = sameY[cityY[cityIndex]]

        def searchClosest(indexToSearch, citySameCoor, target):
            start = 0
            end = len(citySameCoor) - 1
            targetIndex = -1
            nerborIndexes = []

            while start <= end:
                middle = (start + end) // 2

                if citySameCoor[middle][indexToSearch] < target:
                    start = middle + 1
                elif citySameCoor[middle][indexToSearch] > target:
                    end = middle - 1
                else:
                    targetIndex = middle
                    break

            if targetIndex - 1 >= 0:
                nerborIndexes.append(citySameCoor[targetIndex - 1][2])
            if targetIndex + 1 < len(citySameCoor):
                nerborIndexes.append(citySameCoor[targetIndex + 1][2])

            return nerborIndexes

        XIndex = searchClosest(1, citySameX, cityY[cityIndex])
        YIndex = searchClosest(0, citySameY, cityX[cityIndex])
        XIndex.extend(YIndex)
        allNeiborIndexes = []

        for index in XIndex:
            distance = abs(cityY[index] + cityX[index] - cityX[cityIndex] - cityY[cityIndex])

            if distance < minDistance:
                minDistance = distance
                allNeiborIndexes = [index]
            elif distance == minDistance:
                allNeiborIndexes.append(index)

        if not allNeiborIndexes:
            return ""

        resultNames = [citieNames[index] for index in allNeiborIndexes]
        resultNames.sort()
        return resultNames[0]

    @staticmethod
    def main():
        citieNames = ["c1", "c2", "c3", "c4", "c5"]
        cityX = [0, 0, 1, 1, 2]
        cityY = [0, 1, 0, 1, 2]
        print(Solution.nearestStone(citieNames, cityX, cityY, "c2"))


if __name__ == "__main__":
    Solution.main()
