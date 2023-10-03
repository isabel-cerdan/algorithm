#This solution 
#Runtime 785ms
#Beats 5.04% of users with Python3
#Memory  18.16MB
#Beats 96.99%of users with Python3
Class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        num_of_candies_can_eat = len(candyType) // 2
        candyType.sort()
        prev_candy = -1
        types = 0
        for candy in candyType:
            if candy != prev_candy:
                types += 1
                prev_candy = candy

        return min(types,num_of_candies_can_eat)
