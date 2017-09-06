# if an element is 0, set its entire row and col to 0
def set_zeros(matrix):
    m, n = len(matrix), len(matrix[0])
    # record the state before the row is marked
    first_row_has_zero = not all(matrix[0])
    # first row/col as marker
    for i in range(1, m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    # set zeros
    for i in range(1, m):
        for j in range(n - 1, -1, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    # update the first row
    if first_row_has_zero:
        for j in range(n):
            matrix[0][j] = 0


def longest_palindrome(s):
    palindrome = ''
    for i in range(len(s)):
        # get a palindrome of odd length
        palindrome_odd = expand_palindrome(s, i, i)
        if len(palindrome_odd) > len(palindrome):
            palindrome = palindrome_odd
        # get a palindrome of even length
        palindrome_even = expand_palindrome(s, i, i + 1)
        if len(palindrome_even) > len(palindrome):
            palindrome = palindrome_even
    return palindrome


def expand_palindrome(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]


def max_sub_array(nums):
    if not nums:
        return 0
    curr_sum = nums[0]
    max_sum = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        # if curr_sum < 0, have a new start, otherwise accumulate
        curr_sum = max(num, curr_sum + num)
        max_sum = max(curr_sum, max_sum)
    return max_sum


# the array has at least one number
def max_prodcut_array(nums):
    res = pmax = pmin = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        # multiplied by a negative makes big number smaller
        if num < 0:
            pmax, pmin = pmin, pmax
        # either have a new start or further product
        pmax = max(num, pmax * num)
        pmin = min(num, pmin * num)
        # compare with global maximum
        res = max(res, pmax)

    return res


# Merge Intervals
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def merge_intervals(intervals):
    if len(intervals) <= 1:
        return intervals
    intervals.sort(key=lambda inter: inter.start)
    merged = []
    for inter in intervals:
        # list out three situations:
        # 1. merged is empty => append interval
        # 2. merged is not empty, last.end < inter.start => append interval
        # 3. merged is not empty, last.end >= inter.start => update last.end
        if merged and merged[-1].end >= inter.start:
            merged[-1].end = max(merged[-1].end, inter.end)
        else:
            merged.append(inter)
    return merged


# things to handle:
# surrounding whitespace chars
# + or - sign
# letters following digits can be ignored
# integer should be within int range
# return 0 for invalid input
def my_atoi(s):
    s = s.strip()
    if len(s) == 0:
        return 0
    chars = list(s)

    sign = -1 if chars[0] == '-' else 1
    if chars[0] in ['+', '-']:
        del chars[0]
    
    res, i = 0, 0
    digits = '0123456789'
    while i < len(chars) and chars[i] in digits:
        res = res * 10 + digits.index(chars[i])
        i += 1
    
    # return val in the range of [INT_MIN, INT_MAX]
    return max(-2 ** 31, min(sign * res, 2 ** 31 - 1))


# Valid Number
def is_numeric(s):
    # define a DFA
    # type of char => state
    state = [{},
            {'blank': 1, 'sign': 2, 'digit': 3, '.': 4},
            {'digit': 3, '.': 4},
            {'digit': 3, '.': 5, 'e': 6, 'blank': 9},
            {'digit': 5},
            {'digit': 5, 'e': 6, 'blank': 9},
            {'sign': 7, 'digit': 8},
            {'digit': 8},
            {'digit': 8, 'blank': 9},
            {'blank': 9}]
    current_state = 1
    # recognize the type of each char
    for c in s:
        if c >= '0' and c <= '9':
            c = 'digit'
        if c == ' ':
            c = 'blank'
        if c in ['+', '-']:
            c = 'sign'
        if c not in state[current_state].keys():
            return False
        # jump to a new state
        current_state = state[current_state][c]
    # is numeric only if the final state is in the following
    if current_state not in [3, 5, 8, 9]:
        return False
    return True
