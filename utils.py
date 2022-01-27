def NWD(num1, num2):
    if num2>0:
        return NWD(num2, num1%num2)
    return num1


def isPrime(N):
        if N < 2:
            return False
        for i in range(2, N//2 + 1):
            if N % i == 0:
                return False
        return True

def rozklad(num):
    ret=[]
    i=2
    while num!=1:
        while num%i == 0:
            ret.append(i)
            num //= i
        i += 1
    return ret

def canDivide():
    T = [1,2,3,4,5,6,7,8,9,10,5]
    sums = [0,0,0,0,0,0]
    def canDivide_rek(index, sums):
        if index == len(T):
            all_even = 1
            for i in range(len(sums) - 1):
                if sums[i] != sums[i+1]:
                    all_even = 0
                    break
            if all_even:
                return True
            return False
        for i in range(len(sums)):
            sums[i] += T[index]
            if (canDivide_rek(index + 1, sums)):
                return True
            sums[i] -= T[index]
        return False
    return canDivide_rek(0, sums)


if "__main__" == __name__:
    print(NWD(8, 4))