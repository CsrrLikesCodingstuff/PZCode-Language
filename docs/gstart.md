# Getting Started

  ## Requirements

  PZCode requires:

  - Python 3.12 or newer
  - Windows, macOS, or Linux
  - A text editor

  No external Python packages are required to run the interpreter directly.

  ## Downloading PZCode

  Clone the repository:

  ```bash
  git clone https://github.com/CsrrLikesCodingstuff/PZCode-Language.git

  Open the project folder:

  cd PZCode-Language

  ## Starting the Interactive Interpreter

  Run:

  python interpreter.py

  You should see the PZCode prompt:

  pzcode>

  You can now type PZCode commands directly:

  say "Hello, world!"

  To close the interpreter, type:

  exit

  ## Creating a .pzc File

  PZCode source files must use the .pzc extension.

  Create a file named:

  hello.pzc

  Add this code:

  say "Hello from PZCode!"

  Save the file inside the project folder.

  ## Running a .pzc File

  Run the file with:

  python interpreter.py hello.pzc

  The interpreter reads and executes the .pzc file immediately.

  PZCode is interpreted, so it does not create a separate compiled file.

  ## Running an Example

  Example programs are stored in the examples folder.

  Run the Hello World example:

  python interpreter.py examples/helloworld.pzc

  Other examples include:

  examples/math.pzc
  examples/loops.pzc
  examples/ifelse.pzc
  examples/examplegameproj.pzc

  ## Running a File from the Interactive Interpreter

  Start the interpreter:

  python interpreter.py

  Then use the run command:

  run examples/helloworld.pzc

  ## Getting Help

  Inside the interactive interpreter, type:

  help

  You can also view help categories:

  help variables
  help input
  help logic
