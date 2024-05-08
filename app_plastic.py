import os
import time

#variables
op_menu = ""                        # Selección menú principal
op_producto = ""                    # Selección menú productos
nombre_producto = ""                # Nombre del producto
op_tipo_cliente = ""                # Selección General/Socio
tipo_cliente = ""                   # General / Socio
valor_producto = 0                  # Valor por 1 producto
cantidad = 0                        # Cantidad del producto
en_efectivo = "N"                   # S/N -> si paga en efectivo o no
monto_descuento = 0                 # Descuento aplicado
subtotal = 0                        # Precio x Cantidad
total_pagar = 0                     # Monto final a pagar
mensaje = ""                        # Mensaje para el ticket

# estadisticas
total_recaudado = 0
cant_prod_vendidos = 0

# código

while True:
    mensaje = ""                      # ----> se reinicia la variable
    os.system("cls")
    op_menu = str(input(f'''
    ------- MENÚ --------
    1. Venta de productos
    2. Estadísticas
    3. Salir
    \n Elija opción: '''))
    
    if op_menu == "1":
        
        os.system("cls")
        
        op_producto = str(input(f'''
    ------- Venta de productos ------
    Producto \t\t Valor General \t Valor Socio
    1. Tazón \t\t $800 \t\t $500
    2. Llavero \t\t $500 \t\t $300
    3. Polera Estampada  $5000 \t    $3000 
    \n Elija opción: '''))
        
        if op_producto == "1":
            nombre_producto = "Tazón"
            op_tipo_cliente = str(input(f'''
            Selección: {nombre_producto}
            Ingrese el tipo de cliente
            (1) General \t (2) Socio
            \n Elija opción: '''))
            if op_tipo_cliente == "1":
                tipo_cliente = "General"
                valor_producto = 800
            if op_tipo_cliente == "2":
                tipo_cliente = "Socio"
                valor_producto = 500
                
        if op_producto == "2":
            nombre_producto = "Llavero"
            op_tipo_cliente = str(input(f'''
            Selección: {nombre_producto}
            Ingrese el tipo de cliente
            (1) General \t (2) Socio
            \n Elija opción: '''))
            if op_tipo_cliente == "1":
                tipo_cliente = "General"
                valor_producto = 500
            if op_tipo_cliente == "2":
                tipo_cliente = "Socio"
                valor_producto = 300
                
        if op_producto == "3":
            nombre_producto = "Polera Estampada"
            op_tipo_cliente = str(input(f'''
            Selección: {nombre_producto}
            Ingrese el tipo de cliente
            (1) General \t (2) Socio
            \n Elija opción: '''))
            if op_tipo_cliente == "1":
                tipo_cliente = "General"
                valor_producto = 5000
            if op_tipo_cliente == "2":
                tipo_cliente = "Socio"
                valor_producto = 3000
                        
        cantidad = int(input(f'''
            Esta comprando {nombre_producto}
            A un valor de {valor_producto} c/u
            
            Ingrese cantidad deseada: '''))
        
        while cantidad < 0:
            print("Error, minímo 1 producto")
            cantidad = int(input(f'''
            Esta comprando {nombre_producto}
            A un valor de {valor_producto} c/u
                
            Ingrese cantidad deseada: '''))
            
        cant_prod_vendidos = cant_prod_vendidos + cantidad
        
        subtotal = cantidad * valor_producto
        
        en_efectivo = str(input(f'''
            Subtotal: ${subtotal}
            
            Si paga con efectivo se le agregara un 20%
            a la compra.
            
            ¿Paga en efectivo? S/N: ''')).upper().strip()
        
        if en_efectivo == "S":
            monto_descuento = subtotal * 0.2
            mensaje = print(f'''Descuento pago efectivo 20$ 
            ${monto_descuento}''')
        else:
            monto_descuento = 0
            
        total_pagar = subtotal - monto_descuento
        
        total_recaudado = total_recaudado + total_pagar
        
        #Ticket
        
        os.system("cls")
        
        print(f'''
        ---------- TICKET ----------
        Producto: {nombre_producto}
        Cantidad del producto: {cantidad}
        Tipo de cliente: {tipo_cliente}
        Subtotal: ${subtotal}''')
        if en_efectivo == "S":
            print(f'''
        {mensaje}
        Total a pagar: ${total_pagar}''')
        else:
            print(f'''
        Total a pagar: ${total_pagar}''')
        print(f'''
                            Gracias por preferirnos! :D''')
    
        os.system("pause")
        
    if op_menu == "2":
        
        os.system("cls")
        
        print(f'''
        ------- Estadísticas ------
        Total de productos vendidos: {cant_prod_vendidos}
        Total recaudado: {total_recaudado}
        
        Aprete cualquier tecla para volver al menú principal''')
        
        os.system("pause")
        
    if op_menu == "3":
        
        os.system ("cls")
        
        print("...Saliendo de la app...")
        time.sleep(2)
        print("Gracias por preferirnos. :D")
        
        break