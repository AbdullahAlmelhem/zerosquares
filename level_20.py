from board import State
import Algorithm
import logging
import time
# import tracemalloc

logging.basicConfig(
    filename="level_10.log",
    level=logging.INFO,
    format="%(message)s",
)
logging.info("--------------------BFS--------------------")

b = State(5, 9)
b.row(1, 0, 3, "black", "⬛️")
b.row(0, 3, 6, "black", "⬛️")
b.row(1, 6, 8, "black", "⬛️")
b.row(4, 0, 8, "black", "⬛️")
b.row(3, 3, 3, "black", "⬛️")
b.row(3, 6, 6, "black", "⬛️")
b.col(1, 4, 0, "black", "⬛️")
b.col(1, 4, 8, "black", "⬛️")


b.color(3, 7, "yellow", "🟨")
b.color(1, 4, "red", "🟥")
b.color(2, 3, "blue", "🟦")
b.color(2, 2, "purple", "🟪")
b.color(3, 2, "green", "🟩")

b.color(3, 7, "goal_green", "🟢")

b.color([3, 2, "goal_purple", "🟣"])
b.color(2, 1, "goal_blue", "🔵")
b.color([2, 1, "goal_blue", "🔵"])
b.color(3, 4, "goal_red", "🔴")
b.color(3, 4, "goal_red", "🔴")
b.color(1, 5, "goal_yellow", "🟡")
b.color(1, 5, "goal_yellow", "🟡")


start_time = time.time()
b= Algorithm.BFS(b)
end_time = time.time()
path_length = b.get("path_len")
visited_length = b.get("visited_len")
cost = b.get("cost")
end_time = time.time()
logging.info(f"Path_length: {path_length}")
logging.info(f"Visited : {visited_length}")
logging.info(f"Cost: {cost}")
logging.info(f"Execution Time: {end_time - start_time:.4f} seconds")

logging.info("----------------------------------------")

logging.info("--------------------DFS--------------------")

b = State(8, 12)
b.row(0, 2, 9, "black", "⬛️")
b.row(7, 0, 11, "black", "⬛️")
b.row(1, 1, 2, "black", "⬛️")
b.row(2, 0, 1, "black", "⬛️")
b.row(1, 9, 10, "black", "⬛️")
b.row(2, 10, 11, "black", "⬛️")
b.col(2, 7, 0, "black", "⬛️")
b.col(2, 7, 11, "black", "⬛️")
b.col(5, 6, 4, "black", "⬛️")
b.col(4, 5, 5, "black", "⬛️")
b.col(3, 4, 8, "black", "⬛️")
b.col(4, 5, 9, "black", "⬛️")
b.col(2, 2, 4, "black", "⬛️")
b.col(3, 3, 3, "black", "⬛️")
b.col(5, 5, 2, "black", "⬛️")
b.col(2, 2, 7, "black", "⬛️")


b.color(5, 10, "blue", "🟦")
b.color(5, 1, "red", "🟥")
b.color(2, 6, "goal_blue", "🔵")
b.color(3, 5, "goal_red", "🔴")

start_time = time.time()
b = Algorithm.dfs(b)
end_time = time.time()
path_length = b.get("path_len")
visited_length = b.get("visited_len")
cost = b.get("cost")
end_time = time.time()
logging.info(f"Path_length: {path_length}")
logging.info(f"Visited: {visited_length}")
logging.info(f"Cost: {cost}")
logging.info(f"Execution Time: {end_time - start_time:.4f} seconds")

logging.info("----------------------------------------")

logging.info("--------------------dfs_recursive--------------------")

b = State(8, 12)
b.row(0, 2, 9, "black", "⬛️")
b.row(7, 0, 11, "black", "⬛️")
b.row(1, 1, 2, "black", "⬛️")
b.row(2, 0, 1, "black", "⬛️")
b.row(1, 9, 10, "black", "⬛️")
b.row(2, 10, 11, "black", "⬛️")
b.col(2, 7, 0, "black", "⬛️")
b.col(2, 7, 11, "black", "⬛️")
b.col(5, 6, 4, "black", "⬛️")
b.col(4, 5, 5, "black", "⬛️")
b.col(3, 4, 8, "black", "⬛️")
b.col(4, 5, 9, "black", "⬛️")
b.col(2, 2, 4, "black", "⬛️")
b.col(3, 3, 3, "black", "⬛️")
b.col(5, 5, 2, "black", "⬛️")
b.col(2, 2, 7, "black", "⬛️")


b.color(5, 10, "blue", "🟦")
b.color(5, 1, "red", "🟥")
b.color(2, 6, "goal_blue", "🔵")
b.color(3, 5, "goal_red", "🔴")


start_time = time.time()
b = Algorithm.dfs_recursive(b)
end_time = time.time()
path_length = b.get("path_len")
visited_length = b.get("visited_len")
cost = b.get("cost")
end_time = time.time()
logging.info(f"Path_length: {path_length}")
logging.info(f"Visited: {visited_length}")
logging.info(f"Cost: {cost}")
logging.info(f"Execution Time: {end_time - start_time:.4f} seconds")

logging.info("----------------------------------------")

logging.info("--------------------UCS--------------------")

b = State(8, 12)
b.row(0, 2, 9, "black", "⬛️")
b.row(7, 0, 11, "black", "⬛️")
b.row(1, 1, 2, "black", "⬛️")
b.row(2, 0, 1, "black", "⬛️")
b.row(1, 9, 10, "black", "⬛️")
b.row(2, 10, 11, "black", "⬛️")
b.col(2, 7, 0, "black", "⬛️")
b.col(2, 7, 11, "black", "⬛️")
b.col(5, 6, 4, "black", "⬛️")
b.col(4, 5, 5, "black", "⬛️")
b.col(3, 4, 8, "black", "⬛️")
b.col(4, 5, 9, "black", "⬛️")
b.col(2, 2, 4, "black", "⬛️")
b.col(3, 3, 3, "black", "⬛️")
b.col(5, 5, 2, "black", "⬛️")
b.col(2, 2, 7, "black", "⬛️")


b.color(5, 10, "blue", "🟦")
b.color(5, 1, "red", "🟥")
b.color(2, 6, "goal_blue", "🔵")
b.color(3, 5, "goal_red", "🔴")


start_time = time.time()
b = Algorithm.ucs(b)
end_time = time.time()
path_length = b.get("path_len")
visited_length = b.get("visited_len")
cost = b.get("cost")
end_time = time.time()
logging.info(f"Path_length: {path_length}")
logging.info(f"Visited: {visited_length}")
logging.info(f"Cost: {cost}")
logging.info(f"Execution Time: {end_time - start_time:.4f} seconds")

logging.info("----------------------------------------")
logging.info("--------------------A*--------------------")

b= State(8, 12)
b.row(0, 2, 9, "black", "⬛️")
b.row(7, 0, 11, "black", "⬛️")
b.row(1, 1, 2, "black", "⬛️")
b.row(2, 0, 1, "black", "⬛️")
b.row(1, 9, 10, "black", "⬛️")
b.row(2, 10, 11, "black", "⬛️")
b.col(2, 7, 0, "black", "⬛️")
b.col(2, 7, 11, "black", "⬛️")
b.col(5, 6, 4, "black", "⬛️")
b.col(4, 5, 5, "black", "⬛️")
b.col(3, 4, 8, "black", "⬛️")
b.col(4, 5, 9, "black", "⬛️")
b.col(2, 2, 4, "black", "⬛️")
b.col(3, 3, 3, "black", "⬛️")
b.col(5, 5, 2, "black", "⬛️")
b.col(2, 2, 7, "black", "⬛️")


b.color(5, 10, "blue", "🟦")
b.color(5, 1, "red", "🟥")
b.color(2, 6, "goal_blue", "🔵")
b.color(3, 5, "goal_red", "🔴")


start_time = time.time()
b = Algorithm.a_star(b)
end_time = time.time()
path_length = b.get("path_len")
visited_length = b.get("visited_len")
cost = b.get("cost")
end_time = time.time()
logging.info(f"Path_length: {path_length}")
logging.info(f"Visited: {visited_length}")
logging.info(f"Cost: {cost}")
logging.info(f"Execution Time: {end_time - start_time:.4f} seconds")

logging.info("----------------------------------------")

logging.info("--------------------steepest_hill_climbing--------------------")

b = State(8, 12)
b.row(0, 2, 9, "black", "⬛️")
b.row(7, 0, 11, "black", "⬛️")
b.row(1, 1, 2, "black", "⬛️")
b.row(2, 0, 1, "black", "⬛️")
b.row(1, 9, 10, "black", "⬛️")
b.row(2, 10, 11, "black", "⬛️")
b.col(2, 7, 0, "black", "⬛️")
b.col(2, 7, 11, "black", "⬛️")
b.col(5, 6, 4, "black", "⬛️")
b.col(4, 5, 5, "black", "⬛️")
b.col(3, 4, 8, "black", "⬛️")
b.col(4, 5, 9, "black", "⬛️")
b.col(2, 2, 4, "black", "⬛️")
b.col(3, 3, 3, "black", "⬛️")
b.col(5, 5, 2, "black", "⬛️")
b.col(2, 2, 7, "black", "⬛️")


b.color(5, 10, "blue", "🟦")
b.color(5, 1, "red", "🟥")
b.color(2, 6, "goal_blue", "🔵")
b.color(3, 5, "goal_red", "🔴")


start_time = time.time()
b= Algorithm.hill_climbing(b)
end_time = time.time()
path_length = b.get("path_len")
visited_length = b.get("visited_len")
cost = b.get("cost")
end_time = time.time()
logging.info(f"Path_length: {path_length}")
logging.info(f"Visited: {visited_length}")
logging.info(f"Cost: {cost}")
logging.info(f"Execution Time: {end_time - start_time:.4f} seconds")

logging.info("----------------------------------------")

