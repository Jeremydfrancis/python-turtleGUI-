# python-turtleGUI

A Python Turtle-based interactive launcher featuring 9 mini-games and visual demos, all accessible from a single graphical menu prompt.

---

## Requirements

- Python 3.x
- Pillow (`pip install pillow`) - required for Turtle Crossing car and player sprites

---

## Getting Started

```bash
python states_games.py
```

A turtle window will open with a text prompt. Enter the number corresponding to what you want to run. After each demo or game ends, the launcher returns to the main menu.

---

## Menu

| # | Name | Description |
|---|------|-------------|
| 1 | Random Walk | Draws a colorful randomized path across the screen |
| 2 | Draw All Shapes | Draws shapes from a triangle up to a decagon with alternating solid and dashed lines |
| 3 | Spirograph | Overlapping colored circles drawn at increasing angles |
| 4 | Hirst Dot Painting | Fills the screen with a grid of randomly colored dots |
| 5 | Free Draw | Control a turtle with your keyboard to draw freely |
| 6 | Turtle Race | Bet on which colored turtle wins a randomized race |
| 7 | Snake Game | Classic snake - eat food, grow longer, avoid walls and yourself |
| 8 | Pong | Two-player pong with a live scoreboard |
| 9 | Turtle Crossing | Guide a ninja turtle across the road while dodging cars that speed up each level |

---

## Controls

**Free Draw**

| Key | Action |
|-----|--------|
| Up Arrow | Move forward |
| Down Arrow | Move backward |
| Left Arrow | Turn left |
| Right Arrow | Turn right |
| C | Clear screen and return to center |

**Snake Game**

| Key | Action |
|-----|--------|
| Space | Start game |
| Arrow Keys | Change direction |

**Pong**

| Key | Action |
|-----|--------|
| Space | Start game |
| W / S | Left paddle up / down |
| Up / Down Arrow | Right paddle up / down |
| Escape | Quit to menu |

**Turtle Crossing**

| Key | Action |
|-----|--------|
| W | Move turtle forward |

---

## Project Structure

```
python-turtleGUI-/
├── main.py                        # Entry point and launcher menu
├── random_walk.py                 # Random walk logic
├── shapes.py                      # Shape drawing functions
├── circle.py                      # Spirograph logic
├── hirst_painting.py              # Dot grid painting
├── event_listeners.py             # Free draw keyboard controls
├── turtle_race.py                 # Turtle race game
├── snake/
│   ├── snake_game.py              # Game loop
│   ├── snake_class.py             # Snake movement and growth
│   ├── food_class.py              # Food placement
│   └── scoreboard_class.py        # Score display
├── pong/
│   ├── pong_game.py               # Game loop
│   ├── paddle_class.py            # Paddle movement
│   ├── ball_class.py              # Ball physics
│   └── scoreboard_class.py        # Score display
└── turtle_crossing/
    ├── crossing_game.py            # Game loop
    ├── player_class.py             # Player turtle (ninja_turtle.gif)
    ├── car_manager_class.py        # Car spawning and movement
    ├── scoreboard_class.py         # Level display
    └── start_finish_line_class.py  # Start and finish lines
```

---

## Notes

- GIF assets for Turtle Crossing (`ninja_turtle.gif`, `car_*.gif`) must be present in the `turtle_crossing/` directory
- The launcher uses `screen.textinput()` for all menu prompts - no terminal interaction required
- Each sub-game runs in its own turtle window and returns control to the launcher on exit
