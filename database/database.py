import sqlite3

connection = sqlite3.connect("database.db")


def create_table():
    connection.execute("""
        CREATE TABLE IF NOT EXISTS books (
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)
    connection.commit()


def insert_books(name, author, publication_year, genre, number_of_pages, number_of_copies):
    connection.execute("""
        INSERT INTO books (
            name,
            author,
            publication_year,
            genre,
            number_of_pages,
            number_of_copies
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, author, publication_year, genre, number_of_pages, number_of_copies))
    connection.commit()


if __name__ == "__main__":
    create_table()

    insert_books("Война и мир", "Лев Толстой", 1869, "Роман", 1225, 3)
    insert_books("Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", 671, 4)
    insert_books("Мастер и Маргарита", "Михаил Булгаков", 1967, "Роман", 480, 5)
    insert_books("1984", "Джордж Оруэлл", 1949, "Антиутопия", 328, 3)
    insert_books("Гарри Поттер и философский камень", "Джоан Роулинг", 1997, "Фэнтези", 432, 6)
    insert_books("Маленький принц", "Антуан де Сент-Экзюпери", 1943, "Сказка", 96, 5)
    insert_books("Три товарища", "Эрих Мария Ремарк", 1936, "Роман", 480, 2)
    insert_books("Шерлок Холмс", "Артур Конан Дойл", 1887, "Детектив", 350, 4)
    insert_books("Алиса в Стране чудес", "Льюис Кэрролл", 1865, "Сказка", 192, 3)
    insert_books("Дюна", "Фрэнк Герберт", 1965, "Фантастика", 688, 2)

    connection.close()