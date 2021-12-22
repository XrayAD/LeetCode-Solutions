from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        startColor = image[sr][sc]
        image[sr][sc] = newColor
        return self.check_around(image,sr,sc,newColor,startColor)


    def check_around(self, image: List[List[int]], sr: int, sc: int, newColor: int,startColor: int):
        if 0<=sr-1<=len(image)-1 and image[sr-1][sc] == startColor:
            image[sr-1][sc] = newColor
            image = self.check_around(image, sr-1,sc,newColor,startColor)
        if 0 <=sr+1<=len(image)-1 and image[sr+1][sc] == startColor:
            image[sr+1][sc] = newColor
            image = self.check_around(image,sr+1,sc,newColor,startColor)
        if 0<=sc-1<=len(image[0])-1 and image[sr][sc-1] == startColor:
            image[sr][sc-1] = newColor
            image = self.check_around(image,sr,sc-1,newColor,startColor)
        if 0<= sc+1<=len(image[0])-1 and image[sr][sc+1] == startColor:
            image[sr][sc+1] = newColor
            image = self.check_around(image,sr,sc+1,newColor,startColor)
        return image
