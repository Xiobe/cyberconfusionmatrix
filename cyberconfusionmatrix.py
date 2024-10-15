from enum import Enum

class CyberConfusionMatrix(Enum):

    TruePositive = "The detection triggered, something malicious was found"
    FalsePosive = "The detection triggered, nothing malicious was found"
    FalseNegative = "There was no detection, something malicious was found"
    TrueNegative = "There was no detection, acceptable behavior according to policy"
