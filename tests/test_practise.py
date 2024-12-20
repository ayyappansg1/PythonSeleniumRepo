# #
# # def setup_teardown(func):
# #     def wrapper():
# #         print("Setup")
# #         func()
# #         print("Teardown")
# #     return wrapper
# #
# # @setup_teardown
# # def test_example():
# #     print("Test is running")
# #
# # test_example()
#
# def dupArray(arr):
#     dupli = set()
#     remin = set()
#     [dupli.add(i) if i in remin else remin.add(i) for i in arr]
#     # for i in arr:
#     #     if i in remin:
#     #         dupli.add(i)
#     #     else:
#     #         remin.add(i)
#     return list(remin)
#
#
# def test():
#     # marks = [85, 42, 78, 90, 67]
#     # grade=["A" if i>=80 else "B" if i>=60 else "C" for i in marks]
#     # print(grade)
#     print(find_missing_number([1,2,3,4,5,6,8,10],10))
#
# def find_missing_number(arr,num):
#     all=set(range(1,num+1))
#     old=set(arr)
#     return sorted(all-old)
#
#
#
# def fibonaccigenerate(num):
#     a, b = 0, 1
#     print(a)
#     print(b)
#     for i in range(num - 2):
#         c = a + b
#         print(c)
#         a = b
#         b = c
#
#
# def primenumber(num):
#     if num <= 1: return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0: return False
#     return True
#
#
# def removeDupDir(arr):
#     return list(set(arr))
#
#
# def mergeTwosortedarr(arr1, arr2):
#     return sorted(arr1 + arr2)
#
#
# def checkSorted(arr):
#     return arr == sorted(arr)
#
#
# def occurance(str):
#     map = {}
#     for i in str:
#         if i in map:
#             map[i] += 1
#         else:
#             map[i] = 1
#     return map
#
#
# def sortArra(arr):
#     return sorted(arr)
#
#
# def checkPalindrome(str):
#     return str == str[::-1]
#
#
# def checkAnagram(str1, str2):
#     if len(str1) != len(str2):
#         return False
#     return sorted(str1.lower()) == sorted(str2.lower())
#
#
# def reverseString(str):
#     return str[::-1]
#
#
# test()
