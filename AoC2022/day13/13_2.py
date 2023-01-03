from functools import cmp_to_key

def main():
    input = open('input13.txt').read().split('\n\n')
    packets = [[[2]],[[6]]]

    for packetpair in input:
        lists = [eval(x) for x in packetpair.splitlines()] # Don't try this at home! 
        packets.extend(lists)
    
    packets = sorted(packets, key = cmp_to_key(comparer),reverse=True)
    print((packets.index([[2]])+1) * (packets.index([[6]])+1))

def comparer(left,right):
    return 1 if compare_lists(left,right) else -1

def compare_lists(left,right):
    idx = 0
    for idx,elem in enumerate(left):
        try:
            if type(elem) == int and type(right[idx]) == int:
                if elem > right[idx]: return 0
                if elem < right[idx]: return 1
            if type(elem) == list and type(right[idx]) == list:
                cmp = compare_lists(elem,right[idx])
                if  cmp!= -1:
                    return cmp
            if bool(type(elem) == list) ^ bool(type(right[idx]) == list): #xor
                elem = [elem] if type(elem) == int else elem
                rightlist = [right[idx]] if type(right[idx]) == int else right[idx]
                cmp = compare_lists(elem,rightlist)
                if  cmp!= -1:
                    return cmp
        except IndexError:
            return False

    return 1 if len(right)>len(left) else -1     
    
if __name__ == "__main__":
    main()
