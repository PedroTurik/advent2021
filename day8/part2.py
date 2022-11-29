with open('input2.txt') as f:
    data = f.readlines()
    outputs = [x.strip().split('|')[1].split(' ')[1:] for x in data]
    displays = [x.strip().split('|')[0].split(' ')[:-1] for x in data]

def infer_5(display, o):
    for s in display:
        if len(s) == 2: um = s
        if len(s) == 4: quatro = s

    if all([x in o for x in um]):
        return '3'
    elif len([x for x in o if x in quatro]) == 3:
        return '5'
    else:
        return '2'


def infer_6(display, o):
    for s in display:
        if len(s) == 2: um = s
        if len(s) == 4: quatro = s

    if all([x in o for x in quatro]):
        return '9'
    elif any([x not in o for x in um]):
        return '6'
    else:
        return '0'




def infer_number(display, o):
    if len(o) == 2: return '1'
    if len(o) == 3: return '7'
    if len(o) == 4: return '4'
    if len(o) == 7: return '8'
    if len(o) == 5: return infer_5(display, o)
    if len(o) == 6: return infer_6(display, o)




def infer_output(display, output):
    out = ""
    for o in output:
        out += infer_number(display, o)
    return int(out)



def main(outputs, displays):
    ans = 0
    for disp, out in zip(displays, outputs, strict=True):
        ans += infer_output(disp, out)
    return ans


if __name__=="__main__":

    with open('input2.txt') as f:
        data = f.readlines()
        outputs = [x.strip().split('|')[1].split(' ')[1:] for x in data]
        displays = [x.strip().split('|')[0].split(' ')[:-1] for x in data]

    print(main(outputs, displays))