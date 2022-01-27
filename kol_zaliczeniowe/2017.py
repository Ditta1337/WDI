from random import randint


def zadanie1():
    N = 9
    #T = [randint(1, 10) for _ in range(N)]
    T = [1, 2, 3, 1, 5, 2, 2, 2, 6]
    
    def bitmask(n, length): #length = len(N) - 1
        ret = [0 for _ in range(length)]
        i = 0
        while n > 0:
            ret[i] = n%2
            n //= 2
            i += 1
        return ret
    
    def devide(T, mask):
        ret = []
        ret.append(T[0])
        for i in range(len(mask)):
            if mask[i] == 1:
                ret.append("|")
            ret.append(T[i+1])
        return ret

    def isValid(new_tab):
        tmp = []
        sum = 0
        counter = 0
        for i in range(len(new_tab)):
            if new_tab[i] != "|":
                sum += new_tab[i]
            else:
                tmp.append(sum)
                counter += 1
                sum = 0
        elem = tmp[0]
        for k in range(len(tmp) - 1):
            if elem != tmp[k + 1]:
                return False
        return counter + 1 #zwraca ilość kawałków


    def cut_rek(T, counter = 0, n = 1):
        length = len(T)
        if n >= 2**(length - 1):
            return counter
        maska = bitmask(n, length - 1)
        new_tab = devide(T, maska)
        var = isValid(new_tab)
        if var:
            if var > counter:
                counter = var
        return cut_rek(T, counter, n + 1)

    print(cut_rek(T))

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

    
    def delete(l1, l2):
        ret_list = Node()
        if l1.next == None or l2.next == None:
            return ret_list

        l1_cpy = l1
        l1_cpy2 = l1
        l2_cpy = l2
        l2_cpy2 = l2
        l1_prev = l1_cpy
        l2_prev = l2_cpy

        l1_cpy = l1_cpy.next
        l1_cpy2 = l1_cpy2.next
        l2_cpy = l2_cpy.next
        l2_cpy2 = l2_cpy2.next

        l1_start = l1_prev
        l2_start = l2_prev
        print("------")
        l1.print()
        print("------")
        l1_cpy2.print()
        print("------")
        
        #usuwanie z l1 elementów wspolnych z l2
        while l1_cpy != None:
            flag = 0
            value = l1_cpy.val
            while l2_cpy2 != None:
                if value == l2_cpy2.val:
                    flag = 1
                    ret_list.append(value)
                    break
                if value > l2_cpy2.val:
                    l2_cpy2 = l2_cpy2.next
                else:
                    break
            if flag == 1:               
                l1_prev.next = l1_cpy.next
            else:  
                l1_prev = l1_prev.next
            l1_cpy = l1_cpy.next

        l1.next = l1_start.next


        #usuwanie z l2 elementów wspolnych z l1
        while l2_cpy != None:
            flag = 0
            value = l2_cpy.val
            while l1_cpy2 != None:
                if value == l1_cpy2.val:
                    flag = 1
                    ret_list.append(value)
                    break
                if value > l1_cpy2.val:
                    l1_cpy2 = l1_cpy2.next
                else:
                    break
            if flag == 1:               
                l2_prev.next = l2_cpy.next
            else:  
                l2_prev = l2_prev.next
            l2_cpy = l2_cpy.next

        l2.next = l2_start.next
        return ret_list

                    


        
    l1 = Node()
    l2 = Node()

    l1.append(1)
    l1.append(4)
    l1.append(5)
    l1.append(7)
    l1.append(8)

    l2.append(-1)
    l2.append(1)
    l2.append(3)
    l2.append(4)
    l2.append(8)

    l1.print()
    l2.print()

    l3 = delete(l1, l2)

    l1.print()
    l2.print()
    l3.print()








if "__main__" == __name__:
    zadanie3()

