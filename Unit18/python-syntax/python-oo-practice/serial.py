"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.start = self.new_num = start

    def __repr__(self):
        return f"SerialGenerator start={self.start}, next={self.new_num}"

    def generate(self):
        """add one to new_num and return it"""
        self.new_num += 1
        return self.new_num

    def reset(self):
        self.new_num = self.start
