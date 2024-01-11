def maxFreq(s):
    frequency = {}
    max_freq = 0
    for num in s:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
        if frequency[num] > max_freq:
            max_freq = frequency[num]
    return max_freq
test=int(input())
for _ in range(test):
    n=int(input())
    s=input()
    maxcount=maxFreq(s)
    if maxcount<=(n//2):
        print(n%2)
    else:
        print(n-2*(n-maxcount))
 
