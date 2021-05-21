# Hyper Text Markup Language

Hyper Text Markup Language, or HTML, is the language used to create a website.

---

## Document Object Model

HTML is used by browsers to create a Document Object Model, or DOM.
The DOM is a tree-like structure that organized elements of a webpage.
An example DOM might look like:
```
HTML
|
|-- Header
|   |-- Logo
|   `-- Title
|
|-- Main
|   `-- Article
|       |-- SubHeader
|       |-- Content
|       `-- Summary
|
`-- Footer
    |-- Links
    |-- Copyright
    `-- Contact Information
```

This is rendered in the browser to create a website.

---

## Tags

HTML code consists of tags.

### Types
There are three types of tags:

1. Opening tags `<div>`
2. Closing tags `</div>`
3. Self-Closing tags `<div />`

An opening tag MUST have a closing tag. 

An example of these might look like:

```html
<form>
    <label>Email:</label>
    <input name="email" />
</form>
```

Opening and closing are the most common types,
only a few tags are self closing.

### Names

Different tags have different names and server different purposes.

Names are the content that go inside the tag:
```html
<header></header>
<main></main>
```

Common Names include:

- **head**: contains metadata

- **body**: contains the visible content

    - **header**: used to create headers
    
    - **main**: holds the majority of the page content

        - **div**: wildcard, good for any use

        - **ol**: ordered list (1, 2, 3)

        - **ul**: unordered list (*, *, *)

        - **li**: list item

        - **form**: form for inputs

            - **input**: input field, versatile

            - **textarea**: multi-line text input
        
        - **button**: button, great for javascript functionality

    - **h1**, **h2**, **h3**, **h4**, **h5**, **h6**: header text, largest to smallest

    - **p**: paragraph text

    - **a**: hyperlink

    - **br**: single line break

    - **script**: area for javascript code

    - **style**: area for css styling

A special tag called a comment tag can be multi line and is as follows:
```html
<!-- Single Line Comment -->

<!--
    Multi
    Line
    Comment
-->
```

### Attributes

HTML tags have a number of attributes for modifying functionality.
Attributes can be used to target elements for CSS styling,
triggering JavaScript code, and other modifications.

These might look like:
```html
<div class="box"> </div>
```

Common attributes include:

- **class**: targets similar elementsn with CSS, JS

- **id**: targets one element with CSS, JS

- **style**: inline style (bad practice)

- **onclick**: triggers JS function

- **name**: name of input value

- **type**: type of input value (text, password, email, ...)

- **src**: source file (script, style)

- **href**: hyperlink url

---

## Boilerplate

Some important data is needed to create a proper HTML document.

```html
<!-- Specifies Document Type is HTML -->
<!DOCTYPE html>

<!-- Contains HTML code, sets language -->
<html lang="en">

    <!-- Contains Metadata -->
    <head>

        <!-- UTF-8 character encoding -->
        <meta charset="UTF-8">

        <!-- Internet Explorer Stuff -->
        <meta http-equiv="X-UA-Compatible" content="IE=edge">

        <!-- Sets Viewport to width (important for CSS) -->
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <!-- Title, shows up in browser tab -->
        <title>Document</title>

    </head>

    <!-- Contains visual data -->
    <body>
        
    </body>

</html>
```

---

## Importing

Not all code should be contained to the same document.
This makes for inefficient and difficult to read HTML.
Importing files lets the HTML, CSS, and JavaScript reside in
separate files.


The link tag in the document head can be used to import CSS.

```html
<head>
    <link rel="stylesheet" href="style.css" />
</head>
```

You can import JavaScript using the script tag.
This script tag can be anywhere,
but for efficiency and loading speed,
it's best to put at the very end of the body tag

```html
<body>
    <!-- ... --->
    <script src="script.js"><script>
</body>
```

