import re

filename = "(EN)On the Reed-Muller codes.md"
with open(filename, 'r', encoding='utf-8') as file:
    pattern = re.compile(r'\$\$(.*?)\$\$', re.DOTALL)
    text = file.read()
    converted_text = pattern.sub(lambda m: f"$$ {m.group(1).replace(chr(10), ' ')} $$", text)

with open(filename, 'w', encoding='utf-8') as file:
    file.write(converted_text)

