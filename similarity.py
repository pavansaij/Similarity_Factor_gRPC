from math import *
import cv2
from decimal import Decimal

class Similarity():
    def __init__(self):
        pass
        
    def square_rooted(self,img):
        return round(sqrt(sum([a*a for a in img])),3)

    def cosine_similarity(self,image1,image2):
        numerator = sum(a*b for a,b in zip(image1,image2))
        denominator = self.square_rooted(image1)*self.square_rooted(image2)
        return round(numerator/float(denominator),3)