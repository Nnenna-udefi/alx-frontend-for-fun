#!/usr/bin/python3
"""Script that contains markdown to html"""
import sys
import os
import re


if __name__ == '__main__':
    """
        sys.argv[1] = markdown file
        sys.argv[2] = output file
    """
    if len(sys.argv) < 2:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(markdown_file):
        print('Missing {}'.format(markdown_file), file=sys.stderr)
        exit(1)

    # Read the Markdown file and convert it to HTML
    with open(markdown_file, encoding="utf-8") as file:
        html_content = ""
        for line in file:
            # Check for Markdown headings
            match = re.match(r"^(#+) (.*)$", line)
            if match:
                level = len(match.group(1))
                heading_text = match.group(2)
                html_content += '<h{}>{}</h{}>\n'.format(level,
                                                         heading_text, level)
            else:
                html_content += line

    # Write the HTML output to a file
    with open(output_file, "w", encoding="utf-8") as html:
        html.write(html_content)
