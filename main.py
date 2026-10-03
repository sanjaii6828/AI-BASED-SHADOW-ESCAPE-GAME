# ============================================================
# SHADOW ESCAPE
# AI AGENT BASED STEALTH GAME
# ============================================================

import tkinter as tk

from settings import (
    WIDTH,
    HEIGHT,
    BG,
    FLOOR,
    YELLOW,
    RED,
    GREEN,
    WHITE
)

from map_data import (
    START_PLAYER,
    START_GUARDS,
    START_KEYS
)

from ai import move_guards
from player import move_player
from game_logic import check_game
from drawing import draw_game


# ============================================================
# GAME VARIABLES
# ============================================================

player = START_PLAYER
guards = START_GUARDS.copy()
keys = START_KEYS.copy()

collected = 0
moves = 0

game_over = False
game_result = ""

ai_job = None

result_restart_button = None
result_exit_button = None


# ============================================================
# TKINTER WINDOW
# ============================================================

root = tk.Tk()

root.title(
    "SHADOW ESCAPE - AI Police Pursuit"
)

root.configure(
    bg=BG
)

root.resizable(
    False,
    False
)


# ============================================================
# TITLE
# ============================================================

title = tk.Label(
    root,
    text="SHADOW ESCAPE",
    font=("Arial", 24, "bold"),
    bg=BG,
    fg=YELLOW
)

title.pack(
    pady=(10, 2)
)


subtitle = tk.Label(
    root,
    text="ESCAPE THE AI POLICE BEFORE THEY CATCH YOU",
    font=("Arial", 10, "bold"),
    bg=BG,
    fg=WHITE
)

subtitle.pack(
    pady=(0, 8)
)


# ============================================================
# GAME CANVAS
# ============================================================

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg=FLOOR,
    highlightthickness=0
)

canvas.pack(
    padx=12,
    pady=5
)


# ============================================================
# STATUS BAR
# ============================================================

status = tk.Label(
    root,
    text="POLICE: 7    KEYS: 0/5    MOVES: 0",
    font=("Arial", 14, "bold"),
    bg=BG,
    fg=YELLOW
)

status.pack(
    pady=5
)


# ============================================================
# UPDATE STATUS
# ============================================================

def update_status():

    if game_over:
        return

    status.config(
        text=(
            f"POLICE: {len(guards)}    "
            f"KEYS: {collected}/5    "
            f"MOVES: {moves}"
        ),
        fg=YELLOW
    )


# ============================================================
# STOP AI TIMER
# ============================================================

def stop_ai_timer():

    global ai_job

    if ai_job is not None:

        try:
            root.after_cancel(ai_job)

        except tk.TclError:
            pass

        ai_job = None


# ============================================================
# REMOVE RESULT BUTTONS
# ============================================================

def remove_result_buttons():

    global result_restart_button
    global result_exit_button

    if result_restart_button is not None:

        try:
            canvas.delete(
                result_restart_button
            )
        except:
            pass

        result_restart_button = None


    if result_exit_button is not None:

        try:
            canvas.delete(
                result_exit_button
            )
        except:
            pass

        result_exit_button = None


# ============================================================
# SHOW RESULT SCREEN
# ============================================================

def show_result_screen():

    global result_restart_button
    global result_exit_button

    # Remove old buttons
    remove_result_buttons()

    # --------------------------------------------------------
    # DARK OVERLAY
    # --------------------------------------------------------

    canvas.create_rectangle(
        0,
        0,
        WIDTH,
        HEIGHT,
        fill="#000000",
        stipple="gray50",
        outline=""
    )


    # --------------------------------------------------------
    # RESULT
    # --------------------------------------------------------

    if game_result == "WIN":

        result_title = "MISSION COMPLETED!"

        result_subtitle = (
            "YOU ESCAPED SUCCESSFULLY!"
        )

        result_color = GREEN

    else:

        result_title = "GAME OVER!"

        result_subtitle = (
            "THE POLICE CAUGHT YOU!"
        )

        result_color = RED


    # --------------------------------------------------------
    # RESULT PANEL
    # --------------------------------------------------------

    panel_width = 500
    panel_height = 350

    panel_x1 = (
        WIDTH - panel_width
    ) // 2

    panel_y1 = (
        HEIGHT - panel_height
    ) // 2

    panel_x2 = (
        panel_x1 + panel_width
    )

    panel_y2 = (
        panel_y1 + panel_height
    )


    canvas.create_rectangle(
        panel_x1,
        panel_y1,
        panel_x2,
        panel_y2,
        fill="#121722",
        outline=result_color,
        width=5
    )


    # --------------------------------------------------------
    # TITLE
    # --------------------------------------------------------

    canvas.create_text(
        WIDTH // 2,
        panel_y1 + 45,
        text=result_title,
        fill=result_color,
        font=("Arial", 27, "bold")
    )


    # --------------------------------------------------------
    # SUBTITLE
    # --------------------------------------------------------

    canvas.create_text(
        WIDTH // 2,
        panel_y1 + 88,
        text=result_subtitle,
        fill=WHITE,
        font=("Arial", 13, "bold")
    )


    # --------------------------------------------------------
    # KEY RESULT
    # --------------------------------------------------------

    canvas.create_text(
        WIDTH // 2,
        panel_y1 + 130,
        text=f"Keys Collected: {collected}/5",
        fill=YELLOW,
        font=("Arial", 13, "bold")
    )


    # --------------------------------------------------------
    # MOVE RESULT
    # --------------------------------------------------------

    canvas.create_text(
        WIDTH // 2,
        panel_y1 + 158,
        text=f"Total Moves: {moves}",
        fill=WHITE,
        font=("Arial", 12)
    )


    # --------------------------------------------------------
    # POLICE RESULT
    # --------------------------------------------------------

    canvas.create_text(
        WIDTH // 2,
        panel_y1 + 185,
        text=f"AI Police: {len(guards)}",
        fill="#FF7777",
        font=("Arial", 11)
    )


    # ========================================================
    # RESTART BUTTON
    # ========================================================

    restart_button = tk.Button(
        root,
        text="RESTART GAME",
        command=restart_game,
        bg="#2879B9",
        fg=WHITE,
        activebackground="#3498DB",
        activeforeground=WHITE,
        font=("Arial", 11, "bold"),
        width=18,
        height=1,
        relief="flat",
        cursor="hand2"
    )

    result_restart_button = canvas.create_window(
        WIDTH // 2,
        panel_y1 + 235,
        window=restart_button
    )


    # ========================================================
    # EXIT BUTTON
    # ========================================================

    exit_result_button = tk.Button(
        root,
        text="EXIT GAME",
        command=root.destroy,
        bg="#A83232",
        fg=WHITE,
        activebackground="#E84B4B",
        activeforeground=WHITE,
        font=("Arial", 11, "bold"),
        width=18,
        height=1,
        relief="flat",
        cursor="hand2"
    )

    result_exit_button = canvas.create_window(
        WIDTH // 2,
        panel_y1 + 285,
        window=exit_result_button
    )


# ============================================================
# CHECK GAME RESULT
# ============================================================

def process_game_result():

    global game_over
    global game_result

    game_over, game_result = check_game(
        player,
        guards,
        keys
    )

    if game_result == "WIN":

        status.config(
            text="MISSION COMPLETED - YOU WIN!",
            fg=GREEN
        )

        stop_ai_timer()

        return True


    if game_result == "LOSS":

        status.config(
            text="GAME OVER - POLICE CAUGHT YOU!",
            fg=RED
        )

        stop_ai_timer()

        return True


    return False


# ============================================================
# PLAYER MOVEMENT
# ============================================================

def handle_player_move(dx, dy):

    global player
    global keys
    global collected
    global moves

    if game_over:
        return


    old_player = player

    old_key_count = len(keys)


    # --------------------------------------------------------
    # MOVE PLAYER
    # --------------------------------------------------------

    player, keys, key_collected = move_player(
        player,
        dx,
        dy,
        keys.copy()
    )


    # --------------------------------------------------------
    # COUNT MOVEMENT
    # --------------------------------------------------------

    if player != old_player:

        moves += 1


    # --------------------------------------------------------
    # COUNT KEY
    # --------------------------------------------------------

    if len(keys) < old_key_count:

        collected += 1


    # --------------------------------------------------------
    # CHECK WIN / LOSS
    # --------------------------------------------------------

    result = process_game_result()


    # --------------------------------------------------------
    # DRAW GAME
    # --------------------------------------------------------

    canvas.delete("all")

    draw_game(
        canvas,
        player,
        guards,
        keys
    )


    # --------------------------------------------------------
    # SHOW RESULT
    # --------------------------------------------------------

    if result:

        show_result_screen()


    # --------------------------------------------------------
    # STATUS
    # --------------------------------------------------------

    update_status()


# ============================================================
# AI POLICE MOVEMENT
# ============================================================

def update_guards():

    global guards
    global ai_job

    ai_job = None

    if game_over:
        return


    # --------------------------------------------------------
    # MOVE POLICE
    # --------------------------------------------------------

    guards = move_guards(
        guards,
        player
    )


    # --------------------------------------------------------
    # CHECK GAME
    # --------------------------------------------------------

    result = process_game_result()


    # --------------------------------------------------------
    # DRAW
    # --------------------------------------------------------

    canvas.delete("all")

    draw_game(
        canvas,
        player,
        guards,
        keys
    )


    # --------------------------------------------------------
    # SHOW RESULT
    # --------------------------------------------------------

    if result:

        show_result_screen()

        return


    # --------------------------------------------------------
    # STATUS
    # --------------------------------------------------------

    update_status()


    # --------------------------------------------------------
    # CONTINUE AI
    # --------------------------------------------------------

    if not game_over:

        ai_job = root.after(
            600,
            update_guards
        )


# ============================================================
# RESTART GAME
# ============================================================

def restart_game():

    global player
    global guards
    global keys
    global collected
    global moves
    global game_over
    global game_result
    global ai_job


    # --------------------------------------------------------
    # STOP OLD AI
    # --------------------------------------------------------

    stop_ai_timer()


    # --------------------------------------------------------
    # RESET GAME VARIABLES
    # --------------------------------------------------------

    player = START_PLAYER

    guards = START_GUARDS.copy()

    keys = START_KEYS.copy()

    collected = 0

    moves = 0

    game_over = False

    game_result = ""


    # --------------------------------------------------------
    # REMOVE RESULT BUTTONS
    # --------------------------------------------------------

    remove_result_buttons()


    # --------------------------------------------------------
    # CLEAR SCREEN
    # --------------------------------------------------------

    canvas.delete("all")


    # --------------------------------------------------------
    # RESET STATUS
    # --------------------------------------------------------

    status.config(
        text="POLICE: 7    KEYS: 0/5    MOVES: 0",
        fg=YELLOW
    )


    # --------------------------------------------------------
    # DRAW NEW GAME
    # --------------------------------------------------------

    draw_game(
        canvas,
        player,
        guards,
        keys
    )


    # --------------------------------------------------------
    # START AI AGAIN
    # --------------------------------------------------------

    ai_job = root.after(
        600,
        update_guards
    )


# ============================================================
# KEYBOARD CONTROLS
# ============================================================

root.bind(
    "<Up>",
    lambda event: handle_player_move(0, -1)
)

root.bind(
    "<Down>",
    lambda event: handle_player_move(0, 1)
)

root.bind(
    "<Left>",
    lambda event: handle_player_move(-1, 0)
)

root.bind(
    "<Right>",
    lambda event: handle_player_move(1, 0)
)


# ============================================================
# INSTRUCTIONS
# ============================================================

controls = tk.Label(
    root,
    text=(
        "ARROW KEYS: MOVE    |    "
        "COLLECT ALL KEYS    |    "
        "REACH EXIT    |    "
        "AVOID AI POLICE"
    ),
    font=("Arial", 9, "bold"),
    bg=BG,
    fg=WHITE
)

controls.pack(
    pady=3
)


# ============================================================
# BOTTOM BUTTONS
# ============================================================

button_frame = tk.Frame(
    root,
    bg=BG
)

button_frame.pack(
    pady=10
)


restart_button = tk.Button(
    button_frame,
    text="RESTART GAME",
    command=restart_game,
    bg="#2879B9",
    fg=WHITE,
    font=("Arial", 11, "bold"),
    width=16,
    height=1,
    relief="flat"
)

restart_button.pack(
    side="left",
    padx=10
)


exit_button = tk.Button(
    button_frame,
    text="EXIT",
    command=root.destroy,
    bg="#A83232",
    fg=WHITE,
    font=("Arial", 11, "bold"),
    width=10,
    height=1,
    relief="flat"
)

exit_button.pack(
    side="left",
    padx=10
)


# ============================================================
# START GAME
# ============================================================

draw_game(
    canvas,
    player,
    guards,
    keys
)

ai_job = root.after(
    600,
    update_guards
)


# ============================================================
# RUN GAME
# ============================================================

root.mainloop()