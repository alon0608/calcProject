from math import pow
from postfix_calculator import post_calc
from infix_to_postfix import in_to_post
from math_operations import Calculator
from str_to_lst import splitter
from Operators_dict import Operators
def main():
    lst = input("Enter your expression: ")
    lst3 = splitter(lst)
    print(lst3)
    lst2 = in_to_post(lst3)
    print(lst2)
    result = post_calc(lst2)
    print(f"The result is: {result}")
    main()

main()
