from random import randint

def zadanie1():
    

    #N = 10
    #T = [[randint(1, 20) for _ in range(N)] for _ in range(N)]
    T = [[2,11,0,3,0],
         [3,0,2,3,0],
         [0,0,0,5,0],
         [0,0,0,3,0],
         [11,4,2,3,0]]


    def isThereSequence(tab):
        length = len(tab)
        if length <= 2:
            return 0
        ret = 0
        counter = 0
        for i in range(length - 1):
            counter = 0
            r = tab[i + 1] - tab[i]
            print(r, "r")
            for j in range(i + 2, length):
                print(tab[j], "j", tab[j] == tab[j - 1] + r, tab[i + 1], "j - 1", r, "r")
                if tab[j] == tab[i + 1] + r:
                    counter += 1
                else:
                    counter = 0
                if counter > ret:
                    ret = counter
        if ret == 0:
            return ret + 2
        else:
            return ret + 1


    def isPrime(N):
        if N < 2:
            return False
        for i in range(2, N//2 + 1):
            if N % i == 0:
                return False
        return True

    for i in range(30):
        print(i, isPrime(i))

    def checkRows(T):
        ret = 0
        counter = 0
        tmpTab = []
        primeTab = []
        N = len(T[0])
        for i in range(N):
            tmpTab = []
            counter = 0
            for j in range(N):
                if isPrime(T[i][j]):
                    counter += 1
                    tmpTab.append(T[i][j])
                else:
                    tmpTab = []
                    counter = 0
                if counter > ret:
                    primeTab = tmpTab
                    ret = counter
        return primeTab

    def checkColumns(T):
        ret = 0
        counter = 0
        tmpTab = []
        primeTab = []
        N = len(T[0])
        for i in range(N):
            print(ret, "--------")
            tmpTab = []
            counter = 0
            for j in range(N):
                print(T[j][i])
                if isPrime(T[j][i]):
                    counter += 1
                    tmpTab.append(T[j][i])
                else:
                    tmpTab = []
                    counter = 0
                if counter >= ret:
                    primeTab = tmpTab
                    ret = counter
        print(primeTab)
        return primeTab

    def task(T):
        t1 = checkRows(T)
        t2 = checkColumns(T)
        if len(t1) > len(t2):
            return t1
        return t2
    print(task(T))
                        
    print(isThereSequence(task(T)))


def zadanie2():
    T = [[0,0,0,2,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [1,1,1,1,1,1,1,1],
         [0,0,0,0,0,0,0,0],]

    def isLegal(T, y, x):
        N = len(T[0])
        if x > N-1 or x < 0 or y > N-1 or y < 0:
            return 0
        if T[y][x] == 1:
            return 0
        return 1

    def bestpath(T, y = 0, x = 0, counter = 0, ret = [99999]):
        print("pos y: ", y, "pos x: ", x)
        N = len(T[0])
        if y == N - 2:
            if counter < ret[0]:
                ret[0] = counter
            return
        if isLegal(T, y+2, x-1) and y+2 != N - 1:
             bestpath(T, y+2, x-1, counter + 1)
        if isLegal(T, y+2, x+1) and y+2 != N - 1:
             bestpath(T, y+2, x+1, counter + 1)
        if isLegal(T, y+1, x-2):
             bestpath(T, y+1, x-2, counter + 1)
        if isLegal(T, y+1, x+2):
             bestpath(T, y+1, x+2, counter + 1)
        if ret[0] == 99999:
            return "brak"
        return ret[0]

    print(bestpath(T, 0, 3))


def zadanie3():
    class Node():
        def __init__(self, value=0):
            self.val = value
            self.next = None

        def append(self, value):
            if self.next == None:
                self.next = Node(value)
                return
            self.next.append(value)

        def print(self):
            if self.next != None:
                item = self.next
                while item.next != None:
                    print(item.val, end=", ")
                    item = item.next
                print(item.val)

        def printWartownik(self):
            if self.next != None:
                item = self.next
                while item.next != None:
                    print(item.val, end=", ")
                    item = item.next
                print("")
        
    def remFromThree(list1, list2, list3):
        ret = 0
        if list1.next == None or list2.next == None or list3.next == None:
            return ret
        
        list1.append(0)
        list2.append(0)         #dodajemy wartownik
        list3.append(0)

        list1_start = list1
        list2_start = list2
        list3_start = list3

        prev1 = list1
        prev2 = list2
        prev3 = list3

        list1 = list1.next
        list2 = list2.next
        list3 = list3.next

        flag1 = 0
        flag2 = 0
        flag3 = 0
        while list1.next != None:
            val1 = list1.val
            list2 = list2_start.next
            prev2 = list2_start
            flag1 = 0
            while list2.next != None:
                val2 = list2.val
                list3 = list3_start.next
                prev3 = list3_start
                flag2 = 0
                while list3.next != None:
                    flag3 = 0
                    val3 = list3.val

                    if val1 == val2 and val1 == val3:
                        ret += 1
                        prev1.next = list1.next
                        #list1.next = None

                        prev2.next = list2.next
                        #list1.next = None

                        prev3.next = list3.next
                        #list3.next = None
                        flag1 = 1
                        flag2 = 1
                        flag3 = 1

                    if flag3 != 1:    
                        prev3 = prev3.next
                    list3 = list3.next
                if flag2 != 1:
                    prev2 = prev2.next
                list2 = list2.next
            if flag1 != 1:
                prev1 = prev1.next
            list1 = list1.next
        
        list1 = list1_start
        list2 = list2_start
        list3 = list3_start

        return ret

    list1 = Node()
    list2 = Node()
    list3 = Node()

    list1.append(1)
    list1.append(2)
    list1.append(3)
    list1.append(4)

    list2.append(3)
    list2.append(1)
    list2.append(2)
    list2.append(4)

    list3.append(4)
    list3.append(2)
    list3.append(1)
    list3.append(3)

    list1.print()
    list2.print()
    list3.print()

    print("Wynik: ", remFromThree(list1, list2, list3))
    

    list1.printWartownik()
    print("----")
    list2.printWartownik()
    print("----")
    list3.printWartownik()





if "__main__" == __name__:
    #zadanie1()
    #zadanie2()
    zadanie3()