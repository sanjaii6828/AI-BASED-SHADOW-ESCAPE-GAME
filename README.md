# SHADOW ESCAPE – AI Agent Based Stealth Game

## Project Description

Shadow Escape is a Python-based stealth game that demonstrates Artificial Intelligence concepts through autonomous guard movement and player pursuit. The player must collect all required keys, avoid AI guards, and reach the exit to win.

## Features

* Interactive game built using Python and Tkinter.
* AI guards that track the player's position.
* A* pathfinding algorithm for intelligent guard movement.
* Key collection and exit-based winning conditions.
* Collision detection between the player and AI guards.
* Win/Loss screen with restart functionality.
* Simple graphical game interface.

## Technologies Used

* Python
* Tkinter
* A* Search Algorithm
* Artificial Intelligence

## Project Structure

```text
SHADOW ESCAPE/
├── .gitignore
├── README.md
├── main.py
├── settings.py
├── map_data.py
├── drawing.py
├── player.py
├── ai.py
├── game_logic.py
└── requirements.txt
```

## Installation and Execution

### 1. Install Python

Install Python 3.10 or later and ensure Python is added to PATH.

### 2. Open the Project Folder

Open the project folder in Visual Studio Code.

### 3. Run the Game

Open the VS Code terminal and execute:

```bash
python main.py
```

## How to Play

1. Use the arrow keys to move the player.
2. Collect all the required keys.
3. Avoid the AI guards.
4. Reach the exit after collecting the keys.
5. Restart the game after a win or loss.

## AI Concepts

* **A* Search:** Calculates paths for AI guards to pursue the player.
* **Agent-Based Behaviour:** Guards act as autonomous agents.
* **Collision Detection:** Checks whether the player encounters a guard.
* **Game-State Evaluation:** Determines whether the player wins or loses.

## Project Objective

The objective is to demonstrate how AI search algorithms and autonomous agents can be applied in an interactive game environment.

## Author

Student Mini Project
