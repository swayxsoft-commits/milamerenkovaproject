from datetime import datetime
class Expense:
    """Базовый класс расхода (Инкапсуляция)."""
    def __init__(self, amount: float, category: str, date_str: str):
        self.amount = amount  # Вызов сеттера для валидации
        self._category = category.strip().capitalize()
        self.date = date_str  # Вызов сеттера для валидации

    @property
    def amount(self) -> float:
        return self._amount

    @amount.setter
    def amount(self, value: float):
        if value <= 0:
            raise ValueError("Сумма расхода должна быть строго больше нуля.")
        self._amount = float(value)

    @property
    def category(self) -> str:
        return self._category

    @property
    def date(self) -> datetime:
        return self._date

    @date.setter
    def date(self, value: str):
        try:
            self._date = datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Неверный формат даты. Используйте ГГГГ-ММ-ДД.")

    def to_dict(self) -> dict:
        """Конвертация в словарь для JSON."""
        return {
            "type": self.__class__.__name__,
            "amount": self.amount,
            "category": self.category,
            "date": self.date.strftime("%Y-%m-%d")
        }

    def __str__(self) -> str:
        return f"[{self.date.strftime('%Y-%m-%d')}] {self.category}: {self.amount:.2f} руб."


# Наследование: Различные типы трат
class RegularExpense(Expense):
    """Регулярные/обязательные траты (коммуналка, аренда)."""
    def __str__(self) -> str:
        return f"[Фиксированный] {super().__str__()}"


class DiscretionaryExpense(Expense):
    """Спонтанные/необязательные траты (развлечения, кафе)."""
    def __str__(self) -> str:
        return f"[Необязательный] {super().__str__()}"
