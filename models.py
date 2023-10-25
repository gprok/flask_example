
class Product:
    def __init__(self, pid, name, price) -> None:
        self.id = pid
        self.name = name
        self.price = price 

    def __str__(self) -> str:
        return '{} {} {}'.format(self.id, self.name, self.price)
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price
        }