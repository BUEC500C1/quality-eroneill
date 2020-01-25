# EC500 Hw1
# Copyright 2020  Erin K O'Neill erinkate@bu.edu

# convert arabic numerals to roman 
# first pass no edge cases/error checking 

import string 


def convertnum(x):
    """convert the integer x into a string representation of x in roman numerals"""
    # first set up our lists 
    roman = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    arabic = [1000, 500, 100, 50, 10, 5, 1] 
    # divide thru each value and go down 
    stringrom = ""
    xval = x
    for conval in range(len(arabic)):
        nxtlet = xval//arabic[conval]
        xval = xval%arabic[conval]
        for i in range(nxtlet):
            stringrom += roman[conval]
        
    return str(stringrom)

def main():
    print(convertnum(111) + " should be CXI")

if __name__ == '__main__':
    main()