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

            # check for unordered list
            match_list = re.match(r"^\s*- (.*)$", line)
            if match_list:
                if not in_list:
                    """
                        intheList is a flag to track whether a list is being
                        procesed and adds <ul> opening and closing tags
                    """
                    html_content += '<ul>\n'
                    in_list = True
                list_item = match_list.group(1)
                html_content += "    <li>{}</li>".format(list_item)

            else:
                if in_list:
                    html_content += "</ul>\n"
                    in_list = False
                html_content += line

        # Close any open unordered list at the end
        if in_list:
            html_content += "</ul>\n"

    # Write the HTML output to a file
    with open(output_file, "w", encoding="utf-8") as html:
        html.write(html_content)
