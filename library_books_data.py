from collections import defaultdict

library_books = {
    "B001": {"title": "Гарри Поттер и философский камень", "borrower": "Алиса", "due_date": -5, "fine_rate": 0.50},
    "B002": {"title": "Властелин колец: Братство кольца", "borrower": "Боб", "due_date": 3, "fine_rate": 0.75},
    "B003": {"title": "Песнь льда и огня: Игра престолов", "borrower": None, "due_date": 0, "fine_rate": 0.25},
    "B004": {"title": "Хроники Нарнии: Лев, колдунья и платяной шкаф", "borrower": "Алиса", "due_date": 2, "fine_rate": 1.00}
}


def calculate_fine_and_status(library_books):
    total_fine = 0
    borrower_fines = defaultdict(float)
    
    for book_id, book_info in library_books.items():
        due_date = book_info["due_date"]
        fine_rate = book_info["fine_rate"]
        
        # Статус книги
        if book_info["borrower"] is None:
            status = "Доступна"
        elif due_date > 0:
            status = "В срок"
        else:
            status = "Просрочена"
            fine = abs(due_date) * fine_rate
            total_fine += fine
            borrower_fines[book_info["borrower"]] += fine
        
        print(f"Book: {book_info['title']}")
        print(f"Status: {status}")
        print(f"Due date: {due_date} days")
        print(f"Fine rate: {fine_rate} per day")
        print()

    return total_fine, borrower_fines

def find_top_borrower(borrower_fines):
    top_borrower = max(borrower_fines, key=borrower_fines.get, default=None)
    return top_borrower, borrower_fines.get(top_borrower, 0)

total_fine, borrower_fines = calculate_fine_and_status(library_books)
print(f"Total fines: {total_fine:.2f}")

top_borrower, fine_amount = find_top_borrower(borrower_fines)
print(f"Borrower with the most fines: {top_borrower} with a fine of {fine_amount:.2f}")
