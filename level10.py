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

a = State(8, 12)
a.row(0, 2, 9, "black", "⬛️")
a.row(7, 0, 11, "black", "⬛️")
a.row(1, 1, 2, "black", "⬛️")
a.row(2, 0, 1, "black", "⬛️")
a.row(1, 9, 10, "black", "⬛️")
a.row(2, 10, 11, "black", "⬛️")
a.col(2, 7, 0, "black", "⬛️")
a.col(2, 7, 11, "black", "⬛️")
a.col(5, 6, 4, "black", "⬛️")
a.col(4, 5, 5, "black", "⬛️")
a.col(3, 4, 8, "black", "⬛️")
a.col(4, 5, 9, "black", "⬛️")
a.col(2, 2, 4, "black", "⬛️")
a.col(3, 3, 3, "black", "⬛️")
a.col(5, 5, 2, "black", "⬛️")
a.col(2, 2, 7, "black", "⬛️")


a.color(5, 10, "blue", "🟦")
a.color(5, 1, "red", "🟥")
a.color(2, 6, "goal_blue", "🔵")
a.color(3, 5, "goal_red", "🔴")

start_time = time.time()
a = Algorithm.BFS(a)
end_time = time.time()
path_length = a.get("path_len")
visited_length = a.get("visited_len")
cost = a.get("cost")
end_time = time.time()
logging.info(f"Path_length: {path_length}")
logging.info(f"Visited : {visited_length}")
logging.info(f"Cost: {cost}")
logging.info(f"Execution Time: {end_time - start_time:.4f} seconds")

logging.info("----------------------------------------")

logging.info("--------------------DFS--------------------")

a = State(8, 12)
a.row(0, 2, 9, "black", "⬛️")
a.row(7, 0, 11, "black", "⬛️")
a.row(1, 1, 2, "black", "⬛️")
a.row(2, 0, 1, "black", "⬛️")
a.row(1, 9, 10, "black", "⬛️")
a.row(2, 10, 11, "black", "⬛️")
a.col(2, 7, 0, "black", "⬛️")
a.col(2, 7, 11, "black", "⬛️")
a.col(5, 6, 4, "black", "⬛️")
a.col(4, 5, 5, "black", "⬛️")
a.col(3, 4, 8, "black", "⬛️")
a.col(4, 5, 9, "black", "⬛️")
a.col(2, 2, 4, "black", "⬛️")
a.col(3, 3, 3, "black", "⬛️")
a.col(5, 5, 2, "black", "⬛️")
a.col(2, 2, 7, "black", "⬛️")


a.color(5, 10, "blue", "🟦")
a.color(5, 1, "red", "🟥")
a.color(2, 6, "goal_blue", "🔵")
a.color(3, 5, "goal_red", "🔴")

start_time = time.time()
a = Algorithm.dfs(a)
end_time = time.time()
path_length = a.get("path_len")
visited_length = a.get("visited_len")
cost = a.get("cost")
end_time = time.time()
logging.info(f"Path_length: {path_length}")
logging.info(f"Visited: {visited_length}")
logging.info(f"Cost: {cost}")
logging.info(f"Execution Time: {end_time - start_time:.4f} seconds")

logging.info("----------------------------------------")

logging.info("--------------------dfs_recursive--------------------")

a = State(8, 12)
a.row(0, 2, 9, "black", "⬛️")
a.row(7, 0, 11, "black", "⬛️")
a.row(1, 1, 2, "black", "⬛️")
a.row(2, 0, 1, "black", "⬛️")
a.row(1, 9, 10, "black", "⬛️")
a.row(2, 10, 11, "black", "⬛️")
a.col(2, 7, 0, "black", "⬛️")
a.col(2, 7, 11, "black", "⬛️")
a.col(5, 6, 4, "black", "⬛️")
a.col(4, 5, 5, "black", "⬛️")
a.col(3, 4, 8, "black", "⬛️")
a.col(4, 5, 9, "black", "⬛️")
a.col(2, 2, 4, "black", "⬛️")
a.col(3, 3, 3, "black", "⬛️")
a.col(5, 5, 2, "black", "⬛️")
a.col(2, 2, 7, "black", "⬛️")


a.color(5, 10, "blue", "🟦")
a.color(5, 1, "red", "🟥")
a.color(2, 6, "goal_blue", "🔵")
a.color(3, 5, "goal_red", "🔴")


start_time = time.time()
a = Algorithm.dfs_recursive(a)
end_time = time.time()
path_length = a.get("path_len")
visited_length = a.get("visited_len")
cost = a.get("cost")
end_time = time.time()
logging.info(f"Path_length: {path_length}")
logging.info(f"Visited: {visited_length}")
logging.info(f"Cost: {cost}")
logging.info(f"Execution Time: {end_time - start_time:.4f} seconds")

logging.info("----------------------------------------")

logging.info("--------------------UCS--------------------")

a = State(8, 12)
a.row(0, 2, 9, "black", "⬛️")
a.row(7, 0, 11, "black", "⬛️")
a.row(1, 1, 2, "black", "⬛️")
a.row(2, 0, 1, "black", "⬛️")
a.row(1, 9, 10, "black", "⬛️")
a.row(2, 10, 11, "black", "⬛️")
a.col(2, 7, 0, "black", "⬛️")
a.col(2, 7, 11, "black", "⬛️")
a.col(5, 6, 4, "black", "⬛️")
a.col(4, 5, 5, "black", "⬛️")
a.col(3, 4, 8, "black", "⬛️")
a.col(4, 5, 9, "black", "⬛️")
a.col(2, 2, 4, "black", "⬛️")
a.col(3, 3, 3, "black", "⬛️")
a.col(5, 5, 2, "black", "⬛️")
a.col(2, 2, 7, "black", "⬛️")


a.color(5, 10, "blue", "🟦")
a.color(5, 1, "red", "🟥")
a.color(2, 6, "goal_blue", "🔵")
a.color(3, 5, "goal_red", "🔴")


start_time = time.time()
a = Algorithm.ucs(a)
end_time = time.time()
path_length = a.get("path_len")
visited_length = a.get("visited_len")
cost = a.get("cost")
end_time = time.time()
logging.info(f"Path_length: {path_length}")
logging.info(f"Visited: {visited_length}")
logging.info(f"Cost: {cost}")
logging.info(f"Execution Time: {end_time - start_time:.4f} seconds")

logging.info("----------------------------------------")
logging.info("--------------------A*--------------------")

a = State(8, 12)
a.row(0, 2, 9, "black", "⬛️")
a.row(7, 0, 11, "black", "⬛️")
a.row(1, 1, 2, "black", "⬛️")
a.row(2, 0, 1, "black", "⬛️")
a.row(1, 9, 10, "black", "⬛️")
a.row(2, 10, 11, "black", "⬛️")
a.col(2, 7, 0, "black", "⬛️")
a.col(2, 7, 11, "black", "⬛️")
a.col(5, 6, 4, "black", "⬛️")
a.col(4, 5, 5, "black", "⬛️")
a.col(3, 4, 8, "black", "⬛️")
a.col(4, 5, 9, "black", "⬛️")
a.col(2, 2, 4, "black", "⬛️")
a.col(3, 3, 3, "black", "⬛️")
a.col(5, 5, 2, "black", "⬛️")
a.col(2, 2, 7, "black", "⬛️")


a.color(5, 10, "blue", "🟦")
a.color(5, 1, "red", "🟥")
a.color(2, 6, "goal_blue", "🔵")
a.color(3, 5, "goal_red", "🔴")


start_time = time.time()
a = Algorithm.a_star(a)
end_time = time.time()
path_length = a.get("path_len")
visited_length = a.get("visited_len")
cost = a.get("cost")
end_time = time.time()
logging.info(f"Path_length: {path_length}")
logging.info(f"Visited: {visited_length}")
logging.info(f"Cost: {cost}")
logging.info(f"Execution Time: {end_time - start_time:.4f} seconds")

logging.info("----------------------------------------")

logging.info("--------------------steepest_hill_climbing--------------------")

a = State(8, 12)
a.row(0, 2, 9, "black", "⬛️")
a.row(7, 0, 11, "black", "⬛️")
a.row(1, 1, 2, "black", "⬛️")
a.row(2, 0, 1, "black", "⬛️")
a.row(1, 9, 10, "black", "⬛️")
a.row(2, 10, 11, "black", "⬛️")
a.col(2, 7, 0, "black", "⬛️")
a.col(2, 7, 11, "black", "⬛️")
a.col(5, 6, 4, "black", "⬛️")
a.col(4, 5, 5, "black", "⬛️")
a.col(3, 4, 8, "black", "⬛️")
a.col(4, 5, 9, "black", "⬛️")
a.col(2, 2, 4, "black", "⬛️")
a.col(3, 3, 3, "black", "⬛️")
a.col(5, 5, 2, "black", "⬛️")
a.col(2, 2, 7, "black", "⬛️")


a.color(5, 10, "blue", "🟦")
a.color(5, 1, "red", "🟥")
a.color(2, 6, "goal_blue", "🔵")
a.color(3, 5, "goal_red", "🔴")


start_time = time.time()
a = Algorithm.hill_climbing(a)
end_time = time.time()
path_length = a.get("path_len")
visited_length = a.get("visited_len")
cost = a.get("cost")
end_time = time.time()
logging.info(f"Path_length: {path_length}")
logging.info(f"Visited: {visited_length}")
logging.info(f"Cost: {cost}")
logging.info(f"Execution Time: {end_time - start_time:.4f} seconds")

logging.info("----------------------------------------")

