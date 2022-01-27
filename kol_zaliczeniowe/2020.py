
from hashlib import new


def zadanie1():
    def allqs(T):
        ret = []
        lengthT = len(T)
        for i in range(lengthT - 1):
            a1 = T[i][0]
            a2 = T[i][1]
            b1 = T[i+1][0]
            b2 = T[i+1][1]
            if a1 == 0:
                continue
            c = ((b1/a1)/(b2/a2))
            ret.append(c)
        return ret

    def count(qs):
        ret = 0
        for q in qs:
            counter = 0
            for i in range(len(qs)):
                if q == qs[i]:
                    counter+=1
            if counter > ret:
                ret = counter
        return ret

    def longest(T):
        qs = allqs(T)
        elements = count(qs) + 1 # +1 bo tyle jest elementów dla których q jest odpowiednie np: 1 3 6 9 -> q = 3 i jest takich 3, ale ememnty są 4 
        if elements < 3:
            return 0
        return elements

    T =   [(1,2),(2,3),(3,4),(4,5),(5,6)]
    print(longest(T))


def zadanie2(): #16:03

    def bitmask(n, length): #length = len(slowo) - 1
        mask = [0 for _ in range(length)]
        i = 0
        while n > 0:
            mask[i] = n%2
            n //= 2
            i += 1
        return mask
    
    def howManyVow(slowo, samogloski):
        counter = 0
        for litera in slowo:
            if litera in samogloski:
                counter +=1
        return counter

    def get_word(slowo, maska):
        ret = []
        ret.append(slowo[0])
        for i in range(len(maska)):
            if maska[i] == 1:
                ret.append("|")
            ret.append(slowo[i+1])
        return ret

    def isValid(new_slowo, samogloski, howmanyvow):
        flag = 0
        counter = 0
        for i in range(len(new_slowo)):
            if flag == 1 and new_slowo[i] in samogloski:
                return False
            if new_slowo[i] in samogloski:
                flag = 1
            if new_slowo[i] == "|":
                flag = 0
                counter += 1
        if counter != howmanyvow - 1:
            return False
        return True

    def cutting(slowo, samogloski = ["a", "e", "i", "o", "u"], counter = 0, mask = 0):
        if mask >= 2**(len(slowo)-1):
            return counter
        if mask == 0:
            slowo = list(slowo)
        maska = bitmask(mask, len(slowo) - 1)
        new_word = get_word(slowo, maska)
        howmanyvow = howManyVow(slowo, samogloski)
        if isValid(new_word, samogloski, howmanyvow):
            print(new_word)
            return cutting(slowo, samogloski, counter + 1, mask + 1)
        else:
            return cutting(slowo, samogloski, counter, mask + 1)

            
    print(cutting("student"))

    
def zadanie3():
    class Node:
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
                    
    def theR(p):
        a1 = p.next.val
        while p.next != None:
            p = p.next
        a2 = p.val
        if a1 > a2:
            return -1
        return 1

    def repair(p):
        counter = 0
        r = theR(p)
        a = p.next.val
        p = p.next
        while p.next != None:
            if p.next.val != a + r:
                a = a + r
                item = Node(a)
                item.next = p.next
                p.next = item
                p = p.next
                counter += 1
            else:
                a = a + r
                p = p.next
        print(counter)
    p = Node()
    p.append(-13)
    p.append(-3)
    p.append(6)
    p.print()
    print(theR(p))
    repair(p)
    p.print()
    



if "__main__" == __name__:
    #zadanie1()
    #zadanie2()
    zadanie3()