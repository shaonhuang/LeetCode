

def twoSum(List, target):
    for i in List:
        for j in List[List.index(i):]:
            if i+j == target:
                return [List.index(i), List.index(j)]


List = [2, 7, 11, 15]
target = 9

print(twoSum(List, target))
