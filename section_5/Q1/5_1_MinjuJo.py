import sys
sys.stdin = open("in5.txt", "r")

numbers, pop_num = input().split()

pop_num, popped = int(pop_num), 0
final_stack = []

while pop_num > popped:
    if len(numbers) == pop_num - popped: # should be popped more, but if there's only numbers to be popped left
        numbers = ""
        break
    max_idx = numbers.index(max(numbers[:pop_num-popped + 1])) # among popped-able numbers
    popped += max_idx #count the popped numbers
    final_stack.append(numbers[max_idx]) # append the max number to the stack
    numbers = numbers[max_idx + 1 :] # pop the max number and numbers in front of this

print(''.join(final_stack)+numbers)
