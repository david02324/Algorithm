from itertools import permutations
import re

def solution(expression):
    oper = [char for char in expression if not char.isdigit()]
    operand = re.split(r'[+,\-,*]',expression)
            
    oper_set = set(oper)
    oper_count = len(oper_set)
    oper_li = list(permutations(oper_set,oper_count))
    max_value = 0
    
    
    for priority_tuple in oper_li:
        oper_copy = oper[:]
        operand_copy = operand[:]
        for operator in priority_tuple:
            i = 0
            while i < len(oper_copy):
                if oper_copy[i] == operator:
                    del oper_copy[i]
                    operand_copy[i] = str(eval(operand_copy[i]+operator+operand_copy[i+1]))
                    del operand_copy[i+1]
                else:
                    i += 1
        

        max_value = max(abs(int(operand_copy[0])),max_value)
        
    return max_value