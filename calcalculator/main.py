'''
Приложение расчитывает базовые параметры диеты. 
Получив начальные данные от пользователя расчитывает для него следующие параметры:
    - Базальный (базовый) обмен веществ;
    - Нормы калорий для текущего и желаемого веса;
    - Нормы по нутриентам. КБЖУ в виде граммов продуктов.
'''

from typing import NamedTuple

class Person(NamedTuple):
    name:str
    current_weigth:float
    desired_weigth:float
    height:float
    gender:bool
    age:int
    activity:int

def main:
    get_current_person_parameters()
    calculate(Person)
    print_recomendation()
    create_pdf_with_result()

if __name__ == "__main__":
    print("Hi, there!")
