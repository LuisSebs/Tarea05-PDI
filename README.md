# Tarea05: Dithering

El dithering es una técnica usada en computación gráfica para crear la ilusión de profundidad de color en imágenes con una paleta de colores limitada (reducción de color). Los algoritmos implementados en esta tarea son los siguientes:

+ Semitonos (puntos y matrices)
+ Dithering azar
+ Floyd-Steinberg
+ Dithering ordenado y disperso
  
## Author: Luis Sebastian Arrieta Mancera

<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDhiaTcxMXZsOXFsMHpheWc5aXFqYTl1bWJhYmh1aHlpZHJrNmlqeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/lXiRLb0xFzmreM8k8/giphy.gif" width="400px"/>


# Dependencias

+ [Colorama](https://pypi.org/project/colorama/): `pip install colorama`
+ [Pillow](https://pypi.org/project/pillow/): `pip install pillow`
+ [Argparse](https://pypi.org/project/argparse/): `pip install argparse`

# Ejecución

Para saber informacion sobre el programa y los parametros que acepta, ejecuta con **python** o **python3** el siguiente comando:

```bash
python3 dithering.py --help
```

Para probar los algoritmos implementados en este programa ejecuta los siguientes comandos a continuación.

**Nota:** la imagen usada para estos ejemplos es muy grande, por lo que la creación de la imagen puede tardar bastante en algunos algoritmos, te recomiendo tener paciencia y probar con tus propias imagenes, en terminal se mostrará el progreso.

## Dithering semitonos con puntos
```bash
python3 dithering.py --sp ./imgs/luke-braswell.jpg ./luke-braswell-puntos.png
```

## Dithering semitonos con matrices
```bash
python3 dithering.py --sm ./imgs/luke-braswell.jpg ./luke-braswell-matrices.png
```

## Dithering ordenado
```bash
python3 dithering.py --do ./imgs/luke-braswell.jpg ./luke-braswell-ordenado.png
```

## Dithering disperso
```bash
python3 dithering.py --dd ./imgs/luke-braswell.jpg ./luke-braswell-disperso.png
```

## Dithering al azar
```bash
python3 dithering.py --da ./imgs/luke-braswell.jpg ./luke-braswell-azar.png
```

## Dithering de Floyd Steinberg
```bash
python3 dithering.py --fs ./imgs/luke-braswell.jpg ./luke-braswell-floyd-steinberg.png
```

# Referencias

+ [Floyd Steinberg](https://tannerhelland.com/2012/12/28/dithering-eleven-algorithms-source-code.html)
+ [Floyd Steinberg Pseudocode](https://medium.com/analytics-vidhya/exploiting-the-floyd-steinberg-algorithm-for-image-dithering-in-r-c19c8008fc99)
+ [Blog de La_Morsa](https://la-morsa.blogspot.com/search?q=dithering)
