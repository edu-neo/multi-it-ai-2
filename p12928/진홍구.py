def solution(n):
    answer = 0
    k = 1
    lst =[]
    for k in range(n):
        n += 1
        k += 1
        if n % k == 0:
            lst.append(k)
    answer = sum(lst)


    return answer