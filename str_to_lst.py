def splitter(expression):
    """gets a string and convert it into a list for easy work"""
    final_list=[]
    current=""
    counter=0
    for char in expression:
        #take care of Edge Cases like float number or number with factorial and more
        if char.isdigit() or char=="." or(char=="-" and current=="") or(char=="~" and current=="") or(char=="!" ):
            current+=char
        else:
            #push the number to the list and restart the current num
            if current:
                final_list.append(current)
                current=""
            #delete spaces
            if char!=" ":
                final_list.append(char)
    #check that we dont forget number after the loop
    if current:
        final_list.append(current)
    return final_list