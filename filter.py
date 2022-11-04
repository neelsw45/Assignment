# ----------1

# numbers=[1,2,3,4,5,6,7,8,9,10]

# def check_even(number):
#     if number%2==0:
#         return True
#     return False

# even_numbers_iterator=filter(check_even,numbers)


# even_numbers=list(even_numbers_iterator)
# print(even_numbers)

# ---------------------------------------------------------------------------------------------------------------------------

# -------------2

# letters=['a','b','c','d','e','f','g','h']

# def filter_vowels(letter):
#     vowels=['a','e','i','o','u']
#     return True if letter in vowels else False

# filtered_vowels=filter(filter_vowels,letters)

# vowels=tuple(filtered_vowels)
# print(vowels)

# ----------------------------------------------------------------------------------------------------------------------------

# ------------3

numbers=[1,2,3,4,5,6,7]

even_numbers_iterator=filter(lambda x:(x%2==0),numbers)

even_numbers=list(even_numbers_iterator)
print(even_numbers)


# ----------------------------------------------------------------------------------------------------------------------------


#-------------------4 