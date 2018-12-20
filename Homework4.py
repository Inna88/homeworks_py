"""task 1"""


def solution_a(A):
    A.sort()
    result = 0
    for i, x in enumerate(A):
        if x > 0:
            if A[0] == 1:
                if A[i+1] - A[i] >= 2:
                    result = A[i] + 1
                elif A[i+1] - A[i] == 1:
                    result = A[-1] + 1
                print(result)
                break
            elif A[0] > 1:
                result = 1
                print(result)
                break
        elif x < 0:
            result = 1
    print(result)
    return result


solution_a([1, 2, 3])


"""task 2"""


def solution_n(N):
    if N > 0:
        longest_bin_gap = len(max(format(N, 'b').strip('0').split('1')))
        print("The longest binary gap of zeros is: ", longest_bin_gap)
    else:
        print("Please enter only positive numbers")
    return longest_bin_gap


solution_n(529)


"""task 3"""


def solution(A, K):
    if 0 <= K <= 100:
        for x in range(K):
            A = [A[-1]] + A[:-1]
        print(A)
    else:
        print("Please make sure that K is in range from 0 to 100")
    return A


solution([3, 8, 9, 7, 6], 3)