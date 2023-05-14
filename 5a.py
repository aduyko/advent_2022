import re

filename = "inputs/5.txt"

result = ""
state = []
parsing_state = True

def update_state(state: list[list[str]], command: str) -> list[list[str]]: 
    command_regex = re.compile(r"move (\d+) from (\d+) to (\d+)")
    quantity, from_stack, to_stack = command_regex.search(command).groups()
    for _ in range(int(quantity)):
        state[int(to_stack)-1].append(state[int(from_stack)-1].pop())
    return state

for l in open(filename):
    if(l[0:3] == " 1 " or l == "\n"):
        parsing_state = False
        continue
    if(parsing_state): 
        blocks = [l[i:i+3] for i in range(0,len(l),4)]
        if len(state) < len(blocks):
            state = [[] for i in range(0,len(blocks))]
        for idx, block in enumerate(blocks):
            block_val = block[1].strip()
            if block_val:
                state[idx].insert(0,block_val)
    else:
        state = update_state(state, l.rstrip())

for stack in state:
    result += stack.pop()

print(result)