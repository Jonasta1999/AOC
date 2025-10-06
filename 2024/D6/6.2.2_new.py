import re
from IPython.display import clear_output
import time
import numpy as np
from pathlib import Path

# Get the directory where this script lives
here = Path(__file__).parent


# Load data
with open(here / "input6.txt", "r") as file:
    data = file.read().splitlines()

# The direction we are facing
direction = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

# 90 degree turns
turn = {"^": ">", ">": "v", "v": "<", "<": "^"}


def find_pos(data):
    # Find starting position
    for i in range(len(data)):
        # Loop through and find our current location
        regex = re.search("\^|\>|v|\<", data[i])
        if regex:
            try:
                pos = (i, regex.start())
                return pos
            except:
                pass                
    return None


# Function to check if we are still within the map bounds
def is_in_map(data):
    res = False
    for i in range(len(data)):
        if "^" in data[i] or ">" in data[i] or "v" in data[i] or "<" in data[i]:
            res = True
    return res


# Function to replace our currenct position with the new one
def replace_and_move(data):
    n, m = len(data), len(data[0])
    for i in range(len(data)):
        # Loop through and find our current location
        regex = re.search("\^|\>|v|\<", data[i])
        try:
            # If we find current location
            if regex:
                pos = regex.start()
                type = regex.group()
                direc = direction[type]
                x_cord = i + direc[0]
                y_cord = pos + direc[1]

                # Replace current position with 'X' to track progress
                data[i] = data[i][:pos] + "X" + data[i][pos + 1 :]

                # If next step is out of bound then return data
                if not (n > i + direc[0] >= 0 and m > pos + direc[1] >= 0):
                    return data

                # If next step is an obstruction then turn 90 degrees
                if data[i + direc[0]][pos + direc[1]] == "#":
                    type = turn[type]  # direction type
                    direc = direction[type]  # actual direction
                    x_cord = i + direc[0]
                    y_cord = pos + direc[1]

                # Take the next step
                data[x_cord] = data[x_cord][:y_cord] + type + data[x_cord][y_cord + 1 :]
                return data
        except:
            pass
    return data


def is_loop(data):
    data_new = data.copy()
    # Find starting position
    start_pos = find_pos(data_new)

    while is_in_map(data_new):
        data_new = replace_and_move(data_new)
        new_pos = find_pos(data_new)
        # If we return to start position then we have looped
        if start_pos == new_pos:
            return True

    # If we dont find loop
    return False


def replace_with_block(data):
    n, m = len(data), len(data[0])
    new_data = data.copy()
    pos = find_pos(new_data)
    type = data[pos[0]][pos[1]]
    direc = direction[type]
    new_pos = (pos[0] + direc[0], pos[1] + direc[1])
    if (n > new_pos[0] >= 0 and m > new_pos[1] >= 0):
        new_data[new_pos[0]] = (
            new_data[new_pos[0]][: new_pos[1]]
            + "#"
            + new_data[new_pos[0]][new_pos[1] + 1 :]
        )
    return new_data


if __name__ == "__main__":
    data_new = data.copy()
    count = 0
    while is_in_map(data_new):
        #clear_output(wait=True)
        #time.sleep(0.5)
        temp_data = replace_with_block(data_new)
        print(is_loop(temp_data))
            #count += 1
        data_new = replace_and_move(data_new)
        #print(np.reshape(data_new, (10, 1)))
    #print(count)
    print("DONE")
