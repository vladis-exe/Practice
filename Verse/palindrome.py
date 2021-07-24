#Cost is linear

def is_palindrome():
    phrase = input("enter a phrase: ")
    phrase = phrase.replace(" ", "")
    phrase = phrase.replace(",", "")
    phrase = phrase.casefold()
    length = len(phrase)

    for i in range(length // 2): #ceil division
        if phrase[i] != phrase[length - 1 - i]: return False

    return True


print(is_palindrome())
