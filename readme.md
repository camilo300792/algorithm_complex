# Complejidad Algorítmica

Antes de explicarte que es la complejidad algorítmica me gustaría hacerte una pregunta:

**¿Como mides el rendimiento de tus algoritmos?**

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

Además de factores externos al algorítmo como el hardware donde se ejecuta o el lenguaje de programación en el que se implemento, Podemos notar que no tenemos un medida exacta para saber que algorítmo es más eficiente. Pues no vemos una diferencia muy amplia entre ambas implementaciones. 