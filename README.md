# IndentSyntax
Indentation syntax for C-style languages and Ruby/Lua style.
This project allows you to write with indentation syntax in any language that uses C-style curly braces,
or `end` like Ruby, Lua and Julia.

# Examples:

## Rust

```rust
fn main():
    println!("Hello World!");

```

## C

```c
#include <stdio.h>
int main():
    puts("Hello World!");

```

## Lua

```lua
local function hello()
    if true then
        print("Hello world!")
    else
        print("Demonstrating else works, too.")

```

# Usage:
The usage is pretty simple. 
For **C-style** scoping, using `:` followed by a newline results in an opening brace.
For **Ruby and Lua** scoping, there's nothing like that.

In **both**, unindenting leads to respective scope closes.
Indent as you would per normal, for C-style use `:` instead of `{`, and everything should work just fine.

The interface to the application is very friendly and simple, and there's no need to explain it.

# Errors and warnings:
## Warnings:

* `Warning: no new line at end of file`
There is no new line at the end of the file, which is handled by the project.
It is encouraged to add a new line at the end of the file, though.
This hints there may be unexpected behaviour.
**Fix:** just add an empty new line.

## Errors:
* `invalid indentation`
Your indentation is not a multiple of the indent size you gave. This makes no sense to IndentSyntax, or orthodox
indentation.
**Fix:** review how many spaces you added.

# Spaces vs Tabs
To keep this simple, spaces are preferred. Tabs work, too but are not recommended.
Tabs are all converted to four spaces.

# Bad output
Unfortunately, bad output can occur. But there are some reasons this occurs.
This includes unnecessary use of whitespace.
**Bad:**
```lua
print("Hello")
    -- comment used to show there are some unnecessary spaces here.
print("World!")
```
**Good:**
```lua
print("Hello")
-- comment used to show there is no unnecessary spacing.
print("World!")
```

This also means you have to indent empty lines when relevant. For example,
```rust
fn main():
// BAD (again, comment used to show indent)
    println!("Hello World!")
```
```rust
fn main():
    // GOOD (again, comment used to show indent)
    println!("Hello World!")
```
