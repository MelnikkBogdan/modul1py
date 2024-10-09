from mod import *

language='uk'

def read_data(file_name):
    global language
    """Читає дані з файлу та повертає їх у вигляді кортежа (circle_area, square_area, language)."""
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()  # Зчитуємо всі рядки з файлу

        if len(lines) != 3:
            raise ValueError("Некоректні дані у файлі.")

        # Зчитуємо дані з файлу
        circle_area = float(lines[0].strip())  # Площа кола
        square_area = float(lines[1].strip())  # Площа квадрата

        try:
            GoogleTranslator(source='auto', target=lines[2].strip().lower()).translate("test")
            language = lines[2].strip().lower()  # Встановлюємо мову, якщо вона підтримується
        except Exception:
            language = 'uk'  # Встановлюємо українську, якщо мова не підтримується

        return circle_area, square_area, language

    except (FileNotFoundError, ValueError):
        print(f"Файл '{file_name}' не знайдено або в ньому некоректні дані.")

        # Запитуємо дані у користувача
        circle_area = float(input(translate("Введіть площу кола: ", language)))
        square_area = float(input(translate("Введіть площу квадрата: ", language)))
        language = input("Введіть мову інтерфейсу : ").lower()

        # Записуємо дані у файл
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(f"{circle_area}\n{square_area}\n{language}\n")
        print(translate("Дані збережено в файл.", language))
        return circle_area, square_area, language
def main():

    file_name = 'MyData.txt'  # Ім'я файлу з даними

    # Читання даних з файлу або запит у користувача
    circle_area, square_area, language = read_data(file_name)

    # Виконання обчислень і виведення результатів
    calculate_and_display(circle_area, square_area, language)


if __name__ == "__main__":
    main()