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

    def bin_to_hex(self, bin_num):
        bin_len = len(bin_num)
        hex_num = hex(int(bin_num, 2))[2:]
        if bin_len % 4  != 0:
            hex_num = '0' + hex_num
        return hex_num

    def string_to_bin(self, string):
        hex_num = self.string_to_hex(string)
        bin_num = self.hex_to_bin(hex_num)
        return bin_num
    
    def bin_to_dec(self, bin_num):
        mul = 1
        r_bin_num = bin_num[::-1]
        for i in r_bin_num:
            dec_num += mul*int(i)
            mul *= 2
        return str(dec_num)