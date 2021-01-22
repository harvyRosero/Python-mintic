# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 16:45:07 2021

@author: harvy
"""

def prestamo(informacion: dict) -> dict:
    
    id_prestamo = informacion['id_prestamo']
    casado = informacion['casado']
    dependientes = str(informacion['dependientes'])
    historia_credito = informacion['historia_credito']
    educacion = informacion['educacion']
    independiente = informacion['independiente']
    i_d = informacion['ingreso_deudor']
    i_c = informacion['ingreso_codeudor']
    c_p = informacion['cantidad_prestamo']
    p_p = informacion['plazo_prestamo']
    historia_credito = informacion['historia_credito']
    tipo_propiedad = informacion['tipo_propiedad']
    
    
    
    if historia_credito == 1:
        # hiistorial de credito verdadero
        
        if (i_c > 0) and (i_d / 9 > c_p):
            return  {'id_prestamo': id_prestamo, 'aprobado': True }
        elif dependientes > 2 and independiente == 'SI':
            return { 'id_prestamo': id_prestamo, 'aprobado': i_c / 12 > c_p }
        else:
            return { 'id_prestamo': id_prestamo, 'aprobado': c_p < 200 }
        
        # historia de credito falso 
    elif independiente == 'SI':
        if not(casado == 'SI' and dependientes > 1):
            if i_d / 10 > c_p or i_c / 10 > c_p :
                return { 'id_prestamo': id_prestamo, 'aprobado': c_p < 200 }
            else:
                return { 'id_prestamo': id_prestamo, 'aprobado': False }
        else :
            return { 'id_prestamo': id_prestamo, 'aprobado': False }
    else:
        if not( tipo_propiedad == 'semiUrbano' and dependientes < 2):
            if educacion == 'SI':
                return { 'id_prestamo': id_prestamo, 'aprobado': i_d / 11 > c_p and i_c / 11 > c_p }
            else:
                return { 'id_prestamo': id_prestamo, 'aprobado': False}
        else:
            return { 'id_prestamo': id_prestamo, 'aprobado': False }
        
        
diccionario = {'id_prestamo': 'RETOS2_002',
                   'casado' : 'NO',
                   'dependientes' : '3+',
                   'educacion' : 'NO',
                   'independiente' : 'NO',
                   'ingreso_deudor': 1830.0,
                   'ingreso_codeudor' : 0.0,
                   'cantidad_prestamo' : 100,
                   'plazo_prestamo' : 360,
                   'historia_credito': 0,
                   'tipo_propiedad' : 'Urbano'
                   }      

print(prestamo(diccionario))
