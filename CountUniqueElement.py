from collections import Counter

def unique_element():
    word = input("Enter your words : ")
    found = Counter(word)
    print("Count of all chars in the sentence is : \n "+ str(found))

unique_element()
