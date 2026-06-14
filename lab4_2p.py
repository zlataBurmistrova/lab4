"""
Лабораторная работа 4.2 - Наследование и полиморфизм
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

    def __init__(self, asset_id: int, name: str, purchase_price: float):
        """Инициализация объекта Asset."""
        self.asset_id = asset_id
        self.name = name
        self.purchase_price = purchase_price

    def display_info(self):
        """Выводит информацию об активе в консоль."""
        print(f"Актив: {self.name}")
        print(f"ID: {self.asset_id}")
        print(f"Стоимость покупки: {self.purchase_price} руб.")

    def calculate_depreciation(self):
        """
        Полиморфный метод расчета амортизации.
        Должен быть переопределен в дочерних классах.
        """
        raise NotImplementedError("Метод должен быть реализован в дочернем классе")

    def __str__(self):
    #форматирование
        return f"Актив: {self.name} | Цена: {self.purchase_price} руб."


class Employee:
    """
    Базовый класс для представления сотрудника.
    Атрибуты:
        employee_id: Идентификатор сотрудника
        name: Имя сотрудника
        department: Отдел
    """

    def __init__(self, employee_id: int, name: str, department: str):
        """Инициализация объекта Employee."""
        self.employee_id = employee_id
        self.name = name
        self.department = department

    def display_info(self):
        """Выводит информацию о сотруднике в консоль."""
        print(f"Сотрудник: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Отдел: {self.department}")

    def __str__(self):
        #форматирование
        return f"Сотрудник: {self.name} | Отдел: {self.department}"


class Hardware(Asset):
    """
    Дочерний класс для представления аппаратного обеспечения.
    Атрибуты:
    serial_number: Серийный номер оборудования
    """

    def __init__(self, asset_id: int, name: str, purchase_price: float, serial_number: str):
        """
        Инициализация объекта Hardware.
        Args:
            asset_id (int): Идентификатор актива
            name (str): Название актива
            purchase_price (float): Стоимость покупки
            serial_number (str): Серийный номер
        """
        super().__init__(asset_id, name, purchase_price)
        self.serial_number = serial_number

    def calculate_depreciation(self):
        """Расчет амортизации для оборудования."""
        depreciation_rate = 0.10  # 10% для железа
        return self.purchase_price * depreciation_rate

    def display_info(self):
        """Выводит информацию об оборудовании."""
        super().display_info()
        print(f"Серийный номер: {self.serial_number}")

    def __str__(self):
        #форматирование
        return f"Оборудование: {self.name} | Сер. номер: {self.serial_number} | Цена: {self.purchase_price} руб."


class SoftwareLicense(Asset):
    """
    Дочерний класс для представления лицензии на программное обеспечение.
    Атрибуты:
        expiration_date: Дата окончания лицензии
    """

    def __init__(self, asset_id: int, name: str, purchase_price: float, expiration_date: str):
        """
        Инициализация объекта SoftwareLicense.
        Args:
            asset_id (int): Идентификатор актива
            name (str): Название актива
            purchase_price (float): Стоимость покупки
            expiration_date (str): Дата окончания лицензии
        """
        super().__init__(asset_id, name, purchase_price)
        self.expiration_date = expiration_date

    def calculate_depreciation(self):
        """ Расчет амортизации для программного обеспечения."""
        depreciation_rate = 0.20  # 20% для софта (устаревает быстрее)
        return self.purchase_price * depreciation_rate

    def display_info(self):
        """Выводит информацию о лицензии."""
        super().display_info()
        print(f"Дата окончания: {self.expiration_date}")

    def __str__(self):
        """Возвращает красиво отформатированную строку."""
        return f"Лицензия: {self.name} | Окончание: {self.expiration_date} | Цена: {self.purchase_price} руб."


class ITManager(Employee):
    """
    Дочерний класс для представления IT-менеджера.
    Атрибуты:
        budget: Бюджет на активы
    """

    def __init__(self, employee_id: int, name: str, department: str, budget: float):
        """
        Инициализация объекта ITManager.
        Args:
            employee_id (int): Идентификатор сотрудника
            name (str): Имя сотрудника
            department (str): Отдел
            budget (float): Бюджет на активы
        """
        super().__init__(employee_id, name, department)
        self.budget = budget

    def display_info(self):
        """Выводит информацию об IT-менеджере."""
        super().display_info()
        print(f"Бюджет: {self.budget} руб.")

    def __str__(self):
        """Возвращает красиво отформатированную строку."""
        return f"IT-менеджер: {self.name} | Отдел: {self.department} | Бюджет: {self.budget} руб."


class Assignment:
    """
    Класс-контейнер для назначения активов сотруднику.
    Атрибуты:
        manager: IT-менеджер, ответственный за активы
        assets: Список назначенных активов
    """

    def __init__(self, manager: str):
        """
        Инициализация объекта Assignment.
        Args:
            manager (ITManager): IT-менеджер, ответственный за активы
        """
        self.manager = manager
        self.assets = []

    def add_item(self, item: str):
        """
        Добавляет актив в список назначенных.
        Args:
            item (Asset): Актив для назначения
        """
        self.assets.append(item)
        print(f"Актив '{item.name}' назначен менеджеру {self.manager.name}")

    def calculate_total_depreciation(self):
        """
        Расчет общей амортизации всех назначенных активов.
        Перебирает список активов, вызывает полиморфный метод calculate_depreciation()
        и применяет логику ITManager (проверка бюджета).
        """
        total_depreciation = 0
        depreciation_details = []

        for asset in self.assets:
            depreciation = asset.calculate_depreciation()
            total_depreciation += depreciation

            depreciation_details.append({
                'asset': asset.name,
                'type': type(asset).__name__,
                'depreciation': depreciation
            })

        budget_status = "В пределах бюджета"
        remaining_budget = self.manager.budget - total_depreciation

        if total_depreciation > self.manager.budget:
            budget_status = "Превышение бюджета"
            remaining_budget = 0

        return {
            'total_depreciation': total_depreciation,
            'budget': self.manager.budget,
            'remaining_budget': remaining_budget,
            'budget_status': budget_status,
            'details': depreciation_details
        }

    def get_report(self):
        """Формирует детализированный отчет о назначенных активах."""
        report = f"\n{'=' * 60}\n"
        report += f"Отчет о назначенных активах\n"
        report += f"{'=' * 60}\n"
        report += f"Ответственный: {self.manager.name}\n"
        report += f"Отдел: {self.manager.department}\n"
        report += f"Бюджет: {self.manager.budget} руб.\n"
        report += f"{'=' * 60}\n\n"

        report += "Назначенные активы:\n"
        for i, asset in enumerate(self.assets, 1):
            report += f"{i}. {asset}\n"

        report += f"\n{'=' * 60}\n"
        report += "Рассчет амортизации:\n"
        report += f"{'=' * 60}\n"

        calculation = self.calculate_total_depreciation()

        for detail in calculation['details']:
            report += f"- {detail['asset']} ({detail['type']}): {detail['depreciation']:.2f} руб.\n"

        report += f"\nОбщая амортизация: {calculation['total_depreciation']:.2f} руб.\n"
        report += f"Остаток бюджета: {calculation['remaining_budget']:.2f} руб.\n"
        report += f"Статус: {calculation['budget_status']}\n"
        report += f"{'=' * 60}\n"

        return report

    def __str__(self):
        """Возвращает информацию о назначении."""
        return f"Назначение: {len(self.assets)} активов для {self.manager.name}"


def main():
    """Основная функция для демонстрации работы классов."""

    print("=== Создание IT-менеджеров ===")
    # Создание объектов класса ITManager (ДК2)
    manager1 = ITManager(201, "Козлов Дмитрий", "IT", 50000)
    manager2 = ITManager(202, "Новикова Анна", "IT", 30000)

    print(manager1)
    print(manager2)
    print()

    print("=== Создание активов (дочерние классы) ===")
    # Создание объектов дочерних классов БК1
    hardware1 = Hardware(1, "Ноутбук Dell", 75000, "SN123456789")
    hardware2 = Hardware(2, "Монитор LG", 25000, "SN987654321")
    software1 = SoftwareLicense(3, "Windows 11 Pro", 15000, "2025-12-31")
    software2 = SoftwareLicense(4, "Office 365", 8000, "2025-06-30")
    hardware3 = Hardware(5, "Принтер HP", 12000, "SN456789123")

    print(hardware1)
    print(hardware2)
    print(software1)
    print(software2)
    print(hardware3)
    print()

    assignment1 = Assignment(manager1)
    assignment2 = Assignment(manager2)

    print()
    print("=== Добавление активов в назначения ===")
    assignment1.add_item(hardware1)
    assignment1.add_item(software1)
    assignment1.add_item(hardware2)

    print()

    assignment2.add_item(software2)
    assignment2.add_item(hardware3)
    assignment2.add_item(software1)

    print()
    print("=== Демонстрация полиморфизма ===")
    print("\nРасчет амортизации для разных типов активов:")
    print(f"Hardware (Ноутбук Dell): {hardware1.calculate_depreciation():.2f} руб. (10%)")
    print(f"SoftwareLicense (Windows 11 Pro): {software1.calculate_depreciation():.2f} руб. (20%)")
    print(f"Hardware (Монитор LG): {hardware2.calculate_depreciation():.2f} руб. (10%)")

    print()
    print("=== Детализированные отчеты ===")
    print(assignment1.get_report())
    print()
    print(assignment2.get_report())

    print()
    print("=== Демонстрация работы __str__() ===")
    print(assignment1)
    print(assignment2)


if __name__ == "__main__":
    main()