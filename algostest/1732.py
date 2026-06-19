from typing import List


def Solutionone(gain: List[int]) -> int:
        altitudes = [0]
        result = altitudes[0]
        for i in range(len(gain)):
            altitudes.append(altitudes[i] + gain[i])
        
        for i in altitudes:
              if i > result:
                    result = i
        
        return result

def Solutiontwo(gain: List[int]) -> int:
        result = 0
        altitude = 0
        for i in gain:
            altitude = altitude + i
            if altitude > result:
                  result = altitude
        return result

def Solutionthree(gain: List[int]) -> int:
        altitudes = [0]
        for i in range(len(gain)):
            altitudes.append(altitudes[i] + gain[i])
        return max(altitudes)
            
            
            
print(Solutionone([-4,-3,-2,-1,4,3, 90]))
print(Solutiontwo([-4,-3,-2,-1,4,3,90]))
print(Solutionthree([-4,-3,-2,-1,4,3,90]))
#GPT says second is the best also second is the one i spent most of my time on =))))