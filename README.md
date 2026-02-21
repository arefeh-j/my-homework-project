# ♟️ Eight Queens Puzzle Solver

A simple and educational implementation of the classic **Eight Queens problem** using the **Backtracking algorithm** in Python.


## About the Project
The Eight Queens problem is one of the most famous problems in computer science. The goal is to place **eight queens on an 8×8 chessboard** so that no two queens threaten each other.

This project uses the **Backtracking algorithm** to find a valid arrangement.  
The code is clean, readable, and perfect for practicing algorithms and recursive thinking.

##  Features
- ✅ Solves the Eight Queens problem using Backtracking  
- ✅ Checks queen safety with `is_safe()` function  
- ✅ Prints the chessboard with `print_board()` function  
- ✅ Finds all possible solutions (in `utils.py`)  
- ✅ Simple and understandable code structure  
- ✅ Great for students and educational projects  



##  Project Structure


eight-queens/
├── main.py # Main program & Backtracking algorithm
├── utils.py # Helper functions (safety check & board printing)
└── README.md # Documentation

## 🛠️ Installation & Usage

### 1. Clone the repository

git clone git@github.com:arefeh-j/my-homework-project.git
cd my-homework-project

2. Run the program

python3 main.py

## 🕹️ How It Works

The program creates an 8-element array where each index represents a **row**, and the value represents the **column** where the queen is placed.  
It then uses **Backtracking** to place queens ensuring:

- No two queens share the same column
- No two queens share the same diagonal

When a solution is found, the output looks like this:

. Q . . . . . .
. . . Q . . . .
Q . . . . . . .
. . . . Q . . .
. . Q . . . . .
. . . . . . Q .
. . . . . . . Q
. . . . . Q . .
## 📚 File Descriptions

### 🔹 `utils.py`
Contains helper functions:

- `is_safe(board, row, col)`  
  Checks if placing a queen at a given position is safe.

- `print_board(board)`  
  Prints the chessboard with queens.

### 🔹 `main.py`
Contains:
- Number of queens (`N = 8`)
- `solve_queens()` function for Backtracking
- `main()` function to run and display the result

---

## 👤 Author
Created by [Arefeh Jafari](https://github.com/arefeh-j) for the Advanced Programming course.

---

## 📄 License
This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute it.