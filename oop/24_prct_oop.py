'''Create a class C2-d vector and use it to create another class representing a 3-d vector'''


class C2dVec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self) -> str:
        return f"{self.icap}i + {self.jcap}j"


class C3dVec(C2dVec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self) -> str:
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"


V2d = C2dVec(1, 4)
V3d = C3dVec(3, 2, 6)
print(V2d)
print(V3d)
