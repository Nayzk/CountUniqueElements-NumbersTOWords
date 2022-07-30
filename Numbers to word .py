from num2words import num2words

def num_to_words():
    return num2words


num_to_words()
n = int(input('Enter number you want to change : '))
print(num2words(n))
# Other variants, according to the type of article.
print(num2words(n, to = 'ordinal'))
print(num2words(n, to = 'ordinal_num'))
print(num2words(n, to = 'year'))
print(num2words(n, to = 'currency'))
  
# Language Support. #الرقم بالعربي
print(num2words(n, lang ='ar'))
