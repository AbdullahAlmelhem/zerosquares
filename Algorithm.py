from board import State
import numpy as nm
from collections import deque


def bfs(start_state):
    queue = deque([start_state])
    visited = {}
    state_count = 0

    while queue:
        current_state = queue.popleft()
        current_ = current_state.equall()

        if current_ in visited:
            continue

        visited[current_] = True
        state_count += 1

        if current_state.chekc_win(current_state):
            print(f"Total states visited: {state_count}")
            win_path = []
            while current_state:
                win_path.append(current_state)
                current_state = current_state.parent
            win_path.reverse()
            return win_path

        possible_states = current_state.nextstate(current_state)

        for next_state in possible_states:
            next_ = next_state.equall()
            if next_ not in visited:
                next_state.parent = current_state
                queue.append(next_state)

    print(f"Total states visited: {state_count}")
    return None


def dfs(start_state):
    stack = [start_state]
    visited = {}
    state_count = 0

    while stack:
        current_state = stack.pop()
        current_hash = current_state.equall()

        if current_hash in visited:
            continue

        visited[current_hash] = True
        state_count += 1

        if current_state.chekc_win(current_state):
            print(f"Total states visited: {state_count}")

            win_path = []
            while current_state is not None:
                win_path.append(current_state)
                current_state = current_state.parent
            win_path.reverse()
            return win_path

        possible_states = current_state.nextstate(current_state)

        for next_state in possible_states:
            next_ = next_state.equall()
            if next_ not in visited:
                next_state.parent = current_state
                stack.append(next_state)

    print(f"Total states visited: {state_count}")
    return None


def dfs_recursive(current_state, visited, state_count=0):

    current = current_state.equall()

    if current in visited:
        return None, state_count

    visited[current] = True
    state_count += 1

    if current_state.chekc_win(current_state):
        print(f"Total states visited: {state_count}")

        win_path = []
        while current_state is not None:
            win_path.append(current_state)
            current_state = current_state.parent
        win_path.reverse()
        return win_path, state_count

    possible_states = current_state.nextstate(current_state)
    for next in possible_states:
        next_ = next.equall()
        if next_ not in visited:
            next.parent = current_state
            result, state_count = dfs_recursive(next, visited, state_count)
            if result is not None:
                return result, state_count

    return None, state_count


from queue import PriorityQueue


def ucs(start_state):

    queue = PriorityQueue()
    queue.put((0, start_state))
    visited = {}
    state_count = 0

    while not queue.empty():
        current_cost, current_state = queue.get()
        current_ = current_state.equall()

        if current_ in visited:
            continue

        visited[current_] = True
        state_count += 1

        if current_state.chekc_win(current_state):
            print(f"Total states visited: {state_count}")
            win_path = []
            while current_state:
                win_path.append(current_state)
                current_state = current_state.parent
            win_path.reverse()
            return win_path

        possible_states = current_state.nextstate(current_state)

        for next_state in possible_states:
            next_ = next_state.equall()
            if next_ not in visited:

                next_state.cost = current_cost + 1
                next_state.parent = current_state
                queue.put((next_state.cost, next_state))

    print(f"Total states visited: {state_count}")
    return None
from queue import PriorityQueue
def heuristic(state):
        cost = 0
        for i in range(state.size):
            for j in range(state.size):
                cell = state.board[i][j]
                if cell["color"].startswith("goal_"):
                    goal_color = cell["color"][5:] 
                    for x in range(state.size):
                        for y in range(state.size):
                            piece = state.board[x][y]
                            if piece["color"] == goal_color:
                                
                                cost += abs(i - x) + abs(j - y)
        return cost
