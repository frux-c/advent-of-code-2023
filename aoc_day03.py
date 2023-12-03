from common import PartContext
import numpy as np

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

def part1_helper(arr: np.ndarray, r: int, c: int, nums=None):
    if nums is None:
        nums = []
    for tx, ty in DIRECTIONS:
        # check if the next cell is not a wall
        if  r+tx >= 0 and \
            r+tx < arr.shape[0] and \
            c+ty >= 0 and \
            c+ty < arr.shape[1] and \
            arr[r+tx][c+ty] != -1:
            ts, te, x = c+ty, c+ty, r+tx
            tsb, teb = True, True
            while tsb or teb:
                if tsb:
                    if ts >= 0 and arr[x][ts] != -1:
                        ts -= 1 
                    else:
                        if arr[x][ts] == -1:
                            ts += 1
                        tsb = False
                if teb:
                    if te < arr.shape[1] and arr[x][te] != -1:
                        te += 1
                    else:
                        teb = False
            num = 0
            if ts == te:
                num = arr[x][ts]
                arr[x][ts] = -1 # mark as visited
            else:
                # turn list of numbers into a single number
                num = 0
                nth_place = 10 ** ((te - ts) - 1)
                for k in arr[x][ts:te]:
                    num += k * nth_place
                    nth_place //= 10
                arr[x][ts:te] = -1 # mark as visited
            nums.append(num)
                

def part1():
    with PartContext('1', 'day03.txt') as part1:
        lines = part1.data.split('\n')
        total_sum = 0
        arr = np.zeros((len(lines), len(lines[0])), dtype=np.int8)
        symbol_location: list[tuple[int, int]] = []
        for r, line in enumerate(lines):
            for c, _char in enumerate(line):
                if _char == '.':
                    arr[r][c] = -1
                elif _char.isdigit():
                    arr[r][c] = int(_char)
                else:
                    symbol_location.append((r, c))
                    arr[r][c] = -1
        nums = []
        for r, c in symbol_location:
            part1_helper(arr, r, c, nums)
        total_sum = sum(nums)

        print(f'Answer: {total_sum}')


def part2_helper(arr: np.ndarray, r: int, c: int, nums=None):
    if nums is None:
        nums = []
    for tx, ty in DIRECTIONS:
        # check if the next cell is not a wall
        if  r+tx >= 0 and \
            r+tx < arr.shape[0] and \
            c+ty >= 0 and \
            c+ty < arr.shape[1] and \
            arr[r+tx][c+ty] != -1:
            ts, te, x = c+ty, c+ty, r+tx
            tsb, teb = True, True
            while tsb or teb:
                if tsb:
                    if ts >= 0 and arr[x][ts] != -1:
                        ts -= 1 
                    else:
                        if arr[x][ts] == -1:
                            ts += 1
                        tsb = False
                if teb:
                    if te < arr.shape[1] and arr[x][te] != -1:
                        te += 1
                    else:
                        teb = False
            num = 0
            if ts == te:
                num = arr[x][ts]
                arr[x][ts] = -1 # mark as visited
            else:
                # turn list of numbers into a single number
                num = 0
                nth_place = 10 ** ((te - ts) - 1)
                for k in arr[x][ts:te]:
                    num += k * nth_place
                    nth_place //= 10
                arr[x][ts:te] = -1 # mark as visited
            nums.append(num)

def part2():
    with PartContext('2', 'day03.txt') as part2:
        lines = part2.data.split('\n')
        total_sum = 0
        arr = np.zeros((len(lines), len(lines[0])), dtype=np.int8)
        gear_location: list[tuple[int, int]] = []
        for r, line in enumerate(lines):
            for c, _char in enumerate(line):
                if _char == '.':
                    arr[r][c] = -1
                elif _char.isdigit():
                    arr[r][c] = int(_char)
                elif _char == '*':
                    gear_location.append((r, c))
                    arr[r][c] = -1
        nums = []
        for r, c in gear_location:
            part1_helper(arr, r, c, nums)
            if len(nums) == 2:
                total_sum += np.prod(nums)
            nums.clear()

        print(f'Answer: {total_sum}')

if __name__ == '__main__':
    part1()
    part2()