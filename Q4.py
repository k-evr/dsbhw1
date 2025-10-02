def palindrome_check(wrd):
    word = str(wrd.lower())
    for i in range(len(word)//2):
        if word[i] != word[-(i+1)]:
            return wrd + " is not a palindrome"
    return wrd + ' is a palindrome'