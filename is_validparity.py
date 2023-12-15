"""
(3 points) Implement a function called is_valid_parity. It accepts two strings called codeword
           and parity.

           The is_valid_parity function returns True if codeword is parity-encoded correctly. If it
           is not, the function returns False.

           A parity-encoded codeword is a series of binary digits (zeros and ones) where the
           left-most digit has been prepended  to some original number. The left-most digit we
           prepend is either a zero or one depending on the type of parity being used (EVEN or ODD).

           If a word is encoded with EVEN parity the total number of 1 bits in the codeword
           must be an even number.

           If a word is encoded with ODD parity the total number of 1 bits in the codeword
           must be an odd number.

           For example if the original word is 1001:

               an EVEN codeword is 01001 (2 is even, so we prepend a 0 to keep it even)

               an ODD codeword is 11001 (2 is even, so prepend a 1 to make it odd)

           Your function must accept a string codeword (the original value with the parity bit
           prepended to it) and a parity (EVEN or ODD) as parameters and return True if the
           codeword has been correctly parity-encoded, else False.

(3 points) Prove your function works by testing with these unit tests, i.e., assert that:

           is_valid_parity("101", "EVEN") returns True
           is_valid_parity("11", "EVEN") returns True
           is_valid_parity("111111111100000000001010110101", "EVEN") returns True
           is_valid_parity("10", "ODD") returns True
           is_valid_parity("111", "ODD") returns True
           is_valid_parity("1111111111000011111000001010110101", "ODD") returns True
           is_valid_parity("111", "EVEN") returns False
           is_valid_parity("11111111100000000001010110101", "EVEN") returns False
           is_valid_parity("11", "ODD") returns False
           is_valid_parity("101", "ODD") returns False
           is_valid_parity("11111111111000011111000001010110101", "ODD") returns False
"""

def main():
    pass


if __name__ == "__main__":
    main()
