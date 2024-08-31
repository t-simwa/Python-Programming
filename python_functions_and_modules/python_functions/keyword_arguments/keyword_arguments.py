
# Keyword arguments allow you to specify arguments by name. 
# This improves readability and allows arguments to be passed in any order

def book_info(title, author): 
    return f"Title: {title}, Author: {author}"

print(book_info(author="Marcus Aurelius", title="Meditations")) # Output: Title: Meditations, Author: Marcus Aurelius