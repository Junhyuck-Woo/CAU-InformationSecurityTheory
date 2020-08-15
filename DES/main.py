from des import DES
import sys

def main(f_input="input.txt"):
    cipher = DES()
    #cipher.encrypt("abcdefgh")
    c = cipher.encrypt(f_input)
    p = cipher.decrypt(c)


if __name__ == "__main__":
	#main(sys.argv[1])
    main()

