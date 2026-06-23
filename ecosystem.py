"""**Файл экосистемы**

Здесь описываются принципы, по которым взаимодействуют
обьекты из organism.py"""

#Импортируем классы существ
from organism import Plant, Herbivore, Predator, Populy


class Ecosystem:
    """**Класс экосистемы**"""


    def __init__(self):
        """**Обьявление переменных**
        
        organisms - список всех организмов (список)"""



        self.organisms = []


    def add_organism(self, organism, population:Populy):
        """**Функция добавления организма**
        """

        

        self.organisms.append(organism)
        population.add_organizm()




    def simulate_day(self):
        """**Функция симуляции взаимодействий обьектов**"""



        #Проходимся по списку
        for org in self.organisms:

            #Если проверяемый обьект жив:
            if org.is_alive():

                #Проверяем класс обьекта
                tp = str(type(org))

                #Если класс - Predator:
                if tp == "<class 'organism.Predator'>":

                    #Проходимся снова по списку обьектов:
                    for vict in self.organisms:

                        #Проверяем класс второго обьекта
                        vict_tp = str(type(vict))

                        #Проверка условий:
                        #Класс втрого обьекта -
                        pos1 = vict_tp == "<class 'organism.Predator'>"
                        #Кдасс второго обьекта -
                        pos2 = vict_tp == "<class 'organism.Herbivore'>"
                        #Второй обьект - это не первый
                        pos3 = (vict != org)

                        #Если (первое или второе) и третье условия:
                        if (pos1 or pos2) and pos3:
                            #Первый обьект пытается сьест второй
                            org.eat(vict)

                #Если класс обьекта - 
                elif tp == "<class 'organism.Herbivore'>":

                    #Проходимся снова по списку
                    for vict in self.organisms:

                        #Проверяем класс второго обьекта
                        vict_tp = str(type(vict))

                        #Класс второго обьекта - 
                        pos1 = (vict_tp == "<class 'organism.Plant'>")
                        #Второй обьект - это не первый
                        pos2 = (vict != org)

                        #Если первое и второе:
                        if pos1 and pos2:
                            #Первый обьект пытается сьест второй
                            org.eat(vict)

                #Иначе:
                else:
                    #Просто даем обьекту 10 энергии
                    org.eat(10)

            #Иначе - выводим сообщение:          
            else:
                print(f"{org.name} мёртв.")

            