from calculator import *

class Feistel(object):

    def __init__(self):
        cal = Calculator()
        pass

    def __mixer(self, l, r, k):
        right = r
        f_ = self.__des_function(r, k)
        left = cal.xor(l, f_)
        return left, right

    def __swapper(self, l, r):
        mid_code = r + l
        return mid_code

    def __des_function(self, p, k):

        return 

    def run(self, input_string, key):
        left_text = input_string[:32]
        right_text = input_string[31:]

        left_text, right_text = self.__mixer(left_text, right_text, key)
        mid_code = self.__swapper(left_text, right_text)
        return mid_code