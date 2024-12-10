from xmlrpc.client import boolean
from Minus_Check import minus_checker
from Operators_dict import Operators

def splitter(expression):
    final_list=[]
    current=""
    counter=0
    for char in expression:
        if char.isdigit() or char=="." or(char=="-" and current=="") or(char=="~" and current=="") or(char=="!" ):
            current+=char
        else:
            if current:
                final_list.append(current)
                current=""
            if char!=" ":
                final_list.append(char)

    if current:
        final_list.append(current)
    final_list1=minus_checker(final_list)
    return final_list1







