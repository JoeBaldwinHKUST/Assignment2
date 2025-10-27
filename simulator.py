# simulator.py
# Joe Baldwin 21288394
import sys
import os

def run_vmm(program_path=None):
    acc = 0  # accumulator

    # Determine file path
    if program_path is None:
        # Check for both possible filenames (Code for assignment 2 has .txt.txt so handle both)
        if os.path.exists("guest_program.txt"):
            program_path = "guest_program.txt"
        elif os.path.exists("guest_program.txt.txt"):
            program_path = "guest_program.txt.txt"
        else:
            sys.stderr.write("Error: guest_program.txt file not found.\n")
            sys.exit(1)

    # Open file in a way that works on both Python 2 and 3
    if sys.version_info[0] >= 3:
        f = open(program_path, "r", encoding="utf-8")
    else:
        f = open(program_path, "r")

    # Process each instruction
    for raw in f:
        line = raw.strip()
        if not line:
            continue

        parts = line.split()
        instr = parts[0]

        if instr == "add":
            if len(parts) != 2:
                sys.stderr.write("Invalid 'add' instruction: %s\n" % line)
                continue
            value_token = parts[1]
            print("[Guest] Executing: add %s" % value_token)
            try:
                acc += int(value_token)
            except ValueError:
                sys.stderr.write("Invalid number in 'add': %s\n" % value_token)
                continue

        elif instr == "print":
            print("[Guest] Executing: print")
            print("Accumulator value: %d" % acc)

        elif instr == "scan_disk":
            print("[VMM] Trapped privileged instruction 'scan_disk', emulating...")

        elif instr == "halt":
            print("[VMM] Trapped privileged instruction 'halt'. Halting guest.")
            break

        else:
            sys.stderr.write("Unknown instruction: %s\n" % line)

    f.close()


if __name__ == "__main__":
    # Allow optional command-line argument for custom file name
    path_arg = sys.argv[1] if len(sys.argv) > 1 else None
    run_vmm(path_arg)
