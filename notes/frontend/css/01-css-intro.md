# CSS Course — Day 1 Notes


---


## Course Syllabus Overview


| Day | Topics |
|-----|--------|
| **Day 1** | CSS Introduction, How CSS Works, Syntax, Selectors, Colors, Units, Text Styling, Box Model |
| **Day 2** | Backgrounds, Borders, Margin vs Padding, Display, Position, Flexbox, Basic Responsive Design |
| **Day 3** | Advanced Selectors, Pseudo-classes, Pseudo-elements, Transitions, Animations, Grid, Best Practices |


---


## Part 1 — What is CSS?


CSS stands for **Cascading Style Sheets**. It is used to control the **look and layout** of HTML elements on a web page.[web:1][web:4]


If HTML builds the structure of a page, CSS makes that structure **beautiful, readable, and properly arranged**.[web:1]


### Analogy: Dressing a Human Body
- **HTML** is the body and skeleton.
- **CSS** is the clothes, hairstyle, colors, shoes, and overall appearance.
- Without CSS, the page still exists — but it looks plain and unorganized.[web:1]


---


## Part 2 — How CSS Works


When the browser loads an HTML page, it also reads the CSS rules and applies them to matching HTML elements.[web:1][web:2]


```text
Browser loads HTML
        ↓
Browser reads CSS
        ↓
CSS selectors match HTML elements
        ↓
Browser applies styles
        ↓
Final styled page appears on screen
```


### Important Idea
A CSS rule has two main parts:
1. **Selector** → which element to target
2. **Declaration** → what style to apply[web:2][web:4]


Example:
```css
p {
  color: blue;
  font-size: 18px;
}
```


Here:
- `p` is the selector
- `color` and `font-size` are properties
- `blue` and `18px` are values[web:4]


---


## Part 3 — Ways to Add CSS


There are **3 ways** to add CSS to HTML.


### 1. Inline CSS
```html
<p style="color: red;">Hello World</p>
```


- Written directly inside the HTML tag
- Useful for testing
- Not recommended for real projects because it becomes hard to manage


### 2. Internal CSS
```html
<head>
  <style>
    p {
      color: green;
    }
  </style>
</head>
```


- Written inside the `<style>` tag in the `<head>`
- Good for small pages


### 3. External CSS
```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
```


- CSS is written in a separate `.css` file
- Best method for real websites
- Keeps HTML clean and reusable


> **Best Practice:** Use external CSS for almost all real-world projects.


---


## Part 4 — CSS Syntax


### Basic Syntax
```css
selector {
  property: value;
}
```


Example:
```css
h1 {
  color: purple;
  text-align: center;
}
```


### Multiple Declarations
```css
p {
  color: #333;
  font-size: 16px;
  line-height: 1.6;
}
```


### Syntax Rules
- Selector comes first
- Properties go inside curly braces `{ }`
- Each property-value pair ends with `;`
- Property and value are separated by `:`


---


## Part 5 — CSS Selectors


Selectors are used to choose which HTML elements should get styles.[web:2]


### 1. Element Selector
Targets all tags of the same type.
```css
p {
  color: blue;
}
```


### 2. ID Selector
Targets one unique element.
```css
#title {
  color: red;
}
```


```html
<h1 id="title">My Website</h1>
```


### 3. Class Selector
Targets multiple elements with the same class.
```css
.highlight {
  background-color: yellow;
}
```


```html
<p class="highlight">Important text</p>
```


### 4. Universal Selector
Targets all elements.
```css
* {
  margin: 0;
  padding: 0;
}
```


### 5. Group Selector
Applies the same styles to multiple selectors.
```css
h1, h2, p {
  font-family: Arial, sans-serif;
}
```


### 6. Descendant Selector
Targets elements inside another element.
```css
div p {
  color: green;
}
```


### 7. Child Selector
Targets direct children only.
```css
ul > li {
  color: navy;
}
```


### Selector Summary


| Selector | Example | Meaning |
|----------|---------|---------|
| Element | `p` | Selects all `<p>` tags |
| ID | `#header` | Selects element with id `header` |
| Class | `.btn` | Selects all elements with class `btn` |
| Universal | `*` | Selects everything |
| Group | `h1, p` | Selects multiple elements |
| Descendant | `div p` | `<p>` inside `<div>` |
| Child | `ul > li` | Direct `<li>` children of `<ul>` |


---


## Part 6 — Colors in CSS


CSS lets you apply colors in different formats.[web:1]


### 1. Color Name
```css
p {
  color: red;
}
```


### 2. HEX
```css
p {
  color: #ff0000;
}
```


### 3. RGB
```css
p {
  color: rgb(255, 0, 0);
}
```


### 4. RGBA
```css
p {
  color: rgba(255, 0, 0, 0.5);
}
```


- `a` means alpha (transparency)
- Value goes from `0` to `1`


### Background Color
```css
body {
  background-color: #f5f5f5;
}
```


---


## Part 7 — Units in CSS


CSS uses units to define size, spacing, and layout.


### Common Units


| Unit | Meaning | Example |
|------|---------|---------|
| `px` | Pixels | `font-size: 16px;` |
| `%` | Percentage | `width: 50%;` |
| `em` | Relative to parent font size | `padding: 2em;` |
| `rem` | Relative to root font size | `font-size: 1.5rem;` |
| `vh` | Viewport height | `height: 100vh;` |
| `vw` | Viewport width | `width: 100vw;` |


### Beginner Rule
- Use `px` when starting
- Learn `rem` and `%` for responsive design later


---


## Part 8 — Text Styling


CSS gives full control over text appearance.[web:1]


### Common Text Properties
```css
p {
  color: #333;
  font-size: 18px;
  font-family: Arial, sans-serif;
  font-weight: bold;
  font-style: italic;
  text-align: center;
  text-decoration: underline;
  line-height: 1.6;
  letter-spacing: 1px;
}
```


### Text Property Reference


| Property | Purpose |
|----------|---------|
| `color` | Text color |
| `font-size` | Text size |
| `font-family` | Font style |
| `font-weight` | Boldness |
| `font-style` | Italic text |
| `text-align` | Left, right, center |
| `text-decoration` | Underline, line-through, none |
| `line-height` | Space between lines |
| `letter-spacing` | Space between letters |


### Example
```css
h1 {
  text-align: center;
  color: darkblue;
  text-transform: uppercase;
}
```


---


## Part 9 — Backgrounds


CSS can style the background of any element.


### Background Color
```css
div {
  background-color: lightblue;
}
```


### Background Image
```css
body {
  background-image: url("bg.jpg");
}
```


### Useful Background Properties
```css
body {
  background-image: url("bg.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
}
```


| Property | Purpose |
|----------|---------|
| `background-color` | Solid background color |
| `background-image` | Adds image |
| `background-repeat` | Repeats or not |
| `background-size` | Controls image size |
| `background-position` | Sets image position |


---


## Part 10 — The Box Model


Every HTML element is treated like a rectangular box in CSS.[web:1]


### The 4 Parts of Box Model
1. **Content** → actual text/image
2. **Padding** → space inside the box
3. **Border** → line around the box
4. **Margin** → space outside the box


### Analogy: Mobile Phone Box
- **Content** = phone
- **Padding** = soft cushion inside the box
- **Border** = cardboard box wall
- **Margin** = empty space between this box and another box


### Example
```css
div {
  width: 300px;
  padding: 20px;
  border: 2px solid black;
  margin: 30px;
}
```


---


## Part 11 — Width and Height


You can control the size of elements.


```css
div {
  width: 300px;
  height: 150px;
}
```


### Useful Notes
- `width` controls horizontal size
- `height` controls vertical size
- Too much fixed height can break content if text becomes larger


---


## Part 12 — Borders


Borders add outlines around elements.


```css
div {
  border: 2px solid blue;
}
```


### Separate Border Properties
```css
div {
  border-width: 2px;
  border-style: solid;
  border-color: red;
}
```


### Border Radius
```css
button {
  border-radius: 10px;
}
```


This makes corners rounded.


---


## Part 13 — Margin and Padding


These are two of the most confusing CSS concepts for beginners.


### Padding
Space **inside** the border.


### Margin
Space **outside** the border.


### Example
```css
div {
  padding: 20px;
  margin: 30px;
}
```


### Shortcut
```css
div {
  margin: 10px 20px 30px 40px;
}
```


Order:
- top
- right
- bottom
- left


### Easy Memory Trick
- **Padding** = personal space inside
- **Margin** = distance from others outside


---


## Part 14 — Hands-On Practice


Create a simple styled profile card using only Day 1 CSS concepts.


### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Profile Card</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <div class="card">
    <h1>Arjun Sharma</h1>
    <p>Frontend Developer</p>
  </div>

</body>
</html>
```


### CSS
```css
body {
  background-color: #f2f2f2;
  font-family: Arial, sans-serif;
}

.card {
  width: 300px;
  background-color: white;
  padding: 20px;
  margin: 50px auto;
  border: 1px solid #ccc;
  text-align: center;
}

.card h1 {
  color: #222;
}

.card p {
  color: #666;
}
```


---


## Day 1 — Quick Reference Cheat Sheet


```text
CSS BASICS         SELECTORS          TEXT               BOX MODEL
────────────       ──────────         ──────────         ─────────────
selector {}        p                  color              content
property:value     .class             font-size          padding
external CSS       #id                font-family        border
internal CSS       *                  text-align         margin
inline CSS         div p              line-height        width/height

COLORS             BACKGROUNDS        BORDERS            UNITS
────────────       ─────────────      ─────────────      ─────────────
red                background-color   border             px
#ff0000            background-image   border-radius      %
rgb()              background-size                        rem
rgba()             background-repeat                      em
                   background-position                    vh/vw
```