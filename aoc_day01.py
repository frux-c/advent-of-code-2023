from common import PartContext

NUM_MAPPING = {str(k): k for k in range(10)}

WORD_NUM_MAPPING = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six':  6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'zero': 0
}

MIXED_NUM_MAPPING = {
    **NUM_MAPPING, **WORD_NUM_MAPPING
}
def part_1():
    with PartContext('1', 'day1.txt') as part1:
        # part 1
        part1.answer = 0
        lines = part1.data.split('\n')
        for line in lines:
            i, j = 0, len(line) - 1
            num_lft, num_rgt = -1, -1
            for _ in range(len(line)):
                if num_lft == -1 and line[i] in NUM_MAPPING:
                    num_lft = NUM_MAPPING[line[i]]
                if num_rgt == -1 and line[j] in NUM_MAPPING:
                    num_rgt = NUM_MAPPING[line[j]]
                if num_lft != -1 and num_rgt != -1:
                    break
                i += 1
                j -= 1
            part1.answer += (num_lft * 10) + num_rgt

def part_2():
    with PartContext('2', 'day1.txt') as part2:
        part2.answer = 0
        lines = part2.data.split('\n')
        for line in lines:
            i, j = 0, len(line)
            num_lft, num_rgt = -1, -1
            break_flag = False
            for _ in range(len(line)):
                if break_flag:
                    break
                for word in MIXED_NUM_MAPPING:
                    if num_lft == -1 and line[i:i+len(word)] == word:
                        num_lft = MIXED_NUM_MAPPING[word]
                    if num_rgt == -1 and line[j-len(word):j] == word:
                        num_rgt = MIXED_NUM_MAPPING[word]
                    if num_lft != -1 and num_rgt != -1:
                        break_flag = True
                        break
                i += 1
                j -= 1
            cnum = 0
            cnum = (num_lft * 10) + num_rgt
            part2.answer += cnum

if __name__ == '__main__':
    part_1()
    part_2()