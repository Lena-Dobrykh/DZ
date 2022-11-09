#Я считаю, что этот код не упростить функциональным подходом. 
#Логическим возможно получится упростить с помощью pyDatalog для упрощенного поиска.
import datetime

now=datetime.datetime.now()

class People:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f"People('{self.name}')"

class Client(People):
    def __repr__(self):
        return f"Client('{self.name}')"
    
class Master(People):
    def __repr__(self):
        return f"Master('{self.name}')"
    
class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
        
    def __repr__(self):
        return f"Car('{self.brand}',{self.model})"

class Malfunction:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f"Malfunction('{self.name}')"

class Remedy:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __repr__(self):
        return f"Remedy('{self.name}',{self.price}'рублей')"

class Repair:
    def __init__(self,
                 name,
                 client=[],
                 master=[],
                 car=[],
                 remedy=[]):
        self.name = name
        self.client = client
        self.master = master
        self.car = car
        self.remedy = remedy
        
    def __repr__(self):
        return f"Repair('{self.name}', {self.client},{self.master},{self.car},{self.remedy})"

    def receive_repair(self, repair):
        try:
            self.repairs += [repair]
        except AttributeError:
            self.repairs = [repair]

    def enum_repairs(self):
        for x in self.repairs:
            yield x
    
if __name__ =='__main__':
    people = People('Вася')
    client1 = Client('Лена')
    client2 = Client('Наташа')
    master1 = Master ('Александр')
    car1 = Car('Nissan','Almera')
    car2 = Car('Kia', 'Rio')
    malfunction1 = Malfunction('Нет автосигнализации')
    malfunction2 = Malfunction('Перегорела лампочка')
    remedy1 = Remedy('Установка автосигнализации',2500)
    remedy2 = Remedy('Замена лампочки',100)
    check1 = Repair(
        name = 'Чек',      
        client = client1,
        master = master1,
        car = car1,
        remedy = remedy1)
    check2 = Repair(
        name = 'Чек',
        client = client2,
        master = master1,
        car = car2,
        remedy = remedy2)
    check3 = Repair(
        name = 'Чек',
        client = client1,
        master = master1,
        car = car2,
        remedy = remedy2)
    print(client1,master1,car1,malfunction1,remedy1,now)
    print(check1)
    print(check2)
    check1.receive_repair(car1)
    check2.receive_repair(car2)
    check3.receive_repair(car2)
    print(list(check3.enum_repairs()))
