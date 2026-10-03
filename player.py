# ============================================================
# PLAYER OPERATIONS
# ============================================================

from map_data import walls, COLS, ROWS


def move_player(
    player,
    dx,
    dy,
    keys
):

    nx = player[0] + dx
    ny = player[1] + dy

    # Boundary check
    if not (
        0 < nx < COLS - 1
        and
        0 < ny < ROWS - 1
    ):
        return player, keys, False

    # Wall check
    if (nx, ny) in walls:
        return player, keys, False

    new_player = (nx, ny)

    key_collected = False

    # Collect key
    if new_player in keys:

        keys.remove(new_player)

        key_collected = True

    return new_player, keys, key_collected