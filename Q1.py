def num_vowels(wrd):
    vowels = ['a','e','i','o','u']
    word = str(wrd.lower())
    num = 0
    for i in word:
        if i in vowels:
            num += 1
    return num