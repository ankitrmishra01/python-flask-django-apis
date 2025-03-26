# AIM: A program that creates a RESTful API that allows users to create, read, update, and delete resource.

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for books
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"},
]

# Get all books
@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)

# Get a single book by id
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# Create a new book
@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()
    new_book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"]
    }
    books.append(new_book)
    return jsonify(new_book), 201

# Update an existing book by id
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        data = request.get_json()
        book["title"] = data["title"]
        book["author"] = data["author"]
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# Delete a book by id
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return jsonify({"result": True})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
