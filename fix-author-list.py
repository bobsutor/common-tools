# cspell:ignore rangle

import io
import json
import sys

import pyperclip  # type: ignore

output = io.StringIO()

text = pyperclip.paste()
text = text.strip()

while "  " in text:
    text = text.replace("  ", " ")

text = text.replace("\r", "")

new_text_list: list[str] = [t for t in text.split("\n") if t]
print(json.dumps(new_text_list, indent=4))
print(json.dumps(new_text_list, indent=4), file=output)
result = output.getvalue().rstrip()
pyperclip.copy(result)
output.close()
