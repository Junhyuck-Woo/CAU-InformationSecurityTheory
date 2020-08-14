import sys


class FastExponentiation(object):
    y = 1
    a = 0
    n = 0
    x = ""

    def __init__(self, a, x, n):
        self.a = int(a)
        self.n = int(n)
        self.genString(int(x))

    def calculate(self):
        for i in range(len(self.x)-1, -1, -1):
            if int(self.x[i]) == 1:
                self.y = (self.y * self.y * self.a) % self.n
            else:
                self.y = (self.y * self.y) % self.n
        print(self.y)
        return self.y

    def genString(self, x):
        while (x != 1):
            i = int(x % 2)
            self.x = self.x + str(i)
            if i == 1:
                x = (x - 1) / 2
            else:
                x = x / 2
        self.x = self.x + str(1)


if __name__ == "__main__":
    # Check the input commend
    if len(sys.argv) != 4:
        print("Input error")
        exit()
    fe = FastExponentiation(sys.argv[1], sys.argv[2], sys.argv[3])
    fe.calculate()

