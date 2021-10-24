def palindrome(s: str) -> bool:
    return s.replace(" ", "").casefold()[::-1] == s.replace(" ", "").casefold()




# def foo(*args: str):
#     print(' '.join(args))







# class CaseSwitcher:
#     def __init__(self, mode) -> None:
#         self.mode = mode

#     def __call__(self, payload: str) -> str:
#         if self.mode == 'upper':
#             return payload.upper()
#         if self.mode == 'lower':
#             return payload.lower()
#         if self.mode == 'swap':
#             return payload.swapcase()











# res = 0
# for i in range(1200, 1901):
#     n = i
#     r = n
#     while r >= 100:
#         r = 0
#         while n > 0:
#             r += n % 100
#             n //= 100
#         n = r
#     if r % 11 == 0:
#         print(i, 'yes')
#         res += 1

# print(res)






# n = int(input())
# seq = list(map(int, input().strip().split(' ')))[:n]
# d = int(input())

# res = 0
# for i in seq:
#     if sum([int(digit) for digit in str(i)]) % d == 0:
#         res += 1

# print(res)