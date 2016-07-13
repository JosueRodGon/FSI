import games

game = games.ConnectFour()
state = game.initial
#print games.play_game(game, games.random_player, games.alphabeta_player)

while(True):
    print("Dificultades posibles: Facil (1), Medio (2), Dificil (3)")
    dificultad = input ("Que dificultad desea:")
    if dificultad < 1 or dificultad > 3:
        print("Opcion no valida")
    else:
        dificultad += 1
        break
while(True):
    jugador = input("Desea empezar(1) o que la maquina empiece(2):")
    if jugador == 1:
        game.initial.to_move = 'O'
        player = 'O'
        break
    elif jugador == 2:
        game.initial.to_move = 'X'
        player = 'X'
        break
    elif jugador != 1 or jugador != 2:
        print("Opcion no valida")

while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        col_str = raw_input("Movimiento: ")
        coor = int(str(col_str).strip())
        x = coor
        if  x < 1 or x > 7:
            print "Movimiento no valido. Inserte un numero entre 1 y 7"
        else:
            y = -1
            legal_moves = game.legal_moves(state)
            for lm in legal_moves:
                if lm[0] == x:
                    y = lm[1]
            if y > 6:
                print "Movimiento no valido."
            else:
                state = game.make_move((x, y), state)
                player = 'X'
    else:
        print "Calculando siguiente movimiento... \n"
        #move = games.minimax_decision(state, game)
        #move = games.alphabeta_full_search(state, game)

        move = games.alphabeta_search(state, game, dificultad)
        print "Moviendo a: " + str(move) + " \n"
        state = game.make_move(move, state)
        player = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        if player == '0':
            print "\nEl ganador es: LA MAQUINA"
        else:
            print "\nEl ganador es: EL USUARIO"
        print "Final de la partida"
        break
