# Alien Impact

Alien Impact is an arcade-style space shooter game inspired by classic Space Invaders. Pilot your spaceship, shoot down waves of alien enemies, and survive as long as possible to set a high score!

## Features

- Fast-paced arcade gameplay
- Increasing difficulty as you survive longer
- Sound effects and background music
- Simple menu with How to Play and About sections

## Screenshots

_Add screenshots here if desired_

## Installation

### Prerequisites

- Python 3.7+
- [Pygame](https://www.pygame.org/) library

### Setup

1. Clone or download this repository.
2. Install Pygame:
   ```bash
   pip install pygame
   ```
3. Ensure the following files are in the same directory:
   - `alien-impact.py`
   - `player.png`, `enemy.png`, `title.png`
   - `bg.wav`, `bullet.wav`

## Running the Game

Run the game with:

```bash
python alien-impact.py
```

Or, if you have the executable (`alien-impact.exe`), simply run it.

## Controls

- **A / D**: Move left / right
- **Space**: Shoot
- **Esc**: Return to menu (in How to Play/About)
- **Mouse**: Navigate menu and click buttons

## How to Play

1. Use 'A' and 'D' keys to move your spaceship left and right.
2. Press the 'Space' key to shoot and destroy incoming alien ships.
3. Avoid enemy fire to prevent losing lives.
4. Survive as long as possible to score points and set new records!

## Troubleshooting

- If you get errors about missing files, make sure all required images and sound files are present in the same directory as the script.
- If you have issues with sound, ensure your system supports audio playback and Pygame's mixer is working.

## Credits

- Game developed using [Pygame](https://www.pygame.org/)
- All images and sounds are included in this repository. If you use external assets, please credit their creators accordingly.

## License

This project is for educational and personal use. For other uses, please check asset licenses or replace with your own.
