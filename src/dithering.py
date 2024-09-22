import time
import random
import argparse
from PIL import Image
from utils.colores import colores, random_color, reset, rojo
from utils.progress_bar import progress_bar

# Rutas de las imagenes de los puntos
PUNTOS_PATHS = [
        './semitonos/puntos/punto_1.jpg',
        './semitonos/puntos/punto_2.jpg',
        './semitonos/puntos/punto_3.jpg',
        './semitonos/puntos/punto_4.jpg',
        './semitonos/puntos/punto_5.jpg',
        './semitonos/puntos/punto_6.jpg',
        './semitonos/puntos/punto_7.jpg',
        './semitonos/puntos/punto_8.jpg',
        './semitonos/puntos/punto_9.jpg'
]

# Cargamos las imagenes de los puntos
PUNTOS = [Image.open(path) for path in PUNTOS_PATHS]

# Rutas de las imagenes de las matrices
MATRICES_PATHS = [
        './semitonos/matrices/matriz_1.jpg',
        './semitonos/matrices/matriz_2.jpg',
        './semitonos/matrices/matriz_3.jpg',
        './semitonos/matrices/matriz_4.jpg',
        './semitonos/matrices/matriz_5.jpg',
        './semitonos/matrices/matriz_6.jpg',
        './semitonos/matrices/matriz_7.jpg',
        './semitonos/matrices/matriz_8.jpg',
        './semitonos/matrices/matriz_9.jpg',
]

# Cargamos las imagenes de las matrices
MATRICES = [Image.open(path) for path in MATRICES_PATHS]

def dithering_azar(imagen: Image):
    """
        Aplica dithering al azar a una imagen.

        Parameters :
        ------------

            imagen:
                imagen a aplicar el dithering
            
        Returns :
        ---------

            imagen con el dithering aplicado
        
    """
    # Convertimos la imagen a tonos de gris
    imagen_grayscale = imagen.convert('L')

    # Imagen a regresar
    nueva_imagen = Image.new('L', imagen.size)

    # Variables para mostrar el progreso al usuario
    total_pixeles = imagen.width * imagen.height
    pixeles_procesados = 0
    porcentaje_progreso = 0
    color = random_color()

    # Progreso inicial
    print(random_color()+"Generando imagen (Dithering azar)..."+reset)
    progress_bar(pixeles_procesados, total_pixeles, color)
    
    # Iteramos por cada pixel de la imagen
    for x in range(imagen.width):
        for y in range(imagen.height):
            pixel = imagen_grayscale.getpixel((x,y))
            # Generamos un valor random (0-255)
            valor_random = random.randint(0,255)
            if pixel <= valor_random:
                nueva_imagen.putpixel((x,y),0)
            else:
                nueva_imagen.putpixel((x,y),255)

            # Actualizamos la barra de progreso
            pixeles_procesados += 1
            nuevo_porcentaje_progreso = (pixeles_procesados * 100) // total_pixeles
            # Mostramos el progreso cada 10%
            if nuevo_porcentaje_progreso >= porcentaje_progreso + 10:
                porcentaje_progreso = nuevo_porcentaje_progreso
                progress_bar(pixeles_procesados, total_pixeles, color)
                color = random_color()

    print(random_color()+"Dithering azar finalizado ʕ•ᴥ•ʔ"+reset)

    return nueva_imagen

def dithering_ordenado(imagen: Image):
    """
        Aplica dithering ordenado a una imagen.

        Parameters :
        ------------

            imagen:
                imagen a procesar

        Returns :
        ---------

            imagen con el dithering aplicado
    """

    MATRIZ_ORDENADA = [
        [8,3,4],
        [6,1,2],
        [7,5,9]
    ]

    # Convertimos la imagen a tonos de gris
    imagen_grayscale = imagen.convert('L')

    # Imagen a regresar
    nueva_imagen = Image.new('L', imagen.size)

    # Variables para mostrar el progreso al usuario
    total_bloques_x = imagen.width // 3
    total_bloques_y = imagen.height // 3
    total_bloques = total_bloques_x * total_bloques_y
    bloques_procesados = 0
    porcentaje_progreso = 0
    color = random_color()
    
    # Progreso inicial
    print(random_color()+"Generando imagen (Dithering ordenado)..."+reset)
    progress_bar(bloques_procesados, total_bloques, color)

    # Recorremos en bloques de 3x3
    for x in range(0,imagen.width,3):
        for y in range(0,imagen.height,3):
            bloque = imagen_grayscale.crop((x,y,x+3,y+3))
            nuevo_bloque = aplica_matriz(MATRIZ_ORDENADA, bloque)
            nueva_imagen.paste(nuevo_bloque,(x,y))

            #Actualizamos la barra de progreso
            bloques_procesados += 1
            nuevo_porcentaje_progreso = (bloques_procesados * 100) // total_bloques
            # Mostramos el progreso cada 10%
            if nuevo_porcentaje_progreso >= porcentaje_progreso + 10:
                porcentaje_progreso = nuevo_porcentaje_progreso
                progress_bar(bloques_procesados, total_bloques, color)
                color = random_color()

    print(random_color()+"Dithering ordenado finalizado ʕ•ᴥ•ʔ"+reset)
    
    return nueva_imagen

def dithering_disperso(imagen: Image):
    """
        Aplica dithering disperso a una imagen.

        Parameters :
        ------------

            imagen:
                imagen a procesar

        Returns :
        ---------

            imagen con el dithering aplicado
    """

    MATRIZ_DISPERSA= [
        [1,7,4],
        [5,8,3],
        [6,2,9]
    ]

    # Convertimos la imagen a tonos de gris
    imagen_grayscale = imagen.convert('L')

    # Imagen a regresar
    nueva_imagen = Image.new('L', imagen.size)

    # Barra de progreso
    total_bloques_x = imagen.width // 3
    total_bloques_y = imagen.height // 3
    total_bloques = total_bloques_x * total_bloques_y
    bloques_procesados = 0
    porcentaje_progreso = 0
    color = random_color()
    
    # Progreso inicial
    print(random_color()+"Generando imagen (Dithering disperso)..."+reset)
    progress_bar(bloques_procesados, total_bloques, color)

    # Recorremos en bloques de 3x3
    for x in range(0,imagen.width,3):
        for y in range(0,imagen.height,3):
            bloque = imagen_grayscale.crop((x,y,x+3,y+3))
            nuevo_bloque = aplica_matriz(MATRIZ_DISPERSA, bloque)
            nueva_imagen.paste(nuevo_bloque,(x,y))

            #Actualizamos la barra de progreso
            bloques_procesados += 1
            nuevo_porcentaje_progreso = (bloques_procesados * 100) // total_bloques
            # Mostramos el progreso cada 10%
            if nuevo_porcentaje_progreso >= porcentaje_progreso + 10:
                porcentaje_progreso = nuevo_porcentaje_progreso
                progress_bar(bloques_procesados, total_bloques, color)
                color = random_color()

    print(random_color()+"Dithering disperso finalizado ʕ•ᴥ•ʔ"+reset)
    
    return nueva_imagen

def semitonos_puntos(imagen: Image):
    """
        Aplica semitonos con puntos a una imagen.

        Parameters :
        ------------

            imagen:
                imagen a aplicar semitonos

        Returns :
        ---------

            imagen con semitonos aplicado
    """

    # 255 / 9 ≈ 28
    step = 28

    # Tamaño de una de las imagenes de los puntos
    punto_ancho, punto_alto = PUNTOS[0].size

    # Imagen a tonos de gris
    imagen_grayscale = imagen.convert('L')

    # Imagen a regresar
    nueva_imagen = Image.new('L', imagen.size)

    # Barra de progreso
    total_bloques_x = imagen.width // 10
    total_bloques_y = imagen.height // 10
    total_bloques = total_bloques_x * total_bloques_y
    bloques_procesados = 0
    porcentaje_progreso = 0
    color = random_color()

    # Progreso inicial
    print(random_color()+'Generando imagen (Dithering semitonos con puntos)...'+reset)
    progress_bar(bloques_procesados, total_bloques, color)

    # Recorremos la imagen original
    for x in range(0, imagen.width, punto_ancho):
        for y in range(0, imagen.height, punto_alto):
            # Obtenemos un pedazo de la imagen
            bloque = imagen_grayscale.crop((x, y, x + punto_ancho, y + punto_alto))
            # Obtenemos el promedio gris
            promedio = promedio_gris(bloque)
            # Agregamos la imagen adecuada dependiendo del promedio a gris
            indice = min(promedio // step, len(PUNTOS) - 1)
            nueva_imagen.paste(PUNTOS[indice], (x,y))

            #Actualizamos la barra de progreso
            bloques_procesados += 1
            nuevo_porcentaje_progreso = (bloques_procesados * 100) // total_bloques
            # Mostramos el progreso cada 10%
            if nuevo_porcentaje_progreso >= porcentaje_progreso + 10:
                porcentaje_progreso = nuevo_porcentaje_progreso
                progress_bar(bloques_procesados, total_bloques, color)
                color = random_color()

    print(random_color()+"Dithering semitonos con puntos finalizado ʕ•ᴥ•ʔ"+reset)

    return nueva_imagen

def semitonos_matrices(imagen: Image):
    """
        Aplica semitonos con matrices a una imagen.

        Parameters :
        ------------

            imagen:
                imagen a aplicar semitonos

        Returns :
        ---------

            imagen con semitonos aplicado
    """

    # 255 / 9 ≈ 28
    step = 28

    # Tamaño de una de las imagenes de las matrices
    matriz_ancho, matriz_alto = MATRICES[0].size

    # Imagen a tonos de gris
    imagen_grayscale = imagen.convert('L')

    # Imagen a regresar
    nueva_imagen = Image.new('L', imagen.size)

    # Barra de progreso
    total_bloques_x = imagen.width // 10
    total_bloques_y = imagen.height // 10
    total_bloques = total_bloques_x * total_bloques_y
    bloques_procesados = 0
    porcentaje_progreso = 0
    color = random_color()

    # Progreso inicial
    print(random_color()+'Generando imagen (Dithering semitonos con matrices)...'+reset)
    progress_bar(bloques_procesados, total_bloques, color)

    # Recorremos la imagen original
    for x in range(0, imagen.width, matriz_ancho):
        for y in range(0, imagen.height, matriz_alto):
            # Obtenemos un pedazo de la imagen
            bloque = imagen_grayscale.crop((x, y, x + matriz_ancho, y + matriz_alto))
            # Obtenemos el promedio gris
            promedio = promedio_gris(bloque)
            # Agregamos la imagen adecuada dependiendo del promedio a gris
            indice = min(promedio // step, len(MATRICES) - 1)
            nueva_imagen.paste(MATRICES[indice], (x,y))

            #Actualizamos la barra de progreso
            bloques_procesados += 1
            nuevo_porcentaje_progreso = (bloques_procesados * 100) // total_bloques
            # Mostramos el progreso cada 10%
            if nuevo_porcentaje_progreso >= porcentaje_progreso + 10:
                porcentaje_progreso = nuevo_porcentaje_progreso
                progress_bar(bloques_procesados, total_bloques, color)
                color = random_color()

    print(random_color()+"Dithering semitonos con matrices finalizado ʕ•ᴥ•ʔ"+reset)

    return nueva_imagen

def floyd_steinberg(imagen : Image):
    """
        Aplica el alogoritmo de dithering de Floyd Steinberg a una imagen.

        Parameters :
        ------------

            imagen:
                imagen a aplicar el dithering

        Returns :
        ---------

            imagen con el dithering aplicado.            
    """

    # Convertimos la imagen a tonos de gris
    imagen_grayscale = imagen.convert('L')

    # Imagen a regresar
    nueva_imagen = Image.new('L', imagen.size)

    # Variables para mostrar el progreso al usuario
    total_bloques_x = imagen.width // 3
    total_bloques_y = imagen.height // 2
    total_bloques = total_bloques_x * total_bloques_y
    bloques_procesados = 0
    porcentaje_progreso = 0
    color = random_color()

    # Progreso inicial
    print(random_color()+"Generando imagen (Dithering ordenado)..."+reset)
    progress_bar(bloques_procesados, total_bloques, color)

    for x in range(0,imagen.width,3):
        for y in range(0,imagen.height,2):
            bloque = imagen_grayscale.crop((x,y,x+3,y+2))
            nuevo_bloque = aplica_matriz_floyd_steinberg(bloque)    
            nueva_imagen.paste(nuevo_bloque, (x,y))

             #Actualizamos la barra de progreso
            bloques_procesados += 1
            nuevo_porcentaje_progreso = (bloques_procesados * 100) // total_bloques
            # Mostramos el progreso cada 10%
            if nuevo_porcentaje_progreso >= porcentaje_progreso + 10:
                porcentaje_progreso = nuevo_porcentaje_progreso
                progress_bar(bloques_procesados, total_bloques, color)
                color = random_color()

    print(random_color()+"Dithering Floyd Steinberg finalizado ʕ•ᴥ•ʔ"+reset)
                
    return nueva_imagen

def aplica_matriz_floyd_steinberg(bloque: Image):
    """
        Aplica la matriz de Floyd Steinberg a un bloque.
    """
    # Matriz de Floyd Steinberg:
    #
    #   |   X   7|
    #   |3  5   1|

    # Lambda para determinar el valor mas proximo
    clamp = lambda x: 0 if x < 127 else 255

    # Bloque a regresar
    nuevo_bloque = Image.new('L', bloque.size)

    pixel = bloque.getpixel((1,0))
    nuevo_pixel = clamp(pixel)
    nuevo_bloque.putpixel((0,0), 255)
    nuevo_bloque.putpixel((1,0),nuevo_pixel)

    error = pixel - nuevo_pixel

    nuevo_bloque.putpixel((2,0),int(bloque.getpixel((2,0))+error*7/16))
    nuevo_bloque.putpixel((2,1),int(bloque.getpixel((2,1))+error*1/16))
    nuevo_bloque.putpixel((1,1),int(bloque.getpixel((1,1))+error*5/16))
    nuevo_bloque.putpixel((0,1),int(bloque.getpixel((0,1))+error*3/16))

    return nuevo_bloque

def aplica_matriz(matriz, bloque: Image):
    """
        Aplica una matriz a un bloque. La matriz y el bloque deben tener la misma dimension

        Parameters :
        ------------

            matriz:
                matriz a aplicar

            bloque:
                Pillow Image

        Returns :
        ---------

            nuevo bloque
    """
    # 255 / 9 ≈ 28
    step = 28

    # Nuevo bloque
    nuevo_bloque = Image.new('L', bloque.size)

    # Procesamos el bloque
    for x in range(bloque.width):
        for y in range(bloque.height):
            pixel = bloque.getpixel((x,y))
            umbral = matriz[x][y]
            if pixel <= (umbral * step):
                nuevo_bloque.putpixel((x,y),0)
            else:
                nuevo_bloque.putpixel((x,y),255)

    return nuevo_bloque

def promedio_gris(imagen: Image):
    """
        Regresa el promedio a gris de una imagen
    """
    # Verificamos que la imagen este en modo L (grises)
    imagen_grayscale = imagen.convert('L') if imagen.mode != 'L' else imagen
    # Obtenemos los piexeles en una lista
    pixeles = imagen_grayscale.getdata()
    # Regresamos el promedio
    return int(sum(pixeles) / len(pixeles))
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Programa que implementa algoritmos de dithering")

    info_algoritmos = """
        
    --sp: Semitonos con puntos
    --sm: Semitonos con matrices
    --do: Dithering ordenado
    --dd: Dithering disperso
    --da: Dithering al azar
    --fs: Dithering de Floyd Steinberg

    """

    # Argumentos no opcionales
    parser.add_argument("algoritmo", help=info_algoritmos)
    parser.add_argument("ruta_imagen", help="Ruta de la imagen")
    parser.add_argument("ruta_salida", help="Nombre del archivo de salida")

    # Obtenemos los argumentos
    args = parser.parse_args()

    # Cargamos la imagen
    imagen = None
    try:
        imagen = Image.open(args.ruta_imagen)
    except Exception as e:
        print(rojo+f"Error al cargar la imagen: {e}"+reset)
        exit()

    # Dithering a aplicar
    algoritmo = args.algoritmo
    resultado = None
    if algoritmo == "--sp":
        resultado = semitonos_puntos(imagen)        
    elif algoritmo == "--sm":
        resultado = semitonos_matrices(imagen)
    elif algoritmo == "--do":
        resultado = dithering_ordenado(imagen)
    elif algoritmo == "--dd":
        resultado = dithering_disperso(imagen)
    elif algoritmo == "--da":
        resultado = dithering_azar(imagen)
    elif algoritmo == "--fs":
        resultado = floyd_steinberg(imagen)
    else:
        print(rojo+f"Algoritmo no conocido: {args.algoritmo}"+reset)
        exit()

    # Guardamos la imagen
    resultado.save(args.ruta_salida)
    # Mostramos la imagen
    resultado.show()
