"""**Файл с классами**

Здесь хранятся все так или иначе исспользуемые классы"""


class Populy:
    """**Класс популяции**"""


    def __init__(self):
        """**Обьявляем переменные**
        
        populy - количество особей в популяции (целое число)"""


        self.populy = 0


    def add_organizm(self):
        """**Добавляем особь в популяцию**"""


        self.populy += 1


    def del_organizn(self):
        """**Убираем особь из популяции**"""


        self.populy -= 1



class Organism:
    """**Базовывый класс**"""


    def __init__(self, name: str, energy: int):
        """**Обьявляем переменные**
        
        name - имя обьекта (строка)
        energy - энергия (целое число)"""


        self.name = name
        self.energy = energy


    def eat(self, food_energy: int):
        """**Базовая функция еды**

        Принимаем число, добавляем его к энергии и выводим
        сообщение."""


        self.energy += food_energy
        print(f"{self.name} получает {food_energy} энергии.")


    def is_alive(self) -> bool:
        """**Проверка на жизнь**
        
        Если энергия больше нуля - существо живо, 
        если меньше или равна - мертво"""


        return self.energy > 0


class Plant(Organism):
    """**Класс растения**
    
    Ничем не отличается от бащового, 
    но для безопасности вынесен отдельно"""


    def __init__(self, name, energy):
        super().__init__(name, energy)


class Animal(Organism):
    """**Класс животный**
    
    Добавлен параметр straight - сила (целое число)"""


    def __init__(self, name, energy, straight):
        super().__init__(name, energy)
        self.straight = straight


class Herbivore(Animal):
    """**Класс травоядные**"""


    def __init__(self, name, energy, straight):
        """**Опьявляем те же переменные, что и у Animal**"""


        super().__init__(name, energy, straight)


    def eat(self, food:Plant):
        """**Функция поедания растений**"""


        #Если растение живо:
        if food.is_alive:

            #Обьект - обьект, который исполняет функцию
            #Еда - обьект, над которым исполняется функция

            #Если энергия еды меньше/равна силе обьекта
            if food.energy <= self.straight:

                #Энергии обьекта прибавляется энергия еды
                self.energy += food.energy
                #Энергия еды теперь равна 0
                food.energy = 0
                #Выводим информацию на экран:
                print(f"{self.name} получает {food.energy} энергии.")
                print(f"{food.name} умирает.")

            #Иначе (энергия больше силы обьекта):
            else:

                #К энергии обьекта прибавляем силу обьекта
                self.energy += self.straight
                #От энергии еды отнимаем силу обьекта
                food.energy -= self.straight
                #Выводим информацию на экран
                print(f"{self.name} получает {self.straight} энергии.")
                print(f"{food.name} теряет {self.straight} энергии.")

        #Иначе (ежа мертва) выводим сообщение:
        else:
            print(f"{food.name} мертв(а)")


class Predator(Animal):
    """**Класс хищников**
    
    (Предопределение для отсутстви)"""


    def __init__(self, name, energy, straight):
        """**То же, что и у животных**"""


        super().__init__(name, energy, straight)


class Predator(Animal):
    """**Класс хищников**

    Уже действительная часть"""


    def __init__(self, name, energy, straight):
        """**То же, что и у предопределения**"""


        super().__init__(name, energy, straight)


    def eat(self, vict:Predator):
        """**Функция поедания (хищника)**

        Вносится обьект victim класс Predator - другой хищник
        который выступает в роли цели работающего обьекта"""


        #Если обьект жив:
        if vict.is_alive():

            #Обьект - тот обьект, что исполняет функцию
            #Цель - тот обьект, над которым исполняют функцию.

            #Если сила обекта меньше силы цели
            if vict.straight > self.straight:

                #Если энергия обьекта больше силы цели:
                if self.energy > vict.straight:

                    #Из энергии обьекта вычитаем силу цели
                    self.energy -= vict.straight
                    #Энергии цели прибавляем силу цели
                    vict.energy += vict.straight
                    #Выводим информацию о произошедшем
                    print(f"{self.name} теряет {vict.straight} энергии.")
                    print(f"{vict.name} получает {vict.straight} энергии.")

                #Иначе (энергия обьекта меньше силы цели):
                else:
                    #Добавляем энергии цели вс. энергию обьекта 
                    vict.energy += self.energy
                    #Энергия обьекта теперь равна нулю, а обьект умирает
                    self.energy = 0
                    #Выводим информацию на экран
                    print(f"{vict.name} получает {self.energy} энергии.")
                    print(f"{self.name} умирает.")

            #Иначе (сила обьекта больше.равна силе цели):
            else:
                #Если энергия цели больше силы обьекта:
                if vict.energy > self.straight:

                    #Из энергии цели вычитаем силу обьекта
                    vict.energy -= self.straight
                    #К энергии обьекта прибавляем силу обьекта
                    self.energy += self.straight
                    #Выводим информацию на экран:
                    print(f"{self.name} теряет {vict.straight} энергии.")
                    print(f"{vict.name} получает {vict.straight} энергии.")

                #Иначе (энергия цели меньше/равна силе обьекта)
                else:
                    #Энергии обьекта прибавляем энергию цели
                    self.energy += vict.energy
                    #Энергия цели теперь равна нулю (а цель умирает)
                    vict.energy = 0
                    #Выводим информацмю на экран:
                    print(f"{self.name} получает {vict.energy} энергии.")
                    print(f"{vict.name} умирает.")

        #Иначе (цель мертва) выводим сообщение:
        else:
            print(f"{vict.name} мертв(а).")


    def eat(self, vict:Herbivore):
        """**Функция поедания (травоядного)**
        
        Вносится обьект victim класс Herbivore - травоядное
        который выступает в роли цели работающего обьекта"""


        #Обьект - тот обьект, что исполняет функцию
        #Цель - тот обьект, над которым исполняют функцию.

        #Если обьект жив:
        if vict.is_alive():

            #Если сила цели больше силы обьекта:
            if vict.straight > self.straight:
                #Выводим сообщение
                print(f"У {self.name} охота не удалась")

            #Иначе (сила цели меньше/равна силе обьекта)
            else:

                #Если энергия цели больше силы обьекта:
                if vict.energy > self.straight:

                    #Из энергии цели вычитаем силу обьекта
                    vict.energy -= self.straight
                    #Энергии обьекта прибавляем силу обьекта
                    self.energy += self.straight
                    #Выводим информацию на экран
                    print(f"{self.name} получает {self.straight} энергии.")
                    print(f"{vict.name} теряет {self.straight} энергии.")

                #Иначе (энергия цели меньше/равна силе обьекта):
                else:

                    #Энергии обьекта прибавляется энергия цели
                    self.energy += vict.energy
                    #Энергия цели равна 0 (цель умирает):
                    vict.energy = 0
                    #Выводим информацию на экран:
                    print(f"{self.name} получает {vict.energy} энергии.")
                    print(f"{vict.name} умирает.")

        #Иначе (цель мертва) выводим сообщение:
        else:
            print(f"{vict.name} мертв(а).")