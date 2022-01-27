from random import randint

def zadanie1():

    def NWD(num1, num2):
        if num2>0:
            return NWD(num2, num1%num2)
        return num1

    def check(T):
        N = len(T[0])
        for H_X in range(N-1):
            for H_Y in range(N):
                for V_X in range(N):
                    for V_Y in range(N-1):

                        if ((V_X == H_X) or (V_X == H_X + 1) or (H_Y == V_Y) or (H_Y) == (V_Y + 1)):
                            continue
                        if NWD(T[H_X][H_Y], NWD(T[H_X + 1][H_Y], NWD(T[V_X][V_Y], T[V_X][V_Y + 1]))) == 4:
                            return True
        return False

    N = 10
    T = [[randint(1, 20) for _ in range(N)] for _ in range(N)]

    print(check(T))

if "__main__" == __name__:
    zadanie1()