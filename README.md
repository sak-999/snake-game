# snake-game
![game-gui (2)](https://github.com/user-attachments/assets/c4f1cb28-531e-4888-a584-1b2bb72be7d9)

Explanation:
Game Setup:

The game window is created using tkinter's Canvas widget. The canvas is used to draw the snake, the food, and the game boundaries.
Game Variables:

The snake is represented as a list of coordinates where each coordinate is a tuple (x, y) corresponding to a part of the snake.
The snake moves in a grid, and each segment is 20x20 pixels (modifiable).
The food is a red square randomly placed on the screen.
Movement Logic:

The snake moves by adding a new head in the direction it is currently moving. If it eats the food, it grows by keeping the new head, and the tail is not removed.
If it collides with the wall or itself, the game ends and a "Game Over" message is displayed.
Keyboard Controls:

The arrow keys are used to change the snake's direction. The snake cannot reverse its direction, so pressing the opposite direction does nothing.
Game Loop:

The update_game method is called every speed milliseconds (adjustable) to update the state of the game, move the snake, check for collisions, and redraw the screen.
How to Run:
Make sure you have Python installed.
Save the code above in a .py file (e.g., snake_game.py).
Run the file using Python (python snake_game.py).
Control the snake with the arrow keys and try to eat the food while avoiding walls and collisions with itself.
Enjoy your game!
