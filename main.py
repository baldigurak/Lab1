def add(x, y):
 """Сложение двух чисел."""
 return x + y

def subtract(x, y):
 """Вычитание двух чисел."""
 return x - y

def multiply(x, y):
 """Умножение двух чисел."""
 return x * y

def divide(x, y):
 """Деление двух чисел."""
 if y == 0:
  return "Деление на ноль невозможно!"
 else:
  return x / y

while True:
 print("Выберите операцию:")
 print("1. Сложение")
 print("2. Вычитание")
 print("3. Умножение")
 print("4. Деление")
 print("5. Выход")

 choice = input("Введите номер операции (1/2/3/4/5): ")

 if choice in ('1', '2', '3', '4'):
  try:
   num1 = float(input("Введите первое число: "))
   num2 = float(input("Введите второе число: "))

   if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

   elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

   elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

   elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))

  except ValueError:
   print("Неверный ввод. Пожалуйста, введите число.")

 elif choice == '5':
  break
 else:
  print("Неверный ввод. Пожалуйста, введите число от 1 до 5.")