class Worker:
    position='сотрудник'
class Kassir(Worker):
    pass
    name = 'Олег'
    position = "кассир"


class Manager(Worker):
    name='Иван'
    position="Менеджер"
    def greeting(self):
        print('Вас приветствует менеджер Иван!')

    def ask(self):
        client_choose = 0
        print("Какой товар вас интересует?")
        client_choose = int(input("1 - телевизоры, 2 - ноутбуки, 3 - мониторы, 4 - принтеры, 5 - микроволновки:    "))
        if client_choose == 5:
            ans = str(input('В наличии микроволновки Samsung, Вас устраивает? (да или нет)'))
            if ans =='Да':
                print ('Прекрасный выбор! Проходите на кассу')
            else:
                manager.ask()
        elif client_choose == 4:
            ans = str(input("В наличии принтеры HP, Вас устраивает? (Да или Нет)"))
            if ans == 'Да':
                print('Прекрасный выбор! Проходите на кассу')
            else:
                manager.ask()
        elif client_choose == 3:

            ans = str(input("В наличии мониторы HP, Вас устраивает? (Да/Нет)"))
            if ans == 'Да':
                print('Прекрасный выбор! Проходите на кассу')
            else:
                manager.ask()
        elif client_choose == 2:

            ans = str(input("В наличии ноутбуки HP, Вас устраивает? (Да/Нет)"))
            if ans == 'Да':
                print('Прекрасный выбор! Проходите на кассу')
            else:
                manager.ask()
        elif client_choose == 1:
            
            ans = str(input("В наличии телевизоры LD, Вас устраивает? (Да/Нет)"))
            if ans == 'Да':
                print('Прекрасный выбор! Проходите на кассу')
            else:
                manager.ask()

class Customer:

    def ask_name(self):
        name =input('Ваше имя: ')
        self.name=name


    def set_laptop(self, laptop):
        self.laptop = laptop

    def set_microwave(self, microwave):
        self.microwave = microwave

    def set_printer(self, printer):
        self.printer = printer

    def set_Televisor(self, Televisor):
        self.Televisor = Televisor


    def set_name(self, name):
        self.name = name




class Tecnic:
    name = ['tv', 'laptop','monitor', 'printer', 'microwave']

class Televisor(Tecnic):
    pass
    model='LD'
    price=500
    quality =10

    def __init__(self, model, price, quality):
        self.model = model
        self.price = price
        self.quality = quality

    def set_model(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

    def set_squality(self, quality):
        self.quality = quality

    def choose_TV(self, choose_TV):
        pass
class laptop(Tecnic):
    pass
    model = 'HP'
    price = 500
    quality = 10

    def __init__(self, model, price, quality):
        self.model = model
        self.price = price
        self.quality = quality

    def set_model(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

    def set_quality(self, quality):
        self.quality = quality

    def choose_laptop(self, choose_TV):
        pass


class  monitor(Tecnic):
    pass
    model = 'HP'
    price = 500
    quality = 10

    def __init__(self, model, price, quality):
        self.model = model
        self.price = price
        self.quality = quality

    def set_model(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

    def set_quality(self, quality):
        self.quality = quality

    def choose_monitor(self, choose_TV):
        pass
class printer(Tecnic):
    pass
    model = 'HP'
    price =  250
    quality = 10

    def __init__(self, model, price, quality):
        self.model = model
        self.price = price
        self.quality = quality

    def set_model(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

    def set_quality(self, quality):
        self.quality = quality

    def choose_laptop(self, choose_TV):
        pass
class microwave(Tecnic):
    pass
    model = ['Samsung']
    price = [500]
    quality = [10]

    def __init__(self, model, price, quality):
        self.model = model
        self.price = price
        self.quality = quality

    def set_model(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

    def quality(self, quality):
        self.quality = quality

    def choose_microwave(self, choose_TV):
        pass





manager = Manager()
customer = Customer()
manager.greeting()
customer.ask_name()

manager.ask()
