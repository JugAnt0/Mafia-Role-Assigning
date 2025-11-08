# Mafia (Python Edition)

A simple command-line version of the classic social deduction game **Mafia**, where players are secretly assigned roles and must work together (or deceive each other) to survive. This version focuses on the **role-distribution phase**, making it useful for in-person play with friends.

## 🎭 How It Works
1. Enter the number of players (4–10).
2. Each player receives a **secret role**, one at a time:
   - **Mafia** – Knows the truth. Eliminates others at night.
   - **Detective** – Investigates one player each night.
   - **Doctor** – Protects someone from elimination.
   - **Villagers** – Outnumber the Mafia, must discover the liar(s).
3. After assignments, close the computer and continue the game socially.

The program ensures **each player sees only their own role** before clearing the screen.
