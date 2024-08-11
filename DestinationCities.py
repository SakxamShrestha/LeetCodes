class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        startCities, endCities = set(), set()

        for startCity, endCity in paths:
            startCities.add(startCity)
            endCities.add(endCity)

        for endCity in endCities:
            if endCity not in startCities:
                return endCity    

     '''
     Time Complexity is O(n): Used a single for loop once
     Space Complexity is also O(n) cause we used two sets here.    
     '''