import sys
import os
import time
import random

# Windows may use a legacy console encoding that cannot display emoji.
# UTF-8 keeps the welcome and help messages readable.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# pzcode variable memory storage
VARIABLES = {}

def evaluate_expression(expr, line_num):
    """Helper function to parse numbers, strings, variables, or math equations."""
    expr = expr.strip()
    if not expr:
        return None
    
    # 1. Math Operations (+, -, *, /, and %)
    if "+" in expr or "-" in expr:
        operator = "+" if "+" in expr else "-"
        left_part, right_part = expr.split(operator, 1)
        
        left_val = evaluate_expression(left_part, line_num)
        right_val = evaluate_expression(right_part, line_num)
        
        if isinstance(left_val, int) and isinstance(right_val, int):
            if operator == "+": return left_val + right_val
            if operator == "-": return left_val - right_val
        else:
            if left_val is not None and right_val is not None:
                print(f"\u274c Math Error (Line {line_num}): You can only add or subtract numbers.")
            return None

    for operator in ["*", "/", "%"]:
        if operator in expr:
            left_part, right_part = expr.split(operator, 1)
            left_val = evaluate_expression(left_part, line_num)
            right_val = evaluate_expression(right_part, line_num)
            if isinstance(left_val, (int, float)) and isinstance(right_val, (int, float)):
                try:
                    if operator == "*": return left_val * right_val
                    if operator == "/": return left_val / right_val
                    if operator == "%": return left_val % right_val
                except ZeroDivisionError:
                    print(f"Math Error (Line {line_num}): Cannot divide by zero.")
                    return None
            print(f"Math Error (Line {line_num}): Math requires numbers.")
            return None

    # 2. Variable Lookup
    if expr in VARIABLES:
        return VARIABLES[expr]
        
    # 3. Direct Integer Checking
    if expr.isdigit():
        return int(expr)
        
    # 4. Direct String Checking (Single or Double Quotes)
    if (expr.startswith('"') and expr.endswith('"')) or (expr.startswith("'") and expr.endswith("'")):
        return expr[1:-1]
        
    if not expr.replace('"', '').strip() == '':
        print(f"\u274c Value Error (Line {line_num}): Unknown value or token '{expr}'.")
    return None


def evaluate_condition(condition_part, line_num):
    """Helper to check if a logic statement (>, <, ==) evaluates to True or False."""
    comparison_op = None
    for op in [">=", "<=", "==", "!=", ">", "<"]:
        if op in condition_part:
            comparison_op = op
            break
            
    if not comparison_op:
        return None, None, None
        
    left_expr, right_expr = condition_part.split(comparison_op, 1)
    left_val = evaluate_expression(left_expr, line_num)
    right_val = evaluate_expression(right_expr, line_num)
    
    try:
        if comparison_op == ">" and left_val > right_val: return True, left_val, right_val
        elif comparison_op == "<" and left_val < right_val: return True, left_val, right_val
        elif comparison_op == "==" and left_val == right_val: return True, left_val, right_val
        elif comparison_op == "!=" and left_val != right_val: return True, left_val, right_val
        elif comparison_op == ">=" and left_val >= right_val: return True, left_val, right_val
        elif comparison_op == "<=" and left_val <= right_val: return True, left_val, right_val
    except TypeError:
        print(f"\u274c Logic Error (Line {line_num}): Cannot compare different data types.")
        return False, None, None
        
    return False, left_val, right_val


def show_help(category=""):
    """Interactive help center for pzcode documentation."""
    category = category.strip().lower()
    
    if not category:
        print("\n\U0001f4d6 --- pzcode Help Center ---")
        print("Available categories for detailed documentation:")
        print("  • help variables   - Learn about variables, math, and printing")
        print("  • help input       - Learn how to interact with keyboard user input")
        print("  • help logic       - Learn about conditional statements and loops")
        print("\nType 'help [category]' to see syntax rules and code examples.")
        return

    if category == "variables":
        print("\n\U0001f4e6 Category: VARIABLES & BASIC IO")
        print("--------------------------------------------------")
        print("1. Creating a variable:")
        print("   Syntax: store [value] in [variable_name]")
        print("   Example: store 100 in score")
        print("   Example: store \"Alex\" in name\n")
        print("2. Performing math operations:")
        print("   Syntax: store [var/num] + [var/num] in [variable_name]")
        print("   Example: store score + 25 in final_score\n")
        print("3. Printing data to screen:")
        print("   Syntax: say [expression]")
        print("   Example: say \"Hello World\"")
        print("   Example: say score")
        
    elif category == "input":
        print("\n\u2328\ufe0f Category: KEYBOARD USER INPUT")
        print("--------------------------------------------------")
        print("1. Asking for user response:")
        print("   Syntax: ask [prompt_string] in [variable_name]")
        print("   Example: ask \"Enter your username: \" in username")
        print("   Note: If the user inputs numbers, pzcode safely saves it as an integer.")
        
    elif category == "logic":
        print("\n\U0001f9e0 Category: CONDITIONALS & LOOPS")
        print("--------------------------------------------------")
        print("1. Conditional If Statements:")
        print("   Syntax: if [left] [op] [right]: [command]")
        print("   Example: if score > 50: say \"You passed!\"")
        print("   Example: if score > 50: say \"Passed\" else: say \"Try again\"")
        print("   Operators: >, <, ==\n")
        print("2. Loop Control Structures:")
        print("   Syntax: repeat while [condition]: [command]")
        print("   Example: repeat while count < 5: store count + 1 in count")
        print("   Simple loop: repeat 3: say \"Hello\"")
        print("   Pause: wait 1")
        
    else:
        print(f"\u274c Documentation Error: Category '{category}' not found. Type 'help' for options.")


def run_source_file(filename):
    """Run a .pzc file and then return to the interactive interpreter."""
    filename = filename.strip().strip('"').strip("'")

    if not filename.endswith('.pzc'):
        print("Source files must end with the '.pzc' extension.")
        return

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line_num, line in enumerate(lines, 1):
            execute_line(line, line_num)

    except FileNotFoundError:
        print(f"Could not find file '{filename}'.")


def execute_line(line, line_num):
    """Core execution engine for processing a single pzcode instruction line."""
    line = line.strip()
    if not line or line.startswith("#"):
        return

    # --- SCREEN CLEARING ---
    if line.lower() == "clear" or line.lower() == "cls":
        os.system('cls' if os.name == 'nt' else 'clear')
        return

    # Help command detection
    if line.lower() == "help":
        show_help()
        return
    if line.lower().startswith("help "):
        category = line[5:]
        show_help(category)
        return

    # Run a source file while keeping the interactive terminal open.
    if line.lower().startswith("run "):
        run_source_file(line[4:])
        return

    # --- WAIT ---
    if line.lower().startswith("wait "):
        seconds = evaluate_expression(line[5:], line_num)
        if isinstance(seconds, (int, float)) and seconds >= 0:
            time.sleep(seconds)
        else:
            print(f"Wait Error (Line {line_num}): Use a positive number of seconds.")
        return

    # --- SIMPLE COUNTED LOOP ---
    if line.startswith("repeat ") and not line.startswith("repeat while "):
        if ":" not in line:
            print(f"Syntax Error (Line {line_num}): Counted loops must use 'repeat number: command'.")
            return
        count_part, command_part = line[7:].split(":", 1)
        count = evaluate_expression(count_part, line_num)
        if isinstance(count, int) and count >= 0:
            for _ in range(count):
                execute_line(command_part, line_num)
        else:
            print(f"Loop Error (Line {line_num}): The repeat count must be a positive whole number.")
        return

    # --- REPEAT WHILE LOOP ---
    if line.startswith("repeat while "):
        if ":" not in line:
            print(f"\u274c Syntax Error (Line {line_num}): Loop conditions must end with a ':'.")
            return
        condition_part, command_part = line[13:].split(":", 1)
        safety_counter = 0
        while True:
            condition_met, _, _ = evaluate_condition(condition_part, line_num)
            if condition_met is None:
                print(f"\u274c Syntax Error (Line {line_num}): 'repeat while' requires standard operators like '>', '<', or '=='.")
                return
            if not condition_met:
                break
            execute_line(command_part, line_num)
            safety_counter += 1
            if safety_counter > 1000:
                print(f"\u26a0\ufe0f Safety Break (Line {line_num}): Potential infinite loop detected (1000+ executions).")
                break
        return

    # --- IF CONDITION ---
    if line.startswith("if "):
        if ":" not in line:
            print(f"\u274c Syntax Error (Line {line_num}): 'if' conditions must end with a ':'.")
            return
        condition_part, command_part = line[3:].split(":", 1)
        else_command = None
        if " else: " in command_part:
            command_part, else_command = command_part.split(" else: ", 1)
        condition_met, _, _ = evaluate_condition(condition_part, line_num)
        if condition_met:
            execute_line(command_part.strip(), line_num)
        elif else_command is not None:
            execute_line(else_command.strip(), line_num)
        return

    # --- RANDOM NUMBER ---
    if line.lower().startswith("random "):
        if " in " not in line or " to " not in line:
            print(f"Syntax Error (Line {line_num}): Use random 1 to 10 in variable_name.")
            return
        range_part, var_name = line[7:].split(" in ", 1)
        min_part, max_part = range_part.split(" to ", 1)
        minimum = evaluate_expression(min_part, line_num)
        maximum = evaluate_expression(max_part, line_num)
        if isinstance(minimum, int) and isinstance(maximum, int) and minimum <= maximum:
            VARIABLES[var_name.strip()] = random.randint(minimum, maximum)
        else:
            print(f"Random Error (Line {line_num}): Use two whole numbers in the correct order.")
        return

    # --- TEXT HELPERS ---
    for command, operation in [("length ", "length"), ("upper ", "upper"), ("lower ", "lower")]:
        if line.lower().startswith(command) and " in " in line:
            raw_value, var_name = line[len(command):].split(" in ", 1)
            value = evaluate_expression(raw_value, line_num)
            if value is not None:
                if operation == "length":
                    VARIABLES[var_name.strip()] = len(value)
                elif isinstance(value, str):
                    VARIABLES[var_name.strip()] = value.upper() if operation == "upper" else value.lower()
                else:
                    print(f"Text Error (Line {line_num}): {operation} requires text.")
            return

    # --- VARIABLE TOOLS ---
    if line.lower() == "show variables":
        if not VARIABLES:
            print("No variables stored.")
        else:
            for name, value in VARIABLES.items():
                print(f"{name} = {value}")
        return

    if line.lower().startswith("delete "):
        var_name = line[7:].strip()
        if var_name in VARIABLES:
            del VARIABLES[var_name]
        else:
            print(f"Variable Error (Line {line_num}): Unknown variable '{var_name}'.")
        return

    # --- ASK (USER INPUT) ---
    if line.startswith("ask "):
        if " in " not in line:
            print(f"\u274c Syntax Error (Line {line_num}): 'ask' statements require the 'in' keyword.")
            return
        clean_line = line[4:]
        parts = clean_line.split(" in ")
        if len(parts) == 2:
            raw_prompt, var_name = parts[0].strip(), parts[1].strip()
            resolved_prompt = evaluate_expression(raw_prompt, line_num)
            if resolved_prompt is not None:
                user_response = input(str(resolved_prompt))
                if user_response.isdigit():
                    VARIABLES[var_name] = int(user_response)
                else:
                    VARIABLES[var_name] = user_response
            return

    # --- EASY ALIASES ---
    if line.startswith("set "):
        line = "store " + line[4:]
    elif line.startswith("print "):
        line = "say " + line[6:]

    # --- STORE (VARIABLE DECLARATION) ---
    if line.startswith("store "):
        if " in " not in line:
            print(f"\u274c Syntax Error (Line {line_num}): 'store' statements require the 'in' keyword.")
            return
        clean_line = line[6:] 
        parts = clean_line.split(" in ")
        if len(parts) == 2:
            raw_value, var_name = parts[0].strip(), parts[1].strip()
            resolved_value = evaluate_expression(raw_value, line_num)
            if resolved_value is not None:
                VARIABLES[var_name] = resolved_value
            return

    # --- SAY (PRINT TO SCREEN) ---
    if line.startswith("say "):
        target = line[4:].strip()
        resolved_value = evaluate_expression(target, line_num)
        if resolved_value is not None:
            print(resolved_value)
        return

    print(f"\u274c Syntax Error (Line {line_num}): Unknown instruction '{line}'.")


def start_repl():
    """Live Interactive Shell Mode (REPL)"""
    print("\U0001f680 Welcome to the pzcode Interactive Terminal! (v1.4)")
    print("Type 'help' for documentation, 'clear' to clear screen, 'exit' to quit.\n")
    
    line_num = 1
    while True:
        try:
            user_input = input("pzcode> ").strip()
            
            if user_input.lower() == "exit":
                print("Goodbye!")
                break
                
            if user_input:
                execute_line(user_input, line_num)
                line_num += 1
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break


def run_file():
    """File processing execution mode."""
    if len(sys.argv) < 2:
        start_repl()
        return

    filename = sys.argv[1]

    if not filename.endswith('.pzc'):
        print("\u274c Error: pzcode source files must end with the '.pzc' extension.")
        return

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        for line_num, line in enumerate(lines, 1):
            execute_line(line.strip(), line_num)
            
    except FileNotFoundError:
        print(f"\u274c Error: Could not find file '{filename}'.")


if __name__ == "__main__":
    run_file()
