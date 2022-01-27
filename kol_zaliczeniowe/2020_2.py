from random import randint


def zadanie1():
    N = 5
    #T = [[randint(1,100)for _ in range(N)] for _ in range(N)]
    T= [[1,21,1,1,1],
        [21,24,21,1,1],
        [1,21,1,24,1],
        [1,1,24,21,24],
        [1,1,1,24,1]]
    def rozklad(num):
        ret = []
        i = 2
        while num != 1:
            while num % i == 0:
                ret.append(i)
                num //= i
            i += 1
        return ret

    def howManyInCommon(l1, l2):
        counter = 0
        length = len(l2)
        for item in l1:
            for i in range(length):
                if item == l2[i]:
                    counter +=1
        return counter
    
    def change(T):
        N = len(T[0])
        for i in range(N):
            for j in range(N):
                T[i][j] = rozklad(T[i][j])

    def four(T):
        ret = 0
        N = len(T[0])
        print(N)
        change(T)
        for i in range(1, N-1):
            for j in range(1, N-1):
                counter = 0
                if howManyInCommon(T[i][j], T[i+1][j]) == 1:
                    counter += 1
                if howManyInCommon(T[i][j], T[i-1][j]) == 1:
                    counter += 1
                if howManyInCommon(T[i][j], T[i][j+1]) == 1:
                    counter += 1
                if howManyInCommon(T[i][j], T[i][j-1]) == 1:
                    counter += 1
                if counter == 4:
                    ret += 1
        return ret

    print(four(T))

def zadanie3():
    class Node():
        def __init__(self,value=0):
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

    def repair(p):
        if p.next == None:
            return p
        p_cpy = p
        new_list = Node()
        new_list_start = new_list
        start = p_cpy
        prev = p_cpy
        p_cpy = p_cpy.next
        while p_cpy.next != None:
            if p_cpy.val % 2 == 0:
                value = p_cpy.val
                prev.next = p_cpy.next
                while new_list.next != None:
                    new_list = new_list.next
                new_list.next = Node(value)
                p_cpy = p_cpy.next
            else:
                prev = p_cpy
                p_cpy = p_cpy.next
        p_cpy.next = new_list_start.next
        p.next = start.next

    p = Node()
    p.append(1)
    p.append(2)
    p.append(12)
    p.append(3)
    p.append(6)
    p.append(5)
    p.append(4)
    p.append(1)
    p.print()
    repair(p)
    p.print()
    


            


if "__main__" == __name__:
    #zadanie1()
    zadanie3()