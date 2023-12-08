from common import PartContext
import numpy as np

def part1():
    with PartContext('1', 'day04.txt') as part1:
        part1.answer = 0
        filter_fn = lambda x : x != ""
        for line in part1.data.split('\n'):
            card_num, scratch_nums = line.split(": ")
            win_nums, ticket_nums = scratch_nums.split(" | ")
            win_nums = list(filter(filter_fn, win_nums.split(" ")))
            ticket_nums = list(filter(filter_fn, ticket_nums.split(" ")))
            if not win_nums or not ticket_nums:
                continue
            matching_set = set(ticket_nums).intersection(set(win_nums))
            matching_set_len = len(matching_set)
            if matching_set_len == 1:
                part1.answer += 1
            elif matching_set_len > 1:
                part1.answer += (1 << (matching_set_len - 1))

def part2():
    with PartContext('2', 'day04.txt') as part2:
        lines = part2.data.split('\n')
        original_cards = np.zeros(len(lines), dtype=np.int32)
        copy_cards = np.zeros(len(lines), dtype=np.int32)
        copy_cards += 1 # all cards have 1 original copy
        filter_fn = lambda x : x != ""
        for k, line in enumerate(lines):
            card_num, scratch_nums = line.split(": ")
            win_nums, ticket_nums = scratch_nums.split(" | ")
            win_nums = list(filter(filter_fn, win_nums.split(" ")))
            ticket_nums = list(filter(filter_fn, ticket_nums.split(" ")))
            if not win_nums or not ticket_nums:
                continue
            matching_set = set(ticket_nums).intersection(set(win_nums))
            original_cards[k] = len(matching_set)
        for i, v in enumerate(original_cards):
            copy_cards[i+1:i+v+1] += copy_cards[i]
        part2.answer = copy_cards.sum()

if __name__ == '__main__':
    part1()
    part2()