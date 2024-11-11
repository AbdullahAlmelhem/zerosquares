from board import State


def play():
    while True:

        print("move Right : R")
        print("move Left : L ")
        print("move Up : Up")
        print("move down : D")

        user_input = input("Enter R or U or L or D ").lower()

        if user_input == "r":
            State.right()

        elif user_input == "l":
            State.left()

        elif user_input == "u":
            State.up()

        elif user_input == "d":
            State.down()

        else:
            print("Error")
            continue

        if State.chekc_win():
            break


a = State(7)
a.row(0, 0, 6, "White", "⬜️")
a.row(1, 0, 6, "White", "⬜️")
a.row(2, 0, 6, "White", "⬜️")
a.row(3, 0, 6, "White", "⬜️")
a.row(4, 0, 6, "White", "⬜️")
a.row(5, 0, 6, "White", "⬜️")
a.row(6, 0, 6, "White", "⬜️")
a.col(0, 0, 6, "White", "⬜️")
a.col(0, 0, 6, "White", "⬜️")
a.color(4, 4, "Black", "⬛️")
a.color(3, 1, "Blue", "🟦")
a.color(0, 0, "Red", "🟥")
# 🟦🔴🟥🔵

a.color(3, 6, "goal_Blue", "🔵")
# b = State(7)
# b.row(0, 0, 6, "White", "⬜️")
# b.row(1, 0, 6, "White", "⬜️")
# b.row(2, 0, 6, "White", "⬜️")
# b.row(3, 0, 6, "White", "⬜️")
# b.row(4, 0, 6, "White", "⬜️")
# b.row(5, 0, 6, "White", "⬜️")
# b.row(6, 0, 6, "White", "⬜️")
# b.col(0, 0, 6, "White", "⬜️")
# b.color(4, 3, "Black", "⬛️")


a.print_map()
# print("*" * 20)
# # # print("*" * 20)
# # # b.print_map()
# # # print(State.equal(a, b))
# # a.right()
# # print("*" * 20)

# # print("*" * 20)
# # a.left()
# # print("*" * 20)
# # a.print_map()
# # print("*" * 20)
# a.right()
# a.left()
# print("*" * 20)
# a.print_map()
# a.play()
# board_input = a.board
# possible_states = a.nextstate(board_input)
a.up()
a.print_map()
a.play()
a.up()
