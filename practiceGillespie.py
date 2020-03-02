# Partner A: Peter Gillepsie
# Partner B: Andy Hou
#############

def getNRandom(n):
    '''takes in an integer and returns a list of n random integers between 1 and 10, inclusive'''
    retlist = []
    for x in range(n):
        retlist.append(rng.randint(1, 10))
    return retlist


def multiplyRandom(numbers):
    '''takes in a list of n numbers and returns the product of the numbers'''
    product = 1
    for n in numbers:
        product *= n
    return product

def main():
    print(multiplyRandom(getNRandom(10))

if __name__ == '__main__':
    main()
