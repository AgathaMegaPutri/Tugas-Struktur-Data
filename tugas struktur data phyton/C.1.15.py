from typing import List

def areDistinct(data: List[int]) -> bool:
    uniqueNums = {x for x in data}
    return len(uniqueNums) == len(data)

data1 = [5, 10, 16, 15, 3]
data2 = [4, 6, 3, 6, 7, 2]

print(areDistinct(data1))
print(areDistinct(data2))
