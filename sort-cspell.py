import io

import pyperclip  # type: ignore

LINE_LENGTH = 70

CSPELL_PREFIX = "# cspell:ignore"

output = io.StringIO()

text = pyperclip.paste()

text_list = text.replace(CSPELL_PREFIX, " ").split()
text_list.sort(key=str.casefold)

line = ""

for word in text_list:
    line = f"{line} {word}"
    if len(line) > LINE_LENGTH:
        print(f"{CSPELL_PREFIX}{line}", file=output)
        line = ""

if line:
    print(f"{CSPELL_PREFIX}{line}", file=output)

result = output.getvalue().rstrip()

pyperclip.copy(result)
output.close()
