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
a.color(3, 0, "Blue", "🟦")
a.color(6, 6, "Red", "🟥")
# 🟦🔴🟥🔵

a.color(0, 3, "goal_Red", "🔴")
a.color(3, 1, "goal_Blue", "🔵")


###################طباعة الرقعة الاساسية#####
a.print_map()

##############################################


################تابع ال next state ###########
print("#"*20)
b = State.nextstate(a)
for item in b:
    item.print_map()
    print("*" * 50)

#####################تابع ال equal##########

print(State.equal(a, a))
print("*" * 50)

#####################تابع ال down   ###########

b = State.down(a)
b.print_map()

print("*" * 50)

########################تابع ال up  ###########

b = State.up(a)
b.print_map()

print("*" * 50)

################تابع ال left   #################
c = State.left(b)
c.print_map()
print("*" * 50)
################تابع ال right   ################
c = State.right(b)
c.print_map()

print("*" * 20)
###################تابع ال play ###########################

# play(a)


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

    


# ################   DFS ##################
solution_path = Algorithm.dfs(a)


if solution_path:
    print("Solution found!")
    for step in solution_path:
        for row in step.board:
            print("".join(cell["shape"] for cell in row))
        print("\n")
else:
    print("No solution found!")
# ###################dfs_recursive#######################
visited = {} 
solution_path, state_count = Algorithm.dfs_recursive(a, visited)

if solution_path:
    print("Solution found!")
    for step in solution_path:
        for row in step.board:
            print("".join(cell["shape"] for cell in row))
        print("\n")
else:
    print("No solution found!")
#################### ucs #######################
solution_path = Algorithm.ucs(a)


if solution_path:
    print("Solution found!")
    for step in solution_path:
        for row in step.board:
            print("".join(cell["shape"] for cell in row))
        print("\n")
else:
    print("No solution found!")

    
