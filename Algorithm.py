from board import State
import numpy as nm
from collections import deque


def bfs(start_state):
    queue = deque([start_state])
    visited = {}
    state_count = 0

    while queue:
        current_state = queue.popleft()
        current_hash = current_state.equall()

        if current_hash in visited:
            continue

        visited[current_hash] = True
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
            next_hash = next_state.equall()
            if next_hash not in visited:
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
            next_hash = next_state.equall()
            if next_hash not in visited:
                next_state.parent = current_state
                stack.append(next_state)

    print(f"Total states visited: {state_count}")
    return None
