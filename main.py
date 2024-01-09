from game_logic.game_logic import Game
from graphics.graphics import GraphicsEngine


def main():
    graphics = GraphicsEngine()  # Inițializează interfața grafică
    game = Game(graphics.game_width, graphics.game_height)

    graphics.run_game(game)


if __name__ == "__main__":
    main()
