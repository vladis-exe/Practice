#cost:: is n (len) + n * logn (sort) + n (check all chars), being n the total number of chars of both word
# in case the word have dfferent lenght (false) the cost is n.

def is_anagram():
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")

    if len(word1) != len(word2): return False
    word1 = sorted(word1)
    word2 = sorted(word2)

    for i in range(len(word1)):
        if word1[i] != word2[i]: return False

    return True


print(is_anagram())
