import sys

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        list1Map = {}
        i = 0
        for word in list1:
            list1Map[word] = i
            i += 1

        minSum = sys.maxint
        i = 0
        restaurants = [] 
        for word in list2:
            if word in list1Map:
                if minSum > list1Map[word]+i:
                    print minSum
                    minSum = list1Map[word]+i
                    restaurants = []
                    restaurants.append(word)
                elif minSum == list1Map[word]+i:
                    restaurants.append(word)
            i += 1

        return restaurants

assert Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], 
    ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]) == ["Shogun"]
assert Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], 
    ["KFC", "Shogun", "Burger King"]) == ["Shogun"]
assert Solution().findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], 
    ["KFC","Burger King","Tapioca Express","Shogun"]) == ["KFC","Burger King","Tapioca Express","Shogun"]