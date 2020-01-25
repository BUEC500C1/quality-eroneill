# EC500 Hw1
# Copyright 2020  Erin K O'Neill erinkate@bu.edu

# convert arabic numerals to roman 
# first pass no edge cases/error checking 

import string 


def convertnum(x):
    """convert the integer x into a string representation of x in roman numerals"""
    
    # base 6 is 0-5 in each position so divide by 6, save % and keep rolling 
    stringsix = ""
    if x < 6:
        stringsix = str(x%6)
        return stringsix
    while x > 0 : 
        firstsix = int(x%6)
        x = (x-firstsix)/6
        stringsix = str(firstsix) + stringsix
    return str(stringsix)

def main():
    print(convertnum(48))

if __name__ == '__main__':
    main()