from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    """
    Abstract class representing a discount strategy.
    Provides an interface to apply a discount to a given amount.
    """

    @abstractmethod
    def apply_discount(self, amount: float) -> float:
        """
        Apply a discount to the provided amount.

        :param amount: Original amount before applying discount.
        :return: Amount after applying discount.
        """
        pass


class StudentDiscount(DiscountStrategy):
    """
    Concrete strategy that applies a student discount.
    """

    def apply_discount(self, amount: float) -> float:
        """
        Apply a 10% student discount to the provided amount.

        :param amount: Original amount before applying discount.
        :return: Amount after applying 10% discount.
        """
        return amount * 0.90


class SeasonalDiscount(DiscountStrategy):
    """
    Concrete strategy that applies a seasonal discount.
    """

    def apply_discount(self, amount: float) -> float:
        """
        Apply a 20% seasonal discount to the provided amount.

        :param amount: Original amount before applying discount.
        :return: Amount after applying 20% discount.
        """
        return amount * 0.80


class NoDiscount(DiscountStrategy):
    """
    Concrete strategy that applies no discount.
    """

    def apply_discount(self, amount: float) -> float:
        """
        Return the original amount without applying any discount.

        :param amount: Original amount.
        :return: Original amount without any discount.
        """
        return amount


class Product:
    """
    Represents a product with a price and a discount strategy.
    Provides methods to set the discount strategy and get the final price after applying discount.
    """

    def __init__(self, price: float, discount_strategy: DiscountStrategy):
        """
        Initialize the Product with a price and a discount strategy.

        :param price: Base price of the product.
        :param discount_strategy: Initial discount strategy for the product.
        """
        self.price = price
        self._discount_strategy = discount_strategy

    def set_discount_strategy(self, discount_strategy: DiscountStrategy):
        """
        Set a new discount strategy for the product.

        :param discount_strategy: New discount strategy to be set.
        """
        self._discount_strategy = discount_strategy

    def get_final_price(self) -> float:
        """
        Get the final price of the product after applying the discount strategy.

        :return: Price after discount.
        """
        return self._discount_strategy.apply_discount(self.price)
