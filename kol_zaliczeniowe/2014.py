from random import randint

def zadanie1():

    T = [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,1597,2584,4181,0],
         [0,0,0,0,0],
         [0,0,0,0,0],]

    def isFibo(n1, n2, n3):
        a = 1
        b = 1
        c = 0
        while c <= n3:
            c = a + b
            if a == n1 and b == n2:
                return True
            a = b
            b = c
        return False

    def checkTab(T):
        length = len(T[0])
        for i in range(length):
            for j in range(length - 2):
                if T[i][j] + T[i][j+1] == T[i][j+2]:
                    if isFibo(T[i][j], T[i][j+1], T[i][j+2]):
                        return i + 1
        return "brak"

    print(checkTab(T))


def zadanie2():

    N = 20
    T = [randint(2, 20) for _ in range(N)]

    def rozklad(N):
        original = N
        ret = []
        i = 2
        while N > 1:
            while N % i == 0:
                if i == original:
                    return ret
                ret.append(i)
                N //= i
            i += 1
        return ret
    
    def isValid(pos, T, jump):
        length = len(T)
        if pos + jump > length - 2:
            return False
        return True
    
    def rek_check(T, position = 0, counter = 0, ret = [99999999]):
        length = len(T)
        if position == length - 2:
            if counter < ret[0]:
                ret[0] = counter
        
        czynniki = rozklad(T[position])

        for i in range(len(czynniki)):
            if isValid(position, T, czynniki[i]):
                rek_check(T, position + czynniki[i], counter + 1)
        if ret == [99999999]:
            return -1
        return ret[0]
            

    for i in range(N): print(T[i], end=" ")

    print("")
    print(rek_check(T))


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
        
        def printWartownik(self):
            if self.next != None:
                item = self.next
                while item.next.next != None:
                    print(item.val, end = ", ")
                    item = item.next
                print(item.val)

        def push(self, value):
            item = Node(value)
            item.next = self.next
            self.next = item
        
    def howMany5inBase8(num):
        counter = 0
        while num != 0:
            if num % 8 == 5:
                counter += 1
            num //= 8
        return counter

    def remNums(list):
        if list.next == None:
            return
        
        #new_list = Node()
        list_start = list
        prev_list = list

        list = list.next #dodac wartownik na koncu

        while list.next != None:
            value = list.val
            if howMany5inBase8(value) % 2 == 1:
                prev_list.next = list.next
                list_start.push(value)
            else:
                prev_list = prev_list.next
            list = list.next

        list = list_start
    
    list = Node()
    list.append(3)
    list.append(13)
    list.append(15)
    list.append(21)
    list.append(29)
    list.append(155)
    list.append(34)
    list.append(0) #wartownik

    list.printWartownik()
    print("-------------")
    remNums(list)
    list.printWartownik()
    
            








if "__main__" == __name__:

    zadanie1()
