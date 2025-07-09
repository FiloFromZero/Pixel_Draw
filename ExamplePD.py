"""This module is just an example of how to use the PixelDraw compiler."""
from CompilerPD import CompilerPixelDraw


# =========== Example usage ========== #
def example1(compiler_: CompilerPixelDraw):
    """This function is an example of how to use the PixelDraw compiler."""
    input_text = """
    size 10x10
    color #FF0000
    point 2 3
    rectangle 5 5 3 2
    color #0000FF
    repeat 2 {
        point 0 0
        point 1 1
    }
    """
    compiler_.compile(input_text)


def example2(compiler_: CompilerPixelDraw):
    """This function is another example of how to use the PixelDraw compiler."""
    input_text = """
    size 15x15
    color #FFFF00
    rectangle 0 0 15 15
    color #FFA500
    rectangle 3 3 9 9
    color #FF0000
    point 7 7
    """
    compiler_.compile(input_text)


def example3(compiler_: CompilerPixelDraw):
    """This function draws a simple house using rectangles and points."""
    input_text = """
    size 20x20
    color #8B4513
    rectangle 0 0 20 20
    color #F4A460
    rectangle 1 1 18 18
    color #8B4513
    rectangle 8 10 4 8
    color #87CEEB
    rectangle 3 3 4 4
    rectangle 13 3 4 4
    color #8B4513
    rectangle 9 11 2 7
    color #FFD700
    point 10 12
    """
    compiler_.compile(input_text)


if __name__ == "__main__":
    compiler = CompilerPixelDraw()
    # example1(compiler)  # Run first example - RANDOM
    example2(compiler)  # Run second example - PATTERN
    #example3(compiler)  # Run third example - HOUSE
