# pyqb

For when you need those sweet, sweet QuickBasic ANSI interfaces!

Exposes several low-level commands for building that sweet, sweet terminal art
you loved from the 80s, without the overhead and foolish limitations and
"architecture" imposed by (n)curses. Set your terminal to DOS (Latin 1) and
start printing those ╔╦╛ characters!

## Usage

Remember QuickBasic? Color? Locate? CLS? They're all here!

### `** cls **`

Clear the terminal, and reset the cursor to `(0, 0)`.

### `** write ** *(string)*`

Write some characters, with no following new line.

