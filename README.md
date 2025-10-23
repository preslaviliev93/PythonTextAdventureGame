# Dungeon Crawler — The Quest for the Golden Key

A simple yet expandable **text-based adventure game** written in **Python**.  
Move through rooms, collect items, fight monsters, and find the **Golden Key** to win the game.

---

## Gameplay

You start your journey in a randomly generated map filled with rooms.  
Each room may contain:
- A **monster** you must fight.
- A **weapon or item** that boosts your attack.

Your goal is to **find the Golden Key** hidden somewhere on the map.

If your health drops to `0`, the game ends - the monsters have defeated you.

---

## Features

- **Turn-based combat system** (player vs. monster).
- **Procedurally generated map** (3×3 to 10×10 grid).
- **Over 25 unique rooms, 30+ monsters, and 25+ items**.
- **Item-based attack bonuses**.
- **Inventory tracking system**.
- **Hidden Golden Key** to win the game.
- **Permanent death** — lose all progress if you die.

---

##  How It Works

### 1. Map Generation
The game creates a square map filled with `"R"` symbols representing unexplored rooms.

### 2. Random Placement
- The player (`"P"`) and the Golden Key (`"G"`) are placed at random locations.
- The Golden Key’s coordinates are hidden from the player.

### 3. Movement
You can move using the following keys:
[u] - Up
[d] - Down
[l] - Left
[r] - Right

Invalid or out-of-bound moves are rejected.

### 4. Room Events
Each new room triggers:
- A random **description**.
- A random **item** (boosts your attack).
- A random **monster** (battle).

### 5. Combat
Combat alternates turns:
- Player attacks first.
- Then the monster retaliates.
- The fight continues until one side dies.

If your health reaches 0 → Game Over.  
If you find the Golden Key → You win.

---

## Requirements

- Python 3.10+

---

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/preslaviliev93/PythonTextAdventureGame.git
cd dungeon-crawler-golden-key

python main.py

['R', 'R', 'R']
['X', 'P', 'R']
['R', 'R', 'R']
Health: 100

Enter direction to move.
 [u] - Up, [d] - Down, [l] - Left, [r] - Right: d

#################### Temple ####################
Strange chants echo around you as you steel yourself for what's ahead.
You found Machine Gun with +40 attack power
You equipped Machine Gun with +40 attack.
Your new attack power is: 45
Cursed Knight with 45 HP and 28 ATK awaits to fight it.



You have found the Golden Key!
You have won the game!

