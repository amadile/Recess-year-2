#Question 1
def isValid(s):
    stack = []
    matching_bracket = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in matching_bracket.values():
            stack.append(char)
        elif char in matching_bracket.keys():
            if stack == [] or matching_bracket[char] != stack.pop():
                return False
        else:
            return False
    return stack == []

#Question2:
def odd_frequency_count(paragraph):
    from collections import Counter
    freq = Counter(paragraph)
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)
    return odd_count
#Question 3:
def odd_squares_sum(limit):
    total = 0
    n = 1
    while n <= limit:
        if n % 2 != 0:
            total += n * n
            yield total
        n += 1
#Question 4:
import numpy as np

oddSumList = np.array(list(odd_squares_sum(20)))
#Question 5:
mergedList = [(x, x % 5) for x in oddSumList]
#Question 6:
def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a
#question 7:
def get_3_nearest(pt, ptlist):
    def l1_norm(p1, p2):
        return sum(abs(a - b) for a, b in zip(p1, p2))
    
    ptlist.sort(key=lambda p: l1_norm(pt, p))
    return ptlist[:3]
#Question 8:
import numpy as np

def diagonal_vector(M):
    return np.abs(np.diagonal(M))
#Question 9:
def flatten_reverse_lists(lists):
    flat_list = [item for sublist in lists for item in sublist]
    flat_list.sort()
    return flat_list
