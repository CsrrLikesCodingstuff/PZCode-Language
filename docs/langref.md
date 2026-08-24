Markdown
# Language Reference

PZCode programs are plain-text files that use the `.pzc` extension.

PZCode currently executes one command per line.

## Comments

Comments begin with `#`.

```pzc
# This line is ignored
say "This line is executed"
Empty lines are also ignored.

Values
PZCode supports:

Whole numbers

Text strings

Variables

Math expressions

Numbers can be written directly:

Kod snippet'i
say 42
Text must be surrounded by single or double quotation marks:

Kod snippet'i
say "Hello"
say 'Hello'
Variables
Variables store values.

Kod snippet'i
store 100 in score
store "Alex" in player_name
Variables can be used by referring to their names:

Kod snippet'i
say score
say player_name
The set command is an alias for store:

Kod snippet'i
set 100 in coins
Mathematics
PZCode supports these mathematical operators:

+ Addition

- Subtraction

* Multiplication

/ Division

% Remainder

Examples:

Kod snippet'i
store 10 + 5 in total
store 10 - 3 in difference
store 4 * 5 in product
store 20 / 4 in answer
store 10 % 3 in remainder
Variables can be used in expressions:

Kod snippet'i
store 100 in coins
store coins + 25 in new_coins
say new_coins
Input
Use ask to request input from the user:

Kod snippet'i
ask "What is your name? " in name
say name
Whole-number input is stored as an integer:

Kod snippet'i
ask "How old are you? " in age
say age
Other input is stored as text.

Conditions
Conditions use comparison operators.

Kod snippet'i
store 75 in score

if score >= 50: say "You passed!"
Supported comparison operators:

> Greater than

< Less than

== Equal to

!= Not equal to

>= Greater than or equal to

<= Less than or equal to

Conditions and their commands must be written on the same line.

Else Statements
An else command can be added to an if statement:

Kod snippet'i
if score >= 50: say "Passed!" else: say "Failed!"
Counted Loops
Use repeat to execute a command a specific number of times:

Kod snippet'i
repeat 3: say "Hello!"
The command being repeated must be written on the same line.

Repeat-While Loops
Use repeat while to continue executing a command while a condition is true:

Kod snippet'i
store 1 in count
repeat while count <= 5: store count + 1 in count
The interpreter has a safety limit of 1000 executions for a repeat while command. This helps prevent accidental infinite loops.

Random Numbers
Generate a random whole number with:

Kod snippet'i
random 1 to 6 in dice
say dice
The minimum and maximum values are included in the possible results.

Text Operations
Convert text to uppercase:

Kod snippet'i
upper "hello" in loud_text
say loud_text
Convert text to lowercase:

Kod snippet'i
lower "GOODBYE" in quiet_text
say quiet_text
Find the length of text:

Kod snippet'i
length "PZCode" in character_count
say character_count
Waiting
Pause the interpreter for a number of seconds:

Kod snippet'i
wait 2
Clearing the Screen
Clear the terminal:

Kod snippet'i
clear
On Windows, cls is also supported:

Kod snippet'i
cls
Source Files
PZCode source files must end with:

Plaintext
.pzc
For example:

hello.pzc

game.pzc

math_example.pzc
