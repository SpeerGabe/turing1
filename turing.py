from collections import defaultdict

def parse_tuples():
    transitions = {}
    while True:
        line = input().strip()
        if line == ".":
            break
        if len(line) < 4:
            print("Invalid input. Enter in format: State ReadSymbol WriteMoveNextState")
            continue
        state, read_symbol, write_symbol, move, next_state = line[0], line[1], line[2], line[3], line[4:]
        transitions[(state, read_symbol)] = (next_state, write_symbol, move)
    return transitions

def print_tape(tape, head, state):
    min_index = min(tape.keys(), default=0)
    max_index = max(tape.keys(), default=0)
    tape_str = "".join(tape[i] for i in range(min_index, max_index + 1))
    head_pos = head - min_index
    print(tape_str[:head_pos] + f"{{{state}}}" + tape_str[head_pos:])

def run_turing_machine(transitions, tape_str, max_iterations):
    tape = defaultdict(lambda: " ")
    if not tape_str:
        tape[0] = " "
    else:
        for i, char in enumerate(tape_str):
            tape[i] = char
    head = 0
    state = next(iter(transitions.keys()))[0] if transitions else "HALT"
    
    for i in range(max_iterations):  # Keep iteration count correct
        print_tape(tape, head, state)
        current_symbol = tape[head]
        if (state, current_symbol) not in transitions:
            print("HALTED")
            print(f"Final State: {state}")
            return
        next_state, write_symbol, move = transitions[(state, current_symbol)]
        tape[head] = write_symbol
        head += 1 if move == "R" else -1
        state = next_state
    
    print_tape(tape, head, state)  # Ensure final state is printed
    print("Max Iterations Reached")
    print(f"Final State: {state}")

if __name__ == "__main__":
    print("Enter 5-Tuples. A . by itself to end.")
    transitions = parse_tuples()
    print("\nEnter the initial tape and press enter.")
    tape_str = input().strip()
    max_iterations = int(input("\nMaximum Iterations: ").strip())
    run_turing_machine(transitions, tape_str, max_iterations)
