# Cascading StyleSheets

Cascading StyleSheets, or CSS, is a styling language for HTML

---

## Syntax

CSS consists of selectors, properties, and values.

### Comments

Comments in CSS are multi line, and are written as follows:
```css
/* Single Line Comment */

/*
    Multi
    Line
    Comment
*/
```

### Selectors

Selectors can target elements of an HTML document by their name,
class, and id.
Curly braces contain any property/value pairs relevant to the targeted element.

Name:
```css
div {

}
```

Class:
```css
.card {

}
```

Id:
```css
#first-card {

}
```

You can also target elements with multiple classes:

```html
<!--HTML-->
<button class="button primary"></button>
<button class="button secondary"></button>

<style>
    /* CSS */
    .button {
        /* set button shape and shadows */
    }

    .button.primary {
        /* set style for primary buttons */
    }

    .button.secondary {
        /* set style for secondary buttons */
    }

</style>
```

Everything:
```css
* {

}
```

### Properties and Values

Values are unique to each property.

Common values include:

- width:
    - width
- height: 
    - height
- margin: distance between element and parent element:
    - top
    - right
    - bottom
    - left
- padding: distance between element and its content:
    - top
    - right
    - bottom
    - left
- border:
    - width
    - type
    - color
- background:
    - color
- box-shadow:
    - x offset
    - y offset
    - blur
    - color

There are far too many properties to list here.
More can be found online.

Every property/value pair MUST end with a semi-colon.

### Colors

Colors can be written as RGB, RGBA, Hexadecimal, HSL, and HSLA.

- RGBA:
    - Red
    - Green
    - Blue
    - Alpla (opacity, optional)
- Hexadecimal
    - #450235FF
        - \#
        - 45 red
        - 02 green
        - 35 blue
        - FF opacity (optional)
- HSLA
    - Hue
    - Saturation
    - Lightness
    - Alpha (opacity, optional)

---

## Example

```html
<body>
    <div class="card">
        <p id="this-exact-text">This is some text</p>
    </div>

    <style>

        body {
            background: #202020;
        }

        .card {
            background: #303030;
            padding: 8px 8px 8px 8px;
            margin: 24px 24px 24px 24px;
            box-shadow: 8px 8px 8px #000000;
            border: 2px solid #FFFFFF;
        }

        #this-exact-text {
            color: #FFFFFF;
            font-weight: bold;
        }

    </style>
</body>
```