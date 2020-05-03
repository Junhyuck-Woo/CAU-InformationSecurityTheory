class Feistel(object):

    def __init__(self):
        pass

    def __mixer(self, p, k):
        return mid_code

    def __swapper(self, p):
        mid_code = p[31:] + p[:32]
        return mid_code

    def __des_function(self, p, k):
        return mid_code

    def run(self, input_string, key):
        mid_code = self.__mixer(input_string, key)
        mid_code = self.__swapper(mid_code)
        return mid_code