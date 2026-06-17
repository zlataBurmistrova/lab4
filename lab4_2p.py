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
        Инициализация объекта Asset с валидацией данных.

        Args:
            asset_id (int): Идентификатор актива
            name (str): Название актива
            purchase_price (float): Стоимость покупки

        Raises:
            ValidationError: Если данные некорректны
            TypeError: Если типы данных неверны
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

    def calculate_depreciation(self):
        """
        Полиморфный метод расчета амортизации.
        Должен быть переопределен в дочерних классах.

        Returns:
            float: Сумма амортизации
        """
        raise NotImplementedError("Метод должен быть реализован в дочернем классе")

    def __str__(self):
        """Возвращает красиво отформатированную строку."""
        return f"Актив: {self.name} | Цена: {self.purchase_price} руб."


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
        Инициализация объекта Employee с валидацией данных.

        Args:
            employee_id (int): Идентификатор сотрудника
            name (str): Имя сотрудника
            department (str): Отдел

        Raises:
            ValidationError: Если данные некорректны
            TypeError: Если типы данных неверны
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
        """Возвращает красиво отформатированную строку."""
        return f"Сотрудник: {self.name} | Отдел: {self.department}"


class Hardware(Asset):
    """
    Дочерний класс для представления аппаратного обеспечения.

    Атрибуты:
        serial_number: Серийный номер оборудования
    """

    def __init__(self, asset_id, name, purchase_price, serial_number):
        """
        Инициализация объекта Hardware с валидацией данных.

        Args:
            asset_id (int): Идентификатор актива
            name (str): Название актива
            purchase_price (float): Стоимость покупки
            serial_number (str): Серийный номер

        Raises:
            ValidationError: Если данные некорректны
            TypeError: Если типы данных неверны
        """
        super().__init__(asset_id, name, purchase_price)

        if not isinstance(serial_number, str):
            raise TypeError(f"serial_number должен быть строкой, получено: {type(serial_number).__name__}")
        if not serial_number.strip():
            raise ValidationError("serial_number не может быть пустой строкой")

        self.serial_number = serial_number.strip()

    def calculate_depreciation(self):
        """
        Расчет амортизации для оборудования.
        Амортизация составляет 10% от стоимости покупки в год.

        Returns:
            float: Сумма амортизации
        """
        depreciation_rate = 0.10
        return self.purchase_price * depreciation_rate

    def display_info(self):
        """Выводит информацию об оборудовании."""
        super().display_info()
        print(f"Серийный номер: {self.serial_number}")

    def __str__(self):
        """Возвращает красиво отформатированную строку."""
        return f"Оборудование: {self.name} | Сер. номер: {self.serial_number} | Цена: {self.purchase_price} руб."


class SoftwareLicense(Asset):
    """
    Дочерний класс для представления лицензии на программное обеспечение.

    Атрибуты:
        expiration_date: Дата окончания лицензии
    """

    def __init__(self, asset_id, name, purchase_price, expiration_date):
        """
        Инициализация объекта SoftwareLicense с валидацией данных.

        Args:
            asset_id (int): Идентификатор актива
            name (str): Название актива
            purchase_price (float): Стоимость покупки
            expiration_date (str): Дата окончания лицензии

        Raises:
            ValidationError: Если данные некорректны
            TypeError: Если типы данных неверны
        """
        super().__init__(asset_id, name, purchase_price)

        if not isinstance(expiration_date, str):
            raise TypeError(f"expiration_date должен быть строкой, получено: {type(expiration_date).__name__}")
        if not expiration_date.strip():
            raise ValidationError("expiration_date не может быть пустой строкой")

        self.expiration_date = expiration_date.strip()

    def calculate_depreciation(self):
        """
        Расчет амортизации для программного обеспечения.
        Амортизация составляет 20% от стоимости покупки в год.

        Returns:
            float: Сумма амортизации
        """
        depreciation_rate = 0.20
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

    def __init__(self, employee_id, name, department, budget):
        """
        Инициализация объекта ITManager с валидацией данных.

        Args:
            employee_id (int): Идентификатор сотрудника
            name (str): Имя сотрудника
            department (str): Отдел
            budget (float): Бюджет на активы

        Raises:
            ValidationError: Если данные некорректны
            TypeError: Если типы данных неверны
        """
        super().__init__(employee_id, name, department)

        if not isinstance(budget, (int, float)):
            raise TypeError(f"budget должен быть числом, получено: {type(budget).__name__}")
        if budget < 0:
            raise ValidationError(f"budget не может быть отрицательным, получено: {budget}")

        self.budget = float(budget)

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

    def __init__(self, manager):
        """
        Инициализация объекта Assignment.

        Args:
            manager (ITManager): IT-менеджер, ответственный за активы

        Raises:
            TypeError: Если manager не является объектом ITManager
        """
        if not isinstance(manager, ITManager):
            raise TypeError(f"manager должен быть объектом ITManager, получено: {type(manager).__name__}")

        self.manager = manager
        self.assets = []

    def add_item(self, item):
        """
        Добавляет актив в список назначенных.

        Args:
            item (Asset): Актив для назначения

        Raises:
            TypeError: Если item не является объектом Asset
        """
        if not isinstance(item, Asset):
            raise TypeError(f"item должен быть объектом Asset, получено: {type(item).__name__}")

        self.assets.append(item)
        print(f"Актив '{item.name}' назначен менеджеру {self.manager.name}")

    def calculate_total_depreciation(self):
        """
        Расчет общей амортизации всех назначенных активов.
        Перебирает список активов, вызывает полиморфный метод calculate_depreciation()
        и применяет логику ITManager (проверка бюджета).

        Returns:
            dict: Словарь с результатами расчета
        """
        total_depreciation = 0
        depreciation_details = []

        for asset in self.assets:
            try:
                depreciation = asset.calculate_depreciation()
                total_depreciation += depreciation

                depreciation_details.append({
                    'asset': asset.name,
                    'type': type(asset).__name__,
                    'depreciation': depreciation
                })
            except Exception as e:
                print(f"Ошибка при расчете амортизации для '{asset.name}': {e}")

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
        """
        Формирует детализированный отчет о назначенных активах.

        Returns:
            str: Форматированный отчет
        """
        report = f"\n{'=' * 60}\n"
        report += f"ОТЧЕТ О НАЗНАЧЕННЫХ АКТИВАХ\n"
        report += f"{'=' * 60}\n"
        report += f"Ответственный: {self.manager.name}\n"
        report += f"Отдел: {self.manager.department}\n"
        report += f"Бюджет: {self.manager.budget} руб.\n"
        report += f"{'=' * 60}\n\n"

        report += "Назначенные активы:\n"
        for i, asset in enumerate(self.assets, 1):
            report += f"{i}. {asset}\n"

        report += f"\n{'=' * 60}\n"
        report += "РАСЧЕТ АМОРТИЗАЦИИ:\n"
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


def create_asset_from_input():
    """
    Функция для создания актива с пользовательским вводом и обработкой ошибок.

    Returns:
        Asset: Созданный объект актива или None в случае ошибки
    """
    print("\n--- Создание нового актива ---")

    try:
        asset_id_input = input("Введите ID актива (целое число > 0): ")
        if not asset_id_input.strip():
            raise ValidationError("ID актива не может быть пустым")
        asset_id = int(asset_id_input)

        name = input("Введите название актива: ")
        if not name.strip():
            raise ValidationError("Название актива не может быть пустым")

        price_input = input("Введите стоимость покупки (число >= 0): ")
        if not price_input.strip():
            raise ValidationError("Стоимость покупки не может быть пустой")
        purchase_price = float(price_input)

        asset_type = input("Выберите тип актива (1 - Hardware, 2 - SoftwareLicense): ")

        if asset_type == "1":
            serial_number = input("Введите серийный номер: ")
            if not serial_number.strip():
                raise ValidationError("Серийный номер не может быть пустым")
            return Hardware(asset_id, name, purchase_price, serial_number)
        elif asset_type == "2":
            expiration_date = input("Введите дату окончания лицензии (например, 2025-12-31): ")
            if not expiration_date.strip():
                raise ValidationError("Дата окончания не может быть пустой")
            return SoftwareLicense(asset_id, name, purchase_price, expiration_date)
        else:
            raise ValidationError(f"Неверный тип актива: {asset_type}")

    except ValueError as e:
        print(f"Ошибка: Неверный формат данных - {e}")
        return None
    except ValidationError as e:
        print(f"Ошибка валидации: {e}")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return None


def create_employee_from_input():
    """
    Функция для создания сотрудника с пользовательским вводом и обработкой ошибок.

    Returns:
        Employee: Созданный объект сотрудника или None в случае ошибки
    """
    print("\n--- Создание нового сотрудника ---")

    try:
        employee_id_input = input("Введите ID сотрудника (целое число > 0): ")
        if not employee_id_input.strip():
            raise ValidationError("ID сотрудника не может быть пустым")
        employee_id = int(employee_id_input)

        name = input("Введите имя сотрудника: ")
        if not name.strip():
            raise ValidationError("Имя сотрудника не может быть пустым")

        department = input("Введите отдел: ")
        if not department.strip():
            raise ValidationError("Отдел не может быть пустым")

        return Employee(employee_id, name, department)

    except ValueError as e:
        print(f"Ошибка: Неверный формат данных - {e}")
        return None
    except ValidationError as e:
        print(f"Ошибка валидации: {e}")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return None


def create_manager_from_input():
    """
    Функция для создания IT-менеджера с пользовательским вводом и обработкой ошибок.

    Returns:
        ITManager: Созданный объект IT-менеджера или None в случае ошибки
    """
    print("\n--- Создание нового IT-менеджера ---")

    try:
        employee_id_input = input("Введите ID менеджера (целое число > 0): ")
        if not employee_id_input.strip():
            raise ValidationError("ID менеджера не может быть пустым")
        employee_id = int(employee_id_input)

        name = input("Введите имя менеджера: ")
        if not name.strip():
            raise ValidationError("Имя менеджера не может быть пустым")

        department = input("Введите отдел: ")
        if not department.strip():
            raise ValidationError("Отдел не может быть пустым")

        budget_input = input("Введите бюджет (число >= 0): ")
        if not budget_input.strip():
            raise ValidationError("Бюджет не может быть пустым")
        budget = float(budget_input)

        return ITManager(employee_id, name, department, budget)

    except ValueError as e:
        print(f"Ошибка: Неверный формат данных - {e}")
        return None
    except ValidationError as e:
        print(f"Ошибка валидации: {e}")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return None


def main():
    """Основная функция для демонстрации работы классов."""

    print("=" * 60)
    print("СИСТЕМА УПРАВЛЕНИЯ АКТИВАМИ")
    print("=" * 60)

    try:
        manager1 = ITManager(201, "Козлов Дмитрий", "IT", 50000)
        manager2 = ITManager(202, "Новикова Анна", "IT", 30000)
        print(manager1)
        print(manager2)

        print()
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
        assignment1.add_item(hardware1)
        assignment1.add_item(software1)
        assignment1.add_item(hardware2)

        print()
        assignment2.add_item(software2)
        assignment2.add_item(hardware3)
        assignment2.add_item(software1)

        print()
        print("=== Демонстрация полиморфизма ===")
        print(f"\nРасчет амортизации для разных типов активов:")
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

    except ValidationError as e:
        print(f"\nОшибка валидации данных: {e}")
    except TypeError as e:
        print(f"\nОшибка типа данных: {e}")
    except Exception as e:
        print(f"\nНеожиданная ошибка: {e}")
        import traceback
        traceback.print_exc()

    print("\n\n=== Создание актива через пользовательский ввод ===")

    try:
        custom_asset = create_asset_from_input()
        if custom_asset:
            print(f"\nАктив успешно создан: {custom_asset}")
            print(f"  Амортизация: {custom_asset.calculate_depreciation():.2f} руб.")
    except KeyboardInterrupt:
        print("\n\nОперация отменена пользователем")
    except Exception as e:
        print(f"\nОшибка при создании актива: {e}")

    print("\n\n=== Создание сотрудника через пользовательский ввод ===")

    try:
        custom_employee = create_employee_from_input()
        if custom_employee:
            print(f"\nСотрудник успешно создан: {custom_employee}")
    except KeyboardInterrupt:
        print("\n\nОперация отменена пользователем")
    except Exception as e:
        print(f"\nОшибка при создании сотрудника: {e}")

    print("\n\n=== Создание IT-менеджера через пользовательский ввод ===")

    try:
        custom_manager = create_manager_from_input()
        if custom_manager:
            print(f"\nIT-менеджер успешно создан: {custom_manager}")
    except KeyboardInterrupt:
        print("\n\nОперация отменена пользователем")
    except Exception as e:
        print(f"\nОшибка при создании IT-менеджера: {e}")


if __name__ == "__main__":
    main()
