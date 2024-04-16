"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 80
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000

def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.
    """
    # Calculate the space between the lines
    space_between_lines = (width - 2 * GRAPH_MARGIN_SIZE) / (len(YEARS) - 1)
    
    # Calculate the x coordinate
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * space_between_lines
    return int(x_coordinate)


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.
    """
    # Clear the canvas
    canvas.delete('all')

    # Draw the top horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)

    # Draw the bottom horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)

    # Draw the vertical lines for each year and the year labels
    for i, year in enumerate(YEARS):
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_coordinate, 0, x_coordinate, CANVAS_HEIGHT,
                           width=LINE_WIDTH)
        canvas.create_text(x_coordinate + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=str(year), anchor=tkinter.NW)




def draw_names(canvas, name_data, lookup_names):
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # Get the width between each year's line on the canvas
    space_between_lines = (CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE) / (len(YEARS) - 1)

    for i, name in enumerate(lookup_names):
        color = COLORS[i % len(COLORS)]  # Cycle through the COLORS list
        for j in range(len(YEARS)):
            year = str(YEARS[j])
            # Calculate the x coordinate for this year
            x_coordinate = GRAPH_MARGIN_SIZE + j * space_between_lines

            # Determine the y coordinate based on the rank
            if year in name_data[name]:
                rank = name_data[name][year]
                if rank.isnumeric() and int(rank) <= MAX_RANK:
                    y_coordinate = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * (int(rank) / MAX_RANK)
                else:
                    y_coordinate = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    rank = "*"
            else:
                # If no rank data, set y coordinate to bottom and rank to '*'
                y_coordinate = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                rank = "*"

            # Draw the name and rank text
            canvas.create_text(x_coordinate + TEXT_DX, y_coordinate - TEXT_DX,
                               text=f"{name} {rank}", anchor=tkinter.NE, fill=color)

            # Draw the line connecting this point to the next, if it exists
            if j < len(YEARS) - 1:
                next_year = str(YEARS[j+1])
                if next_year in name_data[name]:
                    next_rank = name_data[name][next_year]
                    if next_rank.isnumeric() and int(next_rank) <= MAX_RANK:
                        next_y_coordinate = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * (int(next_rank) / MAX_RANK)
                    else:
                        next_y_coordinate = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                else:
                    next_y_coordinate = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

                next_x_coordinate = GRAPH_MARGIN_SIZE + (j + 1) * space_between_lines
                # Draw the line
                canvas.create_line(x_coordinate, y_coordinate,
                                   next_x_coordinate, next_y_coordinate,
                                   width=LINE_WIDTH, fill=color)



# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
