# cspell:ignore rangle rdquo ldquo

import io

import pyperclip  # type: ignore

USE_ENTITIES = True

LINE_LENGTH = 90

output = io.StringIO()

text = pyperclip.paste()
text = text.strip()

while "  " in text:
    text = text.replace("  ", " ")

if text.startswith('"'):
    text = text[1:]

if text.endswith('"'):
    text = text[:-1]

text = text.replace('",', " ")
text = text.replace("\r", " ")
text = text.replace("\n", " ")

while '"' in text:
    text = text.replace('"', "&ldquo;", 1)
    text = text.replace('"', "&rdquo;", 1)

# text = text.replace(' "', " ")
# text = text.replace('"', "")

if USE_ENTITIES:
    text = text.replace("|", "&vert;")
    text = text.replace("⟩", "&rangle;")
    text = text.replace("π", "&pi;")
    text = text.replace("θ", "&theta;")
    text = text.replace("φ", "&phi;")

while "  " in text:
    text = text.replace("  ", " ")

text = text.strip()

if text[-1] not in [".", "!", "?", ">"]:
    print(text[-1])
    text += "."

text = text.replace("<p> ", "<p>")
text = text.replace("</p> ", "</p>")
text = text.replace(" <p>", "<p>")
text = text.replace(" </p>", "</p>")

new_text_list: list[str] = []

while len(text) > LINE_LENGTH:
    position = LINE_LENGTH
    while text[position] != " ":
        position -= 1
    assert position > 0
    new_text = text[:position].strip()
    new_text_list.append('"' + new_text + '"')
    text = text[position:].strip()

text = text.strip()
if text:
    new_text_list.append('"' + text + '"')

# os.system("cls")

print("[")
reflowed_text = 12 * " " + f",\n{12 * ' '}".join(new_text_list)
print(reflowed_text)
print(reflowed_text, file=output)
print("]")

result = output.getvalue().rstrip()
pyperclip.copy(result)
output.close()

print(f"\nText length = {len(reflowed_text)}")
