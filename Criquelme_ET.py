productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

def mostrar_marca(marca):
    marca = marca.lower()
    encontrados =False
    print(f"El stock disponible {marca.capitalize()}")
    for modelos, datos in productos.items():
        if datos[0].lower() == marca:
            encontrados=True
            unidades=stock.get (modelos, [0, 0][1])
            print(f"Modelo: {modelos} Stock: {unidades}")
    if not encontrados:
          print("Lo sentimos no esta disponible")

def buscar_precio(p_min,p_max):
    encontrados=[]
    for modelos, (precios, cantidad) in stock.items():
        if cantidad > 0 and p_min <= precios <= p_max:
            if modelos in productos:
                marca = productos[modelos][0]
                encontrados.append(f"{marca}--{modelos}")
    if encontrados:
        encontrados.sort
        print("El stock disponible dentro del rango es")
        for item in encontrados:
            print(item)

#Se que o bueno, creo recordar que el comando para actualizar es este, no supe como hacerlo pense que no era tan 
#fundamental, espero me de para un 4 tenga piedad
def actualizar_precio(modelo, p):
    mostrar_producto()
    cmodelo=input("Que modelo desea actualizar: ")
    if cmodelo in productos:
        dict[cmodelo]["modelo"]=n
        p_cambiar=input("Ingrese nuevo precio: ")
        dict[p_cambiar]["p"]=n
        print("Su precio se ha actualizado!!")
    else:
        print("El modelo no existe!!")
        return False
        

def mostrar_producto():
    if not productos:
        print("Lo sentimos no tenemos Notebook")
        return
    for datos in productos.items:
        marca, _, ram, tip_dis, tam_dis, *_= datos 
        print(f"{marca}--{ram}--{tip_dis}--{tam_dis}")


def mostrar2_productos(dict):
    for i, z in dict.items:
        print(i, z)






while True:
    try:
        print('''
**MENU PRINCIPAL**
1.- Stock de marca
2.- Busqueda precio
3.- Actualizar precio
4.- Salir
''')
        op=int(input("¿Que desea hacer?: "))
        match op:
            case 1:
                marca=input("Que marca desea buscar: ")
                mostrar_marca(marca)
            case 2:
                while True:
                    try:
                        p_min=int(input("Ingrese un precio minimo: "))
                        p_max=int(input("Ingrese un precio maximo: "))
                        if p_min > p_max:
                            p_min, p_max = p_max, p_min
                    except ValueError:
                        print("Usar solo numero enteros positivos!!")
                    buscar_precio(p_min, p_max)
                    break
            case 3:
                actualizar_precio()
            case 4:
                print("Saliendo...")
                break
            case _:
                print("Ingrese una opcion valida!!")
    except Exception as error:
        print("Solo numeros enteros positivos")