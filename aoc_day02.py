from common import PartContext
import numpy as np

def part1():
    # max number of cubes per color
    MAX_CUBE = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    with PartContext('1', 'day02.txt') as part1:
        part1.answer = 0 # sum of game ids
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
                part1.answer += i

def part2():
    # Min cube requred for game
    min_cubes = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    reset_min_cubes = min_cubes.copy()
    with PartContext('2', 'day02.txt') as part2:
        part2.answer = 0 # sum of game ids
        lines = part2.data.split('\n')
        for i, line in enumerate(lines, 1):
            game_id, games = line.split(':')
            rounds = games.split(';')
            for _round in rounds:
                for cube in _round.split(','):
                    num, color = cube.strip().split(' ')
                    if (x := int(num)) > min_cubes[color]:
                        min_cubes[color] = x
            part2.answer += np.prod([x for x in min_cubes.values()]) # add product of min cubes
            min_cubes.update(reset_min_cubes) # reset min cubes

if __name__ == '__main__':
    part1()
    part2()
