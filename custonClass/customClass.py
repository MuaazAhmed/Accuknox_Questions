class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Returns an iterator that yields length and width as dicts
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage:
if __name__ == "__main__":
    # Creating an instance of the Rectangle class
    rect = Rectangle(5, 10)

    # Iterating over the instance
    for dimension in rect:
        print(dimension)
