"""
Лабораторная работа 4.1
Вариант 3: Управление активами
Выполнила студентка группы ЦИБ-251 Бурмистрова Злата
"""


class ValidationError(Exception):
    """Пользовательское исключение для ошибок валидации данных."""
    pass


class Asset:
    """
    Базовый класс для представления актива.
    Атрибуты:
        asset_id: Идентификатор актива
        name: Название актива
        purchase_price: Стоимость покупки
    """

    def __init__(self, asset_id, name, purchase_price):
        """
        Инициализация объекта Asset.
        """
        if not isinstance(asset_id, int):
            raise TypeError(f"asset_id должен быть целым числом, получено: {type(asset_id).__name__}")
        if asset_id <= 0:
            raise ValidationError(f"asset_id должен быть положительным числом, получено: {asset_id}")

        if not isinstance(name, str):
            raise TypeError(f"name должен быть строкой, получено: {type(name).__name__}")
        if not name.strip():
            raise ValidationError("name не может быть пустой строкой")

        if not isinstance(purchase_price, (int, float)):
            raise TypeError(f"purchase_price должен быть числом, получено: {type(purchase_price).__name__}")
        if purchase_price < 0:
            raise ValidationError(f"purchase_price не может быть отрицательным, получено: {purchase_price}")

        self.asset_id = asset_id
        self.name = name.strip()
        self.purchase_price = float(purchase_price)

    def display_info(self):
        """Выводит информацию об активе в консоль."""
        print(f"Актив: {self.name}")
        print(f"ID: {self.asset_id}")
        print(f"Стоимость покупки: {self.purchase_price} руб.")


class Employee:
    """
    Базовый класс для представления сотрудника.
    Атрибуты:
        employee_id: Идентификатор сотрудника
        name: Имя сотрудника
        department: Отдел
    """

    def __init__(self, employee_id, name, department):
        """
        Инициализация объекта Employee.
        """
        if not isinstance(employee_id, int):
            raise TypeError(f"employee_id должен быть целым числом, получено: {type(employee_id).__name__}")
        if employee_id <= 0:
            raise ValidationError(f"employee_id должен быть положительным числом, получено: {employee_id}")

        if not isinstance(name, str):
            raise TypeError(f"name должен быть строкой, получено: {type(name).__name__}")
        if not name.strip():
            raise ValidationError("name не может быть пустой строкой")

        if not isinstance(department, str):
            raise TypeError(f"department должен быть строкой, получено: {type(department).__name__}")
        if not department.strip():
            raise ValidationError("department не может быть пустой строкой")

        self.employee_id = employee_id
        self.name = name.strip()
        self.department = department.strip()

    def display_info(self):
        """Выводит информацию о сотруднике в консоль."""
        print(f"Сотрудник: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Отдел: {self.department}")

    def __str__(self):
        """
        Форматирование
        """
        return f"Сотрудник: {self.name} | Отдел: {self.department}"


def main():
    """Основная функция для демонстрации работы классов."""

    # Создание объектов класса Asset
    asset1 = Asset(1, "Ноутбук Dell", 75000)
    asset2 = Asset(2, "Монитор LG", 25000)
    asset3 = Asset(3, "Принтер HP", 15000)

    print("=== Создание сотрудников ===\n")

    try:
        employee1 = Employee(101, "Иванов Иван", "IT")
        print(f"Сотрудник создан: {employee1}")
    except (TypeError, ValidationError) as e:
        print(f"Ошибка при создании Иванова Ивана: {e}")
        employee1 = None

    try:
        employee2 = Employee(102, "Петрова Мария", "IT")
        print(f"Сотрудник создан: {employee2}")
    except (TypeError, ValidationError) as e:
        print(f"Ошибка при создании Петровой Марии: {e}")
        employee2 = None

    try:
        employee3 = Employee(11,"Сидоров Алексей", "Продажи")
        print(f"Сотрудник создан: {employee3}")
    except (TypeError, ValidationError) as e:
        print(f"Ошибка при создании Сидорова Алексея: {e}")
        employee3 = None

    print()
    try:
        employee4 = Employee()
        print(f"Сотрудник создан: {employee4}")
    except (TypeError, ValidationError) as e:
        print(f"Ошибка при создании сотрудника без аргументов: {e}")

    print()

    # Демонстрация работы display_info() для активов
    print("=== Информация об активах ===")
    asset1.display_info()
    print()
    asset2.display_info()
    print()
    asset3.display_info()
    print()

    # Демонстрация работы display_info() для успешно созданных сотрудников
    print("=== Информация о сотрудниках ===")
    if employee1 is not None:
        employee1.display_info()
        print()
    else:
        print("Иванов Иван не был создан из-за ошибки\n")

    if employee2 is not None:
        employee2.display_info()
        print()
    else:
        print("Петрова Мария не была создана из-за ошибки\n")

    if employee3 is not None:
        employee3.display_info()
        print()
    else:
        print("Сидоров Алексей не был создан из-за ошибки\n")

    # Демонстрация работы __str__()
    print("=== Вывод через print() с использованием __str__() ===")
    print(asset1)
    print(asset2)
    print(asset3)
    print()

    if employee1 is not None:
        print(employee1)
    else:
        print("Иванов Иван не был создан из-за ошибки")

    if employee2 is not None:
        print(employee2)
    else:
        print("Петрова Мария не была создана из-за ошибки")

    if employee3 is not None:
        print(employee3)
    else:
        print("Сидоров Алексей не был создан из-за ошибки")


if __name__ == "__main__":
    main()
