# HTML Course — Day 1 Notes

---

## Course Syllabus Overview

| Day | Topics |
|-----|--------|
| **Day 1** | Frontend Introduction, How the Web Works, HTML Fundamentals, Text & Lists, Links & Images, Tables |
| **Day 2** | HTML Forms, Semantic HTML5, Multimedia, Meta tags, SEO basics, HTML best practices |
| **Day 3** | Advanced HTML, Accessibility (ARIA), HTML + CSS integration intro, HTML + JS integration intro, Project |

---

## Part 1 — What is Frontend Development?

When you open any website, you're looking at the **frontend** — everything visible and interactive in the browser.

The three technologies that power every frontend are:

```
HTML  →  Structure   (the skeleton)
CSS   →  Styling     (the skin & clothes)
JS    →  Behaviour   (the muscles & brain)
```

### Analogy: Building a House
- **HTML** is the bricks, walls, doors, and windows — the raw structure.
- **CSS** is the paint, tiles, furniture, and lighting — how it looks.
- **JavaScript** is the electricity, plumbing, and automation — what it *does*.

---

## Part 2 — How Does the Web Work?

```
User types URL in browser
        ↓
Browser sends HTTP Request to a Server
        ↓
Server responds with HTML file
        ↓
Browser parses HTML → builds DOM tree
        ↓
Browser fetches linked CSS → applies styles
        ↓
Browser fetches linked JS → runs scripts
        ↓
Final page renders on screen
```

### Key Terms
| Term | Meaning |
|------|---------|
| **Browser** | Chrome, Firefox, Edge — software that renders HTML |
| **Server** | A computer that stores and sends website files |
| **HTTP/HTTPS** | Protocol (rules) for sending data over the web |
| **URL** | Address of a web resource |
| **DOM** | Document Object Model — the browser's live tree of HTML elements |

> **Important:** HTML is not a programming language. It is a **markup language** — it describes structure and meaning, not logic.

---

## Part 3 — Introduction to HTML

### What is HTML?
**HyperText Markup Language** — uses **tags** to label pieces of content so the browser knows what each part is.

### How Tags Work
```html
<tagname> content </tagname>
```
- **Opening tag:** `<tagname>`
- **Content:** text, images, or other tags
- **Closing tag:** `</tagname>`

### Self-Closing Tags
Some tags have no content and close themselves:
```html
<br>       <!-- line break -->
<hr>       <!-- horizontal rule -->
<img>      <!-- image -->
<input>    <!-- form input -->
```

---

## Part 4 — HTML Boilerplate (Every File Starts Here)

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Page</title>
  </head>
  <body>

    <!-- Your visible content goes here -->

  </body>
</html>
```

### Line-by-line Explanation

| Line | What it does |
|------|-------------|
| `<!DOCTYPE html>` | Tells the browser this is an HTML5 document |
| `<html lang="en">` | Root element; `lang` helps screen readers and search engines |
| `<head>` | Container for metadata — NOT visible on page |
| `<meta charset="UTF-8">` | Supports all characters including ₹, é, ñ, etc. |
| `<meta name="viewport" ...>` | Makes the page responsive on mobile devices |
| `<title>` | Text shown on the browser tab |
| `<body>` | Everything visible on the page lives here |

> **Always write this boilerplate first.** Skipping it causes rendering quirks across browsers.

---

## Part 5 — Headings

HTML has **6 levels** of headings — `<h1>` to `<h6>`.

```html
<h1>Main Page Title</h1>
<h2>Section Heading</h2>
<h3>Sub-section</h3>
<h4>Sub-sub-section</h4>
<h5>Rarely used</h5>
<h6>Smallest heading</h6>
```

### Rules
- Use **only one `<h1>`** per page — it represents the main topic.
- Use headings in **order** (don't skip from `h1` to `h4`).
- Headings are for **structure**, not for making text big (use CSS for size).

---

## Part 6 — Paragraphs & Text Formatting

### Paragraph
```html
<p>This is a paragraph. The browser adds space above and below it automatically.</p>
```

### Inline Text Tags
```html
<strong>Bold — indicates importance</strong>
<em>Italic — indicates emphasis</em>
<u>Underline</u>
<mark>Highlighted text</mark>
<small>Smaller text</small>
<del>Strikethrough — deleted content</del>
<sup>Superscript: x<sup>2</sup></sup>
<sub>Subscript: H<sub>2</sub>O</sub>
<code>Inline code: console.log()</code>
```

### Line Break vs Paragraph
```html
<p>Line one.<br>Line two is in the same paragraph.</p>

<p>This starts a brand new paragraph with spacing above and below.</p>
```

### Horizontal Rule
```html
<hr>  <!-- draws a horizontal dividing line -->
```

---

## Part 7 — Lists

### Unordered List (bullet points)
```html
<ul>
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
</ul>
```

### Ordered List (numbered)
```html
<ol>
  <li>Install VS Code</li>
  <li>Create index.html</li>
  <li>Write your first tag</li>
</ol>
```

### Ordered List — Custom Start & Type
```html
<ol start="5">     <!-- starts counting from 5 -->
<ol type="A">      <!-- A, B, C... -->
<ol type="i">      <!-- i, ii, iii... -->
<ol reversed>      <!-- counts down -->
```

### Nested List
```html
<ul>
  <li>Frontend
    <ul>
      <li>HTML</li>
      <li>CSS</li>
    </ul>
  </li>
  <li>Backend</li>
</ul>
```

### Description List
```html
<dl>
  <dt>HTML</dt>
  <dd>Structure of a web page</dd>

  <dt>CSS</dt>
  <dd>Styling and visual design</dd>
</dl>
```

---

## Part 8 — Links (Anchor Tag)

The `<a>` tag creates hyperlinks.

```html
<a href="https://www.google.com">Visit Google</a>
```

### href Values

| Type | Example |
|------|---------|
| External URL | `href="https://example.com"` |
| Internal page | `href="about.html"` |
| Section on same page | `href="#contact"` |
| Email | `href="mailto:hello@example.com"` |
| Phone | `href="tel:+919876543210"` |

### target Attribute
```html
<a href="https://example.com" target="_blank">Opens in new tab</a>
```

| Value | Behaviour |
|-------|-----------|
| `_self` | Same tab (default) |
| `_blank` | New tab |

### Anchor to a Section on the Same Page
```html
<!-- The link -->
<a href="#about">Go to About</a>

<!-- The target section -->
<section id="about">
  <h2>About Us</h2>
</section>
```

### Image as a Link
```html
<a href="https://example.com">
  <img src="logo.png" alt="Company Logo">
</a>
```

---

## Part 9 — Images

```html
<img src="photo.jpg" alt="A sunset over the mountains" width="600" height="400">
```

### Attributes

| Attribute | Purpose |
|-----------|---------|
| `src` | Path to the image file |
| `alt` | Describes the image (accessibility + SEO) |
| `width` / `height` | Size in pixels |
| `title` | Tooltip on hover |
| `loading="lazy"` | Loads image only when scrolled into view |

### Image Sources
```html
<!-- From same folder -->
<img src="cat.jpg" alt="A cat">

<!-- From a subfolder -->
<img src="images/cat.jpg" alt="A cat">

<!-- From an external URL -->
<img src="https://example.com/cat.jpg" alt="A cat">
```

> **Never leave `alt` empty** unless the image is purely decorative (`alt=""`). Screen readers rely on it.

### Supported Formats

| Format | Use case |
|--------|----------|
| `.jpg` | Photos |
| `.png` | Logos, icons, transparency |
| `.gif` | Simple animations |
| `.svg` | Scalable icons & illustrations |
| `.webp` | Modern format — smaller file, high quality |

---

## Part 10 — Tables

Tables are for **tabular data** — never for page layout.

### Basic Table Structure
```html
<table border="1">
  <thead>
    <tr>
      <th>Name</th>
      <th>Age</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Arjun</td>
      <td>25</td>
      <td>Pune</td>
    </tr>
    <tr>
      <td>Priya</td>
      <td>28</td>
      <td>Mumbai</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="3">End of data</td>
    </tr>
  </tfoot>
</table>
```

### Tags Reference

| Tag | Purpose |
|-----|---------|
| `<table>` | Wraps the entire table |
| `<thead>` | Header section |
| `<tbody>` | Body/data section |
| `<tfoot>` | Footer section |
| `<tr>` | Table row |
| `<th>` | Header cell (bold + centered by default) |
| `<td>` | Data cell |

### Spanning Cells

```html
<!-- Cell spans 2 columns -->
<td colspan="2">Merged across 2 columns</td>

<!-- Cell spans 3 rows -->
<td rowspan="3">Merged across 3 rows</td>
```

---

## Part 11 — HTML Attributes (Common Ones)

Attributes give extra information to tags. They always go in the **opening tag**.

```html
<tag attribute="value">content</tag>
```

### Global Attributes (work on any tag)

| Attribute | Purpose |
|-----------|---------|
| `id` | Unique identifier for the element |
| `class` | Used by CSS and JS to target groups |
| `style` | Inline CSS (avoid in production) |
| `title` | Tooltip on hover |
| `hidden` | Hides the element |
| `contenteditable` | Makes content editable in browser |
| `data-*` | Custom data attributes |

```html
<p id="intro" class="highlight" title="Welcome message">Hello World!</p>

<div data-user-id="42" data-role="admin">User Panel</div>
```

---

## Part 12 — Comments

```html
<!-- This is a comment. It is NOT visible in the browser. -->

<!--
  Multi-line comment.
  Useful for notes or temporarily hiding code.
-->
```

---

## Part 13 — HTML Entities

Some characters have special meaning in HTML and must be written as entities.

| Character | Entity |
|-----------|--------|
| `<` | `&lt;` |
| `>` | `&gt;` |
| `&` | `&amp;` |
| `"` | `&quot;` |
| `©` | `&copy;` |
| `®` | `&reg;` |
| non-breaking space | `&nbsp;` |
| `₹` | `&#8377;` |

```html
<p>5 &lt; 10 and 10 &gt; 5</p>
<p>Copyright &copy; 2025 My Company</p>
<p>Price: &#8377;999</p>
```

---

## Day 1 — Hands-On Practice Project

Build a **personal profile page** using only Day 1 concepts.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Arjun Sharma — Profile</title>
</head>
<body>

  <h1>Arjun Sharma</h1>
  <img src="profile.jpg" alt="Arjun Sharma's photo" width="150">
  <p>
    <strong>Full Stack Developer</strong> with 5 years of experience.<br>
    Passionate about building clean, accessible web applications.
  </p>

  <hr>

  <h2>Skills</h2>
  <ul>
    <li>HTML &amp; CSS</li>
    <li>JavaScript</li>
    <li>React</li>
    <li>Node.js</li>
  </ul>

  <h2>Experience</h2>
  <table border="1">
    <thead>
      <tr>
        <th>Company</th>
        <th>Role</th>
        <th>Duration</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>TechCorp</td>
        <td>Frontend Developer</td>
        <td>2021 – Present</td>
      </tr>
      <tr>
        <td>WebStudio</td>
        <td>Junior Developer</td>
        <td>2019 – 2021</td>
      </tr>
    </tbody>
  </table>

  <h2>Contact</h2>
  <p>
    <a href="mailto:arjun@example.com">arjun@example.com</a> |
    <a href="tel:+919876543210">+91 98765 43210</a> |
    <a href="https://github.com/arjun" target="_blank">GitHub</a>
  </p>

  <hr>
  <p><small>&copy; 2025 Arjun Sharma</small></p>

</body>
</html>
```

---

## Day 1 — Quick Reference Cheat Sheet

```
STRUCTURE         TEXT              LISTS           LINKS & IMAGES
────────────      ────────────      ──────────      ──────────────
<!DOCTYPE html>   <h1>–<h6>        <ul>            <a href="">
<html>            <p>              <ol>            <img src="" alt="">
<head>            <br>             <li>
<body>            <hr>             <dl>            TABLES
<title>           <strong>         <dt>            ──────────────
<meta>            <em>             <dd>            <table>
                  <mark>                           <thead><tbody><tfoot>
GLOBAL ATTRS      <small>          ENTITIES        <tr><th><td>
────────────      <del>            ──────────      colspan rowspan
id  class         <sup><sub>       &lt; &gt;
style  title      <code>           &amp; &copy;
data-*                             &nbsp; &#8377;
```

---
