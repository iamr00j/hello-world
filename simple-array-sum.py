#https://www.hackerrank.com/challenges/simple-array-sum/problem

def simpleArraySum(ar):
    #
    # Write your code here.
    sum = 0
    for x in range(len(ar)):
        sum += ar[x]    
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
