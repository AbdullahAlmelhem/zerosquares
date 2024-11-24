import numpy as nm
import copy
from collections import deque


class State:
    def __init__(self, size):
        self.size = size
        self.board = nm.full((size, size), fill_value="0", dtype="object")
        self.parent = None

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
    @classmethod
    def chekc_win(cls, state):
        for i in range(0, state.size):
            for j in range(0, state.size):
                if state.board[i][j]["color"] not in ["White", "Black"]:
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
    @classmethod
    def right(cls, current_state):
        next_state = copy.deepcopy(current_state)
        # if not hasattr(self, "last_board_state"):
        #     self.last_board_state = self.board

        # temp_board = copy.deepcopy(self.last_board_state)

        for i in range(next_state.size):
            moved = False

            j = next_state.size - 2
            while j >= 0:
                current_color = next_state.board[i][j]["color"]
                goal_color = f"goal_{current_color}"

                if (
                    j + 1 < next_state.size
                    and next_state.board[i][j + 1]["color"] == goal_color
                ):

                    next_state.board[i][j]["color"] = "White"
                    next_state.board[i][j]["shape"] = "⬜️"
                    next_state.board[i][j + 1]["color"] = "White"
                    next_state.board[i][j + 1]["shape"] = "⬜️"
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
                    while new_j + 1 < next_state.size and (
                        next_state.board[i][new_j + 1]["color"] == "White"
                        or (
                            next_state.board[i][new_j + 1]["color"].startswith("goal_")
                            and next_state.board[i][new_j + 1]["color"] != goal_color
                        )
                    ):
                        new_j += 1

                    if new_j != j:
                        next_state.board[i][new_j] = next_state.board[i][j]
                        next_state.board[i][j] = {
                            "i": i,
                            "j": j,
                            "color": "White",
                            "shape": "⬜️",
                        }
                        moved = True

                        if (
                            new_j + 1 < next_state.size
                            and next_state.board[i][new_j + 1]["color"] == goal_color
                        ):
                            next_state.board[i][new_j]["color"] = "White"
                            next_state.board[i][new_j]["shape"] = "⬜️"
                            next_state.board[i][new_j + 1]["color"] = "White"
                            next_state.board[i][new_j + 1]["shape"] = "⬜️"

                else:
                    moved = False

                j -= 1
        return next_state
        # next_state.last_board_state = next_state

        # for row in next_state:
        #     print("".join([cell["shape"] for cell in row]))

    #######################################################################################################################
    def equall(self):
        return hash(
            tuple(
                tuple((cell["color"], cell["shape"]) for cell in row)
                for row in self.board
            )
        )
    ####################################################################################################################
    @classmethod
    def left(cls, current_state):
        next_state = copy.deepcopy(current_state)

        for i in range(next_state.size):
            moved = False

            j = 1
            while j < next_state.size:
                current_color = next_state.board[i][j]["color"]
                goal_color = f"goal_{current_color}"

                if j - 1 >= 0 and next_state.board[i][j - 1]["color"] == goal_color:
                    next_state.board[i][j]["color"] = "White"
                    next_state.board[i][j]["shape"] = "⬜️"
                    next_state.board[i][j - 1]["color"] = "White"
                    next_state.board[i][j - 1]["shape"] = "⬜️"
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
                        next_state.board[i][new_j - 1]["color"] == "White"
                        or (
                            next_state.board[i][new_j - 1]["color"].startswith("goal_")
                            and next_state.board[i][new_j - 1]["color"] != goal_color
                        )
                    ):
                        new_j -= 1

                    if new_j != j:
                        next_state.board[i][new_j] = next_state.board[i][j]
                        next_state.board[i][j] = {
                            "i": i,
                            "j": j,
                            "color": "White",
                            "shape": "⬜️",
                        }
                        moved = True

                        if (
                            new_j - 1 >= 0
                            and next_state.board[i][new_j - 1]["color"] == goal_color
                        ):
                            next_state.board[i][new_j]["color"] = "White"
                            next_state.board[i][new_j]["shape"] = "⬜️"
                            next_state.board[i][new_j - 1]["color"] = "White"
                            next_state.board[i][new_j - 1]["shape"] = "⬜️"

                else:
                    moved = False

                j += 1

        return next_state

    ########################################################################################################################
    @classmethod
    def up(cls, current_state):
        next_state = copy.deepcopy(current_state)

        for j in range(next_state.size):
            moved = False

            i = 1
            while i < next_state.size:
                current_color = next_state.board[i][j]["color"]
                goal_color = f"goal_{current_color}"

                if i - 1 >= 0 and next_state.board[i - 1][j]["color"] == goal_color:
                    next_state.board[i][j]["color"] = "White"
                    next_state.board[i][j]["shape"] = "⬜️"
                    next_state.board[i - 1][j]["color"] = "White"
                    next_state.board[i - 1][j]["shape"] = "⬜️"
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
                        next_state.board[new_i - 1][j]["color"] == "White"
                        or (
                            next_state.board[new_i - 1][j]["color"].startswith("goal_")
                            and next_state.board[new_i - 1][j]["color"] != goal_color
                        )
                    ):
                        new_i -= 1

                    if new_i != i:
                        next_state.board[new_i][j] = next_state.board[i][j]
                        next_state.board[i][j] = {
                            "i": i,
                            "j": j,
                            "color": "White",
                            "shape": "⬜️",
                        }
                        moved = True

                        if (
                            new_i - 1 >= 0
                            and next_state.board[new_i - 1][j]["color"] == goal_color
                        ):
                            next_state.board[new_i][j]["color"] = "White"
                            next_state.board[new_i][j]["shape"] = "⬜️"
                            next_state.board[new_i - 1][j]["color"] = "White"
                            next_state.board[new_i - 1][j]["shape"] = "⬜️"
                    else:
                        i += 1

                else:
                    moved = False
                    i += 1
        return next_state

    ########################################################################################################################
    @classmethod
    def down(cls, current_state):
        next_state = copy.deepcopy(current_state)

        for j in range(next_state.size):
            moved = False

            i = next_state.size - 2
            while i >= 0:
                current_color = next_state.board[i][j]["color"]
                goal_color = f"goal_{current_color}"

                if (
                    i + 1 < next_state.size
                    and next_state.board[i + 1][j]["color"] == goal_color
                ):
                    next_state.board[i][j]["color"] = "White"
                    next_state.board[i][j]["shape"] = "⬜️"
                    next_state.board[i + 1][j]["color"] = "White"
                    next_state.board[i + 1][j]["shape"] = "⬜️"
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
                    while new_i + 1 < next_state.size and (
                        next_state.board[new_i + 1][j]["color"] == "White"
                        or (
                            next_state.board[new_i + 1][j]["color"].startswith("goal_")
                            and next_state.board[new_i + 1][j]["color"] != goal_color
                        )
                    ):
                        new_i += 1

                    if new_i != i:
                        next_state.board[new_i][j] = next_state.board[i][j]
                        next_state.board[i][j] = {
                            "i": i,
                            "j": j,
                            "color": "White",
                            "shape": "⬜️",
                        }
                        moved = True

                        if (
                            new_i + 1 < next_state.size
                            and next_state.board[new_i + 1][j]["color"] == goal_color
                        ):
                            next_state.board[new_i][j]["color"] = "White"
                            next_state.board[new_i][j]["shape"] = "⬜️"
                            next_state.board[new_i + 1][j]["color"] = "White"
                            next_state.board[new_i + 1][j]["shape"] = "⬜️"

                else:
                    moved = False

                i -= 1

        return next_state

    ########################################################################################################################
    def print_map(self):
        for row in self.board:
            print(
                "".join(
                    str(col["shape"]) if isinstance(col, dict) else col for col in row
                )
            )

    #############################################
    @classmethod
    def equal(cls, state1, state2):

        for i in range(state1.size):
            for j in range(state1.size):
                if state1.board[i][j]["color"] != state2.board[i][j]["color"]:
                    return False
        return True

    ###########################################################################################################################
    @classmethod
    def nextstate(cls, current_state):

        possible_states = []

        r = cls.right(current_state)
        if cls.equal(r, current_state) == False:
            possible_states = nm.append(possible_states, r)
        l = cls.left(current_state)
        if cls.equal(l, current_state) == False:
            possible_states = nm.append(possible_states, l)
        u = cls.up(current_state)
        if cls.equal(u, current_state) == False:
            possible_states = nm.append(possible_states, u)
        d = cls.down(current_state)
        if cls.equal(d, current_state) == False:
            possible_states = nm.append(possible_states, d)
        return possible_states

    ##############################################################3
