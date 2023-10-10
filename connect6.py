"""
The goal of this question is to implement Connect6.
For those unfamiliarConnect6 is a very simple board game and is similar to tic-tac-toe.
There are two players, black and white, who alternate turns placing their colored pieces onto a grid.
The first player to connect 6 or more of their pieces together either horizontally, vertically, or diagonally wins.
Black places one piece first then each player alternates placing two pieces onto the board.
The board size should be equal to K x K where k <= 109
An example game may look something like this:

Your Task
You should implement a class called Connect6 with the following methods.
----------------------------------------------------------------------------------------------------------------------------------------------------------
Method Name       ｜     Description                              ｜      Arguments       ｜      Return Value
----------------------------------------------------------------------------------------------------------------------------------------------------------
(constructor)     ｜     Initializes the game                     ｜      k: integer      ｜      void
                  ｜     with a k by k board                      ｜                      ｜
----------------------------------------------------------------------------------------------------------------------------------------------------------
getTurn           ｜     Retrieve which player                    ｜      void            ｜      string: "black" if its black's turn
                  ｜     should move next.                        ｜                      ｜      other wise"white"
----------------------------------------------------------------------------------------------------------------------------------------------------------
placeBlack        ｜     Place a black piece onto the board       ｜      x: integer      ｜      boolean: True if the move resulted in a win else false.
                  ｜     at the specified coordinates.            ｜      y: integer      ｜
----------------------------------------------------------------------------------------------------------------------------------------------------------
placeWhite        ｜     Place a white piece onto the board       ｜      x: integer      ｜     boolean: True if the move resulted in a win else false.
                  ｜     at the specified coordinates.            ｜      y: integer      ｜
----------------------------------------------------------------------------------------------------------------------------------------------------------
"""
from collections import defaultdict
class Connect6:
    def __init__(self, k):
        self.currentPlayer = 1
        self.turnsLeft = 1
        self.occupiedBlack = defaultdict(set)
        self.occupiedWhite = defaultdict(set)

    def getTurn(self):
        return "black" if self.currentPlayer == 1 else "white"

    def placeBlack(self, x, y):
        if (x in self.occupiedBlack and y in self.occupiedBlack[x]) or (x in self.occupiedWhite and y in self.occupiedWhite[x]):
            raise ValueError("Occupied grid. Please enter again")

        self.occupiedBlack[x].add(y)

        win = self.checkWin(x, y)
        self.turnsLeft -= 1
        if self.turnsLeft == 0:
            self.currentPlayer = 0
            self.turnsLeft = 2

        return win

    def placeWhite(self, x, y):
        if (x in self.occupiedBlack and y in self.occupiedBlack[x]) or (x in self.occupiedWhite and y in self.occupiedWhite[x]):
            raise ValueError("Occupied grid. Please enter again")

        self.occupiedWhite[x].add(y)

        win = self.checkWin(x, y)
        self.turnsLeft -= 1
        if self.turnsLeft == 0:
            self.currentPlayer = 1
            self.turnsLeft = 2

        return win

    def checkWin(self, x, y):
        xMove = [0, 1, 1, 1]
        yMove = [1, 0, 1, -1]

        for i in range(4):
            count = 0
            xStart = x - 6 * xMove[i]
            yStart = y - 6 * yMove[i]

            for j in range(11):
                xStart += xMove[i]
                yStart += yMove[i]

                if self.currentPlayer == 1:
                    if xStart in self.occupiedBlack and yStart in self.occupiedBlack[xStart]:
                        count += 1
                    else:
                        count = 0
                    if count == 6:
                        return True
                else:
                    if xStart in self.occupiedWhite and yStart in self.occupiedWhite[xStart]:
                        count += 1
                    else:
                        count = 0
                    if count == 6:
                        return True

        return False

    @staticmethod
    def runSimpleTest():
        board = Connect6(100)

        assert board.getTurn() == "black"
        assert board.placeBlack(50, 50) is False

        assert board.getTurn() == "white"
        assert board.placeWhite(51, 50) is False
        assert board.placeWhite(51, 51) is False

        assert board.getTurn() == "black"
        assert board.placeBlack(50, 51) is False
        assert board.placeBlack(50, 49) is False

        assert board.getTurn() == "white"
        assert board.placeWhite(52, 50) is False
        assert board.placeWhite(53, 51) is False

        assert board.getTurn() == "black"
        assert board.placeBlack(50, 52) is False
        assert board.placeBlack(50, 53) is False

        assert board.getTurn() == "white"
        assert board.placeWhite(53, 50) is False
        assert board.placeWhite(54, 51) is False

        assert board.getTurn() == "black"
        assert board.placeBlack(50, 48) is True  # Black wins along row 50


if __name__ == "__main__":
    Connect6.runSimpleTest()
