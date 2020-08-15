import binascii
from converter import *
from feistel import *
from keygenerator import *

class DES(object):

    conv = Converter()
    round = Feistel()
    k = Key()

    # Initializer
    def __init__(self):
        pass


    def __initial_permutation(self, p):
        output = p[57]+p[49]+p[41]+p[33]+p[25]+p[17]+p[9]+p[1]+\
        p[59]+p[51]+p[43]+p[35]+p[27]+p[19]+p[11]+p[3]+\
        p[61]+p[53]+p[45]+p[37]+p[29]+p[21]+p[13]+p[5]+\
        p[63]+p[55]+p[47]+p[39]+p[31]+p[23]+p[15]+p[7]+\
        p[56]+p[48]+p[40]+p[32]+p[24]+p[16]+p[8]+p[0]+\
        p[58]+p[50]+p[42]+p[34]+p[26]+p[18]+p[10]+p[2]+\
        p[60]+p[52]+p[44]+p[36]+p[28]+p[20]+p[12]+p[4]+\
        p[62]+p[54]+p[46]+p[38]+p[30]+p[22]+p[14]+p[6]
        return output
    

    def __final_permutation(self, p):
        output = p[39]+p[7]+p[47]+p[15]+p[55]+p[23]+p[63]+p[31]+\
        p[38]+p[6]+p[46]+p[14]+p[54]+p[22]+p[62]+p[30]+\
        p[37]+p[5]+p[45]+p[13]+p[53]+p[21]+p[61]+p[29]+\
        p[36]+p[4]+p[44]+p[12]+p[52]+p[20]+p[60]+p[28]+\
        p[35]+p[3]+p[43]+p[11]+p[51]+p[19]+p[59]+p[27]+\
        p[34]+p[2]+p[42]+p[10]+p[50]+p[18]+p[58]+p[26]+\
        p[33]+p[1]+p[41]+p[9]+p[49]+p[17]+p[57]+p[25]+\
        p[32]+p[0]+p[40]+p[8]+p[48]+p[16]+p[56]+p[24]
        return output


    def encrypt(self, input_name):
        # Check whether input is string or text
        if ".txt" in input_name:
            f = open(input_name)
            content = f.readlines()[0].replace('\n', "")
            f.close()
            plaintext = content
        else:
            plaintext = input_name

        # Check the input length, make as 64 bits
        if len(plaintext) < 8:
            for i in range(8-len(plaintext)):
                plaintext = plaintext + " "
        elif len(plaintext) > 8:
            print("Error: Long input")
            exit()

        # Debugging
        print("Input: " + plaintext)

        # convert to binary
        input_string = self.conv.string_to_bin(plaintext)
        
        # initial permutation
        mid_string = self.__initial_permutation(input_string)

        #
        key = self.k.generate()

        # Round
        for i in range(0, 16):
            mid_string = self.round.run(mid_string, key[i])

        final_string = self.__final_permutation(mid_string)

        # Save the cipher


        # Debugging
        print("Output: " + final_string)
        return final_string

    def decrypt(self, cipher):

        # Debugging
        print("Input: " + cipher)

        
        # initial permutation
        mid_string = self.__final_permutation(cipher)

        #
        key = self.k.generate()

        # Round
        for i in range(0, 16):
            mid_string = self.round.run(mid_string, key[i])

        final_string = self.__initial_permutation(mid_string)

        # Save the cipher


        # Debugging
        print("Output: " + final_string)
        return final_string