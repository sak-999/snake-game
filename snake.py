import tkinter as tk
import random

# Game settings
width = 600
height = 400
segment_size = 20
speed = 100  # Time between frames in milliseconds

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        
        # Initialize canvas for game area
        self.canvas = tk.Canvas(self.master, width=width, height=height, bg="black")
        self.canvas.pack()

        # Initial game state
        self.snake = [(100, 100), (80, 100), (60, 100)]  # Initial positions of the snake
        self.snake_direction = "Right"  # Snake's current direction
        self.food = None
        self.game_over = False
        
        # Bind arrow keys for controlling the snake
        self.master.bind("<Left>", self.turn_left)
        self.master.bind("<Right>", self.turn_right)
        self.master.bind("<Up>", self.turn_up)
        self.master.bind("<Down>", self.turn_down)
        
        # Start the game
        self.create_food()
        self.update_game()

    def update_game(self):
        if self.game_over:
            self.canvas.create_text(width // 2, height // 2, text="Game Over", fill="white", font=("Arial", 24))
            return
        
        # Move the snake in the current direction
        head_x, head_y = self.snake[0]
        if self.snake_direction == "Left":
            head_x -= segment_size
        elif self.snake_direction == "Right":
            head_x += segment_size
        elif self.snake_direction == "Up":
            head_y -= segment_size
        elif self.snake_direction == "Down":
            head_y += segment_size

        new_head = (head_x, head_y)
        
        # Check for collision with wall or self
        if (head_x < 0 or head_x >= width or head_y < 0 or head_y >= height or new_head in self.snake):
            self.game_over = True
            self.update_game()
            return

        # Add the new head and remove the tail (unless food is eaten)
        self.snake = [new_head] + self.snake
        if new_head == self.food:
            self.create_food()  # Create new food if eaten
        else:
            self.snake.pop()  # Remove tail if no food eaten

        # Clear and redraw the game area
        self.canvas.delete("all")
        self.draw_snake()
        self.draw_food()

        # Continue the game
        self.master.after(speed, self.update_game)

    def draw_snake(self):
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + segment_size, segment[1] + segment_size, fill="green")

    def draw_food(self):
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + segment_size, self.food[1] + segment_size, fill="red")

    def create_food(self):
        # Randomly place food
        x = random.randint(0, (width - segment_size) // segment_size) * segment_size
        y = random.randint(0, (height - segment_size) // segment_size) * segment_size
        self.food = (x, y)

    def turn_left(self, event):
        if self.snake_direction != "Right":
            self.snake_direction = "Left"

    def turn_right(self, event):
        if self.snake_direction != "Left":
            self.snake_direction = "Right"

    def turn_up(self, event):
        if self.snake_direction != "Down":
            self.snake_direction = "Up"

    def turn_down(self, event):
        if self.snake_direction != "Up":
            self.snake_direction = "Down"


# Create the main game window
root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
