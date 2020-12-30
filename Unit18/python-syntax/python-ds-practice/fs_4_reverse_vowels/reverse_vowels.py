def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = set("aeiou")
    letter_list = list(s)

    idx2 = len(s)-1
    idx1 = 0
    while idx1 < idx2:
        if letter_list[idx1].lower() not in vowels:
            idx1 += 1
        elif letter_list[idx2].lower() not in vowels:
            idx2 -= 1
        else:
            letter_list[idx1], letter_list[idx2] = letter_list[idx2], letter_list[idx1]
            idx1 += 1
            idx2 -= 1

    return "".join(letter_list)
