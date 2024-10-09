from deep_translator import GoogleTranslator
import math

def translate(message, target_language='uk'):
    """Перекладає повідомлення на вказану мову."""
    try:
        return GoogleTranslator(source='auto', target=target_language).translate(message)
    except Exception as e:
        print(f"Помилка перекладу: {e}")
        return message  # Якщо переклад не вдається, повертаємо оригінальне повідомлення


def calculate_and_display(circle_area, square_area, language):
    # Обчислення параметрів кола та квадрата
    circle_diameter = 2 * math.sqrt(circle_area / math.pi)
    square_side = math.sqrt(square_area)
    square_diagonal = square_side * math.sqrt(2)

    # Визначення, чи вміщується коло в квадрат і навпаки
    fits_circle_in_square = circle_diameter <= square_side
    fits_square_in_circle = square_diagonal <= circle_diameter

    # Виведення результатів із перекладом на потрібну мову
    print(translate(f"Мова: {language}", language))
    print(translate(f"Площа кола: {circle_area}", language))
    print(translate(f"Площа квадрата: {square_area}", language))
    print(translate(f"Діаметр кола: {round(circle_diameter, 2)}", language))
    print(translate(f"Сторона квадрата: {round(square_side, 2)}", language))
    print(translate(f"Діагональ квадрата: {round(square_diagonal, 2)}", language))

    # Перевірка та виведення результатів
    if fits_circle_in_square:
        print(translate(f"а) Коло з площею {circle_area} вміщується в квадраті з площею {square_area}.", language))
    else:
        print(translate(f"а) Коло з площею {circle_area} не вміститься в квадраті з площею {square_area}.", language))

    if fits_square_in_circle:
        print(translate(f"б) Квадрат з площею {square_area} вміщується в колі з площею {circle_area}.", language))
    else:
        print(translate(f"б) Квадрат з площею {square_area} не вміститься в колі з площею {circle_area}.", language))