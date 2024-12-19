from board import State
import numpy as nm
from collections import deque


def BFS(start_state):
    my_queue = deque([start_state])
    visited_set = set()

    while my_queue:
        print(len(visited_set))
        current = my_queue.popleft()
        if State.chekc_win(current):
            path = [current]
            while current.parent:
                path.append(current.parent)
                current = current.parent
            path.reverse()
            return {
                "path": path,
                "path_len": len(path),
                "visited_len": len(visited_set),
            }

        current_h = current.get_hash()
        if current_h not in visited_set:
            visited_set.add(current_h)
            for item in State.nextstate(current):
                if (
                    current.parent is None
                    or item.get_hash() != current.parent.get_hash()
                ):
                    item.parent = current
                    my_queue.append(item)

    return {
        "path": [],
        "path_len": 0,
        "visited_len": len(visited_set),
    }

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


####################################
def a_star(start_state):
    queue = PriorityQueue()
    queue.put((0, start_state))
    visited = {}
    state_count = 0

    while not queue.empty():
        _, current_state = queue.get()
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
            print(f"Number of maps in the solution path: {len(win_path)}")
            return win_path

        possible_states = current_state.nextstate(current_state)

        for next_state in possible_states:
            next_ = next_state.equall()
            if next_ not in visited:
                g_cost = current_state.cost + 1
                h_cost = heuristic(next_state)
                f_cost = g_cost + h_cost
                next_state.cost = g_cost
                next_state.parent = current_state
                queue.put((f_cost, next_state))

    print(f"Total states visited: {state_count}")
    return None


###################
def hill_climbing(start_state):
    current_state = start_state
    visited = {}
    state_count = 0

    while True:
        current_ = current_state.equall()
        
      
        if current_ in visited:
            break

        visited[current_] = True
        state_count += 1
        
    
        current_state.print_map()
        print(f"State #{state_count} visited.")
        
       
        if current_state.chekc_win(current_state):
            print(f"Total states visited: {state_count}")
            return [current_state]

      
        possible_states = current_state.nextstate(current_state)
        next_state = None

      
        for state in possible_states:
            h_cost = heuristic(state)
            if next_state is None or h_cost < heuristic(next_state):
                next_state = state

        
        if next_state and heuristic(next_state) < heuristic(current_state):
            next_state.parent = current_state
            current_state = next_state
        else:
            print(f"Total states visited: {state_count}")
            return None
