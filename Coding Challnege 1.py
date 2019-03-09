def solution(S, K):
    # write your code in Python 3.6
    newString = ''
    count = 0
    for i in range(0, len(S)):
        if (count == K):
            newString += '-'
            count = 0
            # i = i + 1
        if (S[i] != '-'):
            newString += S[i]
            count = count + 1
    newString2 = newString.upper()
    return newString2
