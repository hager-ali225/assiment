from flask import Flask
from flask import request, jsonify   
app = Flask(__name__)  

@app.route('/', methods=['GET']) 
def home():
    return "Welcome to Library Management API!"  
books = []  

@app.route('/add-book', methods=['POST'])
def add_book():
    data = request.get_json()  

    if not all(key in data for key in ['title', 'author', 'published_year', 'isbn']):
        return jsonify({"error": "Missing required fields"}), 400

    books.append(data) 
    return jsonify({"message": "Book added successfully", "book": data}), 201
@app.route('/books', methods=['GET'])
def list_books():
    return jsonify({"books": books}), 200
@app.route('/delete/<string:isbn>', methods=['DELETE'])
def delete_book(isbn):
    global books
    books = [book for book in books if book['isbn'] != isbn]  # إزالة الكتاب باستخدام ISBN
    return jsonify({"message": "Book deleted successfully"}), 200
@app.route('/update/<string:isbn>', methods=['PUT'])
def update_book(isbn):
    data = request.get_json()

    for book in books:
        if book['isbn'] == isbn:
            book.update({key: data[key] for key in data if key in book})
            return jsonify({"message": "Book updated successfully", "book": book}), 200

    return jsonify({"error": "Book not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)   
  


