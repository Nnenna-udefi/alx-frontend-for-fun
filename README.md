# Markdown to HTML
## Description
Markdown is awesome! All your README.md are made in Markdown, but do you know how GitHub are rendering them?

It’s time to code a Markdown to HTML!
## Tasks
### 0. Start a script
A script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name
Requirements:

If the number of arguments is less than 2: print in STDERR Usage: ./markdown2html.py README.md README.html and exit 1
If the Markdown file doesn’t exist: print in STDER Missing <filename> and exit 1
Otherwise, print nothing and exit 0

### Headings
Parsing Headings Markdown syntax for generating HTML:

Syntax: (you can assume it will be strictly this syntax)

Markdown	HTML generated
# Heading level 1	<h1>Heading level 1</h1>
## Heading level 2	<h2>Heading level 1</h2>
### Heading level 3	<h3>Heading level 1</h3>
#### Heading level 4	<h4>Heading level 1</h4>
##### Heading level 5	<h5>Heading level 1</h5>
###### Heading level 6	<h6>Heading level 1</h6>

## Unordered list
Parsing Unordered listing syntax for generating HTML:

Syntax: (you can assume it will be strictly this syntax)

Markdown:

- Hello
- Bye
HTML generated:
<ul>
    <li>Hello</li>
    <li>Bye</li>
</ul>

## Ordered list
Parsing Ordered listing syntax for generating HTML:

Syntax: (you can assume it will be strictly this syntax)

Markdown:

* Hello
* Bye
HTML generated:

<ol>
    <li>Hello</li>
    <li>Bye</li>
</ol>

## Paragraph text
Parsing paragraph syntax for generating HTML:

Syntax: (you can assume it will be strictly this syntax)

Markdown:

Hello

I'm a text
with 2 lines
HTML generated:

<p>
    Hello
</p>
<p>
    I'm a text
        <br />
    with 2 lines
</p>

## Bold and emphasis text
Parsing bold syntax for generating HTML:

Syntax: (you can assume it will be strictly this syntax)

| Markdown	| HTML generated |
| --------- | -------------- |
| **Hello** |	<b>Hello</b>   |
| __Hello__ |	<em>Hello</em> |

## Hashlib md5
Parsing bold syntax for generating HTML:

Syntax: (you can assume it will be strictly this syntax)

| Markdown	        | HTML generated	                 | description                                      |
| ----------------- | -------------------------------- | ------------------------------------------------ |
| [[Hello]]         | 8b1a9953c4611296a827abf8c47804d7 | convert in MD5 (lowercase) the content           |
| ((Hello Chicago)) |	Hello hiago	                     | remove all c (case insensitive) from the content |
