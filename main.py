"""**Основной файл**

Рабочее тело проекта"""


#Импортируем модули
from ecosystem import Ecosystem
from organism import Plant, Predator, Herbivore, Populy



def main():
    """**Основная функция**
    
    Рабочее тело проекта"""


    eco = Ecosystem()  #Экосистема
    plants = Populy()  #Популяция растений
    preds = Populy()  #Популяция хищников
    herbs = Populy()  #Популяция травоядных

    #Заяц - травоядное
    rabbit = Herbivore("Заяц", 20, 15)  
    #Лиса - хищник
    fox = Predator("Лиса", 30, 20)  
    #Клубника - растение
    strawberry = Plant("Клубника", 50)  


    #Добавляем существ в экосистему и соответствующие популяции
    eco.add_organism(strawberry, plants) 
    eco.add_organism(rabbit, herbs)
    eco.add_organism(fox, preds)




    #Симулируем день
    eco.simulate_day()


    #Выводим количество существ в популяциях после дня:
    print(f"Растений: {plants.populy}")
    print(f"Хищников: {preds.populy}")
    print(f"Травоядных: {herbs.populy}")




#Запускаем основную функцию:
if __name__ == "__main__":
    main()