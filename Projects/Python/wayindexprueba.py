
def centrar_palabra(patron):
    longitud_maxima = max(len(linea) for linea in patron)
    return [linea.center(longitud_maxima) for linea in patron]

# Patrones de las letras
patron_D = [
    "*****",
    "*    *",
    "*    *",
    "*    *",
    "*****"
]

patron_I = [
    "*****",
    "  *  ",
    "  *  ",
    "  *  ",
    "*****"
]

patron_A = [
    "  *  ",
    " * * ",
    "*   *",
    "*****",
    "*   *"
]

patron_Z = [
    "*****",
    "   * ",
    "  *  ",
    " *   ",
    "*****"
]

patron_F = [
    "*****",
    "*    ",
    "*    ",
    "**** ",
    "*    "
]

patron_L = [
    "*    ",
    "*    ",
    "*    ",
    "*    ",
    "*****"
]

patron_I2 = [
    "*****",
    "  *  ",
    "  *  ",
    "  *  ",
    "*****"
]

patron_G = [
    "*****",
    "*    ",
    "*  **",
    "*   *",
    "*****"
]

patron_H = [
    "*   *",
    "*   *",
    "*****",
    "*   *",
    "*   *"
]

patron_T = [
    "*****",
    "  *  ",
    "  *  ",
    "  *  ",
    "  *  "
]

patron_S = [
    " *****",
    "*    ",
    "*****",
    "    *",
    "*****"
]

# Centrar cada palabra
patron_D_centrado = centrar_palabra(patron_D)
patron_I_centrado = centrar_palabra(patron_I)
patron_A_centrado = centrar_palabra(patron_A)
patron_Z_centrado = centrar_palabra(patron_Z)

patron_F_centrado = centrar_palabra(patron_F)
patron_L_centrado = centrar_palabra(patron_L)
patron_I2_centrado = centrar_palabra(patron_I2)
patron_G_centrado = centrar_palabra(patron_G)
patron_H_centrado = centrar_palabra(patron_H)
patron_T_centrado = centrar_palabra(patron_T)
patron_S_centrado = centrar_palabra(patron_S)

# Imprimir las letras "Diaz" centradas y luego un espacio y las letras "Flights" centradas
for lineas in zip(patron_D_centrado, patron_I_centrado, patron_A_centrado, patron_Z_centrado, [" "] * 5,
                  patron_F_centrado, patron_L_centrado, patron_I2_centrado, patron_G_centrado,
                  patron_H_centrado, patron_T_centrado, patron_S_centrado):
    print(" ".join(lineas))
        
print("")
     
#Nombre de la aerolinea centralizado   
frase = "Bienvenido/a a Diaz Flights"
ancho_total = 130  # Establece el ancho total deseado
frase_centralizada = frase.center(ancho_total)
print(frase_centralizada)

#Fecha en tiempo real centralizada
from datetime import datetime
fecha_hora_actual = datetime.now()
cadena_fecha_hora = "Fecha y hora actuales: " + str(fecha_hora_actual)
cadena_centralizada = cadena_fecha_hora.center(ancho_total)
print(cadena_centralizada)

def centrar_mensaje(mensaje, ancho_total):
    return mensaje.center(ancho_total)

def mostrar_menu_reservar_vuelo():
    print(centrar_mensaje("1. Reservar vuelo", ancho_total))
    print(centrar_mensaje("2. Cerrar la pagina", ancho_total))
    opcion = input("Selecciona una opción (1 o 2): ")
    
    if opcion == "1":
        mostrar_menu_destinacion()
    elif opcion == "2":
        print("Lamentamos su salida de Diaz Flights, Esperamos verlo/a pronto.")
    else:
        print("Opción no válida. Inténtalo de nuevo.", ancho_total)
    
def mostrar_menu_destinacion():
    print(centrar_mensaje("Elige hacia donde será tu vuelo", ancho_total))
    print(centrar_mensaje("Destino...", ancho_total))
    print(centrar_mensaje("1. Caribe", ancho_total))
    print(centrar_mensaje("2. América Central", ancho_total))
    print(centrar_mensaje("3. América del Norte", ancho_total))
    print(centrar_mensaje("4. América del Sur", ancho_total))
    print(centrar_mensaje("5. Todos...", ancho_total))
    opcion = input("Selecciona una opción (1, 2, 3, 4 o 5): ")

    
    if opcion == "1":
        mostrar_paises_caribe()
    elif opcion == "2":
        mostrar_paises_america_central()
    elif opcion == "3":
        mostrar_paises_america_norte()
    elif opcion == "4":
        mostrar_paises_america_sur()
    elif opcion == "5":
        mostrar_todos_paises()
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        mostrar_menu_destinacion()

def mostrar_paises_caribe():
    paises_caribe = ["Cuba", "Jamaica", "Puerto Rico", "Bahamas", "Haití", "Barbados", "Trinidad y Tobago"]
    print(centrar_mensaje("Paises del Caribe:", ancho_total))
    for i, pais in enumerate(paises_caribe, start=1):
        print(f"{i}. {pais}")
    
    opcion_pais = input("Selecciona un país del Caribe: ")
    
    
    if opcion_pais.isdigit() and 1 <= int(opcion_pais) <= len(paises_caribe):
        if paises_caribe[int(opcion_pais) - 1] in ["Cuba", "Jamaica", "Puerto Rico", "Bahamas", "Haití", "Barbados", "Trinidad y Tobago"]:
            fecha_ida = input("Ingresa tu fecha de ida (DD/MM/AAAA): ")
            opciones_precio_vuelo_ida(paises_caribe[int(opcion_pais) - 1], fecha_ida)
        else:
            print(f"Has elegido: {paises_caribe[int(opcion_pais) - 1]}. ¡Disfruta tu vuelo!")
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        
def opciones_precio_vuelo_ida(pais, fecha_ida):
    print(f"Fecha de ida: {fecha_ida}")
    print(centrar_mensaje("Precios de vuelo de ida", ancho_total))

    if pais == "Cuba":
        print("1. Vuelo DO - CU   $130 (Ecónomico)")
        print("1. Vuelo DO - CU   $145 (VIP)")
    elif pais == "Jamaica":
        print("1. Vuelo DO - JA   $130 (Ecónomico)")
        print("2. Vuelo DO - JA   $145 (VIP)")
    elif pais == "Puerto Rico":
        print("1. Vuelo DO - PR   $130 (Ecónomico)")
        print("2. Vuelo DO - PR   $145 (VIP)")
    elif pais == "Bahamas":
        print("1. Vuelo DO - BA   $130 (Ecónomico)")
        print("2. Vuelo DO - BA   $145 (VIP)")
    elif pais == "Haiti":
        print("1. Vuelo DO - HA   $130 (Ecónomico)")
        print("2. Vuelo DO - HA   $145 (VIP)")
    elif pais == "Barbados":
        print("1. Vuelo DO - BR   $130 (Ecónomico)")
        print("2. Vuelo DO - BR   $145 (VIP)")
    elif pais == "Trinidad y Tobago":
        print("1. Vuelo DO - TT   $130 (Ecónomico)")
        print("2. Vuelo DO - TT   $145 (VIP)")
    
        opcion_vuelo = input("Selecciona una opción de vuelo (1 o 2): ")
    
    if opcion_vuelo == "1" or opcion_vuelo == "2":
        fecha_regreso = input("¿Cuál será tu fecha de regreso (DD/MM/AAAA)? ")
        print(f"Fecha de regreso: {fecha_regreso}")
        opciones_precio_vuelo_regreso(pais)
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        opciones_precio_vuelo_ida(pais, fecha_ida)

def opciones_precio_vuelo_regreso(pais):
    print(centrar_mensaje("Precios de vuelo de regreso"))

    if pais == "Cuba":
        print("1. Vuelo CU - DO   $180 (Ecónomico)")
        print("1. Vuelo CU - DO   $190 (VIP)")
    elif pais == "Jamaica":
        print("1. Vuelo JA - DO   $180 (Ecónomico)")
        print("2. Vuelo JA - DO   $190 (VIP)")
    elif pais == "Puerto Rico":
        print("1. Vuelo PR - DO   $180 (Ecónomico)")
        print("2. Vuelo PR - DO   $190 (VIP)")
    elif pais == "Bahamas":
        print("1. Vuelo BA - DO   $180 (Ecónomico)")
        print("2. Vuelo BA - DO   $190 (VIP)")
    elif pais == "Haiti":
        print("1. Vuelo HA - DO   $180 (Ecónomico)")
        print("2. Vuelo HA - DO   $190 (VIP)")
    elif pais == "Barbados":
        print("1. Vuelo BR - DO   $180 (Ecónomico)")
        print("2. Vuelo BR - DO   $190 (VIP)")
    elif pais == "Trinidad y Tobago":
        print("1. Vuelo TT - DO   $180 (Ecónomico)")
        print("2. Vuelo TT - DO   $190 (VIP)")

        opcion_vuelo = input("Selecciona una opción de vuelo de regreso (1 o 2): ")
   
        
def mostrar_paises_america_central():
    paises_america_central = ["Guatemala", "El Salvador", "Honduras", "Nicaragua", "Costa Rica", "Panamá", "Belice"]
    print(centrar_mensaje("Paises de América Central:", ancho_total))
    for i, pais in enumerate(paises_america_central, start=1):
        print(f"{i}. {pais}")
    
    opcion_pais = input("Selecciona un país de América Central: ")
   
    
    if opcion_pais.isdigit() and 1 <= int(opcion_pais) <= len(paises_america_central):
        if paises_america_central[int(opcion_pais) - 1] in ["Guatemala", "El Salvador", "Honduras", "Nicaragua", "Costa Rica", "Panamá", "Belice"]:
            fecha_ida = input("Ingresa tu fecha de ida (DD/MM/AAAA): ")
            opciones_precio_vuelo_ida(paises_america_central[int(opcion_pais) - 1], fecha_ida)
        else:
            print(f"Has elegido: {paises_america_central[int(opcion_pais) - 1]}. ¡Disfruta tu vuelo!")
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        mostrar_paises_america_central()
        
def opciones_precio_vuelo_ida(pais, fecha_ida):
    print(f"Fecha de ida: {fecha_ida}")
    print(centrar_mensaje("Precios de vuelo de ida", ancho_total))

    if pais == "Guatemala":
        print("1. Vuelo DO - GU   $130 (Ecónomico)")
        print("1. Vuelo DO - GU   $145 (VIP)")
    elif pais == "El Salvador":
        print("1. Vuelo DO - SA   $130 (Ecónomico)")
        print("2. Vuelo DO - SA   $145 (VIP)")
    elif pais == "Honduras":
        print("1. Vuelo DO - HO   $130 (Ecónomico)")
        print("2. Vuelo DO - HO   $145 (VIP)")
    elif pais == "Nicaragua":
        print("1. Vuelo DO - NI   $130 (Ecónomico)")
        print("2. Vuelo DO - NI   $145 (VIP)")
    elif pais == "Costa Rica":
        print("1. Vuelo DO - CR   $130 (Ecónomico)")
        print("2. Vuelo DO - CR   $145 (VIP)")
    elif pais == "Panamá":
        print("1. Vuelo DO - PA   $130 (Ecónomico)")
        print("2. Vuelo DO - PA   $145 (VIP)")
    elif pais == "Belice":
        print("1. Vuelo DO - BE   $130 (Ecónomico)")
        print("2. Vuelo DO - BE   $145 (VIP)")
    
    opcion_vuelo = input("Selecciona una opción de vuelo (1 o 2): ")
    
    if opcion_vuelo == "1" or opcion_vuelo == "2":
        fecha_regreso = input("¿Cuál será tu fecha de regreso (DD/MM/AAAA)? ")
        print(f"Fecha de regreso: {fecha_regreso}")
        opciones_precio_vuelo_regreso(pais)
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        opciones_precio_vuelo_ida(pais, fecha_ida)

def opciones_precio_vuelo_regreso(pais):
    print(centrar_mensaje("Precios de vuelo de regreso", ancho_total))

    if pais == "Guatemala":
        print("1. Vuelo GU - DO   $180 (Ecónomico)")
        print("1. Vuelo GU - DO   $190 (VIP)")
    elif pais == "El Salvador":
        print("1. Vuelo SA - DO   $180 (Ecónomico)")
        print("2. Vuelo SA - DO   $190(VIP)")
    elif pais == "Honduras":
        print("1. Vuelo HO - DO   $180 (Ecónomico)")
        print("2. Vuelo HO - DO   $190 (VIP)")
    elif pais == "Nicaragua":
        print("1. Vuelo NI - DO   $180 (Ecónomico)")
        print("2. Vuelo NI - DO   $190 (VIP)")
    elif pais == "Costa Rica":
        print("1. Vuelo CR - DO   $180 (Ecónomico)")
        print("2. Vuelo CR - DO   $190 (VIP)")
    elif pais == "Panamá":
        print("1. Vuelo PA - DO   $180 (Ecónomico)")
        print("2. Vuelo PA - DO   $190 (VIP)")
    elif pais == "Belice":
        print("1. Vuelo BE - DO   $180 (Ecónomico)")
        print("2. Vuelo BE - DO   $190 (VIP)")

        opcion_vuelo = input("Selecciona una opcion de vuelo: ")

def mostrar_paises_america_norte():
    paises_america_norte = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawái"]
    print(centrar_mensaje("Paises de América del Norte:", ancho_total))
    for i, pais in enumerate(paises_america_norte, start=1):
        print(f"{i}. {pais}")
    
    opcion_pais = input("Selecciona un país de América del Norte: ")
    
    if opcion_pais.isdigit() and 1 <= int(opcion_pais) <= len(paises_america_norte):
        if paises_america_norte[int(opcion_pais) - 1] in ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawái"]:
            fecha_ida = input("Ingresa tu fecha de ida (DD/MM/AAAA): ")
            opciones_precio_vuelo_ida(paises_america_norte[int(opcion_pais) - 1], fecha_ida)
        else:
            print(f"Has elegido: {paises_america_norte[int(opcion_pais) - 1]}. ¡Disfruta tu vuelo!")
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        mostrar_paises_america_norte()
        
def opciones_precio_vuelo_ida(pais, fecha_ida):
    print(f"Fecha de ida: {fecha_ida}")
    print(centrar_mensaje("Precios de vuelo de ida", ancho_total))

    if pais == "Alabama":
        print("1. Vuelo DO - AL   $130 (Ecónomico)")
        print("1. Vuelo DO - AL   $145 (VIP)")
    elif pais == "Alaska":
        print("1. Vuelo DO - AK   $130 (Ecónomico)")
        print("2. Vuelo DO - AK   $145 (VIP)")
    elif pais == "Arizona":
        print("1. Vuelo DO - AR   $130 (Ecónomico)")
        print("2. Vuelo DO - AR   $145 (VIP)")
    elif pais == "Arkansas":
        print("1. Vuelo DO - AS   $130 (Ecónomico)")
        print("2. Vuelo DO - AS   $145 (VIP)")
    elif pais == "California":
        print("1. Vuelo DO - CF   $130 (Ecónomico)")
        print("2. Vuelo DO - CF   $145 (VIP)")
    elif pais == "Colorado":
        print("1. Vuelo DO - CO   $130 (Ecónomico)")
        print("2. Vuelo DO - CO   $145 (VIP)")
    elif pais == "Connecticut":
        print("1. Vuelo DO - CC   $130 (Ecónomico)")
        print("2. Vuelo DO - CC   $145 (VIP)")
    elif pais == "Delaware":
        print("Vuelo DO - DW   $130 (Ecónomico)")
        print("Vuelo DO - DW   $145 (VIP)")
    elif pais == "Florida":
        print("Vuelo DO - FL   $130 (Ecónomico)")
        print("Vuelo DO - FL   $145 (VIP)")
    elif pais == "Georgia":
        print("Vuelo DO - GEO   $130 (Ecónomico)")
        print("Vuelo DO - GEO   $145 (VIP)")
    elif pais == "Hawái":
        print("Vuelo DO - HW   $130 (Ecónomico)")
        print("Vuelo DO - HW   $145 (VIP)")
    
        opcion_vuelo = input("Selecciona una opción de vuelo (1 o 2): ")
    
    if opcion_vuelo == "1" or opcion_vuelo == "2":
        fecha_regreso = input("¿Cuál será tu fecha de regreso (DD/MM/AAAA)? ")
        print(f"Fecha de regreso: {fecha_regreso}")
        opciones_precio_vuelo_regreso(pais)
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        opciones_precio_vuelo_ida(pais, fecha_ida)

def opciones_precio_vuelo_regreso(pais):
    print(centrar_mensaje("Precios de vuelo de regreso"))

    if pais == "Alabama":
        print("1. Vuelo AL - DO   $130 (Ecónomico)")
        print("1. Vuelo AL - DO   $145 (VIP)")
    elif pais == "Alaska":
        print("1. Vuelo AK - DO   $130 (Ecónomico)")
        print("2. Vuelo AK - DO   $145 (VIP)")
    elif pais == "Arizona":
        print("1. Vuelo AR - DO   $130 (Ecónomico)")
        print("2. Vuelo AR - DO   $145 (VIP)")
    elif pais == "Arkansas":
        print("1. Vuelo AS - DO   $130 (Ecónomico)")
        print("2. Vuelo AS - DO   $145 (VIP)")
    elif pais == "California":
        print("1. Vuelo CF - DO   $130 (Ecónomico)")
        print("2. Vuelo CF - DO   $145 (VIP)")
    elif pais == "Colorado":
        print("1. Vuelo CO - DO   $130 (Ecónomico)")
        print("2. Vuelo CO - DO   $145 (VIP)")
    elif pais == "Connecticut":
        print("1. Vuelo CC - DO   $130 (Ecónomico)")
        print("2. Vuelo CC - DO   $145 (VIP)")
    elif pais == "Delaware":
        print("Vuelo DW - DO   $130 (Ecónomico)")
        print("Vuelo DW - DO   $145 (VIP)")
    elif pais == "Florida":
        print("Vuelo FL - DO   $130 (Ecónomico)")
        print("Vuelo FL - DO   $145 (VIP)")
    elif pais == "Georgia":
        print("Vuelo GEO - DO   $130 (Ecónomico)")
        print("Vuelo GEO - DO   $145 (VIP)")
    elif pais == "Hawái":
        print("Vuelo HW - DO   $130 (Ecónomico)")
        print("Vuelo HW - DO   $145 (VIP)")
        
        opcion_vuelo = input("Selecciona una opción de vuelo (1 o 2): ")

def mostrar_paises_america_sur():
    paises_america_sur = ["Brasil", "Argentina", "Colombia", "Perú", "Venezuela", "Chile", "Ecuador", "Bolivia", "Paraguay", "Uruguay"]
    print(centrar_mensaje("Paises de América del Sur:", ancho_total))
    for i, pais in enumerate(paises_america_sur, start=1):
        print(f"{i}. {pais}")
    
    opcion_pais = input("Selecciona un país de América del Sur: ")
    
    if opcion_pais.isdigit() and 1 <= int(opcion_pais) <= len(paises_america_sur):
        if paises_america_sur[int(opcion_pais) - 1] in ["Brasil", "Argentina", "Colombia", "Perú", "Venezuela", "Chile", "Ecuador", "Bolivia", "Paraguay", "Uruguay"]:
            fecha_ida = input("Ingresa tu fecha de ida (DD/MM/AAAA): ")
            opciones_precio_vuelo_ida(paises_america_sur[int(opcion_pais) - 1], fecha_ida)
        else:
            print(f"Has elegido: {paises_america_sur[int(opcion_pais) - 1]}. ¡Disfruta tu vuelo!")
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        mostrar_paises_america_norte()
        
def opciones_precio_vuelo_ida(pais, fecha_ida):
    print(f"Fecha de ida: {fecha_ida}")
    print(centrar_mensaje("Precios de vuelo de ida", ancho_total))

    if pais == "Brasil":
        print("1. Vuelo DO - AL   $130 (Ecónomico)")
        print("1. Vuelo DO - AL   $145 (VIP)")
    elif pais == "Argentina":
        print("1. Vuelo DO - AK   $130 (Ecónomico)")
        print("2. Vuelo DO - AK   $145 (VIP)")
    elif pais == "Colombia":
        print("1. Vuelo DO - AR   $130 (Ecónomico)")
        print("2. Vuelo DO - AR   $145 (VIP)")
    elif pais == "Perú":
        print("1. Vuelo DO - AS   $130 (Ecónomico)")
        print("2. Vuelo DO - AS   $145 (VIP)")
    elif pais == "Venezuela":
        print("1. Vuelo DO - CF   $130 (Ecónomico)")
        print("2. Vuelo DO - CF   $145 (VIP)")
    elif pais == "Chile":
        print("1. Vuelo DO - CO   $130 (Ecónomico)")
        print("2. Vuelo DO - CO   $145 (VIP)")
    elif pais == "Ecuador":
        print("1. Vuelo DO - CC   $130 (Ecónomico)")
        print("2. Vuelo DO - CC   $145 (VIP)")
    elif pais == "Bolivia":
        print("Vuelo DO - DW   $130 (Ecónomico)")
        print("Vuelo DO - DW   $145 (VIP)")
    elif pais == "Paraguay":
        print("Vuelo DO - FL   $130 (Ecónomico)")
        print("Vuelo DO - FL   $145 (VIP)")
    elif pais == "Uruguay":
        print("Vuelo DO - GEO   $130 (Ecónomico)")
        print("Vuelo DO - GEO   $145 (VIP)")          
    
    opcion_vuelo = input("Selecciona una opción de vuelo (1 o 2): ")
    
    if opcion_vuelo == "1" or opcion_vuelo == "2":
        fecha_regreso = input("¿Cuál será tu fecha de regreso (DD/MM/AAAA)? ")
        print(f"Fecha de regreso: {fecha_regreso}")
        opciones_precio_vuelo_regreso(pais)
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        opciones_precio_vuelo_ida(pais, fecha_ida)

def opciones_precio_vuelo_regreso(pais):
    print(centrar_mensaje("Precios de vuelo de regreso"))

    if pais == "Brasil":
        print("1. Vuelo AL - DO   $180 (Ecónomico)")
        print("1. Vuelo AL - DO   $190 (VIP)")
    elif pais == "Argentina":
        print("1. Vuelo AK - DO   $180 (Ecónomico)")
        print("2. Vuelo AK - DO   $190 (VIP)")
    elif pais == "Colombia":
        print("1. Vuelo AR - DO   $180 (Ecónomico)")
        print("2. Vuelo AR - DO   $190 (VIP)")
    elif pais == "Perú":
        print("1. Vuelo AS - DO   $180 (Ecónomico)")
        print("2. Vuelo AS - DO   $190 (VIP)")
    elif pais == "Venezuela":
        print("1. Vuelo CF - DO   $180 (Ecónomico)")
        print("2. Vuelo CF - DO   $190 (VIP)")
    elif pais == "Chile":
        print("1. Vuelo CO - DO   $180 (Ecónomico)")
        print("2. Vuelo CO - DO   $190")
    elif pais == "Ecuador":
        print("1. Vuelo CC - DO   $180")
        print("2. Vuelo CC - DO   $190")
    elif pais == "Bolivia":
        print("Vuelo DW - DO   $180")
        print("Vuelo DW - DO   $190")
    elif pais == "Paraguay":
        print("Vuelo FL - DO   $180")
        print("Vuelo FL - DO   $190")
    elif pais == "Uruguay":
        print("Vuelo GEO - DO   $180")
        print("Vuelo GEO - DO   $190")
        
        opcion_vuelo = input("Selecciona una opción de vuelo (1 o 2): ")
    

def mostrar_todos_paises():
    todos_los_paises = ["Antigua y Barbuda", "Argentina", "Bahamas", "Barbados", "Belice", "Bolivia", "Brasil", "Colombia", "Costa Rica", "Cuba", "Chile", "Dominica", "Ecuador", "El Salvador", "Granada", "Guatemala", "Guyana", "Haití", "Honduras", "Jamaica", "México", "Nicaragua", "Panamá", "Paraguay", "Perú", "República Dominicana", "San Cristóbal y Nieves", "San Vicente y las Granadinas", "Santa Lucía", "Surinam", "Trinidad y Tobago", "Uruguay", "Venezuela"]
    print(centrar_mensaje("Todos los países del mundo:", ancho_total))
    for i, pais in enumerate(todos_los_paises, start=1):
        print(f"{i}. {pais}")
    
    opcion_pais = input("Selecciona un país: ")
    
    if opcion_pais.isdigit() and 1 <= int(opcion_pais) <= len(todos_los_paises):
        if todos_los_paises[int(opcion_pais) - 1] in ["Antigua y Barbuda", "Argentina", "Bahamas", "Barbados", "Belice", "Bolivia", "Brasil", "Colombia", "Costa Rica", "Cuba", "Chile", "Dominica", "Ecuador", "El Salvador", "Granada", "Guatemala", "Guyana", "Haití", "Honduras", "Jamaica", "México", "Nicaragua", "Panamá", "Paraguay", "Perú", "República Dominicana", "San Cristóbal y Nieves", "San Vicente y las Granadinas", "Santa Lucía", "Surinam", "Trinidad y Tobago", "Uruguay", "Venezuela"]:
            fecha_ida = input("Ingresa tu fecha de ida (DD/MM/AAAA): ")
            opciones_precio_vuelo_ida(todos_los_paises[int(opcion_pais) - 1], fecha_ida)
        else:
            print(f"Has elegido: {todos_los_paises[int(opcion_pais) - 1]}. ¡Disfruta tu vuelo!")
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        mostrar_paises_america_norte()
        
def opciones_precio_vuelo_ida(pais, fecha_ida):
    print(f"Fecha de ida: {fecha_ida}")
    print(centrar_mensaje("Precios de vuelo de ida", ancho_total))

    if pais == "Antigua y Barbuda":
        print("1. Vuelo DO - ABA   $130")
        print("1. Vuelo DO - ABA   $145")
    elif pais == "Argentina":
        print("1. Vuelo DO - ARG   $130")
        print("2. Vuelo DO - ARG   $145")
    elif pais == "Bahamas":
        print("1. Vuelo DO - BAH   $130") 
        print("2. Vuelo DO - BAH   $145")
    elif pais == "Barbados":
        print("1. Vuelo DO - BRB   $130")
        print("2. Vuelo DO - BRB   $145")
    elif pais == "Belice":
        print("1. Vuelo DO - BE   $130")
        print("2. Vuelo DO - BE   $145")
    elif pais == "Bolivia":
        print("1. Vuelo DO - BOV   $130")
        print("2. Vuelo DO - BOV   $145")
    elif pais == "Brasil":
        print("1. Vuelo DO - BRA   $130")
        print("2. Vuelo DO - BRA   $145")
    elif pais == "Colombia":
        print("1. Vuelo DO - COL  $130")
        print("2. Vuelo DO - COL  $145")
    elif pais == "Costa Rica":
        print("1. Vuelo DO - CR  $130")
        print("2. Vuelo DO - CR  $145")
    elif pais == "Cuba":
        print("1. Vuelo DO - CU  $130")
        print("2. Vuelo DO - CU  $145")
    elif pais == "Chile":
        print("1. Vuelo DO - CHI   $130")
        print("2. Vuelo DO - CHI   $145")
    elif pais == "Dominica":
        print("1. Vuelo DO - DOA   $130")
        print("2. Vuelo DO - DOA   $145")
    elif pais == "Ecuador":
        print("1. Vuelo DO - ECU   $130")
        print("2. Vuelo DO - ECU   $145")
    elif pais == "El Salvador":
        print("1. Vuelo DO - SAL   $130")
        print("2. Vuelo DO - SAL   $145")
    elif pais == "Granada":
        print("1. Vuelo DO - GRA   $130")
        print("2. Vuelo DO - GRA   $145")
    elif pais == "Guatemala":
        print("1. Vuelo DO - GUA   $130")
        print("2. Vuelo DO - GUA   $145")
    elif pais == "Guyana":
        print("1. Vuelo DO - GY   $130")
        print("2. Vuelo DO - GY   $145")
    elif pais == "Haiti":
        print("1. Vuelo DO - HAI   $130")
        print("2. Vuelo DO - HAI   $145")
    elif pais == "Honduras":
        print("1. Vuelo DO - HOU   $130")
        print("2. Vuelo DO - HOU   $145")
    elif pais == "Jamaica":
        print("1. Vuelo DO - JAM   $130")
        print("2. Vuelo DO - JAM   $145")
    elif pais == "Mexico":
        print("1. Vuelo DO - MEX   $130")
        print("2. Vuelo DO - MEX   $145")
    elif pais == "Nicaragua":
        print("1. Vuelo DO - NIC   $130")
        print("2. Vuelo DO - NIC   $145")
    elif pais == "Panama":
        print("1. Vuelo DO - PAN   $130")
        print("2. Vuelo DO - PAN   $145")
    elif pais == "Paraguay":
        print("1. Vuelo DO - GUY   $130")
        print("2. Vuelo DO - GUY   $145")
    elif pais == "Peru":
        print("1. Vuelo DO - PER   $130")
        print("1. Vuelo DO - PER   $145")
    elif pais == "San Cristobal y Nieves":
        print("1. Vuelo DO - SCN   $130")
        print("2. Vuelo DO - SCN   $145")
    elif pais == "San Vicente y las Granadinas":
        print("1. Vuelo DO - SVG   $130")
        print("2. Vuelo DO - SVG   $145")
    elif pais == "Santa Lucia":
        print("1. Vuelo DO - SL   $130")
        print("2. Vuelo DO - SL   $145")
    elif pais == "Surinam":
        print("1. Vuelo DO - SUM   $130")
        print("2. Vuelo DO - SUM   $145")
    elif pais == "Trinidad y Tobago":
        print("1. Vuelo DO - TT    $130")
        print("2. Vuelo DO - TT    $145")
    elif pais == "Uruguay":
        print("1. Vuelo DO - URU   $130")
        print("2. Vuelo DO - URU   $145")
    elif pais == "Venezuela":
        print("1. Vuelo DO - VEN   $130")
        print("2. Vuelo DO - VEN   $145")                                     
    
    opcion_vuelo = input("Selecciona una opción de vuelo (1 o 2): ")
    
    if opcion_vuelo == "1" or opcion_vuelo == "2":
        fecha_regreso = input("¿Cuál será tu fecha de regreso (DD/MM/AAAA)? ")
        print(f"Fecha de regreso: {fecha_regreso}")
        opciones_precio_vuelo_regreso(pais)
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        opciones_precio_vuelo_ida(pais, fecha_ida)

def opciones_precio_vuelo_regreso(pais):
    print(centrar_mensaje("Precios de vuelo de regreso", ancho_total))

    if pais == "Antigua y Barbuda":
        print("1. Vuelo ABA - DO   $180")
        print("1. Vuelo ABA - DO   $190")
    elif pais == "Argentina":
        print("1. Vuelo ARG - DO   $180")
        print("2. Vuelo ARG - DO   $190")
    elif pais == "Bahamas":
        print("1. Vuelo BAH - DO   $180") 
        print("2. Vuelo BAH - DO   $190")
    elif pais == "Barbados":
        print("1. Vuelo BRB - DO   $180")
        print("2. Vuelo BRB - DO   $190")
    elif pais == "Belice":
        print("1. Vuelo BE - DO   $180")
        print("2. Vuelo BE - DO   $190")
    elif pais == "Bolivia":
        print("1. Vuelo BOV - DO   $180")
        print("2. Vuelo BOV - DO   $190")
    elif pais == "Brasil":
        print("1. Vuelo BRA - DO   $180")
        print("2. Vuelo BRA - DO   $190")
    elif pais == "Colombia":
        print("1. Vuelo COL - DO  $180")
        print("2. Vuelo COL - DO  $190")
    elif pais == "Costa Rica":
        print("1. Vuelo CR - DO  $180")
        print("2. Vuelo CR - DO  $190")
    elif pais == "Cuba":
        print("1. Vuelo CU - DO  $180")
        print("2. Vuelo CU - DO  $190")
    elif pais == "Chile":
        print("1. Vuelo CHI - DO   $180")
        print("2. Vuelo CHI - DO   $190")
    elif pais == "Dominica":
        print("1. Vuelo DOA - DO   $180")
        print("2. Vuelo DOA - DO   $190")
    elif pais == "Ecuador":
        print("1. Vuelo ECU - DO   $180")
        print("2. Vuelo ECU - DO   $190")
    elif pais == "El Salvador":
        print("1. Vuelo SAL - DO   $180")
        print("2. Vuelo SAL - DO   $190")
    elif pais == "Granada":
        print("1. Vuelo GRA - DO   $180")
        print("2. Vuelo GRA - DO   $190")
    elif pais == "Guatemala":
        print("1. Vuelo GUA - DO   $180")
        print("2. Vuelo GUA - DO   $190")
    elif pais == "Guyana":
        print("1. Vuelo GY - DO   $180")
        print("2. Vuelo GY - DO   $190")
    elif pais == "Haiti":
        print("1. Vuelo HAI - DO   $180")
        print("2. Vuelo HAI - DO   $190")
    elif pais == "Honduras":
        print("1. Vuelo HOU - DO   $180")
        print("2. Vuelo HOU - DO   $190")
    elif pais == "Jamaica":
        print("1. Vuelo JAM - DO   $180")
        print("2. Vuelo JAM - DO   $190")
    elif pais == "Mexico":
        print("1. Vuelo MEX - DO   $180")
        print("2. Vuelo MEX - DO   $190")
    elif pais == "Nicaragua":
        print("1. Vuelo NIC - DO   $180")
        print("2. Vuelo NIC - DO   $190")
    elif pais == "Panama":
        print("1. Vuelo PAN - DO   $180")
        print("2. Vuelo PAN - DO   $190")
    elif pais == "Paraguay":
        print("1. Vuelo GUY - DO   $180")
        print("2. Vuelo GUY - DO   $190")
    elif pais == "Peru":
        print("1. Vuelo PER - DO   $180")
        print("1. Vuelo PER - DO   $190")
    elif pais == "San Cristobal y Nieves":
        print("1. Vuelo SCN - DO   $180")
        print("2. Vuelo SCN - DO   $190")
    elif pais == "San Vicente y las Granadinas":
        print("1. Vuelo SVG - DO   $180")
        print("2. Vuelo SVG - DO   $190")
    elif pais == "Santa Lucia":
        print("1. Vuelo SL - DO   $180")
        print("2. Vuelo SL - DO   $190")
    elif pais == "Surinam":
        print("1. Vuelo SUM - DO   $180")
        print("2. Vuelo SUM - DO   $190")
    elif pais == "Trinidad y Tobago":
        print("1. Vuelo TT - DO    $180")
        print("2. Vuelo TT - DO    $190")
    elif pais == "Uruguay":
        print("1. Vuelo URU - DO   $180")
        print("2. Vuelo URU - DO   $190")
    elif pais == "Venezuela":
        print("1. Vuelo URU - DO   $180")
        print("2. Vuelo URU - DO   $190") 
        
    opcion_vuelo = input("Selecciona una opción de vuelo (1 o 2): ")
    
#Maletas
def mostrar_menu_maletas():
    print(centrar_mensaje("Maleta/s (incluyendo la maleta de mano):", ancho_total))
    print(centrar_mensaje("a) 1", ancho_total))
    print(centrar_mensaje("b) 2", ancho_total))
    print(centrar_mensaje("c) 3", ancho_total))
    print(centrar_mensaje("d) 4", ancho_total))
    print(centrar_mensaje("e) 5", ancho_total))

def calcular_maletas_precio(opcion):
    if opcion == 'a':
        return 60
    elif opcion == 'b':
        return 120
    elif opcion == 'c':
        return 189
    elif opcion == 'd':
        return 240
    elif opcion == 'e':
        return 300
    else:
        return 0  

def principal():
    opcion_elegida = input("Seleccione el número de maletas (a, b, c, d, e): ").lower()
    precio = calcular_maletas_precio(opcion_elegida)
    if precio > 0:
        print(f"Ha elegido {opcion_elegida}, El precio es: ${precio}")
        print("")
    else:
        print("Opción inválida. Por favor, elija una opción válida.")
        
   
#Asientos
def mostrar_menu_asientos():
    print("Elija su asiento:")
    print("Asientos A.. (Junto a la ventana), Asientos B.. (En el medio), Asientos C.. (Junto al pasillo)")
    print("")
    for fila in range(1, 11):
        for columna in ['A', 'B', 'C']:
            print(f"{columna}{fila}", end=" ")
        print()

def calcular_precio(asiento):
    if asiento[0] == 'A':
        return 15
    elif asiento[0] == 'B':
        return 13
    elif asiento[0] == 'C':
        return 14

def main():
    print("")
    asiento_elegido = input("Ingrese el asiento que desea reservar (Ejemplo: A1): ").upper()
    if len(asiento_elegido) == 2 and asiento_elegido[0] in ['A', 'B', 'C'] and asiento_elegido[1].isdigit():
        precio = calcular_precio(asiento_elegido)
        print(f"Ha elegido el asiento {asiento_elegido}. El precio es: ${precio}")
        print("")
    else:
        print("Entrada inválida. Por favor, ingrese un asiento válido.")
    
        
#Datos Personales
def ingresar_datos_personales():
    print("\nIngrese sus datos personales:")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    edad = input("Edad: ")
    sexo = input("Sexo: ")
    #(5 Numeros y 4 Letras en Mayuscula - Pasaporte)
    pasaporte = input("Pasaporte:")
    email = input("Email: ")
    print("")
    extra = input("¿Lleva acompañante? ")
    
    if extra() == "si" or "Si":
        ingresar_datos_personales()
    else: extra() == "no" or "No"

mostrar_menu_reservar_vuelo()
mostrar_menu_maletas()
principal()
mostrar_menu_asientos()
main()
ingresar_datos_personales()

