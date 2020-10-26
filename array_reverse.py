# array reversal in python

def reverseArray(a):
    x = len(a)-1
    y = 0
    while y<x:
        temp = a[x]
        a[x] = a[y]
        a[y] = temp
        x=x-1
        y=y+1
    return a

    # return a[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
