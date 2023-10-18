from abc import ABC, abstractmethod


"""
    Abstracción: Se define una estructura común (interfaz) para
        las estrategias de descuento.
    Segregación de Interfaz: Se define una interfaz específica 
        y enfocada para aplicar descuentos.
"""


class DiscountStrategy(ABC):
    # Polimorfismo: A través de este método abstracto, diferentes
    #   estrategias podrán tener diferentes implementaciones.
    @abstractmethod
    def apply_discount(self, amount: float) -> float:
        pass


"""
    Herencia: StudentDiscount hereda de DiscountStrategy y define 
        una estrategia concreta.
    Sustitución de Liskov: Esta clase concreta puede ser sustituida
        por su clase padre (DiscountStrategy) sin afectar
        el comportamiento.
"""


class StudentDiscount(DiscountStrategy):
    def apply_discount(self, amount: float) -> float:
        """Apply student discount"""
        return amount * 0.90


# Herencia: Otra clase que hereda de DiscountStrategy.
class SeasonalDiscount(DiscountStrategy):
    def apply_discount(self, amount: float) -> float:
        """Apply seasonal discount"""
        return amount * 0.80


# Herencia: Otra clase que hereda de DiscountStrategy.
class NoDiscount(DiscountStrategy):
    """Not apply any discount"""

    def apply_discount(self, amount: float) -> float:
        return amount


"""
    Modularidad: El comportamiento de descuento se ha separado en 
        diferentes clases (estrategias), y esta clase Product solo 
        se preocupa por los detalles del producto y cómo aplicar 
        un descuento.
"""


class Product:
    # Inversión de Dependencias: En lugar de depender de estrategias
    #   de descuento concretas, Product depende de la abstracción
    #   (DiscountStrategy).
    def __init__(self, price: float, discount_strategy: DiscountStrategy):
        self.price = price
        self._discount_strategy = discount_strategy

    # Responsabilidad Única: Un método que solo se encarga de
    #   establecer la estrategia de descuento.
    def set_discount_strategy(self, discount_strategy: DiscountStrategy):
        self._discount_strategy = discount_strategy

    # Responsabilidad Única: Un método que solo se encarga de obtener
    #   el precio final después del descuento.
    # Abierto-Cerrado: Podemos cambiar la estrategia de descuento en
    #   tiempo de ejecución sin modificar la clase Product.
    def get_final_price(self) -> float:
        return self._discount_strategy.apply_discount(self.price)


# Ejemplo de uso:

# Create a product with a base price of $100 and no discount
product = Product(100, NoDiscount())
print(f"Price without discount: ${product.get_final_price()}")

# Set a student discount strategy and get the price
product.set_discount_strategy(StudentDiscount())
print(f"Price with student discount: ${product.get_final_price()}")

# Set a seasonal discount strategy and get the price
product.set_discount_strategy(SeasonalDiscount())
print(f"Price with seasonal discount: ${product.get_final_price()}")
