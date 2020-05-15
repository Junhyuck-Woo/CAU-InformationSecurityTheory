import sys

class FastExponentiation(object):
    y = 1
    a = 0
    n = 0
    x = "111001"

    def __init__(self, n, a):
        self.a = int(a)
        self.n = int(n)
    
    def calculate(self):
        for i in range(6):
            if int(self.x[i]) == 1:
                self.y = (self.y * self.a)%self.n
            self.a = (self.a*self.a)%self.n
        print(self.y)
        return self.y








if __name__ == "__main__":
    # Check the input commend
    if len(sys.argv) != 3:
        print("Input error")
        exit()
    fe = FastExponentiation(sys.argv[1], sys.argv[2])
    fe.calculate()

