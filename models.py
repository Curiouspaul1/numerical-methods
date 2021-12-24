from helpers import get_sup
import json


class Functions:
    #  models a function of 4 variables
    def __init__(self, order=4, a=0, b=0, c=0, d=0, k=0) -> None:
        self.order = order
        self.a = [a, None]
        self.b = [b, None]
        self.c = [c, None]
        self.d = [d, None]
        self.k = [k, None]
        self.term_map = {
            1: self.a,
            2: self.b,
            3: self.c,
            4: self.d,
            5: self.k
        }
        count_ = len(self.term_map.values())-1
        for i in self.term_map.values():
            i[1] = count_
            count_ -= 1

    def __repr__(self) -> str:
        ans = ""
        ord_ = self.order
        for i in range(1, self.order+2):
            if ord_ == 0:
                ans += (f"{self.term_map[i][0]}")
                break
            elif ord_ == 1:
                ans += (f"{self.term_map[i][0]}x + ")
            else:
                ans += (f"{self.term_map[i][0]}x{get_sup(str(ord_))} + ")
            ord_ -= 1
        return repr(ans)

    def derivative(self):
        # find the derivative
        print(self.a)
        self.a[0] = self.a[0] * self.a[1]
        self.b[0] = self.b[0] * self.b[1]
        self.c[0] = self.c[0] * self.c[1]
        self.d[0] = self.d[0] * self.d[1]
        self.k[0] = self.k[0] * self.k[1]
        self.order -= 1
        self.a[1] -= 1
        self.b[1] -= 1
        self.c[1] -= 1
        self.d[1] -= 1
        return self

    def eval(self, x: float):
        result = 0
        for i in range(1, self.order+2):
            if i == 5:
                result += self.term_map[i][0]
                break
            result += self.term_map[i][0] * pow(x,self.term_map[i][1])
        return result


class Newton:
    def __init__(self, fx: Functions, initial_guess: float, nit: int) -> None:
        self.fx = fx
        self.nit = nit

    def findroots(self, root):
        count_ = self.nit
        root = root
        while count_ > 0:
            root = root + self.fx.derivative().eval(root)
            self.findroots(root)
            count_ -= 1
        return root


class Secant:
    pass


class Falsi:
    pass

