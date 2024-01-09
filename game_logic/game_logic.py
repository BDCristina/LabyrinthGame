import random


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.labirint = self.generate_labirint()
        self.start_color = (0, 255, 0)  # Culoarea pentru căsuța de start (verde)
        self.finish_color = (255, 0, 0)  # Culoarea pentru căsuța finală (roșie)

    def generate_labirint(self):
        # Creăm o matrice pentru labirint cu ziduri peste tot
        labirint = [[1 for _ in range(self.width)] for _ in range(self.height)]

        # Setăm startul și sfârșitul labirintului
        labirint[0][1] = 0  # Start
        labirint[self.height - 1][self.width - 2] = 0  # Finish
        labirint[self.height - 1][self.width -1] = 2  # Finish

        # Algoritmul de generare a labirintului
        def recursive_backtracking(x, y):
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            random.shuffle(directions)

            for dx, dy in directions:
                nx, ny = x + dx * 2, y + dy * 2

                if 0 <= nx < self.height and 0 <= ny < self.width and labirint[nx][ny] == 1:
                    labirint[nx - dx][ny - dy] = 0
                    labirint[nx][ny] = 0
                    recursive_backtracking(nx, ny)

        recursive_backtracking(1, 1)
        return labirint

    def reset_labirint(self):
        self.labirint = self.generate_labirint()

    def find_final_position(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.labirint[y][x] == 2:  # Verifică dacă valoarea este cea pentru poziția finală
                    return x, y  # Returnează coordonatele poziției finale
