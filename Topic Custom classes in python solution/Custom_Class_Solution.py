
class Rectangle:
    # Constructor to initialize the value of length and breadth
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    # Iterator 
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

class Main:
    @staticmethod
    def execute():
        # Input from user
        try:
            length = int(input("Enter the length of the rectangle: "))
            width = int(input("Enter the width of the rectangle: "))
        except ValueError:
            print("Please enter valid integer values for length and width.")
            return

        # Create a Rectangle class instance
        rect = Rectangle(length, width)

        # Print the values by iterating over the Rectangle instance
        for item in rect:
            print(item)

# Entry point of the program or main method
if __name__ == "__main__":
    Main.execute()
