#!/usr/bin/env python3

import sys

def palindrome(line: str):
    line=line.lower()
    return line[:]==line[::-1]
def number_palindrome(num: int):
    return int(str(num)[::-1])

def digits_of_two(power: int):
    return len(str(2**power))
def addition_arg():
    if len(sys.argv)<2:
        return "Nincs elég parancssori argumentum"
    else:
        return sys.argv[0]+sys.argv[1]
def addition(a: int, b: int):
    return a+b
def pretty_str(str_list):
    print ("{} {} {} ".format("test1", "test2","test3"))
    for element in str_list:
        print (f"{element[0]} {element[1]} {element[2]}")

def main():
    print(palindrome("Anna"))
    print(number_palindrome(1923))
    print(digits_of_two(256))
    print(addition_arg())
    print(addition(1,2))
    pretty_str([("ttest1",23121,22.0), ("ttest2",3124,3.141592),
              ("ttest3",1223,456.66), ("ttest4",1522213,456.012),])
    

if __name__ == "__main__":
    main()