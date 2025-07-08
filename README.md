# PixelDraw

PixelDraw is a simple domain-specific language (DSL) and compiler for creating pixel art through code. The project is designed for educational purposes, demonstrating the phases of compilation: lexical analysis, syntactic analysis, semantic analysis, and visualization.

## Project Overview

PixelDraw allows users to write code that describes pixel art using drawing commands (such as `pixel`, `line`, `circle`, `color`, etc.). The compiler processes this code and visualizes the resulting pixel art using a graphical interface (Tkinter).

### Main Features
- **Lexical Analysis:** Breaks down the source code into tokens using regular expressions.
- **Syntactic Analysis:** Validates the structure of the code to ensure it follows the PixelDraw grammar.
- **Semantic Analysis:** Interprets the validated tokens to generate drawing instructions.
- **Visualization:** Renders the pixel art on a Tkinter canvas, where each pixel is drawn as a colored rectangle.

## File Structure
- `LexicalPd.py`: Implements the lexical analyzer (tokenizer) for PixelDraw.
- `SintacticPD.py`: Contains the syntactic analyzer for validating code structure.
- `SemanticPD.py`: Handles semantic analysis and generates drawing instructions.
- `CompilerPD.py`: Orchestrates the compilation process and displays the pixel art.
- `ExamplePD.py`: (Optional) Example usage or sample PixelDraw code.

## How It Works
1. **Write PixelDraw code** using the supported commands (see documentation in `LexicalPd.py`).
2. **Compile the code** using the `CompilerPixelDraw` class in `CompilerPD.py`.
3. **View the result** in a graphical window, where your pixel art is displayed.

## Requirements
- Python 3.x
- Tkinter (usually included with Python)

## Authors
- Nicolás Alberto Rodríguez Delgado
- Daniel Mateo Montoya González

---

*This project is for educational purposes and demonstrates the basic principles of compiler construction and graphical output in Python.*