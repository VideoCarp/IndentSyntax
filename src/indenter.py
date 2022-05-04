from os.path import realpath
def doindents(file, code, rubyluastyle=False, indentsize=4):
    def ws(line):
        stripped = line.strip()
        if stripped != "":
            return len(line[0:line.find(stripped)])
        else:
            return line.count(" ")

    code = code.replace("\t", " " * indentsize)
    ender = "end\n"
    if not rubyluastyle:
        code = code.replace(":\n", " {\n")
        ender = "}\n"
    lines = code.split("\n")
    previous_indent = 0
    # add EOF line
    if lines[len(lines) - 1].strip() != "":
        print("Warning: no line at end of file.")
        lines.append("")

    new_lines = []
    for index, line in enumerate(lines):
        indent = ws(line)
        if indent < previous_indent:
            stripped = line.strip()
            if stripped.startswith("else") or stripped.startswith("else if"):
                new_lines.append(line)
            else:
                times = (previous_indent - indent) / indentsize
                if type(times) != int:
                    print(
                        f"Error: invalid indentation at line {index}"
                        f"Indent not a multiple of {indentsize}."
                        f"In line:\n`{line}`"
                    )
                    return
                new_lines.append((ender * times) + line)
        else:
            new_lines.append(line)
        previous_indent = indent

    with open(f"done_{file}", "+w") as f:
        f.write("\n".join(new_lines))
        output = realpath(f)
    print(f"Output at `{output}'")
