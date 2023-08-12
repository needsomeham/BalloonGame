# Balloons Puzzle
Author Jacob Needham  
Game inspired by Ethan Edward and co.


### Objective
Within a nine by nine array of tiles, find the board that matches all balloons across internal edges.


## Board setup
### Tile
    An individual tile:
         _ _ _ _  
        |   1   |  
        | 4   2 |  
        |   3   |  
         _ _ _ _  

Where positions correlate with numbers as follows:
- 1: Top
- 2: Right
- 3: Bottom
- 4: Left

#### Board
A solved board consists of 9 tiles where each of their internal edges match with their neighbor:  

    Solved board
         _ _ _ _   _ _ _ _   _ _ _ _
        |   1   | |   3   | |   2   |
        | 2   4 | | 4   2 | | 2   3 |
        |   3   | |   2   | |   5   |
         _ _ _ _   _ _ _ _   _ _ _ _
         _ _ _ _   _ _ _ _   _ _ _ _
        |   3   | |   2   | |   5   |
        | 5   5 | | 5   4 | | 4   3 |
        |   2   | |   1   | |   3   |
         _ _ _ _   _ _ _ _   _ _ _ _
         _ _ _ _   _ _ _ _   _ _ _ _
        |   2   | |   1   | |   3   |
        | 1   5 | | 5   3 | | 3   4 |
        |   3   | |   2   | |   1   |
         _ _ _ _   _ _ _ _   _ _ _ _

Balloons from board above are loaded as follows:  
[1,4,3,2, 3,2,2,4, 2,3,5,2, 3,5,2,5, 2,4,1,5, 5,3,3,4, 2,5,3,1, 1,3,2,5, 3,4,1,3]  
Where the first four ints represent the first tile moving clockwise around the tile.
Second four ints represent the second tile moving clockwise around that tile.
So on.

    Positions of tiles:
         _ _ _ _   _ _ _ _   _ _ _ _
        |       | |       | |       |
        |   0   | |   1   | |   2   |
        |       | |       | |       |
         _ _ _ _   _ _ _ _   _ _ _ _
         _ _ _ _   _ _ _ _   _ _ _ _
        |       | |       | |       |
        |   3   | |   4   | |   5   |
        |       | |       | |       |
         _ _ _ _   _ _ _ _   _ _ _ _
         _ _ _ _   _ _ _ _   _ _ _ _
        |       | |       | |       |
        |   6   | |   7   | |   8   |
        |       | |       | |       |
         _ _ _ _   _ _ _ _   _ _ _ _


### Moves
Player can:
 - rotate a tile counterclockwise or clockwise
 - swap two tiles

     
    A right (clockwise) rotation yields:
         _ _ _ _
        |   4   |
        | 3   1 |
        |   2   |
         _ _ _ _

     A left (counterclockwise) rotation yields:
         _ _ _ _
        |   2   |
        | 1   3 |
        |   4   |
         _ _ _ _

    Swapping tiles 1 and 5:
         _ _ _ _   _ _ _ _   _ _ _ _
        |       | |       | |       |
        |   4   | |   1   | |   2   |
        |       | |       | |       |
         _ _ _ _   _ _ _ _   _ _ _ _
         _ _ _ _   _ _ _ _   _ _ _ _
        |       | |       | |       |
        |   3   | |   0   | |   5   |
        |       | |       | |       |
         _ _ _ _   _ _ _ _   _ _ _ _
         _ _ _ _   _ _ _ _   _ _ _ _
        |       | |       | |       |
        |   6   | |   7   | |   8   |
        |       | |       | |       |
         _ _ _ _   _ _ _ _   _ _ _ _
