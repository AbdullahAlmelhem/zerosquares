from board import State
import Algorithm


def play(state):
    while True:
        print("move Right : R")
        print("move Left : L ")
        print("move Up : Up")
        print("move down : D")

        user_input = input("Enter R or U or L or D ").lower()

        if user_input == "r":
            state = State.right(state)  

        elif user_input == "l":
            state = State.left(state)  

        elif user_input == "u":
            state = State.up(state)  

        elif user_input == "d":
            state = State.down(state)  
    
        else:
            print("Error")
            continue

        
        state.print_map()

        
        if state.chekc_win(state):
            print(" won!")
            break
a=State(11)
for row in range(0,11):
    for col in range(0,11):
        a.board[row][col]={
                "i": row,
                "j": col,
                "color": "White",
                "shape": "⬜️",
            }
a.row(0,1,5,"Black","⬛️")
a.row(1,0,1,"Black","⬛️")
a.row(1,5,9,"Black","⬛️")
a.row(2,5,6,"Black","⬛️")
a.col(0,1,6,"Black","⬛️")
a.col(1,6,7,"Black","⬛️")
a.col(9,1,3,"Black","⬛️")
a.col(10,3,5,"Black","⬛️")
a.col(9,5,6,"Black","⬛️")
a.row(6,4,9,"Black","⬛️")
a.row(7,1,4,"Black","⬛️")
a.row(4,4,6,"Black","⬛️")
a.color(1, 2, "Red", "🟥")
a.color(6, 2, "Blue", "🟦")
a.color(2,7, "goal_Blue", "🔵")
a.color(4, 9, "goal_Red", "🔴")
# a = State(7)
# a.row(0, 0, 6, "White", "⬜️")
# a.row(1, 0, 6, "White", "⬜️")
# a.row(2, 0, 6, "White", "⬜️")
# a.row(3, 0, 6, "White", "⬜️")
# a.row(4, 0, 6, "White", "⬜️")
# a.row(5, 0, 6, "White", "⬜️")
# a.row(6, 0, 6, "White", "⬜️")
# a.col(0, 0, 6, "White", "⬜️")
# a.col(0, 0, 6, "White", "⬜️")
# a.color(3, 3, "Black", "⬛️")
# a.color(5, 2, "Blue", "🟦")
# a.color(1, 2, "Red", "🟥")
# # 🟦🔴🟥🔵
# a.row(0, 2, 6, "Black", "⬛️")
# a.color(3, 5, "goal_Red", "🔴")
# a.color(1,5, "goal_Bl", "🔵")
# a.col(0,2,5,"Black","⬛️")
# a.color(2, 1, "Black", "⬛️")
# a.color(1, 1, "Black", "⬛️")
# a.color(0, 1, "Black", "⬛️")
# a.color(1, 0, "Black", "⬛️")
# a.color(1, 4, "Black", "⬛️")
# a.color(6, 1, "Black", "⬛️")
# a.row(6, 1,6, "Black", "⬛️")
# a.col(6, 1,6, "Black", "⬛️")
# a.color(5, 4, "Black", "⬛️")
# a.color(5, 1, "Black", "⬛️")
###################طباعة الرقعة الاساسية#####
a.print_map()
# c = State.right(a)
# c.print_map()

# print("*" * 20)
# b = State.up(c)
# b.print_map()

# print("*" * 50)
##############################################

# ################تابع ال next state ###########
# print("#"*20)
# b = State.nextstate(a)
# for item in b:
#     item.print_map()
#     print("*" * 50)

# #####################تابع ال equal##########

# print(State.equal(a, a))
# print("*" * 50)

# #####################تابع ال down   ###########

# b = State.down(a)
# b.print_map()

# print("*" * 50)

# ########################تابع ال up  ###########

# b = State.up(a)
# b.print_map()

# print("*" * 50)

# ################تابع ال left   #################
# c = State.left(b)
# c.print_map()
# print("*" * 50)
# ################تابع ال right   ################
# c = State.right(b)
# c.print_map()

# print("*" * 20)
# ###################تابع ال play ###########################

# # play(a)


################   BFS  ######################
solution_path = Algorithm.bfs(a)


if solution_path:
    print("Solution found!")
    for step in solution_path:
        for row in step.board:
            print("".join(cell["shape"] for cell in row))
        print("\n")
else:
    print("No solution found!")

    


# # ################   DFS ##################
# solution_path = Algorithm.dfs(a)


# if solution_path:
#     print("Solution found!")
#     for step in solution_path:
#         for row in step.board:
#             print("".join(cell["shape"] for cell in row))
#         print("\n")
# else:
#     print("No solution found!")
# # ###################dfs_recursive#######################
# visited = {} 
# solution_path, state_count = Algorithm.dfs_recursive(a, visited)

# if solution_path:
#     print("Solution found!")
#     for step in solution_path:
#         for row in step.board:
#             print("".join(cell["shape"] for cell in row))
#         print("\n")
# else:
#     print("No solution found!")
# #################### ucs #######################
# solution_path = Algorithm.ucs(a)


# if solution_path:
#     print("Solution found!")
#     for step in solution_path:
#         for row in step.board:
#             print("".join(cell["shape"] for cell in row))
#         print("\n")
# else:
#     print("No solution found!")

    
