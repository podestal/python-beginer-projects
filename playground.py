import math

# def is_staircase(nums):
#     col_length = 0
#     staircase = []
#     input_list = nums.copy()

#     while len(input_list) > 0:
#         col_length = col_length + 1
#         column = []

#         for i in range(0, col_length):
#             column.append(input_list.pop(0))

#             if (len(input_list) == 0):
#                 if i < col_length - 1:
#                     return False
#                 staircase.append(column)
#                 return staircase
#         staircase.append(column)

# print(is_staircase( [1, 2, 3, 4, 5, 6, 7]))

# def isPrime(n):
#     end = math.floor(math.sqrt(n)) + 1
#     iteration = 0
#     for i in range(2, end):
#         print("i ->",i)
#         iteration += 1
#         if n % i == 0:
#             return False
#     print("iteration A",iteration)
#     return True

# print(isPrime(1117))

# def isPrimeB(n):
#     factors = list(range(2, n))
#     iteration = 0
#     for i in factors:
#         iteration += 1
#         if n % i != 0:
#             factors.remove(i)
#     # print(factors)
#     if len(factors) != 0:
#         return False
#     print("iteration B", iteration)
#     return True

# print(isPrimeB(1117))

# def isPrimeC(n):
#     iteration = 0
#     for i in range(1, n+1):
#         iteration += 1
#         if i != 1 and i != n and n % i == 0:
#             return False
#     print("iteration C", iteration)
#     return True

# print(isPrimeC(1117))

# n = 10351
# print(n%10)
# n = n//10
# print(n%10)
# n = n//10
# print(n%10)

def decode_message(encoded_message_file) :
    content_dict = {}
    index = 1
    progression = 2
    decoded_message = ""
    file = open(encoded_message_file, "r")
    for line in file.readlines():
        key = line.split(" ")[0]
        value = line.split(" ")[1].strip()
        content_dict.update({key: value})

    while index <= len(content_dict):
        decoded_message += content_dict.get(str(index)) + " "
        index += progression
        progression += 1

    return decoded_message

print(decode_message("message_file.txt"))