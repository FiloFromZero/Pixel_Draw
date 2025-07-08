"""This module contains the Compiler class for PixelDraw.

The PixelDraw compiler processes source code through three main phases:
1. Lexical Analysis - Breaks code into tokens
2. Syntactic Analysis - Validates token structure
3. Semantic Analysis - Generates drawing instructions
4. Visualization - Displays the pixel art using Tkinter

Authors: Nicolás Alberto Rodríguez Delgado <20202020019>
         Daniel Mateo Montoya González <20202020098>
"""

import tkinter as tk

from LexicalPd import LexicalAnalyzer
from SintacticPD import SintacticAnalyzerPixelDraw
from SemanticPD import SemanticAnalyzer


class CompilerPixelDraw:
    """
    Main compiler class for the PixelDraw language.
    
    This class orchestrates the entire compilation process from source code
    to visual output. It coordinates the lexical, syntactic, and semantic
    analyzers to transform PixelDraw code into pixel art.
    """

    def __init__(self):
        """
        Initialize the PixelDraw compiler with default settings.
        
        Sets up default canvas dimensions, pixel size, and drawing color
        for the visualization phase.
        """
        self.canvas_size = (500, 500)  # Default window size in pixels
        self.pixel_size = 20           # Default size of each pixel block in pixels
        self.current_color = "#000000" # Default color (black)
        self.grid = []                 # Grid to store pixel data

    def compile(self, code: str):
        """
        Compile PixelDraw source code into visual output.
        
        This method implements the complete compilation process:
        1. Lexical analysis to tokenize the code
        2. Syntactic analysis to validate structure
        3. Semantic analysis to generate drawing instructions
        4. Visualization to display the result
        
        Args:
            code (str): The PixelDraw source code to compile
            
        Raises:
            RuntimeError: If lexical analysis fails
            SyntaxError: If syntactic analysis fails
            Exception: If semantic analysis or visualization fails
        """
        # Phase 1: Lexical analysis - Convert code to tokens
        tokens = LexicalAnalyzer.lex(code)

        # Phase 2: Syntactic analysis - Validate token structure
        sintactic_analyzer = SintacticAnalyzerPixelDraw(tokens)
        sintactic_analyzer.parse()

        # Phase 3: Semantic analysis - Generate drawing instructions
        semantic_analyzer = SemanticAnalyzer(tokens)
        width, height, pixels = semantic_analyzer.analyze()

        # Phase 4: Draw the pixel art on screen
        self.draw_canvas(width, height, pixels)

    def draw_canvas(self, width: int, height: int, pixels: list):
        """
        Create and display the pixel art using Tkinter.
        
        This method creates a graphical window showing the compiled pixel art.
        Each pixel is drawn as a colored rectangle on the canvas.
        
        Args:
            width (int): Width of the pixel grid
            height (int): Height of the pixel grid
            pixels (list): List of (x, y, color) tuples representing the pixel art
            
        Note:
            The canvas size is automatically adjusted based on the grid dimensions
            and pixel size. Each grid cell becomes a pixel_size x pixel_size rectangle.
        """
        # Create the main Tkinter window
        root = tk.Tk()
        root.title("PixelDraw Output")

        # Calculate canvas dimensions based on grid size and pixel size
        canvas_width = width * self.pixel_size
        canvas_height = height * self.pixel_size
        
        # Create the drawing canvas with white background
        canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
        canvas.pack()

        # Draw each pixel as a colored rectangle
        for (x, y, color) in pixels:
            # Calculate pixel coordinates in canvas space
            x1 = x * self.pixel_size
            y1 = y * self.pixel_size
            x2 = x1 + self.pixel_size
            y2 = y1 + self.pixel_size
            
            # Draw the pixel rectangle with specified color and gray border
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

        # Start the Tkinter event loop to display the window
        root.mainloop()
