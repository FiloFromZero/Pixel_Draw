"""This module represents the behavior of a semantic analyzer for PixelDraw.

The semantic analyzer processes tokens from the lexical analyzer and converts them
into actual drawing instructions, validating the meaning and context of the commands.

Authors: Nicolás Alberto Rodríguez Delgado <20202020019>
         Daniel Mateo Montoya González <20202020098>
"""

class SemanticAnalyzer:

    """This class represents the behavior of a semantic analyzer for PixelDraw.
    
    The semantic analyzer takes tokens from the lexical analyzer and interprets
    their meaning to generate the final pixel art. It handles canvas sizing,
    color management, drawing operations, and coordinate validation.
    """

    def __init__(self, tokens_input: list):
        # Store the list of tokens to be analyzed
        self.tokens = tokens_input
        
        # Canvas dimensions (will be set by SIZE command)
        self.canvas_width = None
        self.canvas_height = None
        
        # List to store all pixels as (x, y, color) tuples
        self.pixels = []
        
        # Current drawing color (defaults to black)
        self.current_color = "#000000"

    def analyze(self):
        """
        Analyzes the tokens and returns a tuple containing:
            - Width and height of the canvas
            - A list of pixels as (x, y, color) tuples
            
        Returns:
            tuple: (canvas_width, canvas_height, pixels_list)
            
        Raises:
            Exception: If canvas size is not defined or coordinates are invalid
        """
        token_count = len(self.tokens)
        i = 0  # Current token index

        # Process each token sequentially
        while i < token_count:
            token = self.tokens[i]

            # Handle SIZE command: "size WxH" - sets canvas dimensions
            if token.type_ == "SIZE":
                # Extract width and height from "size WxH" format
                size_parts = token.value.split()[1].split("x")
                self.canvas_width = int(size_parts[0])
                self.canvas_height = int(size_parts[1])
                print(f"Canvas size: {self.canvas_width}x{self.canvas_height}")
                i += 1

            # Handle COLOR command: "color <value>" - sets current drawing color
            elif token.type_ == "COLOR":
                # Extract color value (can be color name or hex code)
                self.current_color = token.value.split()[1]
                print(f"Current color set to: {self.current_color}")
                i += 1

            # Handle POINT command: "point X Y" - draws a single pixel
            elif token.type_ == "POINT":
                # Extract X and Y coordinates from "point X Y" format
                _, x_str, y_str = token.value.split()
                x, y = int(x_str), int(y_str)
                
                # Validate that coordinates are within canvas bounds
                self._validate_coordinates(x, y)
                
                # Add the pixel to our drawing list
                self.pixels.append((x, y, self.current_color))
                print(f"Added point at ({x},{y}) with color {self.current_color}")
                i += 1

            # Handle RECTANGLE command: "rectangle X Y W H" - draws a filled rectangle
            elif token.type_ == "RECTANGLE":
                # Extract position (X,Y) and dimensions (W,H) from "rectangle X Y W H" format
                parts = token.value.split()
                x, y, w, h = map(int, parts[1:])
                
                # Draw each pixel in the rectangle
                for dx in range(w):  # Iterate through width
                    for dy in range(h):  # Iterate through height
                        px, py = x + dx, y + dy  # Calculate pixel position
                        self._validate_coordinates(px, py)  # Validate coordinates
                        self.pixels.append((px, py, self.current_color))  # Add pixel
                        
                print(f"Added rectangle at ({x},{y}) size {w}x{h} with color {self.current_color}")
                i += 1

            # Handle REPEAT command: "repeat N { ... }" - repeats a block of commands
            elif token.type_ == "REPEAT_INI":
                # Extract repeat count from "repeat N {" format
                parts = token.value.split()
                repeat_count = int(parts[1])
                i += 1  # Move past "repeat N {" token
                
                # Collect all tokens inside the repeat block
                block_tokens = []
                while i < token_count and self.tokens[i].type_ != "REPEAT_END":
                    block_tokens.append(self.tokens[i])
                    i += 1
                    
                # Validate that we found the closing brace
                if i >= token_count or self.tokens[i].type_ != "REPEAT_END":
                    raise Exception("Semantic Error: Missing closing '}' for repeat block.")
                    
                # Execute the block the specified number of times
                for _ in range(repeat_count):
                    # Create a new analyzer for the block with current context
                    block_analyzer = SemanticAnalyzer(block_tokens)
                    block_analyzer.canvas_width = self.canvas_width
                    block_analyzer.canvas_height = self.canvas_height
                    block_analyzer.current_color = self.current_color
                    block_analyzer.analyze()
                    
                    # Add all pixels from the repeated block to our main pixel list
                    self.pixels.extend(block_analyzer.pixels)
                    
                i += 1  # Skip the closing "}" token
            else:
                # Skip any unrecognized tokens (for future extensibility)
                i += 1

        # Validate that canvas size was defined before returning
        if self.canvas_width is None or self.canvas_height is None:
            raise Exception("Semantic Error: Canvas size not defined with 'size'.")

        return self.canvas_width, self.canvas_height, self.pixels

    def _validate_coordinates(self, x: int, y: int):
        """Validates that the coordinates are within the canvas size.
        
        Args:
            x (int): X coordinate to validate
            y (int): Y coordinate to validate
            
        Raises:
            Exception: If coordinates are outside the canvas bounds
        """
        # Check if coordinates are within valid range (0 to width-1, 0 to height-1)
        if self.canvas_width is None or self.canvas_height is None:
            raise Exception("Semantic Error: Cannot validate coordinates - canvas size not set.")
            
        if not (0 <= x < self.canvas_width and 0 <= y < self.canvas_height):
            raise Exception(f"Semantic Error: Point ({x},{y}) is outside the canvas size {self.canvas_width}x{self.canvas_height}.")
