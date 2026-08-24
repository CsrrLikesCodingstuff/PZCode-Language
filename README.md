 # PZCode

  PZCode is a small programming language I made using Python.

  I created it as a beginner-friendly project to learn more about interpreters, programming languages, and how commands
  can be processed by code. PZCode uses simple English-like commands and `.pzc` source files.

  ## Features

  PZCode currently supports:

  - Printing messages and values
  - Variables
  - Basic math
  - User input
  - Conditions
  - `else` statements
  - Counted loops
  - `repeat while` loops
  - Random numbers
  - Text conversion
  - Text length checking
  - Waiting and clearing the screen
  - Running `.pzc` files from the interpreter
  - Interactive help commands

  ## Requirements

  You need:

  - Python 3
  - Windows, macOS, or Linux

  No external Python packages are required to run the interpreter.

  ## Getting Started

  Clone or download this project, then open a terminal in the project folder.

  Start the interactive PZCode terminal:

  ```text
  python interpreter.py
  ```

  You should see the PZCode prompt:

  ```text
  pzcode>
  ```

  You can now enter commands such as:

  ```text
  say "Hello, world!"
  ```

  Type `exit` to close the interpreter.

  ## Running a PZCode File

  PZCode files use the `.pzc` extension.

  Create a file such as `hello.pzc`:

  ```text
  say "Hello from PZCode!"
  ```

  Run it with:

  ```text
  python interpreter.py hello.pzc
  ```

  You can also run a file from inside the interactive terminal:

  ```text
  run hello.pzc
  ```

  ## Basic Commands

  ### Printing Text

  Use `say` to display text or values:

  ```text
  say "Hello, world!"
  ```

  `print` is also available as an alias:

  ```text
  print "This also works!"
  ```

  ### Variables

  Create or change a variable with `store`:

  ```text
  store 10 in score
  store "Alex" in name

  say score
  say name
  ```

  `set` is an alias for `store`:

  ```text
  set 100 in coins
  ```

  Show all currently stored variables:

  ```text
  show variables
  ```

  Delete a variable:

  ```text
  delete coins
  ```

  ### Math

  PZCode supports addition, subtraction, multiplication, division, and remainders:

  ```text
  store 10 + 5 in total
  store 10 - 3 in difference
  store 4 * 5 in product
  store 20 / 4 in answer
  store 10 % 3 in remainder

  say total
  ```

  Variables can also be used in calculations:

  ```text
  store 100 in coins
  store coins + 25 in new_coins
  say new_coins
  ```

  ### User Input

  Use `ask` to receive input from the user:

  ```text
  ask "What is your name? " in name
  say name
  ```

  Whole-number input is stored as an integer:

  ```text
  ask "How old are you? " in age
  say age
  ```

  Other input is stored as text.

  ### Conditions

  Use `if` to make decisions:

  ```text
  store 75 in score

  if score >= 50: say "You passed!"
  if score < 50: say "Try again."
  ```

  PZCode supports these comparison operators:

  ```text
  >     greater than
  <     less than
  ==    equal to
  !=    not equal to
  >=    greater than or equal to
  <=    less than or equal to
  ```

  You can also use `else`:

  ```text
  if score >= 50: say "Passed!" else: say "Failed!"
  ```

  ### Loops

  Repeat a command a fixed number of times:

  ```text
  repeat 3: say "Hello!"
  ```

  Repeat while a condition is true:

  ```text
  store 1 in count
  repeat while count <= 5: store count + 1 in count
  ```

  PZCode has a safety limit of 1000 executions for `repeat while` commands. This helps prevent accidental infinite
  loops.

  ### Random Numbers

  Create a random whole number:

  ```text
  random 1 to 6 in dice
  say dice
  ```

  ### Text Tools

  Convert text to uppercase:

  ```text
  upper "hello" in loud_text
  say loud_text
  ```

  Convert text to lowercase:

  ```text
  lower "GOODBYE" in quiet_text
  say quiet_text
  ```

  Find the length of text:

  ```text
  length "PZCode" in character_count
  say character_count
  ```

  ### Waiting and Clearing the Screen

  Pause for a number of seconds:

  ```text
  say "Starting..."
  wait 2
  say "Finished!"
  ```

  Clear the terminal:

  ```text
  clear
  ```

  `cls` can also be used on Windows.

  ### Comments

  Lines beginning with `#` are comments and are ignored:

  ```text
  # This is a comment
  say "This line will run"
  ```

  ## Example Projects

  Example `.pzc` programs are stored in the `examples` folder.

  They include examples for:

  - Hello World
  - Variables and math
  - Conditions
  - Loops
  - A small example game

  To run one, use its path from the project folder:

  ```text
  python interpreter.py ExampleProjs/helloworld.pzc
  ```

  ## Complete Example

  Here is a small game example for PZCode.

  ```text
  say "Welcome to the number game!"

  random 1 to 10 in secret
  ask "Guess a number from 1 to 10: " in guess

  if guess == secret: say "Correct!"
  if guess != secret: say "Nope.."

  say "The secret number was:"
  say secret
  ```

  ## Building an Executable

  If you want to build a Windows executable, install PyInstaller:

  ```text
  python -m pip install pyinstaller
  ```

  Then run:

  ```text
  python -m PyInstaller --onefile --name pz_interpreter --icon=pzcode.ico interpreter.py
  ```

  The executable will be created inside the `dist` folder.

  The `build`, `dist`, and PyInstaller `.spec` files are generated files and are ignored by Git.

  ## Current Design

  PZCode currently executes one command per line.

  Conditions and loops use single-line commands. Future versions may include:

  - Multi-line code blocks
  - Functions
  - Lists
  - More advanced expressions
  - Better error messages
  - More built-in commands
  - A more complete parser

  ## Why I Made PZCode

  I made PZCode as a learning project. I wanted to create something simple that feels like a programming language while
  also helping me understand how interpreters work.

  It is still a work in progress, but I plan to continue improving it and adding new features.

  ## License

  PZCode is licensed under the MIT License.

  Copyright (c) 2026 Iliketocode/CsrrLikesCodingstuff