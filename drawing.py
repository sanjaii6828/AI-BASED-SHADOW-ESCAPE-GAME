# ============================================================
# DRAWING MODULE
# ============================================================

import math
import tkinter as tk

from settings import (
    CELL,
    COLS,
    ROWS,
    WIDTH,
    HEIGHT,
    BG,
    FLOOR,
    YELLOW,
    RED,
    GREEN,
    WHITE,
    BROWN
)

from map_data import (
    crates,
    cars,
    EXIT
)


# ============================================================
# FLOOR
# ============================================================

def draw_floor(canvas):

    canvas.create_rectangle(
        0,
        0,
        WIDTH,
        HEIGHT,
        fill=FLOOR,
        outline=""
    )

    for y in range(0, HEIGHT, CELL):

        offset = 0

        if (y // CELL) % 2 == 1:
            offset = CELL // 2

        for x in range(
            -CELL,
            WIDTH + CELL,
            CELL
        ):

            canvas.create_rectangle(
                x + offset,
                y,
                x + CELL + offset,
                y + CELL,
                outline="#45463D",
                width=1
            )


# ============================================================
# BORDER
# ============================================================

def draw_border(canvas):

    for x in range(0, WIDTH, CELL):

        for y in [4, HEIGHT - 27]:

            canvas.create_polygon(
                x + 3,
                y + 20,
                x + CELL // 2,
                y,
                x + CELL - 3,
                y + 20,
                fill="#202733",
                outline="#64717B"
            )

    for y in range(0, HEIGHT, CELL):

        for x in [4, WIDTH - 27]:

            canvas.create_polygon(
                x + 20,
                y + 3,
                x,
                y + CELL // 2,
                x + 20,
                y + CELL - 3,
                fill="#202733",
                outline="#64717B"
            )


# ============================================================
# CRATES
# ============================================================

def draw_crates(canvas):

    for x1, y1, x2, y2 in crates:

        x = x1 * CELL
        y = y1 * CELL

        width = (
            x2 - x1 + 1
        ) * CELL

        height = (
            y2 - y1 + 1
        ) * CELL

        canvas.create_rectangle(
            x + 6,
            y + 8,
            x + width + 6,
            y + height + 8,
            fill="#171717",
            outline=""
        )

        canvas.create_rectangle(
            x,
            y,
            x + width,
            y + height,
            fill=BROWN,
            outline="#735338",
            width=3
        )

        for i in range(
            1,
            x2 - x1 + 1
        ):

            xx = x + i * CELL

            canvas.create_line(
                xx,
                y + 5,
                xx,
                y + height - 5,
                fill="#352317",
                width=3
            )

        canvas.create_line(
            x + 5,
            y + height // 2,
            x + width - 5,
            y + height // 2,
            fill="#735338",
            width=4
        )


# ============================================================
# CARS
# ============================================================

def draw_cars(canvas):

    for x, y, w, h in cars:

        x1 = x * CELL
        y1 = y * CELL

        x2 = (x + w) * CELL
        y2 = (y + h) * CELL

        canvas.create_oval(
            x1 + 5,
            y1 + 10,
            x2 + 8,
            y2 + 15,
            fill="#202020",
            outline=""
        )

        canvas.create_rectangle(
            x1 + 8,
            y1 + 8,
            x2 - 8,
            y2 - 8,
            fill="#176B37",
            outline="#368A51",
            width=3
        )

        canvas.create_rectangle(
            x1 + 35,
            y1 + 12,
            x2 - 35,
            y2 - 12,
            fill="#17202B",
            outline="#34404D",
            width=3
        )

        for wx in [
            x1 + 12,
            x2 - 22
        ]:

            for wy in [
                y1 + 5,
                y2 - 14
            ]:

                canvas.create_rectangle(
                    wx,
                    wy,
                    wx + 12,
                    wy + 12,
                    fill="#090B10",
                    outline="#3C4148"
                )


# ============================================================
# EXIT
# ============================================================

def draw_exit(canvas):

    x, y = EXIT

    x1 = x * CELL
    y1 = y * CELL

    canvas.create_rectangle(
        x1 - 18,
        y1 - 18,
        x1 + 50,
        y1 + 50,
        fill="#1A202A",
        outline="#64717B",
        width=4
    )

    canvas.create_rectangle(
        x1 - 9,
        y1 - 9,
        x1 + 41,
        y1 + 41,
        fill="#657078",
        outline="#111820",
        width=4
    )

    canvas.create_text(
        x1 + 16,
        y1 + 16,
        text="EXIT",
        fill=WHITE,
        font=("Arial", 9, "bold")
    )


# ============================================================
# KEYS
# ============================================================

def draw_keys(canvas, keys):

    for x, y in keys:

        cx = x * CELL + CELL // 2
        cy = y * CELL + CELL // 2

        canvas.create_oval(
            cx - 9,
            cy - 9,
            cx + 9,
            cy + 9,
            outline=YELLOW,
            width=4
        )

        canvas.create_line(
            cx + 8,
            cy,
            cx + 18,
            cy,
            fill=YELLOW,
            width=4
        )

        canvas.create_line(
            cx + 14,
            cy,
            cx + 14,
            cy + 6,
            fill=YELLOW,
            width=3
        )


# ============================================================
# FLASHLIGHT
# ============================================================

def draw_flashlight(canvas, guard, player):

    gx, gy = guard

    px = gx * CELL + CELL // 2
    py = gy * CELL + CELL // 2

    dx = player[0] - gx
    dy = player[1] - gy

    distance = math.sqrt(
        dx * dx + dy * dy
    )

    if distance == 0:
        return

    dx /= distance
    dy /= distance

    perp_x = -dy
    perp_y = dx

    length = 190
    spread = 70

    tip_x = px + dx * length
    tip_y = py + dy * length

    p1 = (
        px + perp_x * 12,
        py + perp_y * 12
    )

    p2 = (
        tip_x + perp_x * spread,
        tip_y + perp_y * spread
    )

    p3 = (
        tip_x - perp_x * spread,
        tip_y - perp_y * spread
    )

    p4 = (
        px - perp_x * 12,
        py - perp_y * 12
    )

    canvas.create_polygon(
        p1,
        p2,
        p3,
        p4,
        fill="#665C1C",
        stipple="gray50",
        outline=""
    )


# ============================================================
# POLICE
# ============================================================

def draw_guard(canvas, guard, number):

    x, y = guard

    cx = x * CELL + CELL // 2
    cy = y * CELL + CELL // 2

    canvas.create_oval(
        cx - 14,
        cy - 6,
        cx + 14,
        cy + 12,
        fill="#171717",
        outline=""
    )

    canvas.create_oval(
        cx - 13,
        cy - 12,
        cx + 13,
        cy + 14,
        fill="#11151D",
        outline="#28313A",
        width=2
    )

    canvas.create_oval(
        cx - 10,
        cy - 16,
        cx + 10,
        cy + 3,
        fill="#171D27",
        outline="#343E49"
    )

    canvas.create_arc(
        cx - 12,
        cy - 20,
        cx + 12,
        cy - 3,
        start=0,
        extent=180,
        fill="#080B10",
        outline="#303944"
    )

    canvas.create_oval(
        cx + 8,
        cy + 4,
        cx + 14,
        cy + 10,
        fill=YELLOW,
        outline=""
    )

    canvas.create_text(
        cx,
        cy + 18,
        text=str(number),
        fill=WHITE,
        font=("Arial", 7, "bold")
    )


# ============================================================
# PLAYER
# ============================================================

def draw_player(canvas, player):

    x, y = player

    cx = x * CELL + CELL // 2
    cy = y * CELL + CELL // 2

    canvas.create_oval(
        cx - 13,
        cy - 7,
        cx + 13,
        cy + 12,
        fill="#171717",
        outline=""
    )

    canvas.create_oval(
        cx - 10,
        cy - 13,
        cx + 10,
        cy + 9,
        fill="#171D29",
        outline="#394554",
        width=2
    )

    canvas.create_oval(
        cx - 8,
        cy - 17,
        cx + 8,
        cy - 3,
        fill="#D1B18B",
        outline=""
    )

    canvas.create_arc(
        cx - 11,
        cy - 19,
        cx + 11,
        cy - 3,
        start=0,
        extent=180,
        fill="#090D16",
        outline=""
    )


# ============================================================
# COMPLETE GAME DRAW
# ============================================================

def draw_game(
    canvas,
    player,
    guards,
    keys
):

    canvas.delete("all")

    draw_floor(canvas)

    for guard in guards:

        draw_flashlight(
            canvas,
            guard,
            player
        )

    draw_crates(canvas)
    draw_cars(canvas)
    draw_exit(canvas)
    draw_keys(canvas, keys)

    for index, guard in enumerate(guards):

        draw_guard(
            canvas,
            guard,
            index + 1
        )

    draw_player(
        canvas,
        player
    )

    draw_border(canvas)