
This is a simple RESTful API for managing a collection of books in a library.


- Python 3.x
- Flask


```bash
git clone https://github.com/yourusername/LibraryAPI.git

cd LibraryAPI


1. Add a new book
URL: /add-book
Method: POST
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "published_year": 1925,
  "isbn": "1234567890",
  "genre": "Fiction"
}
Response:
{
  "message": "Book added successfully",
  "book": {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "published_year": 1925,
    "isbn": "1234567890",
    "genre": "Fiction"
  }

{
  "message": "Book added successfully",
  "book": {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "published_year": 1925,
    "isbn": "1234567890",
    "genre": "Fiction"
  }
URL: /books
Method: GET
{
  "books": [
    {
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "published_year": 1925,
      "isbn": "1234567890",
      "genre": "Fiction"
    }
  ]
}
URL: /delete/<isbn>
Method: DELETE
{
  "message": "Book deleted successfully"
}
Method: PUT
{
  "title": "The Great Gatsby - Updated",
  "genre": "Classic Fiction"
}
from flask import Flask, request, jsonify  # Importing the necessary Flask libraries
app = Flask(__name__)  # Initializing the Flask app

# Home page
@app.route('/', methods=['GET']) 
def home():
    return "Welcome to Library Management API!"  # Welcome message

# List of books (in-memory storage)
books = []  # In-memory storage for book data

# Add a new book
@app.route('/add-book', methods=['POST'])
def add_book():
    data = request.get_json()  # Getting the data sent by the user

    # Checking if all required fields are present
    if not all(key in data for key in ['title', 'author', 'published_year', 'isbn']):
        return jsonify({"error": "Missing required fields"}), 400  # If required fields are missing

    # Adding the book to the list
    books.append(data) 
    return jsonify({"message": "Book added successfully", "book": data}), 201  # Confirmation of adding the book

# List all books
@app.route('/books', methods=['GET'])
def list_books():
    return jsonify({"books": books}), 200  # Returning the list of books

# Delete a book using ISBN
@app.route('/delete/<string:isbn>', methods=['DELETE'])
def delete_book(isbn):
    global books
    books = [book for book in books if book['isbn'] != isbn]  # Removing the book by ISBN
    return jsonify({"message": "Book deleted successfully"}), 200  # Confirmation of deletion

# Update a book using ISBN
@app.route('/update/<string:isbn>', methods=['PUT'])
def update_book(isbn):
    data = request.get_json()  # Getting the new data sent by the user

    # Searching for the book to update
    for book in books:
        if book['isbn'] == isbn:
            book.update({key: data[key] for key in data if key in book})  # Updating the book data
            return jsonify({"message": "Book updated successfully", "book": book}), 200  # Confirmation of the update

    return jsonify({"error": "Book not found"}), 404  # If the book is not found

# Run the application
if __name__ == "__main__":
    app.run(debug=True)  # Running the app in debug mode
