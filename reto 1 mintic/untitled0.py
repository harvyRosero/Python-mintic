# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 15:01:34 2021

@author: harvy
"""

"""
necesitamos calcular el promedio
son 5 notas
de las 5 se elimina la peor y se calcula el promedio 
las notas se encuentran en una escala de 0 a 100
debo comnvertir las notas a las escala de 0 a 5
hacer una funcion que resiva un codigo alfanumerico y 5 notas en numeros 

El promedio ajustado del estudiante {código} es: {promedio}

RETORNAR UNA CEDEAN DE CARACTERES
"""


def nota_quices(codigo: str, nota1: int, nota2: int, nota3: int, nota4: int, nota5: int) -> str:
    
    notaBaja = min(nota1, nota2, nota3, nota4, nota5)
    
    promedio = (nota1/20 + nota2/20 + nota3/20 + nota4/20 + nota5/20 - notaBaja/20) / 4
    
    promedioTotal = str(round(promedio, 2))
    
    return "El promedio ajustado del estudiante " + codigo +" es: " + promedioTotal
   
    
print(nota_quices("AA0010276", 40, 50, 39, 76, 96))

         
    
    