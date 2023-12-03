from common import PartContext
import numpy as np

def part1():
    # max number of cubes per color
    MAX_CUBE = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    with PartContext('1', 'day2.txt') as part1:
        total_sum = 0 # sum of game ids
        lines = part1.data.split('\n')
        for i, line in enumerate(lines, 1):
            vaild_game = True
            game_id, games = line.split(':')
            rounds = games.split(';')
            for _round in rounds:
                if not vaild_game:
                    break
                for cube in _round.split(','):
                    if not vaild_game:
                        break
                    num, color = cube.strip().split(' ')
                    if int(num) > MAX_CUBE[color]:
                        vaild_game = False
                        break
            if vaild_game:
                total_sum += i
        print(f'total_sum: {total_sum}')

                



if __name__ == '__main__':
    part1()
