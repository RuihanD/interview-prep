"""
Given a mouse with 2 APIs in a maze. Design an algorithm to find a cheese in the maze using only the 2 given APIs shown below.

class Mouse {

	/**
	* Moves to one of the directions (left, right, up, down) and returns false if you can't move and true if you can.
	*/
	public boolean move(Direction direction);

	/**
	* Returns true if there is a cheese in the current cell.
	*/
	public boolean hasCheese();

	/**
	* Should return true and leave the mouse at that location or false if we can't find cheese and return the mouse back to where it started.
	*/
	public boolean getCheese() {
		// your code goes here
	}
}
"""
class Mouse:
    def __init__(self):
        self.visited = {}  # A dictionary to store visited cells

    def move(self, direction):
        # Implement your logic for moving in the specified direction
        # Return True if movement is possible, otherwise False
        pass

    def has_cheese(self):
        # Implement your logic to check if there is cheese in the current cell
        pass

    def get_cheese(self):
        return self.dfs(0, 0, None)

    def dfs(self, x, y, last_dir):
        if self.has_cheese():
            return True

        if (x, y) not in self.visited:
            self.visited[(x, y)] = True

            directions = [Direction.up, Direction.left, Direction.down, Direction.right]

            for direction in directions:
                if self.move(direction):
                    new_x, new_y = x, y
                    if direction == Direction.up:
                        new_y += 1
                    elif direction == Direction.left:
                        new_x -= 1
                    elif direction == Direction.down:
                        new_y -= 1
                    elif direction == Direction.right:
                        new_x += 1

                    if self.dfs(new_x, new_y, direction):
                        return True

        # Found nothing, backtrack
        if last_dir is not None:
            if last_dir == Direction.up:
                self.move(Direction.down)
            elif last_dir == Direction.down:
                self.move(Direction.up)
            elif last_dir == Direction.left:
                self.move(Direction.right)
            elif last_dir == Direction.right:
                self.move(Direction.left)

        return False
