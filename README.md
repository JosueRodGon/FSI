# FSI
# Búsqueda con adversario: Conecta 4

*Josué Rodríguez González

##Introducción
En este trabajo se ha de aplicar una heurística que realice el correcto funcionamiento de una inteligencia artificial en el juego de conecta en 4.

##Realización

**run.py**:
Aquí es donde realizo las consultas al usuario sobre la dificultad y si desea empezar primero.
```{language:Python}
while(True):
    print("Dificultades posibles: Facil (1), Medio (2), Dificil (3)")
    dificultad = input ("Que dificultad desea:")
    if dificultad < 1 or dificultad > 3:
        print("Opcion no valida")
    else:
        dificultad += 1
        break
```
En el archivo **game.py** es donde utilizaremos esta dificultad, consistiendo en la profundidad del árbol.

```{language:Python}
    def alphabeta_search(state, game, d, cutoff_test=None, eval_fn=heuristica.heuristica):
```
  EModificando los parametros que reciben *d* y *eval_fn*

Para la creación de la heurística he creado el archivo **heuristica.py**. Sigo el mismo principio que está en **game.py** sobre la detección de líneas en su código adicional del 3 en raya pero ajustándolo para el Conecta-4.
```{language:Python}
    def heuristica(state):
    n = 0
    if state.utility != 0:
        return state.utility * 10000
    else:
        for move in state.moves:
            n -= value(state.board, move, 'O')
            n += value(state.board, move, 'X')
        return n
```
  En primer lugar, se comprueba si el estado actual hay posibilidad de que se pierda/gane la partida comprobando el atributo de *utility* que te devolverá 1 o -1 en sus respectivos casos. En caso de que no esté en un movimiento definitivo se comprueba si es posible formar líneas para cada jugador, O para el humano y X para la máquina.
```{language:Python}
    def value(board, move, player):
    n= (k_in_row(board, move, player, (0, 1)) +
        k_in_row(board, move, player, (1, 0)) +
        k_in_row(board, move, player, (1, 1)) +
        k_in_row(board, move, player, (1, -1)))
    return n
```
  Como el conecta en 4 se pueden formar más de una línea y se pueden generar más de una línea comparado con el 3 en raya se comprueba en todas las líneas posibles en ese punto y se hace un sumatorio aumentando el valor para el usuario en caso favorable, y disminuyéndolo en caso de que favorable a la IA. Es decir, tras calcularlo, la máquina moverá siempre al valor de la heurística más alto.
```{language:Python}
    def k_in_row(board, move, player, (delta_x, delta_y)):
    x, y = move
    n = 0  # n is number of moves in row
    while board.get((x, y)) == player or board.get((x, y)) ==  None:
        if (board.get((x, y), '.') == player):
            n += 1
        x, y = x + delta_x, y + delta_y
        if x > 7 or x < 0 or y > 6 or y < 0:
            break
    x, y = move
    while board.get((x, y)) == player or board.get((x, y)) == None:
        if (board.get((x, y)) == player):
            n += 1
        x, y = x - delta_x, y - delta_y
        if x > 7 or x < 0 or y > 6 or y < 0:
            break

    return n
```

