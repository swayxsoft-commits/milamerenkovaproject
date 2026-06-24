from datetime import datetime
from manager import ExpenseManager
from expense import RegularExpense, DiscretionaryExpense


def get_valid_amount() -> float:
    while True:
        try:
            amount = float(input("Введите сумму: "))
            if amount <= 0:
                print("Ошибка: сумма должна быть больше 0.")
                continue
            return amount
        except ValueError:
            print("Ошибка: введите число.")


def get_valid_date(prompt: str, allow_empty=False) -> str:
    while True:
        date_str = input(prompt).strip()
        if not date_str and allow_empty:
            return None
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Ошибка: неверный формат даты (нужен ГГГГ-ММ-ДД).")


def main():
    manager = ExpenseManager()

    while True:
        print("\n--- Expense Chart Menu ---")
        print("1. Добавить расход")
        print("2. Просмотреть все расходы")
        print("3. Удалить расход")
        print("4. Фильтрация и подсчет суммы")
        print("5. Показать график расходов")
        print("6. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            print("Тип расхода: 1 - Регулярный, 2 - Необязательный")
            t_choice = input("Выбор: ").strip()
            cls = RegularExpense if t_choice == "1" else DiscretionaryExpense

            amount = get_valid_amount()
            category = input("Введите категорию: ")
            date_str = get_valid_date("Введите дату (ГГГГ-ММ-ДД): ")

            try:
                expense = cls(amount, category, date_str)
                manager.add_expense(expense)
                print("Расход успешно добавлен!")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "2":
            if not manager.expenses:
                print("Список расходов пуст.")
            for i, exp in enumerate(manager.expenses):
                print(f"{i}. {exp}")

        elif choice == "3":
            if not manager.expenses:
                print("Список пуст.")
                continue
            try:
                idx = int(input("Введите индекс для удаления: "))
                if manager.remove_expense(idx):
                    print("Запись удалена.")
                else:
                    print("Неверный индекс.")
            except ValueError:
                print("Введите корректное число.")

        elif choice == "4":
            cat = input("Категория для фильтра (оставьте пустым для всех): ").strip() or None
            s_date = get_valid_date("Начальная дата (ГГГГ-ММ-ДД) или Enter: ", True)
            e_date = get_valid_date("Конечная дата (ГГГГ-ММ-ДД) или Enter: ", True)

            start = datetime.strptime(s_date, "%Y-%m-%d") if s_date else None
            end = datetime.strptime(e_date, "%Y-%m-%d") if e_date else None

            filtered = manager.get_filtered_expenses(cat, start, end)
            print("\nРезультаты фильтрации:")
            for exp in filtered:
                print(exp)
            print(f"Общая сумма за период: {manager.calculate_total(filtered):.2f} руб.")

        elif choice == "5":
            manager.plot_chart()

        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()
