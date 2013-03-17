#Redux Challenge:

You are creating the game connect-4 (http://en.wikipedia.org/wiki/Connect_Four). There are two players, and each of the players take turns trying to get four of their game pieces in a row.  Your job is to enable two players to play each other remotely, sharing the same game board.

Given this overall goal, please answer each question below in a few sentences, focusing on the most important details. The last question will require you to write functioning code segments.

1.  How would you represent the game board, players and game pieces?  What data structures or code architecture would you use?

2.  Given that the players are playing each other remotely, what additional concerns do you need to address? (e.g. what if the players are playing on unreliable internet connections)

3.  Write a functional subset of the code for the code for the game board, game pieces, and player state. Your code should include a function to print out the board, in ASCII e.g. here is a plausible print out after two turns - one from player 'x' and player 'o'.

            
            * * * * * * *
            * * * * * * *
            * * * * * * *
            * * * * * * *
            * x O * * * *

Other functions required are for each player to place a new piece onto the board and checking if one of the players has won the game.

You do not need to worry about collecting the input from the players,  you can assume that the arguments to all functions/methods have been  gathered from the appropriate input device.

IMPORTANT: Give careful thought to your code organization and low-level algorithms. You can use the language of your choice to complete the question, but the code must be functional and given to us in a state where we can easily run it.

#Answers:
##Q. *How would you represent the game board, players and game pieces?  What data structures or code architecture would you use?*

###A. I would represent the game board as two level array. Each bucket would contain the values 0, 1, or 2. 0 is an empty space, 1 represents player 1, and 2 represents player 2. 

##Q. Given that the players are playing each other remotely, what additional concerns do you need to address? (e.g. what if the players are playing on unreliable internet connections)

###A. The game must be tolerant for mistakes introduced by the communication protocol. Messages could arrive malformed so the game server should enforce that the rules are being followed. e.g. no player may place two pieces during their turn, or a player may not move twice in a row. In addition, the communication protocol should support encryption and authentication so that the client messages can be trusted. Game state synchronization on the client-side is important for having an enjoyable gameplay. The client and the game should have an easy, low cost way to check if they are displaying the same game state. A move-counter could be used as a synchronization signal. If a client's move counter does not match up with the current game state, then that client needs to refresh their game state. 

##Q.  Write a functional subset of the code for the code for the game board, game pieces, and player state. Your code should include a function to print out the board, in ASCII e.g. here is a plausible print out after two turns - one from player 'x' and player 'o'.

###A. See attached file. 

