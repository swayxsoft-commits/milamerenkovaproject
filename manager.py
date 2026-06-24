import json
import os
import matplotlib.pyplot as plt
from typing import List
from expense import Expense, RegularExpense, DiscretionaryExpense

class ExpenseManager:
    def __init__(self, filename: str = "expenses.json"):
        self.filename = filename
        self.expenses: List[Expense] = []
        self.load_from_json()

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)
        self.save_to_json()

    def remove_expense(self, index: int) -> bool:
        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)
            self.save_to_json()
            return True
        return False

    def get_filtered_expenses(self, category: str = None, start_date=None, end_date=None) -> List[Expense]:
        filtered = self.expenses
        if category:
            filtered = [e for e in filtered if e.category.lower() == category.lower()]
        if start_date:
            filtered = [e for e in filtered if e.date >= start_date]
        if end_date:
            filtered = [e for e in filtered if e.date <= end_date]
        return filtered

    def calculate_total(self, expenses_list: List[Expense]) -> float:
        return sum(e.amount for e in expenses_list)

    def save_to_json(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([e.to_dict() for e in self.expenses], f, ensure_ascii=False, indent=4)

    def load_from_json(self):
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    exp_type = item.get("type", "Expense")
                    if exp_type == "RegularExpense":
                        cls = RegularExpense
                    elif exp_type == "DiscretionaryExpense":
                        cls = DiscretionaryExpense
                    else:
                        cls = Expense
                    self.expenses.append(cls(item["amount"], item["category"], item["date"]))
        except (json.JSONDecodeError, KeyError, ValueError):
            print("Ошибка загрузки файла данных. Начнем с пустого списка.")

    def plot_chart(self):
        """Построение круговой диаграммы расходов по категориям."""
        if not self.expenses:
            print("Нет данных для построения графика.")
            return

        category_totals = {}
        for e in self.expenses:
            category_totals[e.category] = category_totals.get(e.category, 0) + e.amount

        labels = list(category_totals.keys())
        sizes = list(category_totals.values())

        plt.figure(figsize=(8, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title("Расходы по категориям")
        plt.axis('equal')
        plt.show()
