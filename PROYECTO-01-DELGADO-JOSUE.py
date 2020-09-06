
from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches


logins=[["Admi","blabla1"],["Seb","Falcorito"],["Litul","maguno"],["Emtech","Python"]]


acceder=0 #Si es cero el usuario no puede acceder
registro= input("¿Tiene un registro? (si/no): ")

if registro=="si":
  print("")
  usuario=input("Ingrese nombre de usuario: ")
  for i in logins:
    if usuario == i[0]:
      print("")
      print("Usuario registrado")
      print("")
      contrase=input("Ingrese su contraseña: ")
      if contrase==i[1]:
        print("")
        print("Bienvenido a Life-Store")
        acceder=1
        break
      else:
        print("")
        print("Contraseña incorrecta")   
elif registro=="no":
  print("")
  nombre=input("Ingrese su nuevo nombre de usario: ")
  contrase1=input("Ingrese contraseña: ")
  contrase2=input("Confirme su contraseña: ")
  if contrase1==contrase2:
    print("")
    print("Se ha registrado correctamente")
    print("")
    print("Inicie sesión")
    logins.append([nombre,contrase1])
    print("")
    usuario=input("Ingrese nombre de usuario: ")
    for i in logins:
      if usuario == i[0]:
        print("Usuario registrado")
        contrase=input("Ingrese su contraseña: ")
        if contrase==i[1]:
          print("")
          print("Bienvenido a LifeStore")
          acceder=1
          break
        else:
          print("")
          print("Contraseña incorrecta") 
  else:
    print("Las contraseñas no coinciden")
    print("")
    print("El registro no fue completado")
else:
  print("Opción no valida")


if acceder ==0:
  print("")
  print("El usuario no está registrado para visualizar la información")
  opcion=10
elif acceder==1:
  print("")
  print("Información disponible: ")
  print("")
  print("1 : Lista de los productos mas vendidos")
  print("2 : Lista de los productos mas buscados")
  print("3 : Lista de los productos menos vendidos por categoría")
  print("4 : Lista de los productos menos buscados por categoría")
  print("5 : Mejores reseñas")
  print("6 : Peores reseñas")
  print("7 : Ingresos total de ventas")
  print("8 : Meses con mayores ventas")
  print("")
  opcion=int(input("Introduzca el número deseado según la información que desea conocer:"))
  


"Codigo para ver productos mas vendidos"

if opcion==1:

  #En esta lista almacenamos el ID del producto vendido"
  ventas=[] 
  for producto in lifestore_sales:
    ventas.append(producto[1])

  ventas.append(0)


  "Este ciclo nos auyda a ver cuantos veces se vendio un producto y así crear una lista de parejas donde nos de el ID del producto y la cantidad de unidades vendidas de ese producto"
  totalventas=[]
  k=0
  for i in range(1,97): 
    contador=0
    while ventas[k]== i:
      contador+=1
      k+=1
    totalventas.append([i,contador])
    

  "Luego eliminamos de nuestra lista aquellos prodcutos de los que no se vendió ningún artículo"
  cantidadventas=[]
  for i in totalventas:
    if i[1]!=0:
      cantidadventas.append(i)

  "Con este ciclo ordenaremos de mayor a menor las ventas por producto"
  ordenventas=[]
  for i in cantidadventas:
    "tomamos un elemento de la lista como pivote para ir comparando, si un elemento es mayor entonces este será nuestro nuevo pivote"
    pivote=i 
    for j in cantidadventas:
      "Ese pivote se irá comparando con cada elemento de la lista"
      comparacion=j 
      "Si es mayor continua siendo el pivote"
      if pivote[1]>j[1]: 
        continue
      else:
        "Si es menor, entonces el mayor es el nuevo pivote y se compara con los elementos restantes de la lista"
        pivote=j 
    ordenventas.append(pivote) 
    "Una vez que se tiene el mayor se agrega como primer elemento a la lista"
    "Pero si lo dejamos en la lista siempre será el mayor"
    for k in range(0,42): #Son 42 elementos en la lista
      "Entonces buscamos el pivote en la lista"
      if pivote==cantidadventas[k]:
          cantidadventas[k]=[pivote[0],0] 
    "Y cambiamos el numero de unidades vendidas a cero,de esta manera eliminamos al mayor y ahora podremos encontrar al segundo lugar, tercero y así sucesivamente"

  "Finalmente hacemos coincidir el primer elemento de cada lista con la lista de productos para mostrar los nombres de los productos"
  productos_masvendidos=[]
  a=0
  print("")
  print("PRODUCTOS MAS VENDIDOS")
  for i in ordenventas:
    for k in lifestore_products:
      if i[0]==k[0]:
        a+=1
        print("")
        print(a,".- ",k[1])
        print("Categoría: ",k[3])
        productos_masvendidos.append(k[1])

  "Termina codigo para ver productos mas vendidos"




elif opcion==2:
  "Código productos mas buscados"

  "Aplicaremos la misma lógica haciendo las modificaciones necesarias"

  "En esta lista almacenamos el ID del producto buscado"
  busqueda=[] 
  for producto in lifestore_searches:
    busqueda.append(producto[1])

  busqueda.append(0)

  "Este ciclo nos auyda a ver cuantos veces se buscó un producto y así crear una lista de parejas donde nos de el ID del prodcuto y la cantidad de veces que se buscó ese producto"
  totalbusquedas=[]
  k=0
  for i in range(1,97): 
    contador=0
    while busqueda[k]== i:
      contador+=1
      k+=1
    totalbusquedas.append([i,contador])

  "Luego eliminamos de nuestra lista aquellos prodcutos de los que no se buscó ningún artículo"
  cantidadbusquedas=[]
  for i in totalbusquedas:
    if i[1]!=0:
      cantidadbusquedas.append(i)

  "Con este ciclo ordenaremos de mayor a menor las ventas por producto"
  ordenbusquedas=[]
  for i in cantidadbusquedas:
    "tomamos un elemento de la lista como pivote para ir comparando, si un elemento es mayor entonces este será nuestro nuevo pivote"
    pivote=i 
    for j in cantidadbusquedas:
      "Ese pivote se irá comparando con cada elemento de la lista"
      comparacion=j 
      "Si es mayor continua siendo el pivote"
      if pivote[1]>j[1]: 
        continue
      else:
        "Si es menor, entonces el mayor es el nuevo pivote y se compara con los elementos restantes de la lista"
        pivote=j 
    ordenbusquedas.append(pivote) 
    "Una vez que se tiene el mayor se agrega como primer elemento a la lista"
    "Pero si lo dejamos en la lista siempre será el mayor"
    for k in range(0,56): #Hasta 56 porque son los elementos en la lista
      "Entonces buscamos el pivote en la lista"
      if pivote==cantidadbusquedas[k]:
          cantidadbusquedas[k]=[pivote[0],0] 
    "Y cambiamos el numero de unidades vendidas a cero,de esta manera eliminamos al mayor y ahora podremos encontrar al segundo lugar, tercero y así sucesivamente"

  "Finalmente hacemos coindices el primer elemento de cada lista con la lista de productos para mostrar los nombres de los productos"
  productos_masbuscados=[]
  a=0
  print("")
  print("")
  print("PRODUCTOS MAS BUSCADOS")
  for i in ordenbusquedas:
    for k in lifestore_products:
      if i[0]==k[0]:
        a+=1
        print("")
        print(a,".- ",k[1])
        print("Categoría: ",k[3])
        productos_masbuscados.append(k[1])

  "Termina codigo para ver productos mas buscados"



elif opcion==3:
  "Código para ver productos con menores ventas"

  "En esta lista almacenamos el ID del producto vendido"
  ventas=[] 
  for producto in lifestore_sales:
    ventas.append(producto[1])

  ventas.append(0)


  "Este ciclo nos auyda a ver cuantos veces se vendio un producto y así crear una lista de parejas donde nos de el ID del prodcuto y la cantidad deunidades vendidas de ese producto"
  totalventas=[]
  k=0
  for i in range(1,97): 
    contador=0
    while ventas[k]== i:
      contador+=1
      k+=1
    totalventas.append([i,contador])
    

  "Luego eliminamos de nuestra lista aquellos productos de los que se vendió algún artículo"
  sinventas=[]

  for i in totalventas:
    if i[1]==0:
      sinventas.append(i)
    

  #Ahora queremos conocer las categrorias
  categorias=[]

  for i in lifestore_products:
    if i[3] not in categorias:
      categorias.append(i[3])


  #Luego mostramos los productos menos vendidos por categoría
  for cat in categorias:
    menos_vendidos_categoria=[]
    print("")
    print("")
    print("LOS MENOS VENDIDOS DE LA CATEGORÍA ",cat," SON:")
    print("")
    print("")
    a=0
    for i in sinventas:
      for k in lifestore_products:
        if i[0]==k[0] and cat==k[3]:
          menos_vendidos_categoria.append(k[1])
          a+=1
          print(a,".- ",k[1])
        
  
#Termina código de menos ventas"



#Empieza código de menos busquedas"

elif opcion==4:
  "Trabajemos este código de manera similar al de menos ventas"


  "En esta lista almacenamos el ID del producto buscado"
  busqueda=[] 
  for producto in lifestore_searches:
    busqueda.append(producto[1])

  busqueda.append(0)

  "Este ciclo nos auyda a ver cuantos veces se buscó un producto y así crear una lista de parejas donde nos de el ID del prodcuto y la cantidad de veces que se buscó ese producto"
  totalbusquedas=[]
  k=0
  for i in range(1,96): 
    contador=0
    while busqueda[k]== i:
      contador+=1
      k+=1
    totalbusquedas.append([i,contador])

  "Luego eliminamos de nuestra lista aquellos prodcutos de los que se buscó el artículo"  
  sinbusquedas=[]
  for i in totalbusquedas:
    if i[1]==0:
      sinbusquedas.append(i)

  #Ahora queremos conocer las categrorias
  categorias=[]

  for i in lifestore_products:
    if i[3] not in categorias:
      categorias.append(i[3])


  #Luego mostramos los productos menos vendidos por categoría
  for cat in categorias:
    menos_buscados_categoria=[]
    print("")
    print("")
    print("LOS MENOS BUSCADOS DE LA CATEGORÍA ",cat," SON:")
    print("")
    print("")
    a=0
    for i in sinbusquedas:
      for k in lifestore_products:
        if i[0]==k[0] and cat==k[3]:
          menos_buscados_categoria.append(k[1])
          a+=1
          print(a,".- ",k[1])

#Finaliza código de menos búsquedas por categoría"





#Empieza código de mejores reseñas"
elif opcion==5:
  #Primero crearemos una lista que incluya el ID de los productos menos_vendidos
  productos_vendidos=[]
  for i in lifestore_sales:
    if i[1] not in productos_vendidos:
      productos_vendidos.append(i[1])


  "Ahora,para cada producto vendido sacaremos el promedio de sus reseñas y el número de devoluciones de cada una,de este modo tendremos una lista que despues podremos ocupar para obtener las mejores y las peores reseñas"
  resenas_prod=[]
  for i in productos_vendidos:
    suma=0
    contador=0
    devolucion=0
    for k in lifestore_sales:
      if i==k[1]:
        suma+=k[2]
        contador+=1
        if k[4]==1:
          devolucion+=1
    promedio=suma/contador
    resenas_prod.append([i,promedio,devolucion])

  "Ahora procedemos a ordenar de mayor a menor"

  "Con este ciclo ordenaremos de mayor a menor las ventas por producto"
  orden_resena=[]
  for i in resenas_prod:
    "tomamos un elemento de la lista como pivote para ir comparando, si un elemento es mayor entonces este será nuestro nuevo pivote"
    pivote=i 
    for j in resenas_prod:
      "Ese pivote se irá comparando con cada elemento de la lista"
      comparacion=j 
      "Si es mayor continua siendo el pivote"
      if pivote[1]>j[1]: 
        continue
      else:
        "Si es menor, entonces el mayor es el nuevo pivote y se compara con los elementos restantes de la lista"
        pivote=j 
    orden_resena.append(pivote) 
    "Una vez que se tiene el mayor se agrega como primer elemento a la lista"
    "Pero si lo dejamos en la lista siempre será el mayor"
    for k in range(0,42): #Son 42 elementos en la lista
      "Entonces buscamos el pivote en la lista"
      if pivote==resenas_prod[k]:
          resenas_prod[k]=[pivote[0],0,0] 
    "Y cambiamos el promedio de la mejor reseña a cero,de esta manera eliminamos al mayor y ahora podremos encontrar al segundo lugar, tercero y así sucesivamente"

  "Finalmente hacemos coindices el primer elemento de cada lista con la lista de productos para mostrar los nombres de los productos"
  a=1
  print("")
  print("")
  print("MEJORES RESEÑAS")
  for i in orden_resena:
    if a==21:
      break
    for k in lifestore_products:
      if i[0]==k[0]:
        print("")
        print(a,".- ",k[1])
        print("Calificación promedio: ",i[1])
        print("Devoluciones de este producto: ",i[2])
        print("Categoría: ",k[3])
        a+=1
    

#Termina codigo para ver mejores reseñas"








#Empieza código de peores reseñas"
elif opcion==6:
  #Primero crearemos una lista que incluya el ID de los productos 
  productos_vendidos=[]
  for i in lifestore_sales:
    if i[1] not in productos_vendidos:
      productos_vendidos.append(i[1])


  "Ahora,para cada producto vendido sacaremos el promedio de sus reseñas y el número de devoluciones de cada una,de este modo tendremos una lista que despues podremos ocupar para obtener las mejores y las peores reseñas"
  resenas_prod=[]
  for i in productos_vendidos:
    suma=0
    contador=0
    devolucion=0
    for k in lifestore_sales:
      if i==k[1]:
        suma+=k[2]
        contador+=1
        if k[4]==1:
          devolucion+=1
    promedio=suma/contador
    resenas_prod.append([i,promedio,devolucion])


  "Ahora procedemos a ordenar de menor a mayor"

  "Con este ciclo ordenaremos de menor a mayor las ventas por producto"
  orden_resena=[]
  for i in resenas_prod:
    "tomamos un elemento de la lista como pivote para ir comparando, si un elemento es mayor entonces este será nuestro nuevo pivote"
    pivote=i 
    for j in resenas_prod:
      "Ese pivote se irá comparando con cada elemento de la lista"
      comparacion=j 
      "Si es mayor continua siendo el pivote"
      if pivote[1]<j[1]: 
        continue
      else:
        "Si es menor, entonces el mayor es el nuevo pivote y se compara con los elementos restantes de la lista"
        pivote=j 
    orden_resena.append(pivote) 
    "Una vez que se tiene el mayor se agrega como primer elemento a la lista"
    "Pero si lo dejamos en la lista siempre será el mayor"
    for k in range(0,42): #Son 42 elementos en la lista
      "Entonces buscamos el pivote en la lista"
      if pivote==resenas_prod[k]:
          resenas_prod[k]=[pivote[0],10,0] 
    "Y cambiamos el promedio de la mejor reseña a cero,de esta manera eliminamos al mayor y ahora podremos encontrar al segundo lugar, tercero y así sucesivamente"

  "Finalmente hacemos coindices el primer elemento de cada lista con la lista de productos para mostrar los nombres de los productos"
  a=1
  print("")
  print("")
  print("PEORES RESEÑAS")
  for i in orden_resena:
    if a==21:
      break
    for k in lifestore_products:
      if i[0]==k[0]:
        print("")
        print(a,".- ",k[1])
        print("Calificación promedio: ",i[1])
        print("Devoluciones de este producto: ",i[2])
        print("Categoría: ",k[3])
        a+=1


#Finaliza código peores reseñas"





#Empieza código de total de ingresos,ventas promedio,etc."
elif opcion==7:

  "Iniciaremos con la suma total de ingresos que se ha obtenido"
  ingresos=0
  productos_vendidos=[]
  for i in lifestore_sales:
    productos_vendidos.append(i[1])

  for i in productos_vendidos:
    for k in lifestore_products:
      if i==k[0]:
        ingresos+=k[2]
  print("")
  print("Los ingresos hasta este momento son: $",ingresos,".00")
  ingreso_mensual=ingresos/8.166666 #Se tomo esta determinación porque se tiene aproximadamente 1/6 del mes de semtiembre en cuenta para este analisis
  ingreso_anual=ingreso_mensual*12
  print("")
  print("El ingreso promedio mensual es: $", ingreso_mensual)
  print("Este ingreso promedio toma en cuenta que solo se lleva un sexto del mes de septiemebre")
  print("")
  print("El ingreso anual promedio es: $",ingreso_anual)
  print("")
  print("Estos calculos toman en cuenta que solo ha pasado una tercera parte del mes de septiembre")

#Finaliza código promedios mensuales tomando en cuenta septiembre


elif opcion==8:
  #Vamos a contar el número de ventas por mes
  ventas_mensuales=[]
  for i in lifestore_sales:
    fecha=i[3]
    ventas_mensuales.append([i[1],fecha[3:5]])

  cantidad_e_ingresos_men=[]
  meses=["Diciembre","Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre"]
  suma=0
  numventa=0
  for i in range(1,10):
    contador=0
    ingresos=0
    for k in ventas_mensuales:
      mes=int(k[1])
      if mes==i:
        contador+=1
        for j in lifestore_products:
          if k[0]==j[0]:
            ingresos+=j[2]
    cantidad_e_ingresos_men.append([meses[i],contador,ingresos])
    suma+=ingresos
    numventa+=contador

  prom_mensual=(suma-ingresos)/8
  prom_anual=prom_mensual*12



  "Con este ciclo ordenaremos de mayor a menor los ingresos por mes"
  orden_ventas=[]
  for i in cantidad_e_ingresos_men:
    "tomamos un elemento de la lista como pivote para ir comparando, si un elemento es mayor entonces este será nuestro nuevo pivote"
    pivote=i 
    for j in cantidad_e_ingresos_men:
      "Ese pivote se irá comparando con cada elemento de la lista"
      comparacion=j 
      "Si es mayor continua siendo el pivote"
      if pivote[2]>j[2]: 
        continue
      else:
        "Si es menor, entonces el mayor es el nuevo pivote y se compara con los elementos restantes de la lista"
        pivote=j 
    orden_ventas.append(pivote) 
    "Una vez que se tiene el mayor se agrega como primer elemento a la lista"
    "Pero si lo dejamos en la lista siempre será el mayor"
    for k in range(0,9): #Son 9 elementos en la lista
      "Entonces buscamos el pivote en la lista"
      if pivote==cantidad_e_ingresos_men[k]:
          cantidad_e_ingresos_men[k]=[pivote[0],0,0] 
    "Y cambiamos el promedio de la mejor reseña a cero,de esta manera eliminamos al mayor y ahora podremos encontrar al segundo lugar, tercero y así sucesivamente"


  print("")

  print("Promedios mensual y anual")
  print("")
  print("El promedio mensual sin contar septiembre es: $",prom_mensual)
  print("")
  print("El promedio anual sin contar septiembre es: $",prom_anual)
  print("")
  print("Meses con mayores ventas")

  a=1
  for i in orden_ventas:
    mes=i[0]
    print("")
    print(a,".-",mes)
    print("Ingresos del mes por los articulos vendidos: $",i[2])
    print("Cantidad de articulos vendidos:",i[1])
    
    a+=1

#Finaliza código ventas mensuales

elif opcion==10:
  print("")

else:
  print("")
  print("Opción no válida")