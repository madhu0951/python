
#All combinations for given numbers in list whose sum is 10

def combinations(iterable):
    if len(iterable)==0:
        return [[]]
    combos=[]
    a=combinations(iterable[1:])
    for combo in a:
        combos+=[combo,combo+[iterable[0]]]
    return combos

numbers=[1,2,3,4,5]
combos=combinations(numbers)
for x in combos:
    if sum(x)==10:
        print(x)

