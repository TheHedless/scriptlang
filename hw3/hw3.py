#!/usr/bin/env python3

def prod(num_list: list[int])->int:
    helper_int=1
    for item in num_list:
        helper_int*=item
    return helper_int

def read_text(text: str) -> str:
    letter_dict: dict = {
        "3" : "E",
        "4" : "A",
        "0" : "O",
        "1" : "I",
        "7" : "T",
        "5" : "S"
    }
    for number,letter in letter_dict.items():
        text=text.replace(number,letter)
    return text
def palindrome_iterative(line: str):
    line=line.lower()
    return line[:]==line[::-1]

def palindrome_recursive(text: str)->bool:
  text=text.lower()
  if len(text) <= 1:
    return True
  else:
    return text[0] == text[-1] and palindrome_recursive(text[1:-1])

def hugo_helper(text: str)->str:
   return " ".join(text.split())

def decoder(text: str)-> str:
    helper_str=""
    for letter in text:
        if letter.isalpha():
            start_pos= ord('A') if letter.isupper() else ord('a')
            helper_str+=chr((ord(letter)-start_pos+2) % 26+start_pos)
        else:
            helper_str+=letter
    return helper_str

def main():
    print(prod([1,2,3,4]))

    TEXT: str="""
3Z 4Z UZ3N37 4Z7 4 C3L7 5Z0LG4LJ4, H0GY B3B1Z0NY1754
M1LY3N C50D4L4705 D0LG0KR4 K3P35 4Z 3LM3.
3LK3P35Z70 D0LG0KR4! N3H3Z V0L7 3L05Z0R 3L0LV45N0D
3Z7, D3 M1R3 1D33R5Z 3HH3Z 4 50RH0Z, 4Z 3LM3D
4U70M471KU54N 3L 7UDJ4 0LV45N1.
4N3LKUL H0GY G0ND0LK0DN0D K3LL3N3 R4J74.
L3GY BU5ZK3! C54K K3V35 3MB3R K3P35 3L0LV45N1 3Z7.
H4 7375Z377, 05ZD M3G M450KK4L 15!"""
    print(read_text(TEXT))
    print(palindrome_iterative("Anna"))
    print(palindrome_recursive("Anna"))
    """
    # needs 3.10 or newer python to work
    inp = input("Do you really want to quit [y/Y/yes]? ")
    match inp:
        case "y" | "Y" | "yes":
            print('bye')
            sys.exit(0)
        case _:
            print('The show goes on...')
            """
    print(hugo_helper("  valami    sdadas "))

    father_text: str="""
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb    
"""
    print(decoder(father_text))

    
if __name__=="__main__":
    main()