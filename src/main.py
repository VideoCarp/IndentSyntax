import indenter
# IMPORTANT: to learn how to use this, just take a look at README.md in the repo.
file = input("File path: ")
style = input("Ruby/Lua style? (no|yes): ")
indentsize = int(input("Number of spaces for indent?: "))
with open(file) as f:
    code = f.read()
if style.lower().startswith("y"):
    rubyluastyle = True
else:
    rubyluastyle = False

indenter.doindents(file, code, rubyluastyle, indentsize)
