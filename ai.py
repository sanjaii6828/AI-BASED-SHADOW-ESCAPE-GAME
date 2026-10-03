# ============================================================
# AI POLICE
# ============================================================

import heapq

from settings import COLS, ROWS
from map_data import walls


# ============================================================
# A* SEARCH ALGORITHM
# ============================================================

def astar(start, goal):

    open_list = []

    heapq.heappush(
        open_list,
        (0, start)
    )

    came_from = {}

    cost = {
        start: 0
    }

    while open_list:

        _, current = heapq.heappop(open_list)

        # Goal reached
        if current == goal:

            path = []

            while current in came_from:

                path.append(current)
                current = came_from[current]

            path.reverse()

            return path

        x, y = current

        neighbors = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)
        ]

        for nx, ny in neighbors:

            if not (
                0 <= nx < COLS
                and
                0 <= ny < ROWS
            ):
                continue

            if (nx, ny) in walls:
                continue

            next_cell = (nx, ny)

            new_cost = cost[current] + 1

            if (
                next_cell not in cost
                or new_cost < cost[next_cell]
            ):

                cost[next_cell] = new_cost

                came_from[next_cell] = current

                h = (
                    abs(nx - goal[0])
                    +
                    abs(ny - goal[1])
                )

                priority = new_cost + h

                heapq.heappush(
                    open_list,
                    (priority, next_cell)
                )

    return []


# ============================================================
# MOVE AI POLICE
# ============================================================

def move_guards(guards, player):

    new_guards = []

    for guard in guards:

        path = astar(
            guard,
            player
        )

        if path:

            new_guards.append(
                path[0]
            )

        else:

            new_guards.append(
                guard
            )

    return new_guards