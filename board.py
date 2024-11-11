import numpy as nm
import copy


class State:
    def __init__(self, size):
        self.size = size
        self.board = nm.full((size, size), fill_value="0", dtype="object")

    #############################################
    def color(self, i, j, color, shape):

        self.board[i][j] = {
            "i": i,
            "j": j,
            "color": color,
            "shape": shape,
        }

    #############################################

    def row(self, row, col1, col2, color, shape):
        while col1 <= col2:
            self.board[row][col1] = {
                "i": row,
                "j": col1,
                "color": color,
                "shape": shape,
            }
            col1 += 1
        return

    #############################################

    def col(self, col, row1, row2, color, shape):
        while row1 <= row2:
            self.board[row1][col] = {
                "i": col,
                "j": row1,
                "color": color,
                "shape": shape,
            }
            row1 += 1

    #############################################

    def chekc_win(self):
        for row in self.last_board_state:
            for i in row:
                if i["color"] not in ["White", "Black"]:
                    return False

        print("win")
        return True

    #############################################

    def mobility_move_Right(self, i, j):
        if (
            self.board[i][j + 1]["color"] != "White"
            and "goal" not in self.board[i][j + 1]["color"]
        ):
            print("False")
        else:
            print("True")

    #############################################

    def mobility_move_left(self, i, j):
        if (
            self.board[i][j - 1]["color"] != "White"
            and "goal" not in self.board[i][j - 1]["color"]
        ):
            print("False")
        else:
            print("True")

    #############################################

    def mobility_move_up(self, i, j):
        if (
            self.board[i - 1][j]["color"] != "White"
            and "goal" not in self.board[i - 1][j]["color"]
        ):
            print("False")
        else:
            print("True")
        #############################################

    def mobility_move_down(self, i, j):
        if (
            self.board[i + 1][j]["color"] != "White"
            and "goal" not in self.board[i][j + 1]["color"]
        ):
            print("False")
        else:
            print("True")
            #######################################

    #######################################################################################################################

    def right(self):

        if not hasattr(self, "last_board_state"):
            self.last_board_state = self.board

        temp_board = copy.deepcopy(self.last_board_state)

        for i in range(self.size):
            moved = False

            j = self.size - 2
            while j >= 0:
                current_color = temp_board[i][j]["color"]
                goal_color = f"goal_{current_color}"

                if j + 1 < self.size and temp_board[i][j + 1]["color"] == goal_color:

                    temp_board[i][j]["color"] = "White"
                    temp_board[i][j]["shape"] = "⬜️"
                    temp_board[i][j + 1]["color"] = "White"
                    temp_board[i][j + 1]["shape"] = "⬜️"
                    moved = True

                    j -= 1
                    continue
                if (
                    current_color != "White"
                    and current_color != "Black"
                    and not current_color.startswith("goal_")
                ):
                    if moved:
                        moved = False
                        j -= 1
                        continue

                    new_j = j
                    while new_j + 1 < self.size and (
                        temp_board[i][new_j + 1]["color"] == "White"
                        or (
                            temp_board[i][new_j + 1]["color"].startswith("goal_")
                            and temp_board[i][new_j + 1]["color"] != goal_color
                        )
                    ):
                        new_j += 1

                    if new_j != j:
                        temp_board[i][new_j] = temp_board[i][j]
                        temp_board[i][j] = {
                            "i": i,
                            "j": j,
                            "color": "White",
                            "shape": "⬜️",
                        }
                        moved = True

                        if (
                            new_j + 1 < self.size
                            and temp_board[i][new_j + 1]["color"] == goal_color
                        ):
                            temp_board[i][new_j]["color"] = "White"
                            temp_board[i][new_j]["shape"] = "⬜️"
                            temp_board[i][new_j + 1]["color"] = "White"
                            temp_board[i][new_j + 1]["shape"] = "⬜️"

                else:
                    moved = False

                j -= 1

        self.last_board_state = temp_board

        for row in temp_board:
            print("".join([cell["shape"] for cell in row]))

    #######################################################################################################################

    def left(self):
        if not hasattr(self, "last_board_state"):
            self.last_board_state = self.board

        temp_board = copy.deepcopy(self.last_board_state)

        for i in range(self.size):
            moved = False

            j = 1
            while j < self.size:
                current_color = temp_board[i][j]["color"]
                goal_color = f"goal_{current_color}"

                if j - 1 >= 0 and temp_board[i][j - 1]["color"] == goal_color:
                    temp_board[i][j]["color"] = "White"
                    temp_board[i][j]["shape"] = "⬜️"
                    temp_board[i][j - 1]["color"] = "White"
                    temp_board[i][j - 1]["shape"] = "⬜️"
                    moved = True

                    j += 1
                    continue
                if (
                    current_color != "White"
                    and current_color != "Black"
                    and not current_color.startswith("goal_")
                ):
                    if moved:
                        moved = False
                        j += 1
                        continue

                    new_j = j
                    while new_j - 1 >= 0 and (
                        temp_board[i][new_j - 1]["color"] == "White"
                        or (
                            temp_board[i][new_j - 1]["color"].startswith("goal_")
                            and temp_board[i][new_j - 1]["color"] != goal_color
                        )
                    ):
                        new_j -= 1

                    if new_j != j:
                        temp_board[i][new_j] = temp_board[i][j]
                        temp_board[i][j] = {
                            "i": i,
                            "j": j,
                            "color": "White",
                            "shape": "⬜️",
                        }
                        moved = True

                        if (
                            new_j - 1 >= 0
                            and temp_board[i][new_j - 1]["color"] == goal_color
                        ):
                            temp_board[i][new_j]["color"] = "White"
                            temp_board[i][new_j]["shape"] = "⬜️"
                            temp_board[i][new_j - 1]["color"] = "White"
                            temp_board[i][new_j - 1]["shape"] = "⬜️"

                else:
                    moved = False

                j += 1

        self.last_board_state = temp_board

        for row in temp_board:
            print("".join([cell["shape"] for cell in row]))

    ########################################################################################################################

    def up(self):
        if not hasattr(self, "last_board_state"):
            self.last_board_state = self.board

        temp_board = copy.deepcopy(self.last_board_state)

        for j in range(self.size):
            moved = False

            i = 1
            while i < self.size:
                current_color = temp_board[i][j]["color"]
                goal_color = f"goal_{current_color}"

                if i - 1 >= 0 and temp_board[i - 1][j]["color"] == goal_color:
                    temp_board[i][j]["color"] = "White"
                    temp_board[i][j]["shape"] = "⬜️"
                    temp_board[i - 1][j]["color"] = "White"
                    temp_board[i - 1][j]["shape"] = "⬜️"
                    moved = True
                    i += 1
                    continue

                if (
                    current_color != "White"
                    and current_color != "Black"
                    and not current_color.startswith("goal_")
                ):
                    if moved:
                        moved = False
                        i += 1
                        continue

                    new_i = i
                    while new_i - 1 >= 0 and (
                        temp_board[new_i - 1][j]["color"] == "White"
                        or (
                            temp_board[new_i - 1][j]["color"].startswith("goal_")
                            and temp_board[new_i - 1][j]["color"] != goal_color
                        )
                    ):
                        new_i -= 1

                    if new_i != i:
                        temp_board[new_i][j] = temp_board[i][j]
                        temp_board[i][j] = {
                            "i": i,
                            "j": j,
                            "color": "White",
                            "shape": "⬜️",
                        }
                        moved = True

                        if (
                            new_i - 1 >= 0
                            and temp_board[new_i - 1][j]["color"] == goal_color
                        ):
                            temp_board[new_i][j]["color"] = "White"
                            temp_board[new_i][j]["shape"] = "⬜️"
                            temp_board[new_i - 1][j]["color"] = "White"
                            temp_board[new_i - 1][j]["shape"] = "⬜️"
                    else:
                        i += 1

                else:
                    moved = False
                    i += 1
        self.last_board_state = temp_board

        for row in temp_board:
            print("".join([cell["shape"] for cell in row]))

    ########################################################################################################################

    def down(self):
        if not hasattr(self, "last_board_state"):
            self.last_board_state = self.board

        temp_board = copy.deepcopy(self.last_board_state)

        for j in range(self.size):
            moved = False

            i = self.size - 2
            while i >= 0:
                current_color = temp_board[i][j]["color"]
                goal_color = f"goal_{current_color}"

                if i + 1 < self.size and temp_board[i + 1][j]["color"] == goal_color:
                    temp_board[i][j]["color"] = "White"
                    temp_board[i][j]["shape"] = "⬜️"
                    temp_board[i + 1][j]["color"] = "White"
                    temp_board[i + 1][j]["shape"] = "⬜️"
                    moved = True

                    i -= 1
                    continue

                if (
                    current_color != "White"
                    and current_color != "Black"
                    and not current_color.startswith("goal_")
                ):
                    if moved:
                        moved = False
                        i -= 1
                        continue

                    new_i = i
                    while new_i + 1 < self.size and (
                        temp_board[new_i + 1][j]["color"] == "White"
                        or (
                            temp_board[new_i + 1][j]["color"].startswith("goal_")
                            and temp_board[new_i + 1][j]["color"] != goal_color
                        )
                    ):
                        new_i += 1

                    if new_i != i:
                        temp_board[new_i][j] = temp_board[i][j]
                        temp_board[i][j] = {
                            "i": i,
                            "j": j,
                            "color": "White",
                            "shape": "⬜️",
                        }
                        moved = True

                        if (
                            new_i + 1 < self.size
                            and temp_board[new_i + 1][j]["color"] == goal_color
                        ):
                            temp_board[new_i][j]["color"] = "White"
                            temp_board[new_i][j]["shape"] = "⬜️"
                            temp_board[new_i + 1][j]["color"] = "White"
                            temp_board[new_i + 1][j]["shape"] = "⬜️"

                else:
                    moved = False

                i -= 1

        self.last_board_state = temp_board

        for row in temp_board:
            print("".join([cell["shape"] for cell in row]))

    ########################################################################################################################
    def print_map(self):
        for row in self.board:
            print(
                "".join(
                    str(col["shape"]) if isinstance(col, dict) else col for col in row
                )
            )

    #############################################

    def equal(self, board1, board2):

        for i in range(len(board1)):
            for j in range(len(board1[i])):
                if board1[i][j]["color"] != board2[i][j]["color"]:
                    return False
        return True

    ###########################################################################################################################

    def nextstate(self, board_input):

        possible_states = []

        original_board = copy.deepcopy(board_input)

        self.right()
        if not self.equal(original_board, self.board):
            possible_states.append(copy.deepcopy(self.board))

        self.board = copy.deepcopy(original_board)

        self.left()
        if not self.equal(original_board, self.board):
            possible_states.append(copy.deepcopy(self.board))

        self.board = copy.deepcopy(original_board)

        self.up()
        if not self.equal(original_board, self.board):
            possible_states.append(copy.deepcopy(self.board))

        self.board = copy.deepcopy(original_board)

        self.down()
        if not self.equal(original_board, self.board):

            possible_states.append(copy.deepcopy(self.board))

        self.board = copy.deepcopy(original_board)

        return possible_states

    ##############################################################3
    
    

    def nextstate(self, board_input):

        possible_states = []

        original_board = copy.deepcopy(board_input)

        self.right()
        if not self.equal(original_board, self.board):
            possible_states.append(copy.deepcopy(self.board))

        self.board = copy.deepcopy(original_board)

        self.left()
        if not self.equal(original_board, self.board):
            possible_states.append(copy.deepcopy(self.board))

        self.board = copy.deepcopy(original_board)

        self.up()
        if not self.equal(original_board, self.board):
            possible_states.append(copy.deepcopy(self.board))

        self.board = copy.deepcopy(original_board)

        self.down()
        if not self.equal(original_board, self.board):

            possible_states.append(copy.deepcopy(self.board))

        self.board = copy.deepcopy(original_board)

        return possible_states

    ##############################################################3


