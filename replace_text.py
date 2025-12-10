
import json
import re

file_path = r"c:\Users\MUHAMMAD OWAIS\Downloads\Surizai_letters_searching-main\Surizai_letters_searching-main\letters_from_docx.json"
target_line_content = '      "link": "C:\\\\Users\\\\MUHAMMAD OWAIS\\\\Downloads\\\\Surizai_letters_searching-main\\\\Surizai_letters_searching-main\\\\No"'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
count = 0
for line in lines:
    # Check if line has "text": value
    if '"text":' in line:
        # Preserve indentation (whitespace before "text")
        indentation = line[:line.find('"text":')]
        
        # Check for trailing comma
        has_comma = line.strip().endswith(',')
        
        # Construct new line
        new_line = target_line_content
        if has_comma:
            new_line += ','
        new_line += '\n'
        
        new_lines.append(new_line)
        count += 1
    else:
        new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Replaced {count} occurrences of 'text' with 'link'.")
