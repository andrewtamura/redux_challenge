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
