def getMinOperations(location:list, k:int):
    result = 0
    location.sort()
    location = list(set(location))
    while True:
        print(location)
        result += 1
        median = len(location)//2
        size = len(location)
        if len(location) == 1:
            break
        for i in range(size):
            if i == median:
                continue
            elif i < median:
                location[i] -= k
                if location[i] < 0:
                    location[i] = -1
            elif i > median:
                location[i] += k
            
        print(location)
        try: 
            location.remove(location[median])
            location.remove(-1)
        except:
            pass
        location = list(set(location))
    return result        








if __name__ == "__main__":
    testArray = [
        [[1,3,5], 2, 2]
    ]
    for i,test in enumerate(testArray):
        res = getMinOperations(test[0],test[1])
        print(f"Test {i+1} " + ("Başarılı " if test[2] == res else "Başarısız ") + f" Result = {res} Expect = {test[2]}")