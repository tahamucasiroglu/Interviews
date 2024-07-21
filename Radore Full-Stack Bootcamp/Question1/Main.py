def findMaximumTasks(task:list, m):
    if m == 1:
        return len(task)
    task.sort()
    result = 0
    for t in set(task):
        result += task.count(t) // m
    result *= m
    return result






if __name__ == "__main__":

    testSamples = [
        [[4,1,2,1,1,2], 2, 2],
        [[3,1,2,3,3], 3, 3],
        [[1,1,1,1,1],1,5]
    ]

    for i,test in enumerate(testSamples):
        res = findMaximumTasks(test[0],test[1])
        print(f"Test {i+1} " + ("Başarılı" if res == test[2] else "Başarısız") + f" Result = {res} Expect = {test[2]}")





