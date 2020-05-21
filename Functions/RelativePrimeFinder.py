import sys

class RelativePrimeFinder (object):
    
    n = 0
    count = 0
    a_list = []

    def __init__(self, n):
        self.n = int(n)

    def find(self):
        for a in range(self.n):
            self.count=0
            for i in range(2, self.n):
                if (a%i==0) and (self.n%i==0):
                    self.count = self.count + 1
                    break
            if self.count==0:
                self.a_list.append(a)
        print(self.a_list)


if __name__ == "__main__":
    # Check the input commend
    if len(sys.argv) != 2:
        print("Input error")
        exit()

    rpf = RelativePrimeFinder(sys.argv[1])
    rpf.find()