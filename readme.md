# Complejidad Algorítmica

Antes de explicarte que es la complejidad algorítmica me gustaría hacerte una pregunta:

**¿Cómo mides el rendimiento de tus algoritmos?**

> Quizá tu respuesta fue: Obviamente por el tiempo de ejecución...

Pues te quiero felicitar, acabas de encontrar una oportunidad de mejora porque estás equivocado.
Pero tranquilo no te desanimes voy a mostrarte porque este método no proporciona una métrica exacta para medir como se comporta tu algorítmo, veamos un ejemplo:

Tenemos dos funciones con diferente implementación que hacen exactamente lo mismo: *encontrar en factorial de un númeno n*

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

Además de factores externos al algorítmo como el hardware donde se ejecuta o el lenguaje de programación en el que se implementó, Podemos notar que no tenemos un medida exacta para saber que algorítmo es más eficiente. Pues no vemos una diferencia muy amplia entre ambas implementaciones.

# Entonces... ¿Existe un método para medir la eficiencia de un algorítmo?

> La respuesta es sí pero antes de hablar de el veamos un método un poco más abstracto

```python
def f(x):
    for i in range(x): # x loops
        print(x % 2) # 1 Operation

def f2(x):
    return x ** 2 # Zero loop 1 Operation

def f3(x):
    for i in range(x): # x loops
        for j in range(x): # x loops
            print(i, j) # 1 Operation
```

Aquí podemos ver un metodo un poco más abstracto, y es que literalmente estamos buscando una métrica nos permita medir la eficiencia de un algorítmo independientemente del hardware o el lenguaje de programación. Lo que hacemos en un conteo de las operaciones realizadas en nuestros algoritmos.

***
En nuestra primer función *f(x)* vemos que depende completamente de *(x)* así que si nuestro input *(x)* es el número mil vamos a iterar mil veces para operar sobre cada uno de los valores.
Lo que resulta en un binomio:
- x + 1
La equis por nuestro input más uno que corresponde a la operación dentro del loop.
***

***
Para nuestra segunda función *f2(x)* vemos uná operación en relación de *(x)*.
Por lo que tenemos una constante:
- 1
Uno porque apesar de que equis puede tomar cualquier valor nuestro número de operaciones no crece ni cambia en lo absoluto.
***

***
Nuestra tercer función tiene una particularidad, tiene un bucle dentro de otro así que mientras se ejecuta el primero el segundo toma el valor de *(x)* e itera sobre el mismo antes de saltar al siguiente indice del primero.
En este caso lo que se debe hacer es una multiplicación:
- x * x + 1
Multiplamos equis porque ambos bucles dependen del input y sumamos uno por la operación dentro de ellos.
***