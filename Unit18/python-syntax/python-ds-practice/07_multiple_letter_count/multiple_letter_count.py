def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_frequency = {}

    for letter in phrase:
        letter_frequency[letter] = letter_frequency.get(letter, 0) + 1
    return letter_frequency
