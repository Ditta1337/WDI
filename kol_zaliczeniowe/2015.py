


from concurrent.futures import thread


def zadanie1():
    N = 5
    T = [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,1597,2584,4181,0],
         [0,0,0,0,0],
         [0,0,0,0,0],]

    def isValid(num1, num2, num3):
        a = 1
        b = 1
        c = 0
        while c <= num3:
            c = a + b
            if (a == num1 and b == num2):
                return True
            a = b
            b = c
        return False

    def checkTab(T):
        length = len(T[0])
        for i in range(length):
            for j in range(length - 2):
                if T[i][j] + T[i][j+1] == T[i][j+2]:
                    if isValid(T[i][j], T[i][j+1], T[i][j+2]):
                        return i + 1
        return "brak"
        
    print(checkTab(T))

def zadanie2():
    T = [2, 3, 5, 7, 11, 13, 16]

    def howManyOnesInBinary(num):
        counter = 0
        while num != 0:
            if num % 2 == 1:
                counter += 1
            num //= 2
        return counter


    def changeSet(T):
        ret = T
        length = len(ret)
        for i in range(length):
            ret[i] = howManyOnesInBinary(ret[i])
        return ret
    
    def canDivide(T):
        newSet = changeSet(T)
        sums = [0,0,0]
        def canDivide_rek(index, sums):
            if index == len(newSet):
                all_even = 1
                for i in range(len(sums) - 1):
                    if sums[i] != sums[i+1]:
                        all_even = 0
                        break
                if all_even:
                    return True
                return False
            for i in range(len(sums)):
                sums[i] += newSet[index]
                if (canDivide_rek(index + 1, sums)):
                    return True
                sums[i] -= newSet[index]
            return False
        return canDivide_rek(0, sums)

    print(canDivide(T))

def zadanie3():
    class Node():
        def __init__(self, xval=0, yval=0):
            self.x = xval
            self.y = yval
            self.next = None

        def append(self, x, y):
            if self.next == None:
                self.next = Node(x, y)
                return
            self.next.append(x, y)

        def printWart(self):
            if self.next != None:
                item = self.next
                while item.next != None:
                    print("x: ", item.x, "y: ", item.y)
                    item = item.next
        
    def divideToQuater(list):
        firstQ = Node()
        secondQ = Node()
        thirdQ = Node()
        fourthQ = Node()
        if list.next == None:
            return firstQ, secondQ, thirdQ, fourthQ
        
        start_list = list
        prev_list = list
        list = list.next

        while list.next != None:
            if list.x == 0 or list.y == 0:
                prev_list.next = list.next
            else:
                prev_list = prev_list.next
            if list.x > 0 and list.y > 0:
                firstQ.append(list.x, list.y)
            if list.x < 0 and list.y > 0:
                secondQ.append(list.x, list.y)
            if list.x < 0 and list.y < 0:
                thirdQ.append(list.x, list.y)
            if list.x > 0 and list.y < 0:
                fourthQ.append(list.x, list.y)
            list = list.next
        
        list = start_list
        firstQ.append(0, 0)
        secondQ.append(0, 0)
        thirdQ.append(0, 0)
        fourthQ.append(0, 0)
        return firstQ, secondQ, thirdQ, fourthQ
    
    list = Node()
    list.append(1, 0)
    list.append(-1, 0)
    list.append(0, -1)
    list.append(0, -1)
    list.append(0, 1)
    list.append(-3, 0)
    list.append(2, 0)
    list.append(0, 0) #wartowanik

    list.printWart()
    print("1st")
    stq, ndq, rdq, thq = divideToQuater(list)
    stq.printWart()
    print("2nd")
    ndq.printWart()
    print("3rd")
    rdq.printWart()
    print("4th")
    thq.printWart()
    print("-------")

    list.printWart()







if "__main__" == __name__:

    zadanie3()