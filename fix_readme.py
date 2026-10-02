import re

with open("README.md", "r") as f:
    content = f.read()

# Replace github.com/builtbyrahulX with github.com/builtbyrahulX
content = content.replace("github.com/builtbyrahulX", "github.com/builtbyrahulX")
# Replace builtbyrahulX@gmail.com with builtbyrahulX@gmail.com? The user might just want builtbyrahulX as email, I'll leave email alone or change it. Let's just change github related ones.
content = content.replace("username=builtbyrahulX", "username=builtbyrahulX")
content = content.replace("raw.githubusercontent.com/builtbyrahulX/builtbyrahulX", "raw.githubusercontent.com/builtbyrahulX/builtbyrahulX")

with open("README.md", "w") as f:
    f.write(content)
