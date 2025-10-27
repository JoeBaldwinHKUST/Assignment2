# simulator.py

def run_vmm(program_path: str = "guest_program.txt") -> None:
    acc = 0  # accumulator

    with open(program_path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue  # ignore empty lines

            parts = line.split()
            instr = parts[0]


            if instr == "add":
                # Expect exactly one integer operand (can be negative) else raise error
                if len(parts) != 2:
                    raise ValueError(f"Invalid 'add' instruction format: {line}")
                value_token = parts[1]
                print(f"[Guest] Executing: add {value_token}")
                acc += int(value_token)

            elif instr == "print":
                print("[Guest] Executing: print")
                print(f"Accumulator value: {acc}")

            elif instr == "scan_disk":
                print("[VMM] Trapped privileged instruction 'scan_disk', emulating...")

            elif instr == "halt":
                print("[VMM] Trapped privileged instruction 'halt'. Halting guest.")
                break


if __name__ == "__main__":
    run_vmm()
