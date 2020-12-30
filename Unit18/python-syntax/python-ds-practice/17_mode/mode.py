def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    num_frequency = {}
    max_count = max(num_frequency)
    for num in nums:
        if num in num_frequency:
            num_frequency[num] += 1
        else:
            num_frequency[num] = 1

    for (num, freq) in num_frequency.items():
        if freq == max_count:
            return num
