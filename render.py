import sys
import os
import re

def render(template_path, context):
    template = open(template_path, 'r').read()
    return template.format(**context).strip('"')

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 render.py <template_file>")
        sys.exit(1)

    template_path = sys.argv[1]

    if not template_path.endswith('.template'):
        print("Error: Template file must have a .template extension.")
        sys.exit(1)

    if not os.path.exists(template_path):
        print(f"Error: {template_path} does not exist.")
        sys.exit(1)

        
    context = {}
    settings = open("settings.py", 'r').read()
    for line in settings.splitlines():
        if line.startswith('#'):
            continue
        match = re.match(r'(\w+)\s*=\s*(.*)', line)
        if match:
            key, value = match.groups()
            context[key] = value.strip('"')

    rendered_html = render(template_path, context)

    output_file = template_path.replace('.template', '.html')
    open(output_file, 'w').write(rendered_html)

if __name__ == '__main__':
    main()
