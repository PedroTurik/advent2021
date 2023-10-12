from math import ceil, floor

LEFT = 0
RIGHT = 1
STOP = 3

def calculate_magnitude(snail):
    if type(snail) is int:
        return snail

    return 3*calculate_magnitude(snail[LEFT]) + 2*calculate_magnitude(snail[RIGHT])

def __add_explode(s, direction, n):
    if type(s) is int: raise RuntimeError("BLABLAB")

    if type(s[direction]) is int:
        s[direction] += n
    else:
        __add_explode(s[direction], direction, n)  

def explode(s, dives):
    if type(s) is int:
        return None

    if dives >= 4:
        for SideA, SideB in ((LEFT, RIGHT),(RIGHT, LEFT)):
            if type(s[SideA]) is list:
                if type(s[SideB]) is list:
                    s[SideB][SideA] += s[SideA][SideB]
                else:
                    s[SideB] += s[SideA][SideB]
                
                val = s[SideA][SideA]
                s[SideA] = 0
                return (val, SideA) 
            
        return None
    
    for i in (LEFT, RIGHT):
        res = explode(s[i], dives+1)

        if type(res) is tuple:
            val, side = res

            if side == i:
                return res
                        
            if type(s[side]) is int:
                s[side] += val
            else:
                __add_explode(s[side], i, val)
        

            return STOP

        if res == STOP:
            return STOP

    


def split_snail(s) -> bool:
    if type(s) is int: return False

    for index in (LEFT,RIGHT):
        if type(s[index]) is int and s[index] >= 10:
            s[index] = [floor(s[index]/2), ceil(s[index]/2)]
            return True
    
        if split_snail(s[index]):
            return True
    
    return False
    


def add_snail(a, b):
    return [a, b]


def reduce(s):
    while True:
        if explode(s, 1):
            continue
        if split_snail(s):
            continue
        break