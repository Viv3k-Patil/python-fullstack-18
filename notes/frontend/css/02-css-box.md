# CSS Course — Day 2 Notes


---


## Part 1 — Revision of Day 1


Before learning layout, remember:
- CSS styles HTML elements
- Selectors choose elements
- Properties change appearance
- Box model controls spacing and size[web:1][web:2]


Day 2 moves from **appearance** to **layout and alignment**.


---


## Part 2 — Display Property


The `display` property controls how an element behaves in the page layout.[web:1]


### Common Values


| Value | Meaning |
|------|---------|
| `block` | Takes full width |
| `inline` | Takes only content width |
| `inline-block` | Inline but allows width/height |
| `none` | Hides element completely |


### Example
```css
span {
  display: block;
}
```


### Real Meaning
- `<div>` is block by default
- `<span>` is inline by default
- `display: none` removes the element from layout flow


---


## Part 3 — Position Property


Position controls where an element appears.


### Types of Position


| Value | Meaning |
|------|---------|
| `static` | Default normal flow |
| `relative` | Moves relative to original position |
| `absolute` | Moves relative to nearest positioned parent |
| `fixed` | Stays fixed on screen |
| `sticky` | Sticks when scrolling |


### Example
```css
.box {
  position: relative;
  top: 20px;
  left: 30px;
}
```


### Real-World Analogy
Think of a classroom:
- **static** = student sits in normal seat
- **relative** = student shifts slightly from seat
- **absolute** = student is placed based on classroom corner
- **fixed** = student glued to screen position
- **sticky** = student moves normally, then sticks at top


---


## Part 4 — Display Flex


Flexbox is a layout system designed for arranging items in **one dimension** — either row or column.[web:3][web:6]


### Why Flexbox?
Before Flexbox, alignment in CSS was difficult. Flexbox makes it much easier to align items, distribute space, and create responsive layouts.[web:3][web:6]


### Basic Flex Container
```css
.container {
  display: flex;
}
```


This makes child elements line up in a row by default.[web:3]


### Important Flex Properties


| Property | Purpose |
|----------|---------|
| `display: flex` | Turns element into flex container |
| `flex-direction` | Row or column |
| `justify-content` | Horizontal alignment |
| `align-items` | Vertical alignment |
| `gap` | Space between items |
| `flex-wrap` | Allows items to wrap |


### Example
```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
}
```


### Common Values
```css
justify-content: flex-start;
justify-content: center;
justify-content: space-between;

align-items: stretch;
align-items: center;
align-items: flex-start;
```


---


## Part 5 — Flex Direction


Flexbox can work in row or column direction.[web:3][web:6]


```css
.container {
  display: flex;
  flex-direction: row;
}
```


### Values
- `row` → left to right
- `column` → top to bottom
- `row-reverse`
- `column-reverse`


### Example
```css
.container {
  display: flex;
  flex-direction: column;
}
```


---


## Part 6 — Justify Content vs Align Items


This is one of the most important CSS layout topics.


### `justify-content`
Controls alignment on the **main axis**.[web:3][web:6]


### `align-items`
Controls alignment on the **cross axis**.[web:3][web:6]


If `flex-direction: row`
- main axis = horizontal
- cross axis = vertical


If `flex-direction: column`
- main axis = vertical
- cross axis = horizontal


### Example
```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
```


This centers content both horizontally and vertically.[web:3][web:6]


---


## Part 7 — Gap and Wrap


### Gap
Adds space between flex items.
```css
.container {
  display: flex;
  gap: 16px;
}
```


### Flex Wrap
Allows items to move to the next line if needed.
```css
.container {
  display: flex;
  flex-wrap: wrap;
}
```


This is useful when many items cannot fit in one row.[web:3]


---


## Part 8 — Styling Links


Links can be styled using CSS.


```css
a {
  color: blue;
  text-decoration: none;
}
```


### Link Pseudo-classes
```css
a:hover {
  color: red;
}

a:visited {
  color: purple;
}
```


### Common States
- `:hover` → when mouse is over element
- `:active` → when clicked
- `:visited` → visited links


---


## Part 9 — Styling Lists


Lists can be customized using CSS.


```css
ul {
  list-style-type: square;
}
```


### Remove Bullets
```css
ul {
  list-style: none;
}
```


### Add Spacing
```css
li {
  margin-bottom: 10px;
}
```


---


## Part 10 — Styling Tables


Tables can be made cleaner with CSS.


```css
table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ccc;
  padding: 10px;
  text-align: left;
}
```


### Zebra Striping
```css
tr:nth-child(even) {
  background-color: #f9f9f9;
}
```


This improves readability.


---


## Part 11 — Basic Responsive Design


Responsive design means making the layout adapt to different screen sizes.


### Viewport Meta Tag
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```


This helps pages scale correctly on mobile devices.


### Simple Responsive Rule
```css
img {
  max-width: 100%;
  height: auto;
}
```


This prevents images from overflowing the container.


### Media Query Introduction
```css
@media (max-width: 600px) {
  body {
    background-color: lightyellow;
  }
}
```


This means: apply styles only when screen width is 600px or less.


---


## Part 12 — Hands-On Practice Project


Build a simple **team cards layout** using Flexbox.


### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Team Cards</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <h1>Our Team</h1>

  <div class="team">
    <div class="card">
      <h2>Asha</h2>
      <p>Frontend Developer</p>
    </div>

    <div class="card">
      <h2>Rohan</h2>
      <p>Backend Developer</p>
    </div>

    <div class="card">
      <h2>Neha</h2>
      <p>UI Designer</p>
    </div>
  </div>

</body>
</html>
```


### CSS
```css
body {
  font-family: Arial, sans-serif;
  background: #f4f4f4;
  margin: 0;
  padding: 20px;
}

h1 {
  text-align: center;
}

.team {
  display: flex;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
}

.card {
  background: white;
  padding: 20px;
  width: 220px;
  border: 1px solid #ddd;
  text-align: center;
  border-radius: 8px;
}
```


---


## Day 2 — Quick Reference Cheat Sheet


```text
LAYOUT             FLEXBOX              POSITION            RESPONSIVE
────────────       ─────────────        ─────────────       ─────────────
display            display:flex         static             @media
block              flex-direction       relative           max-width
inline             justify-content      absolute           viewport
inline-block       align-items          fixed              height:auto
none               gap                  sticky

LINKS              LISTS                TABLES
────────────       ─────────────        ─────────────
a                  list-style           border-collapse
:hover             list-style-type      padding
:visited           margin               text-align
text-decoration                         nth-child(even)
```