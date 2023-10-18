from abc import ABC, abstractmethod
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, amount: float) -> float:
        pass
class StudentDiscount(DiscountStrategy):
    def apply_discount(self, amount: float) -> float:
        return amount * 0.90
class SeasonalDiscount(DiscountStrategy):
    def apply_discount(self, amount: float) -> float:
        return amount * 0.80
class NoDiscount(DiscountStrategy):
    def apply_discount(self, amount: float) -> float:
        return amount
class Product:
    def __init__(self, price: float, discount_strategy: DiscountStrategy):
        self.price = price
        self._discount_strategy = discount_strategy
    def set_discount_strategy(self, discount_strategy: DiscountStrategy):
        self._discount_strategy = discount_strategy
    def get_final_price(self) -> float:
        return self._discount_strategy.apply_discount(self.price)
product = Product(100, NoDiscount())
print(f"Price without discount: ${product.get_final_price()}")
product.set_discount_strategy(StudentDiscount())
print(f"Price with student discount: ${product.get_final_price()}")
product.set_discount_strategy(SeasonalDiscount())
print(f"Price with seasonal discount: ${product.get_final_price()}")