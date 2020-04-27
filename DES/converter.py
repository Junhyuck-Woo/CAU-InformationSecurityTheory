import binascii

class Converter(object):

    # Initializer
    def __init__(self):
        pass

    def string_to_hex(self, string):
        hex_num = binascii.hexlify(string.encode())
        return hex_num.decode()


    def hex_to_bin(self, hex_num):
        bin_num = ""
        for i in hex_num:
            bin_num = bin_num + bin(int(i, 16))[2:].zfill(4)
        return bin_num


    def string_to_bin(self, string):
        hex_num = self.string_to_hex(string)
        bin_num = self.hex_to_bin(hex_num)
        return bin_num