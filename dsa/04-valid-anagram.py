# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

s = "rushikesh"
t = "keshrushi"

# solution 1
# if sorted(s)==sorted(t):
#     print("string is anagram")
# else:
#     print("String is not an anagram")

char_dict = dict()
# {
# #       "a":1
#         "b":0
#         c:0
#         d:0
# }

# solution 2
# s = "abcd"
# t = "dcab"

# for char in s:
#     char_dict[char] = char_dict.get(char, 0) + 1

# for char in t:
#     char_dict[char] = char_dict.get(char, 0) - 1

# for key, value in char_dict.items():
#      if value != 0:
#         print("This is not anagram")
#         break

