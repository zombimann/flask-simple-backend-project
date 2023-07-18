from flask import jsonify, request
from app import app, db
from app.models import Book

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')

    book = Book(title=title, author=author)
    db.session.add(book)
    db.session.commit()

    return jsonify({'id': book.id, 'title': book.title, 'author': book.author}), 201

@app.route('/books', methods=['GET'])
def get_all_books():
    books = Book.query.all()
    book_list = [{'id': book.id, 'title': book.title, 'author': book.author} for book in books]
    return jsonify(book_list)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        return jsonify({'id': book.id, 'title': book.title, 'author': book.author})
    return jsonify({'message': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    data = request.get_json()
    title = data.get('title')
    author = data.get('author')

    book.title = title
    book.author = author
    db.session.commit()

    return jsonify({'id': book.id, 'title': book.title, 'author': book.author})

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    db.session.delete(book)
    db.session.commit()

    return jsonify({'message': 'Book deleted'})
