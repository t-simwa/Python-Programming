
# Create a class `Book` with the following:
# Instance attributes: `title`, `author`, `year`.
# Instance method: `get_book_info` that returns a string with the book's title, author, and year.

# Define a class named Book:
class Book: 
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    # Instance method to get book info:
    def get_book_info(self):
        return f"{self.title} by {self.author}, published in {self.year}."
    
# Create an object of the Book class:
book = Book("Meditations", "Marcus Aurelius", 2014)

# Call the get_book_info method:
print(book.get_book_info()) # Output: Meditations by Marcus Aurelius, published in 2014.