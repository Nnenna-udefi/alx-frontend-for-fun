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
    if len(sys.argv) < 3:
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
        
        # Initialize the flags
        in_unorderedlist = False
        in_orderedlist = False
        in_paragraph = False
        
        for line in file:
            # check for the bold syntax
            line = line.replace('**', '<b>', 1)
            line = line.replace('**', '</b>', 1)
            line = line.replace('__', '<em>', 1)
            line = line.replace('__', '</em>', 1)

            
            length = len(line)
            # Check for Markdown headings
            match = re.match(r"^(#+) (.*)$", line)
            if match:
                level = len(match.group(1))
                heading_text = match.group(2)
                html_content += '<h{}>{}</h{}>\n'.format(level,
                                                         heading_text, level)

            # check for unordered list
            match_unorderedlist = re.match(r"^\s*- (.*)$", line)
            if match_unorderedlist:
                if not in_unorderedlist:
                    """
                        in_unorderedlist is a flag to track whether a list
                        is being procesed and adds <ul>
                        opening and closing tags
                    """
                    html_content += '<ul>\n'
                    in_unorderedlist = True
                list_item = match_unorderedlist.group(1)
                html_content += "    <li>{}</li>\n".format(list_item)
            if in_unorderedlist and not match_unorderedlist:
                html_content += "</ul>\n"
                in_unorderedlist = False

            # check for ordered list
            match_orderedlist = re.match(r"^\s*\* (.*)$", line)
            if match_orderedlist:
                if not in_orderedlist:
                    html_content += '<ol>\n'
                    in_orderedlist = True
                ordered_listitem = match_orderedlist.group(1)
                html_content += "    <li>{}</li>\n".format(ordered_listitem)
            if in_orderedlist and not match_orderedlist:
                html_content += "</ol>\n"
                in_orderedlist = False

            # check for paragraph
            if not (match or match_unorderedlist or match_orderedlist):
                if not in_paragraph and length > 1:
                    html_content += "<p>\n"
                    in_paragraph = True
                elif length > 1:
                    html_content += "<br/>\n"
                elif in_paragraph:
                    html_content += "</p>\n"
                    in_paragraph = False
                # paragraph_text = line.strip()
                # html_content += "    {}\n".format(paragraph_text)


            if length > 1:
                html_content += html_content
        # Close any open list at the end
        if in_unorderedlist:
            html_content += "</ul>\n"
        if in_orderedlist:
            html_content += "</ol>\n"
        # Close if any paragraph is open
        if in_paragraph:
            html_content += "</p>\n"

    # Write the HTML output to a file
    with open(output_file, "w", encoding="utf-8") as html:
        html.write(html_content)

    exit(0)
