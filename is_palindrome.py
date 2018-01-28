def is_palindrome(word):
    """
    function, that takes any string and returns True
    if a word is an anagram
    """
    i = 0
    word_length = len(word)

    while i <= word_length / 2:
        if word[i] != word[-i - 1]:
            print("%s is not an anagram" % (word))
            return False
        i += 1
    else:
        print("%s is an anagram" % (word))


is_palindrome('noon')
