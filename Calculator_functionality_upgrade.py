# Step 1: Designing the Calculator BG/ENG
# Нека определим основните функционалности, които искаме от нашия калкулатор:
# - Събиране
# - Изваждане
# - Умножение
# - Деление
# - Квадратен корен
# - Степенуване
# - Решаване на системи от линейни уравнения (матричен метод)

# Step 2: Getting User Input
# Ще попитаме потребителя за избор на операция.

# Step 3: Performing Arithmetic Operations
# Ще създадем функции за всяка операция.

# Step 4: Calculating the Result
# Ще използваме избраната функция за изчисление на резултата.

# Step 5: Displaying the Result
# Ще изведем изчисления резултат.

# Step 6: Putting it All Together

import math

def add(x, y):
    """Събира две числа."""
    return x + y

def subtract(x, y):
    """Изважда две числа."""
    return x - y

def multiply(x, y):
    """Умножава две числа."""
    return x * y

def divide(x, y):
    """Дели две числа."""
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def square_root(x):
    """Изчислява квадратен корен."""
    return math.sqrt(x)

def power(x, y):
    """Изчислява x на степен y."""
    return x ** y

def solve_linear_system(matrix, vector):
    """Решава система от линейни уравнения (матричен метод)."""
    # Вашата имплементация на метода на Гаус ще бъде тук
    pass

# Примерно използване:
if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Solve Linear System")

    choice = input("Enter choice (1/2/3/4/5/6/7): ")

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", square_root(num1))
    elif choice == '6':
        power_num = float(input("Enter power: "))
        print("Result:", power(num1, power_num))
    elif choice == '7':
        # Въведете матрица и вектор за решаване на системата
        # solve_linear_system(matrix, vector)
        print("System solution will be calculated here")
    else:
        print("Invalid choice")
#Калкулатора е подобрен според задание от домашно, направено наскоро, благодаря за вниманието ! BG
#Calculator has been improved according to a homework assignment made recently, thanks for your attention ! ENG
