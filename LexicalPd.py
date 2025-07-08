"""This module represents the behavior of a lexical analyzer for PixelDraw.

Authors: Nicolás Alberto Rodríguez Delgado <20202020019>
         Daniel Mateo Montoya González <20202020098>
"""

import re


# pylint: disable=too-few-public-methods
class Token:
    """This class represents the data structure of a token.
    It means: a type of token and its value (lexeme)."""

    def __init__(self, type_: str, value):
        # Initialize token with its type (e.g., "NUMBER", "COLOR") and value (e.g., "42", "red")
        self.type_ = type_
        self.value = value

    def __repr__(self):
        # String representation for debugging and logging
        return f"Token({self.type_}, {self.value})"


class LexicalAnalyzer:
    """This class represents the behavior of a lexical analyzer for PixelDraw.
    
    The lexical analyzer breaks down the input code into individual tokens
    that can be processed by the syntactic analyzer.
    """

    @staticmethod
    def lex(code):
        """This method receives a code and returns a list of tokens.
        
        Args:
            code (str): The source code to be tokenized
            
        Returns:
            list: List of Token objects representing the lexical analysis
            
        Raises:
            RuntimeError: If an unrecognized character or token is found
        """
        tokens = []
        
        # Define token patterns using regular expressions
        # Order is important: more specific patterns should come before general ones
        token_specification = [

                        # Drawing Characteristics
            ("CLEAR",      r"clear"),                                    # clear - clears the canvas
            ("PIXEL",      r"pixel"),                                    # pixel - draws a single pixel
            ("LINE",       r"line"),                                     # line - draws a line
            ("FRAME",      r"frame"),                                    # frame - draws an empty rectangle
            ("CIRCLE",     r"circle"),                                   # circle - draws a circle
            ("TO",         r"to"),                                       # to - used for coordinates (e.g., "to (10,20)")
            ("RADIUS",     r"radius"),                                   # radius - sets circle radius
            ("COLOR",      r"color\s+(#[0-9a-fA-F]{6}|[a-zA-Z]+)"),     # color #FF0000 or color red
            
            # Space set patterns
            ("SIZE",    r"size\s+\d+x\d+"),                         # size WxH - sets canvas size
            ("POINT",      r"point\s+\d+\s+\d+"),                         # point X Y - draws a point
            ("RECTANGLE", r"rectangle\s+\d+\s+\d+\s+\d+\s+\d+"),        # rectangle X Y W H - draws rectangle
            ("REPEAT_INI",r"repeat\s+\d+\s+\{"),                        # repeat N { - start repeat block
            ("REPEAT_END",r"\}"),                                        # } - end repeat block
            
            # Punctuation and symbols
            ("LPAREN",     r"\("),                                       # ( - left parenthesis
            ("RPAREN",     r"\)"),                                       # ) - right parenthesis
            ("COMMA",      r","),                                        # , - comma separator
            
            # Numeric and coordinate patterns
            ("NUMBER",     r"\d+"),                                      # integers - any sequence of digits
            ("COORDINATE", r"\(\s*\d+\s*,\s*\d+\s*\)"),                  # (X,Y) - coordinate pair with optional spaces
            ("DIMENSION",  r"\(\s*\d+\s*,\s*\d+\s*\)"),                  # (W,H) - dimension pair (same pattern as coordinate)
            
            # Color value patterns (must be after COLOR)
            ("COLORNAME",  r"[a-zA-Z]+"),                                # color names like red, blue, green, etc.
            ("COLORHEX",   r"#[0-9a-fA-F]{6}"),                         # hex colors like #FF0000, #00FF00, etc.
            
            # Comments and whitespace (to be ignored)
            ("COMMENT",    r"#.*"),                                      # # comment - everything from # to end of line
            ("SKIP",       r"[ \t\n]+"),                                  # Skip spaces, tabs, newlines
            ("MISMATCH",   r"."),                                         # Any other character - will cause error
        ]

        # Combine all patterns into a single regex for efficient matching
        tok_regex = "|".join(
            f"(?P<{pair[0]}>{pair[1]})" for pair in token_specification
        )

        # Iterate through all matches in the input code
        for mo in re.finditer(tok_regex, code):
            kind = mo.lastgroup  # Get the name of the matched group
            value = mo.group()   # Get the actual matched text

            if kind is None:
                # This should not happen with our regex, but just in case
                raise RuntimeError(f"Unexpected regex match without group: '{value}'")
            
            if kind == "MISMATCH":
                # Throw an error if the character is not recognized by any pattern
                raise RuntimeError(f"Unexpected token: '{value}'")
            if kind == "SKIP":
                # Skip whitespace - don't create tokens for spaces, tabs, newlines
                continue
            if kind == "COMMENT":
                # Skip comments - don't create tokens for comment lines
                continue
                
            # Create a token for the matched pattern and add it to the list
            tokens.append(Token(kind, value.strip()))

        return tokens 