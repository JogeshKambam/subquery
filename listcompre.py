nums=[2,3,4,5,7,8,10]
squares=[x*x for x in nums]
print(squares)

num1=[1,3,6,5,8,12,35,77,82,91]
even=[x for x in num1 if x%2==0]
print(even)

str=["hello","world","python","programming"]
leng=[len(x) for x in str]
print(leng)

nums2=[1,4,7,-1,13,-7]
replace_negative=['0' if x<=0 else x for x in nums2]
print(replace_negative)


list_a=[1,2,3]
list_b=['a','b','c']
def pairs(list_a, list_b):
    return [(a, b) for a in list_a for b in list_b]
print(pairs(list_a, list_b))

def flatten(matrix):
    return [num for row in matrix for num in row]
print(flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def primes(nums):
    return [n for n in nums if is_prime(n)]


print(primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 11]))


def unique_chars(strings):
    result = []

    for s in strings:
        for ch in s:
            if ch not in result:
                result.append(ch)

    return result


print(unique_chars(["apple", "banana"]))

def weighted_sum(pairs):
    return [value * weight for value, weight in pairs]


print(weighted_sum([(2, 3), (4, 5), (6, 2)]))

def matrix_transpose(matrix):
    return [[matrix[row][col] for row in range(len(matrix))]
            for col in range(len(matrix[0]))]


print(matrix_transpose([[1, 2, 3], [4, 5, 6]]))
