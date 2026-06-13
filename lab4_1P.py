"""
Лабораторная работа 4.1
Вариант 3: Управление активами
Выполнила студентка группы ЦИБ-251 Бурмистрова Злата
"""


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
        self.asset_id = asset_id
        self.name = name
        self.purchase_price = purchase_price

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
        self.employee_id = employee_id
        self.name = name
        self.department = department

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

    # Создание объектов класса Employee
    employee1 = Employee(101, "Иванов Иван", "IT")
    employee2 = Employee(102, "Петрова Мария", "Бухгалтерия")
    employee3 = Employee(103, "Сидоров Алексей", "Продажи")

    # Демонстрация работы display_info()
    print("=== Информация об активах ===")
    asset1.display_info()
    print()
    asset2.display_info()
    print()
    asset3.display_info()
    print()

    print("=== Информация о сотрудниках ===")
    employee1.display_info()
    print()
    employee2.display_info()
    print()
    employee3.display_info()
    print()

    # Демонстрация работы __str__()
    print("=== Вывод через print() с использованием __str__() ===")
    print(asset1)
    print(asset2)
    print(asset3)
    print()
    print(employee1)
    print(employee2)
    print(employee3)


if __name__ == "__main__":
    main()