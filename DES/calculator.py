class Calculator(object):

    def __init__(self):
        pass

    def xor(self, a, b):
        # check the input length
        if (len(a) != len(b)):
            print("Different input size")

        result = ""

        for i, j in zip(a, b):
            if (i==j):
                result = result + '0'
            else:
                result = result + '1'
        
        return result
