# Complejidad Algorítmica

Antes de explicarte que es la complejidad algorítmica me gustaría hacerte una pregunta:

**¿Cómo mides el rendimiento de tus algoritmos?**

> Obviamente por el tiempo de ejecución...

Si tu respuesta tiene algo que ver con el tiempo de ejecución... Pues te quiero felicitar acabas de encontrar una oportunidad de mejora porque estás equivocado. Pero tranquilo no te desanimes voy a mostrarte porque este método no proporciona una métrica exacta para medir como se comporta tu algorítmo, veamos un ejemplo:

Tenemos dos funciones con diferente implementación que hacen exactamente lo mismo: *encontrar el factorial de un númeno n*

```python
import time

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def factorial_r(n):
    if n == 1:
        return 1
    return n * factorial_r(n - 1)


if __name__ == '__main__':

    n = 8
    start = time.time()
    factorial(n)
    end = time.time()
    print('Factorial execution end: ' + str(end - start))

    start = time.time()
    factorial_r(n)
    end = time.time()
    print('Factorial execution end: ' + str(end - start))
```

Además de factores externos al algorítmo, como el hardware donde se ejecuta o el lenguaje de programación en el que se implementó, podemos notar que no tenemos un medida exacta para saber que algorítmo es más eficiente. Ya que no vemos una diferencia muy amplia entre ambas implementaciones.

**Entonces... ¿Existe un método para medir la eficiencia de un algorítmo?**

> Sí, pero antes de verlo entendamos un concepto un poco más abstracto.

```
proceso f1(numero)
    para i hasta numero con paso 1 hacer
        imprimir numero % 2
    fin para
fin proceso

proceso f2(numero)
    imprimir numero * numero
fin proceso

proceso f3(numero)
    para i hasta numero con paso 1 hacer        
        para j hasta numero con paso 1 hacer
            imprimir i, "->", j
        fin para
    fin para
fin proceso
```

Dejando de lado el lenguaje de programación, el hardware u otros factores externos que nos impiden determinar la eficiencia de nuestros algorítmos. 

> No es lo mismo ejecutar una función en *python* que una en *C* o ejecutarla en un equipo con procesador Celeron que en uno con procesador Xeon.

Podemos contar cuantos procesos realizan nuestros algorítmos. Por ejemplo:

En nuestro primer caso vemos que el proceso *f1* recibe un número e itera esa cantidad de veces para imprimir el resultado de una operación con el indice actual... Tenemos *n* pasos para ejecutar una intrucción *"El módulo dos del paso para saber si es un número primo"*. 
El resultado es (n + 1)

A diferencia del proceso *f1* el proceso *f2* no tiene instrucciones iterativas y aunque depende de *numero* para operar, el número de ejecuciones no va a crecer conforme el input se haga más grande. Entonces si el input es mil nuestro proceso solo se ejecuta una vez y retorna el cuadrado de la entrada. 
El resultado es (1)

Por último pero no menos importante tenemos nuestro proceso *f3* que como podemos notar depende de nuestro input *numero*, pero con la particularidad de que tiene un ciclo dentro de otro, esto multiplica la cantidad de veces que se ejecuta nuestro algorítmo en cada iteración y como tenemos dos ciclos que dependen del input más una operación interna. 
El resultado es (n * n + 1) o (n^2 + 1)

Con esto en mente podemos empezar a hablar de complejidad algorítmica...

![](https://i.ytimg.com/vi/ONNTDstfzsg/sddefault.jpg)

Entender de complejidad algorítmica nos permite evaluar como se comporta un algorítmo en función al tamaño de su entrada y cuál es la tasa de crecimiento conforme se acerca al infinito. A esto se le conoce como notación asintótica. Una de ellas es *Big O Notation* o *notación de (O) grande*.

*Big O* Nos permite descartar los terminos menos significativos para enfoncarnos en el tiempo de ejecución y su tasa de crecimiento. 
En teoría, ya hemos visto un poco de esto con los ejemplos anteriores y si tomamos como referencia el primero de ellos vemos que nuestro resultado fue *(n + 1)*. 

> Pero... *Big O* nos permite descartar terminos menos significativos. :confused: eso que quiere decir. 
 
Esto nos indica que podemos descartar aquello que no influye en como crece el tiempo de ejecución de nuestro algorítmo. Entonces, si analizamos *(n + 1)* podríamos descartar el ***1*** y quedarnos con la ***n*** ya que a medida que sea más grande, más tiempo le tomará a nuestro algorítmo terminar. Entonces el *Big O* de *f1* es *O(n)*.
Si me has seguido hasta acá entonces serás capaz de entender porque el *Big O* de *f2* es *O(1)* y el de *f3* es *O(n^2)*. Sino, te lo explicaré rápidamente: 

* *f2* es *O(1)* porque no tenemos que descatar ya que solo operamos una vez, osea tenemos el mejor performance posible para nuestro algoritmo porque es constante no importa cuán grande sea el input siempre se tardara lo mismo en procesarlo.

* *f3* es *O(n^2)* porque al igual que en el primer ejemplo descartamos terminos menos significativos y nos quedamos con *(n * n)* o *ene al cuadrado*.