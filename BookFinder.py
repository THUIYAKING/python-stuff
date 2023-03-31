import csv

def read_csv_file(file_name):
    with open(file_name, "r") as f:
        reader = csv.DictReader(f)
        books = [row for row in reader]
    return books

def search_books_by_author(books, author):
    result = []
    for book in books:
        if book['author'] == author:
            result.append(book)
    return result

def search_book_by_ISBN(books, ISBN):
    for book in books:
        if book['ISBN'] == ISBN:
            return (book['title'], float(book['price']))
    return None

def search_books_by_price_range(books, min_price, max_price):
    result = []
    for book in books:
        price = float(book['price'])
        if price >= min_price and price <= max_price:
            result.append(book)
    return result

def add_book_to_csv_file(file_name, book):
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([book['title'], book['author'], book['ISBN'], book['price']])

def display_books(books):
    if not books:
        print("No books found.")
    else:
        for book in books:
            print(f"{book['title']} by {book['author']}, ISBN: {book['ISBN']}, price: ${book['price']}")

def main():
    file_name = "books.csv"
    books = read_csv_file(file_name)
    while True:
        print("\nSelect an option:")
        print("1. Search books by author")
        print("2. Search book by ISBN")
        print("3. Search books by price range")
        print("4. Add a new book")
        print("5. Quit")
        choice = input("> ")
        if choice == "1":
            author = input("Enter author name: ")
            result = search_books_by_author(books, author)
            display_books(result)
        elif choice == "2":
            ISBN = input("Enter ISBN: ")
            result = search_book_by_ISBN(books, ISBN)
            if result:
                title, price = result
                print(f"{title}, price: ${price}")
            else:
                print("Book not found.")
        elif choice == "3":
            min_price = float(input("Enter minimum price: "))
            max_price = float(input("Enter maximum price: "))
            result = search_books_by_price_range(books, min_price, max_price)
            display_books(result)
        elif choice == "4":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            ISBN = input("Enter book ISBN: ")
            price = input("Enter book price: ")
            book = {'title': title, 'author': author, 'ISBN': ISBN, 'price': price}
            add_book_to_csv_file(file_name, book)
            print("Book added successfully.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
