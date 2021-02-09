import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    freq = {} # (k, v) is value, frequency
    output = []
    for query in queries:
        if query[0] == 1:
            if query[1] in freq:
                freq[query[1]] += 1
            else:
                freq[query[1]] = 1
        elif query[0] == 2: #delete one if exists
            if query[1] in freq:
                if freq[query[1]] > 1:
                    freq[query[1]] -= 1
                else:
                    freq.pop(query[1])
                    
        else: #query[0] == 3, check freq
            count = 0
            for k in freq:
                if freq[k] == query[1]:
                    count = 1
                    break
            output.append(count)
    return output
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
