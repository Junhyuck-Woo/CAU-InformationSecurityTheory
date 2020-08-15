import binascii
from converter import *
from feistel import *

class Key(object):

    shift_bits = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    key_list = []

    # Initializer
    def __init__(self):
        pass

    def generate(self, input_name="key.txt"):
        # Check whether input is string or text
        if ".txt" in input_name:
            f = open(input_name)
            content = f.readlines()[0].replace('\n', "")
            f.close()
            key = content
        else:
            key = input_name

        # Debugging
        print("Key: " + key)

        left = key[:28]
        right = key[28:]

        for i in self.shift_bits:
            left = self.shift(left, i)
            right = self.shift(right, i)
            key = self.compression(left, right)
            self.key_list.append(key)
        # Debugging
        print("======end=====")
        return self.key_list
        
    def compression(self, l, r):
        sk = l + r
        compression_key = sk[13] + sk[16] + sk[10] + sk[23] + sk[0] + sk[4] + sk[2] + sk[27] + \
        sk[14] + sk[5] + sk[20] + sk[9] + sk[22] + sk[18] + sk[11] + sk[3] + \
        sk[25] + sk[7] + sk[15] + sk[6] + sk[26] + sk[19] + sk[12] + sk[1] + \
        sk[40] + sk[51] + sk[30] + sk[36] + sk[46] + sk[54] + sk[29] + sk[39] + \
        sk[50] + sk[44] + sk[32] + sk[47] + sk[43] + sk[48] + sk[38] + sk[55] + \
        sk[33] + sk[52] + sk[45] + sk[41] + sk[49] + sk[35] + sk[28] + sk[31]
        return compression_key
    
    def shift(self, p, i):
        if i == 1:
            p = p[1:] + p[0]
        else:
            p = p[2:] + p[:2]
        return p