def find_anagram (words_list, word):
    anagrams_list = []
    sorted_word = ''.join(sorted(word.lower()))
    for w in words_list:
        list_w = ''.join(sorted(w.lower()))
        if list_w == sorted_word:
            anagrams_list.append(w)
    print anagrams_list
    return anagrams_list
l = ["noon","foo","camila","valet"]
w = "telva"

find_anagram(l, w)
