# HTML Course — Day 2 Notes

---

## Quick Recap — Day 1 Covered
- HTML boilerplate, headings, paragraphs, text formatting
- Lists (ul, ol, dl), links, images, tables, global attributes, entities

---

## Part 1 — HTML Forms

Forms are how websites collect data from users — login pages, search bars, registration, checkout, contact pages. Every form has two key questions: **where does the data go?** (`action`) and **how is it sent?** (`method`).

```html
<form action="/submit" method="POST">
  <!-- form fields go here -->
  <button type="submit">Submit</button>
</form>
```

### `method` Values

| Method | When to use |
|--------|-------------|
| `GET` | Searching, filtering — data appears in the URL |
| `POST` | Login, registration, payments — data is hidden in request body |

### `action` Attribute
Points to the server-side URL that will process the form data. Leave empty (`action=""`) to submit to the same page.

---

## Part 2 — Input Types

The `<input>` tag is the most versatile form element. The `type` attribute controls what it looks like and how it behaves.

```html
<input type="text" name="username" placeholder="Enter your name">
```

### All Important Input Types

```html
<!-- Text -->
<input type="text">           <!-- single-line text -->
<input type="password">       <!-- masked text -->
<input type="email">          <!-- validates email format -->
<input type="number">         <!-- only numbers, with up/down arrows -->
<input type="tel">            <!-- telephone number -->
<input type="url">            <!-- validates URL format -->
<input type="search">         <!-- search box with clear button -->

<!-- Date & Time -->
<input type="date">           <!-- date picker -->
<input type="time">           <!-- time picker -->
<input type="datetime-local"> <!-- date + time together -->
<input type="month">          <!-- month + year picker -->
<input type="week">           <!-- week picker -->

<!-- Selection -->
<input type="checkbox">       <!-- tick box, multiple can be selected -->
<input type="radio">          <!-- one from a group -->
<input type="range">          <!-- slider (min, max, step) -->
<input type="color">          <!-- color picker -->

<!-- File & Hidden -->
<input type="file">           <!-- file upload -->
<input type="hidden">         <!-- invisible, holds data for server -->

<!-- Buttons -->
<input type="submit">         <!-- submits the form -->
<input type="reset">          <!-- clears all fields -->
<input type="button">         <!-- custom button (no default behaviour) -->
```

---

## Part 3 — Input Attributes

```html
<input
  type="text"
  name="username"
  id="username"
  value="John"
  placeholder="Enter name"
  required
  disabled
  readonly
  maxlength="50"
  minlength="3"
  min="1"
  max="100"
  step="5"
  pattern="[A-Za-z]+"
  autocomplete="off"
  autofocus
>
```

### Attribute Reference

| Attribute | Purpose |
|-----------|---------|
| `name` | Key sent to the server (required for form submission) |
| `id` | Links to a `<label>` via `for` attribute |
| `value` | Pre-filled default value |
| `placeholder` | Ghost text shown when field is empty |
| `required` | Field must be filled before submitting |
| `disabled` | Field is greyed out and not submitted |
| `readonly` | Value visible but not editable |
| `maxlength` | Maximum number of characters allowed |
| `minlength` | Minimum number of characters required |
| `min` / `max` | Minimum/maximum for number, date, range |
| `step` | Increment for number/range inputs |
| `pattern` | Regex pattern the value must match |
| `autocomplete` | Browser autofill on/off |
| `autofocus` | Field is focused automatically on page load |
| `multiple` | Allow multiple values (file, email) |

---

## Part 4 — Labels

Always pair every input with a `<label>`. It improves accessibility and clicking the label focuses the input.

```html
<!-- Method 1: for + id (recommended) -->
<label for="email">Email Address</label>
<input type="email" id="email" name="email">

<!-- Method 2: wrap the input inside the label -->
<label>
  Email Address
  <input type="email" name="email">
</label>
```

> **Never skip labels.** Screen readers cannot identify inputs without them.

---

## Part 5 — Textarea & Select

### Textarea (multi-line text)
```html
<label for="message">Message</label>
<textarea id="message" name="message" rows="5" cols="40" placeholder="Write your message..."></textarea>
```

- `rows` — visible height in lines
- `cols` — visible width in characters
- Content between tags is the default value (unlike `<input>`)

### Select (dropdown)
```html
<label for="city">City</label>
<select id="city" name="city">
  <option value="">-- Select City --</option>
  <option value="pune">Pune</option>
  <option value="mumbai" selected>Mumbai</option>
  <option value="delhi">Delhi</option>
</select>
```

### Select with Option Groups
```html
<select name="course">
  <optgroup label="Frontend">
    <option value="html">HTML</option>
    <option value="css">CSS</option>
  </optgroup>
  <optgroup label="Backend">
    <option value="node">Node.js</option>
    <option value="python">Python</option>
  </optgroup>
</select>
```

### Multi-select
```html
<select name="skills" multiple size="4">
  <option value="html">HTML</option>
  <option value="css">CSS</option>
  <option value="js">JavaScript</option>
  <option value="react">React</option>
</select>
```
Hold `Ctrl` (or `Cmd`) to select multiple options.

---

## Part 6 — Radio Buttons & Checkboxes

### Radio Buttons (pick one from a group)
All radios in a group must share the same `name`.

```html
<p>Gender</p>
<label><input type="radio" name="gender" value="male"> Male</label>
<label><input type="radio" name="gender" value="female"> Female</label>
<label><input type="radio" name="gender" value="other" checked> Other</label>
```

### Checkboxes (pick any number)
```html
<p>Interests</p>
<label><input type="checkbox" name="interest" value="html" checked> HTML</label>
<label><input type="checkbox" name="interest" value="css"> CSS</label>
<label><input type="checkbox" name="interest" value="js"> JavaScript</label>
```

---

## Part 7 — Fieldset & Legend

Group related fields visually and semantically.

```html
<form>
  <fieldset>
    <legend>Personal Information</legend>
    <label for="fname">First Name</label>
    <input type="text" id="fname" name="fname"><br>
    <label for="lname">Last Name</label>
    <input type="text" id="lname" name="lname">
  </fieldset>

  <fieldset>
    <legend>Account Details</legend>
    <label for="email">Email</label>
    <input type="email" id="email" name="email"><br>
    <label for="pass">Password</label>
    <input type="password" id="pass" name="pass">
  </fieldset>

  <button type="submit">Register</button>
</form>
```

---

## Part 8 — Datalist (Autocomplete Suggestions)

Shows suggestions while allowing free text input.

```html
<label for="browser">Favourite Browser</label>
<input list="browsers" id="browser" name="browser" placeholder="Type or choose...">

<datalist id="browsers">
  <option value="Chrome">
  <option value="Firefox">
  <option value="Safari">
  <option value="Edge">
  <option value="Brave">
</datalist>
```

---

## Part 9 — Button Types

```html
<button type="submit">Submit Form</button>   <!-- submits the form -->
<button type="reset">Clear Form</button>     <!-- resets all fields -->
<button type="button">Click Me</button>      <!-- does nothing by default, used with JS -->
```

> Always specify `type` on buttons inside forms. A button without `type` defaults to `submit` and can accidentally submit the form.

---

## Part 10 — Complete Registration Form Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Registration Form</title>
</head>
<body>

<h1>Create Account</h1>

<form action="/register" method="POST">

  <fieldset>
    <legend>Personal Info</legend>

    <label for="fname">First Name *</label><br>
    <input type="text" id="fname" name="fname" required placeholder="Arjun"><br><br>

    <label for="lname">Last Name *</label><br>
    <input type="text" id="lname" name="lname" required placeholder="Sharma"><br><br>

    <label for="dob">Date of Birth</label><br>
    <input type="date" id="dob" name="dob"><br><br>

    <p>Gender</p>
    <label><input type="radio" name="gender" value="male"> Male</label>
    <label><input type="radio" name="gender" value="female"> Female</label>
    <label><input type="radio" name="gender" value="other"> Other</label><br><br>
  </fieldset>

  <fieldset>
    <legend>Account Details</legend>

    <label for="email">Email *</label><br>
    <input type="email" id="email" name="email" required placeholder="arjun@example.com"><br><br>

    <label for="password">Password *</label><br>
    <input type="password" id="password" name="password" required minlength="8"><br><br>

    <label for="phone">Phone Number</label><br>
    <input type="tel" id="phone" name="phone" placeholder="+91 98765 43210"><br><br>

    <label for="city">City</label><br>
    <select id="city" name="city">
      <option value="">-- Select --</option>
      <option value="pune">Pune</option>
      <option value="mumbai">Mumbai</option>
      <option value="delhi">Delhi</option>
    </select><br><br>

    <label for="bio">Short Bio</label><br>
    <textarea id="bio" name="bio" rows="4" placeholder="Tell us about yourself..."></textarea><br><br>
  </fieldset>

  <fieldset>
    <legend>Preferences</legend>

    <p>Skills (select all that apply)</p>
    <label><input type="checkbox" name="skill" value="html"> HTML</label>
    <label><input type="checkbox" name="skill" value="css"> CSS</label>
    <label><input type="checkbox" name="skill" value="js"> JavaScript</label><br><br>

    <label for="avatar">Profile Picture</label><br>
    <input type="file" id="avatar" name="avatar" accept="image/*"><br><br>
  </fieldset>

  <label>
    <input type="checkbox" name="terms" required>
    I agree to the <a href="/terms">Terms & Conditions</a>
  </label><br><br>

  <button type="submit">Create Account</button>
  <button type="reset">Clear</button>

</form>

</body>
</html>
```

---

## Part 11 — Semantic HTML5

**Semantic** means the tag name describes the *meaning* of its content, not just its appearance.

### Non-Semantic vs Semantic

```html
<!-- Non-semantic — tells browser nothing about purpose -->
<div id="header">...</div>
<div id="nav">...</div>
<div id="content">...</div>
<div id="footer">...</div>

<!-- Semantic — browser, search engines, and screen readers all understand -->
<header>...</header>
<nav>...</nav>
<main>...</main>
<footer>...</footer>
```

### Why Semantics Matter
- **SEO** — search engines rank content higher when structure is clear
- **Accessibility** — screen readers navigate by landmarks (header, main, nav)
- **Maintainability** — code is easier to read and maintain
- **Browser defaults** — some semantic tags come with built-in behaviour

---

## Part 12 — Semantic Layout Tags

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Semantic Layout</title>
</head>
<body>

  <header>
    <h1>My Website</h1>
    <nav>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <article>
      <h2>Blog Post Title</h2>
      <p>Published on <time datetime="2025-05-10">May 10, 2025</time></p>
      <p>Post content goes here...</p>

      <section>
        <h3>Comments</h3>
        <p>User comment here...</p>
      </section>
    </article>

    <aside>
      <h3>Related Posts</h3>
      <ul>
        <li><a href="#">Another Post</a></li>
      </ul>
    </aside>
  </main>

  <footer>
    <p>&copy; 2025 My Website. All rights reserved.</p>
  </footer>

</body>
</html>
```

### Semantic Tags Reference

| Tag | Purpose |
|-----|---------|
| `<header>` | Introductory content — logo, site title, top nav |
| `<nav>` | Navigation links — menus, breadcrumbs, pagination |
| `<main>` | The primary content of the page — **use only once** |
| `<article>` | Self-contained content — blog post, news article, comment |
| `<section>` | Thematic grouping of content with a heading |
| `<aside>` | Content tangentially related to main — sidebars, ads, tips |
| `<footer>` | Bottom of page or section — copyright, contact, links |
| `<figure>` | Self-contained media — image, diagram, code block |
| `<figcaption>` | Caption for `<figure>` |
| `<time>` | Machine-readable date/time |
| `<address>` | Contact information for the nearest `<article>` or `<body>` |
| `<mark>` | Highlighted/relevant text |
| `<summary>` | Visible heading for `<details>` |
| `<details>` | Expandable/collapsible content |

---

## Part 13 — article vs section vs div

This is one of the most common points of confusion.

| Tag | Rule of thumb |
|-----|--------------|
| `<article>` | Could be lifted out and published independently (blog post, tweet, review) |
| `<section>` | A themed chapter of a page — always has a heading |
| `<div>` | No semantic meaning — use only for styling/layout purposes |

```html
<!-- article: self-contained, reusable content -->
<article>
  <h2>How JavaScript Works</h2>
  <p>JavaScript is a single-threaded language...</p>
</article>

<!-- section: a themed block that needs context of the page -->
<section>
  <h2>Our Services</h2>
  <p>We offer web design, development...</p>
</section>

<!-- div: pure layout container, no meaning -->
<div class="card-grid">
  <div class="card">...</div>
  <div class="card">...</div>
</div>
```

---

## Part 14 — figure & figcaption

```html
<figure>
  <img src="architecture.png" alt="System architecture diagram">
  <figcaption>Fig 1: High-level system architecture showing client-server flow.</figcaption>
</figure>

<!-- Works for code blocks too -->
<figure>
  <pre><code>
    const greet = name => `Hello, ${name}!`;
  </code></pre>
  <figcaption>Arrow function example in JavaScript</figcaption>
</figure>
```

---

## Part 15 — details & summary (Native Accordion)

No JavaScript needed for a basic expand/collapse.

```html
<details>
  <summary>What is HTML?</summary>
  <p>HTML stands for HyperText Markup Language. It is the standard language for creating web pages.</p>
</details>

<details open>
  <summary>What is CSS?</summary>
  <p>CSS stands for Cascading Style Sheets. It controls the visual presentation of HTML elements.</p>
</details>
```

The `open` attribute makes it expanded by default.

---

## Part 16 — Multimedia: Video

```html
<video width="640" height="360" controls>
  <source src="demo.mp4" type="video/mp4">
  <source src="demo.webm" type="video/webm">
  Your browser does not support the video tag.
</video>
```

### Video Attributes

| Attribute | Purpose |
|-----------|---------|
| `controls` | Show play, pause, volume controls |
| `autoplay` | Starts playing automatically (must pair with `muted` on most browsers) |
| `muted` | Starts with sound off |
| `loop` | Replays when finished |
| `poster` | Image shown before video plays |
| `preload` | `auto` / `metadata` / `none` |
| `width` / `height` | Size in pixels |

```html
<!-- Background video with no controls -->
<video autoplay muted loop poster="thumbnail.jpg">
  <source src="bg.mp4" type="video/mp4">
</video>
```

---

## Part 17 — Multimedia: Audio

```html
<audio controls>
  <source src="podcast.mp3" type="audio/mpeg">
  <source src="podcast.ogg" type="audio/ogg">
  Your browser does not support the audio element.
</audio>
```

| Attribute | Purpose |
|-----------|---------|
| `controls` | Show play/pause/volume |
| `autoplay` | Auto-play on load |
| `muted` | Start muted |
| `loop` | Repeat continuously |
| `preload` | `auto` / `metadata` / `none` |

---

## Part 18 — Embedding: iframe

Embed another webpage, YouTube video, Google Map, or any external content.

```html
<!-- Embed a YouTube video -->
<iframe
  width="560"
  height="315"
  src="https://www.youtube.com/embed/VIDEO_ID"
  title="YouTube video player"
  frameborder="0"
  allowfullscreen>
</iframe>

<!-- Embed a Google Map -->
<iframe
  src="https://maps.google.com/maps?q=Pune&output=embed"
  width="600"
  height="450"
  style="border:0;"
  allowfullscreen
  loading="lazy">
</iframe>
```

| Attribute | Purpose |
|-----------|---------|
| `src` | URL of the content to embed |
| `width` / `height` | Size of the frame |
| `frameborder` | Border around frame (use `0`) |
| `allowfullscreen` | Lets user go fullscreen |
| `loading="lazy"` | Loads only when scrolled into view |
| `title` | Accessibility description |

---

## Part 19 — Meta Tags (Head Section)

Meta tags live inside `<head>` and are not visible on the page. They provide information *about* the page to browsers, search engines, and social media.

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- SEO -->
  <meta name="description" content="Learn HTML in 3 days with hands-on examples and projects.">
  <meta name="keywords" content="HTML, web development, frontend, tutorial">
  <meta name="author" content="Arjun Sharma">
  <meta name="robots" content="index, follow">

  <!-- Refresh page after 5 seconds -->
  <meta http-equiv="refresh" content="5; url=https://example.com">

  <!-- Open Graph (Facebook, LinkedIn, WhatsApp previews) -->
  <meta property="og:title" content="HTML in 3 Days">
  <meta property="og:description" content="A hands-on HTML course for professionals.">
  <meta property="og:image" content="https://example.com/preview.jpg">
  <meta property="og:url" content="https://example.com/html-course">
  <meta property="og:type" content="website">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="HTML in 3 Days">
  <meta name="twitter:description" content="A hands-on HTML course for professionals.">
  <meta name="twitter:image" content="https://example.com/preview.jpg">

  <title>HTML in 3 Days — Complete Course</title>
</head>
```

### Most Important Meta Tags

| Tag | Impact |
|-----|--------|
| `charset` | Prevents garbled characters — always include |
| `viewport` | Controls mobile rendering — always include |
| `description` | Shown in search engine results under the page title |
| `og:image` | The image shown when shared on social media |
| `robots` | Controls if search engines index the page |

> The `<meta name="description">` should be **150–160 characters** — this is what appears in Google search results.

---

## Part 20 — Link Tag (CSS, Favicon, Fonts)

```html
<head>
  <!-- External CSS stylesheet -->
  <link rel="stylesheet" href="styles.css">

  <!-- Favicon (icon in browser tab) -->
  <link rel="icon" href="favicon.ico" type="image/x-icon">
  <link rel="icon" href="favicon.png" type="image/png">

  <!-- Apple touch icon (iOS home screen) -->
  <link rel="apple-touch-icon" href="apple-icon.png">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">

  <!-- Canonical URL (avoid duplicate content in SEO) -->
  <link rel="canonical" href="https://example.com/html-course">
</head>
```

---

## Part 21 — Script Tag (Linking JavaScript)

```html
<!-- In <head> — blocks rendering (avoid for large scripts) -->
<script src="app.js"></script>

<!-- With defer — downloads in parallel, runs after HTML is parsed (recommended) -->
<script src="app.js" defer></script>

<!-- With async — downloads in parallel, runs as soon as ready (for independent scripts) -->
<script src="analytics.js" async></script>

<!-- Inline JavaScript -->
<script>
  console.log("Hello from inline JS");
</script>
```

| Placement | Behaviour |
|-----------|-----------|
| `<head>` without attribute | Blocks HTML parsing — avoid |
| `<body>` end | Runs after HTML loads — old approach |
| `defer` | Runs after HTML is parsed — **recommended** |
| `async` | Runs as soon as downloaded — good for analytics |

---

## Part 22 — HTML Best Practices

### Code Quality
```html
<!-- Bad: missing quotes, uppercase tags, poor nesting -->
<IMG SRC=photo.jpg ALT=Photo>
<P>Hello <B>World</p></B>

<!-- Good: lowercase, quoted attributes, proper nesting -->
<img src="photo.jpg" alt="A professional headshot">
<p>Hello <strong>World</strong></p>
```

### Checklist

- Always include `<!DOCTYPE html>`
- Always include `lang` on `<html>`
- Always include `charset` and `viewport` meta tags
- Every `<img>` must have a meaningful `alt`
- Every `<input>` must have a `<label>`
- Use semantic tags instead of generic `<div>` where possible
- Use only one `<h1>` per page
- Headings must be in logical order (h1 → h2 → h3)
- Use `defer` when linking external JavaScript
- Validate HTML at **validator.w3.org**

---

## Day 2 — Hands-On Practice Project

Build a **job application form** page with semantic layout.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Apply for a frontend developer position at TechCorp.">
  <title>Job Application — TechCorp</title>
</head>
<body>

  <header>
    <h1>TechCorp</h1>
    <nav>
      <a href="/">Home</a> |
      <a href="/jobs">Jobs</a> |
      <a href="/about">About</a>
    </nav>
  </header>

  <main>
    <article>
      <h2>Frontend Developer Application</h2>
      <p>Fill out the form below. Fields marked with * are required.</p>

      <form action="/apply" method="POST">

        <fieldset>
          <legend>Personal Details</legend>

          <label for="name">Full Name *</label><br>
          <input type="text" id="name" name="name" required placeholder="Arjun Sharma"><br><br>

          <label for="email">Email *</label><br>
          <input type="email" id="email" name="email" required><br><br>

          <label for="phone">Phone</label><br>
          <input type="tel" id="phone" name="phone" placeholder="+91 98765 43210"><br><br>

          <label for="dob">Date of Birth</label><br>
          <input type="date" id="dob" name="dob"><br><br>
        </fieldset>

        <fieldset>
          <legend>Professional Info</legend>

          <label for="exp">Years of Experience *</label><br>
          <input type="number" id="exp" name="exp" min="0" max="30" required><br><br>

          <label for="role">Applying For</label><br>
          <select id="role" name="role">
            <option value="">-- Select Role --</option>
            <option value="junior">Junior Developer</option>
            <option value="mid" selected>Mid-Level Developer</option>
            <option value="senior">Senior Developer</option>
          </select><br><br>

          <p>Skills</p>
          <label><input type="checkbox" name="skill" value="html"> HTML</label>
          <label><input type="checkbox" name="skill" value="css"> CSS</label>
          <label><input type="checkbox" name="skill" value="js"> JavaScript</label>
          <label><input type="checkbox" name="skill" value="react"> React</label><br><br>

          <label for="portfolio">Portfolio URL</label><br>
          <input type="url" id="portfolio" name="portfolio" placeholder="https://yoursite.com"><br><br>

          <label for="resume">Upload Resume (PDF)</label><br>
          <input type="file" id="resume" name="resume" accept=".pdf"><br><br>

          <label for="cover">Cover Letter</label><br>
          <textarea id="cover" name="cover" rows="6" placeholder="Why do you want to join TechCorp?"></textarea><br><br>
        </fieldset>

        <label>
          <input type="checkbox" name="terms" required>
          I confirm all information provided is accurate.
        </label><br><br>

        <button type="submit">Submit Application</button>
        <button type="reset">Clear Form</button>

      </form>
    </article>

    <aside>
      <h3>About This Role</h3>
      <p>Location: Pune, Maharashtra</p>
      <p>Type: Full-time</p>
      <p>Salary: &#8377;8–15 LPA</p>

      <details>
        <summary>Required Qualifications</summary>
        <ul>
          <li>3+ years of frontend experience</li>
          <li>Strong HTML, CSS, JavaScript skills</li>
          <li>Experience with React or Vue</li>
        </ul>
      </details>
    </aside>
  </main>

  <footer>
    <p>&copy; 2025 TechCorp Pvt. Ltd. | <a href="/privacy">Privacy Policy</a></p>
  </footer>

</body>
</html>
```

---

## Day 2 — Quick Reference Cheat Sheet

```
FORMS                    SEMANTIC LAYOUT       MULTIMEDIA
─────────────────        ───────────────       ──────────────
<form action method>     <header>              <video controls>
<input type="...">       <nav>                 <audio controls>
<label for="">           <main>                <source src type>
<textarea>               <article>             <iframe src>
<select> <option>        <section>
<optgroup>               <aside>               META & HEAD
<fieldset> <legend>      <footer>              ───────────────
<datalist>               <figure>              <meta charset>
<button type="">         <figcaption>          <meta viewport>
                         <details>             <meta description>
INPUT TYPES              <summary>             <meta og:...>
─────────────            <time>                <link rel>
text  password  email    <address>             <script defer>
number  tel  url
date  time  range        BEST PRACTICE
color  file  hidden      ───────────────
checkbox  radio          1 x <h1> per page
submit  reset  button    alt on every img
                         label for every input
                         semantic > div
                         validate at w3.org
```

---