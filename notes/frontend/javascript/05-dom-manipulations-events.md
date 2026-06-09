# JavaScript — Day 5: DOM Manipulation & Browser APIs

---

## 1. What is the DOM?

The **Document Object Model (DOM)** is a tree-shaped, in-memory representation of your HTML that JavaScript can read and modify. The browser parses HTML and builds this tree — every tag becomes a **node**.

```
document
└── html
    ├── head
    │   └── title → "My Page"
    └── body
        ├── h1 → "Hello"
        └── div.container
            ├── p → "World"
            └── button#submit → "Click me"
```

**Analogy:** The DOM is like a live blueprint of a building. The HTML file is the printed plan. The DOM is the actual building you can walk around in, rearrange furniture, and repaint walls — all while people are inside.

---

## 2. Selecting Elements

### Single element selectors

```js
// By CSS selector — most versatile (returns first match)
document.querySelector(".card");
document.querySelector("#submit");
document.querySelector("input[type='email']");
document.querySelector("ul > li:first-child");

// Legacy selectors
document.getElementById("submit");        // fastest
document.getElementsByClassName("card");  // HTMLCollection (live)
document.getElementsByTagName("div");     // HTMLCollection (live)
```

### Multiple element selectors

```js
// Returns NodeList (static snapshot)
document.querySelectorAll(".card");
document.querySelectorAll("input, select, textarea");

// Convert to array for full array methods
const cards = [...document.querySelectorAll(".card")];
const cards2 = Array.from(document.querySelectorAll(".card"));

cards.filter(card => card.classList.contains("active"));
cards.map(card => card.textContent);
```

### Scoped queries — search within an element

```js
const form = document.querySelector("#loginForm");
const inputs = form.querySelectorAll("input");  // only inside #loginForm
const submit = form.querySelector("[type='submit']");
```

### NodeList vs HTMLCollection

| Feature         | NodeList (querySelectorAll) | HTMLCollection (getElementsBy*) |
|-----------------|----------------------------|----------------------------------|
| Live?           | No (static snapshot)       | Yes (auto-updates with DOM)      |
| forEach?        | Yes                        | No                               |
| Array methods?  | No (convert first)         | No (convert first)               |

```js
// Live HTMLCollection demo
const divs = document.getElementsByTagName("div");
console.log(divs.length); // 3

document.body.appendChild(document.createElement("div"));
console.log(divs.length); // 4 — auto-updated!
```

---

## 3. Traversing the DOM

```js
const el = document.querySelector(".parent");

// Children
el.children;          // HTMLCollection of element children
el.childNodes;        // NodeList including text/comment nodes
el.firstElementChild; // First element child
el.lastElementChild;  // Last element child
el.childElementCount; // Count of element children

// Parent
el.parentElement;     // Parent element
el.parentNode;        // Parent node (could be document)
el.closest(".card");  // Nearest ancestor matching selector (including self)

// Siblings
el.nextElementSibling;     // Next sibling element
el.previousElementSibling; // Previous sibling element

// Useful patterns
const listItem = document.querySelector("li");
const list = listItem.parentElement;         // ul/ol
const allItems = [...list.children];         // all li siblings
const index = allItems.indexOf(listItem);    // position of this li
```

---

## 4. Reading and Writing Content

### Text content

```js
const el = document.querySelector("p");

el.textContent;        // All text, including hidden elements, no HTML
el.innerText;          // Visible text only, respects CSS (slower — causes reflow)
el.innerHTML;          // HTML string including tags

// Write
el.textContent = "New text";       // Safe — escapes HTML automatically
el.innerHTML = "<b>Bold</b> text"; // Renders HTML — XSS risk if using user input!

// Safe HTML insertion with user data
el.textContent = userInput; // ✅ always escape user content this way
```

### ⚠️ XSS Warning

```js
// ❌ Never do this with user-provided data
el.innerHTML = `<div>${userInput}</div>`;
// If userInput = '<script>stealCookies()</script>' → executed!

// ✅ Safe alternatives
el.textContent = userInput;
// or sanitize with DOMPurify library
el.innerHTML = DOMPurify.sanitize(userInput);
```

---

## 5. Modifying Elements

### Classes

```js
const el = document.querySelector(".card");

el.classList.add("active");
el.classList.remove("hidden");
el.classList.toggle("selected");           // add if absent, remove if present
el.classList.toggle("selected", true);     // force add
el.classList.toggle("selected", false);    // force remove
el.classList.replace("old-class", "new-class");
el.classList.contains("active");           // boolean
el.classList;                              // DOMTokenList
[...el.classList];                         // ["card", "active", ...]
```

### Attributes

```js
el.getAttribute("href");
el.setAttribute("href", "https://example.com");
el.removeAttribute("disabled");
el.hasAttribute("data-id");

// Data attributes
el.dataset.userId;             // reads data-user-id attribute
el.dataset.userId = "123";    // sets data-user-id="123"
el.dataset.firstName;         // reads data-first-name (camelCase ↔ kebab-case)

// Boolean attributes
el.disabled = true;
el.checked = true;
el.hidden = true;
```

### Styles

```js
// Inline styles (avoid for complex styling — use CSS classes instead)
el.style.color = "red";
el.style.backgroundColor = "blue";
el.style.display = "none";
el.style.cssText = "color: red; background: blue;"; // set multiple at once

// Read computed styles (the actual rendered style)
const styles = getComputedStyle(el);
styles.color;          // "rgb(255, 0, 0)"
styles.fontSize;       // "16px"
styles.display;        // "block"
// Computed styles are read-only
```

---

## 6. Creating and Inserting Elements

### Creating elements

```js
const div = document.createElement("div");
div.className = "card";
div.textContent = "New card";
div.dataset.id = "123";

// Create with HTML (careful with user data!)
const wrapper = document.createElement("div");
wrapper.innerHTML = `
  <h2 class="title">Hello</h2>
  <p class="body">World</p>
`;
const title = wrapper.querySelector(".title"); // query within new element
```

### Inserting elements

```js
const parent = document.querySelector(".container");
const child = document.createElement("div");

// Append/Prepend (modern — accepts strings or nodes)
parent.append(child);          // end of parent
parent.prepend(child);         // start of parent
parent.append("text node");    // can append text directly
parent.append(el1, el2, el3);  // multiple at once

// insertAdjacentElement — precise positioning
el.insertAdjacentElement("beforebegin", newEl); // before el itself
el.insertAdjacentElement("afterbegin", newEl);  // inside, before first child
el.insertAdjacentElement("beforeend", newEl);   // inside, after last child
el.insertAdjacentElement("afterend", newEl);    // after el itself

// insertAdjacentHTML — insert HTML string
el.insertAdjacentHTML("beforeend", "<span>New</span>");

// Legacy (still valid)
parent.appendChild(child);
parent.insertBefore(newEl, referenceEl);
```

### Moving elements

```js
// Inserting an existing element moves it (no need to clone)
const el = document.querySelector(".card");
document.querySelector(".other-container").append(el); // moves it
```

### Removing elements

```js
el.remove();                          // remove from DOM
parent.removeChild(child);            // legacy
el.replaceWith(newEl);                // replace with another element
el.replaceWith("just text");          // replace with text node
```

### Cloning elements

```js
const clone = el.cloneNode(false); // shallow — element only, no children
const deepClone = el.cloneNode(true);  // deep — element + all children
```

---

## 7. Document Fragments — Batch DOM Updates

Inserting elements one by one causes multiple reflows. Use a `DocumentFragment` to batch.

**Analogy:** Instead of carrying 10 bags from the car to the house one at a time, put them all on a cart and make one trip.

```js
// ❌ Slow — 1000 reflows
const ul = document.querySelector("ul");
for (let i = 0; i < 1000; i++) {
  const li = document.createElement("li");
  li.textContent = `Item ${i}`;
  ul.appendChild(li); // reflow on every append
}

// ✅ Fast — 1 reflow
const fragment = document.createDocumentFragment();
for (let i = 0; i < 1000; i++) {
  const li = document.createElement("li");
  li.textContent = `Item ${i}`;
  fragment.appendChild(li); // no reflow — fragment is not in DOM
}
ul.appendChild(fragment); // one single DOM update
```

---

## 8. Events

### Adding and removing event listeners

```js
const btn = document.querySelector("#submit");

function handleClick(event) {
  console.log("clicked!", event);
}

btn.addEventListener("click", handleClick);
btn.removeEventListener("click", handleClick); // same reference needed!

// Options
btn.addEventListener("click", handleClick, {
  once: true,    // auto-removes after first call
  capture: true, // fire on capture phase (top-down)
  passive: true  // hint: won't call preventDefault (scroll perf)
});
```

### The Event Object

```js
document.addEventListener("click", (event) => {
  event.target;          // element that was clicked
  event.currentTarget;   // element the listener is attached to
  event.type;            // "click"
  event.timeStamp;       // when it happened
  event.bubbles;         // does it bubble?

  event.preventDefault(); // stop default browser behavior (e.g., form submit, link nav)
  event.stopPropagation(); // stop bubbling/capturing
  event.stopImmediatePropagation(); // stop + prevent other listeners on same element
});

// Mouse events
document.addEventListener("mousemove", (e) => {
  e.clientX; e.clientY;  // relative to viewport
  e.pageX; e.pageY;      // relative to full page
  e.offsetX; e.offsetY;  // relative to target element
  e.buttons;             // which mouse buttons are pressed
});

// Keyboard events
document.addEventListener("keydown", (e) => {
  e.key;        // "Enter", "a", "ArrowLeft"
  e.code;       // "KeyA", "Enter" — physical key
  e.ctrlKey;    // boolean
  e.shiftKey;   // boolean
  e.altKey;     // boolean
  e.metaKey;    // Cmd on Mac, Win key on Windows
});
```

### Event Bubbling and Capturing

Events travel in 3 phases:
1. **Capture** — document → target (top-down)
2. **Target** — fires on the element itself
3. **Bubble** — target → document (bottom-up)

**Analogy:** Drop a stone in a pond. Capturing is the ripple going inward to where the stone hit. Bubbling is the ripple expanding outward from the impact point.

```js
<div id="outer">
  <div id="inner">
    <button id="btn">Click</button>
  </div>
</div>

document.querySelector("#outer").addEventListener("click", () => console.log("outer"));
document.querySelector("#inner").addEventListener("click", () => console.log("inner"));
document.querySelector("#btn").addEventListener("click", () => console.log("btn"));

// Click on button → logs: btn → inner → outer (bubble order)
```

### Event Delegation

Instead of attaching listeners to every child, attach one listener to the parent and use `event.target` to detect which child was clicked.

**Analogy:** Instead of hiring a security guard for each desk in an office, you put one guard at the entrance and check who's coming in.

```js
// ❌ Naive — adds 1000 listeners
document.querySelectorAll(".delete-btn").forEach(btn => {
  btn.addEventListener("click", handleDelete);
});

// ✅ Delegation — one listener, works for dynamically added items too
document.querySelector(".list").addEventListener("click", (event) => {
  const btn = event.target.closest(".delete-btn");
  if (!btn) return; // click was elsewhere

  const item = btn.closest(".list-item");
  const id = item.dataset.id;
  deleteItem(id);
});
```

---

## 9. Common Event Types

```js
// Mouse
"click"        // single click
"dblclick"     // double click
"mousedown"    // button pressed
"mouseup"      // button released
"mousemove"    // cursor moved
"mouseenter"   // cursor enters (does NOT bubble)
"mouseleave"   // cursor leaves (does NOT bubble)
"mouseover"    // cursor enters + bubbles
"mouseout"     // cursor leaves + bubbles
"contextmenu"  // right click

// Keyboard
"keydown"      // key pressed (repeats if held)
"keyup"        // key released
"keypress"     // deprecated — use keydown

// Form
"submit"       // form submitted
"change"       // input value changed (after blur for text)
"input"        // fires on every character typed (real-time)
"focus"        // element gains focus (does NOT bubble)
"blur"         // element loses focus (does NOT bubble)
"focusin"      // focus (bubbles)
"focusout"     // blur (bubbles)
"reset"        // form reset

// Document / Window
"DOMContentLoaded"  // DOM parsed, scripts run (no images/css needed)
"load"              // everything loaded (images, stylesheets, etc.)
"beforeunload"      // user is leaving the page
"resize"            // window resized
"scroll"            // page or element scrolled
"visibilitychange"  // tab becomes visible/hidden

// Drag
"dragstart" "drag" "dragend"
"dragenter" "dragover" "dragleave" "drop"

// Touch (mobile)
"touchstart" "touchmove" "touchend" "touchcancel"

// Pointer (unified mouse + touch + stylus)
"pointerdown" "pointermove" "pointerup" "pointerenter" "pointerleave"
```

---

## 10. Custom Events

```js
// Create
const event = new CustomEvent("user:login", {
  bubbles: true,
  cancelable: true,
  detail: { userId: 123, name: "Alice" }
});

// Dispatch
document.dispatchEvent(event);
someElement.dispatchEvent(event);

// Listen
document.addEventListener("user:login", (e) => {
  console.log(e.detail.name); // "Alice"
});

// Real-world pattern — component communication
class Modal {
  constructor(el) { this.el = el; }

  open() {
    this.el.classList.add("open");
    this.el.dispatchEvent(new CustomEvent("modal:open", { bubbles: true }));
  }

  close() {
    this.el.classList.remove("open");
    this.el.dispatchEvent(new CustomEvent("modal:close", {
      bubbles: true,
      detail: { closedAt: Date.now() }
    }));
  }
}
```

---

## 11. DOM Dimensions and Position

```js
const el = document.querySelector(".box");

// getBoundingClientRect — position relative to viewport
const rect = el.getBoundingClientRect();
rect.top;     // distance from top of viewport
rect.left;    // distance from left of viewport
rect.right;   // rect.left + rect.width
rect.bottom;  // rect.top + rect.height
rect.width;   // element width (including padding, border)
rect.height;  // element height

// Scroll position
window.scrollX;     // horizontal scroll (px)
window.scrollY;     // vertical scroll (px)
el.scrollTop;       // scroll from top of scrollable element
el.scrollLeft;      // scroll from left
el.scrollHeight;    // total scrollable height (including hidden)
el.clientHeight;    // visible height of element (excluding border)
el.offsetHeight;    // height including border

// Is element in viewport?
function isInViewport(el) {
  const rect = el.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= window.innerHeight &&
    rect.right <= window.innerWidth
  );
}
```

### Scrolling

```js
// Smooth scroll to element
el.scrollIntoView({ behavior: "smooth", block: "center" });

// Scroll window
window.scrollTo({ top: 500, behavior: "smooth" });
window.scrollTo(0, 0); // back to top instantly

// Scroll element
el.scrollTo({ top: 100, behavior: "smooth" });
```

---

## 12. Intersection Observer

Efficiently detect when an element enters/leaves the viewport — without scroll event listeners.

**Analogy:** Instead of a security guard constantly looking out the window (polling on scroll), you have a motion sensor that triggers only when something crosses a line (Intersection Observer).

```js
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
      observer.unobserve(entry.target); // stop watching once visible
    }
  });
}, {
  threshold: 0.1,    // fire when 10% of element is visible
  rootMargin: "0px"  // or "100px" to trigger 100px before entering
});

document.querySelectorAll(".animate-on-scroll").forEach(el => {
  observer.observe(el);
});

// Infinite scroll
const sentinel = document.querySelector("#load-more-sentinel");
const scrollObserver = new IntersectionObserver(([entry]) => {
  if (entry.isIntersecting) loadMoreItems();
});
scrollObserver.observe(sentinel);
```

---

## 13. Mutation Observer

Watch for changes to the DOM — elements added, removed, or attributes changed.

```js
const observer = new MutationObserver((mutations) => {
  for (const mutation of mutations) {
    if (mutation.type === "childList") {
      console.log("Children changed");
      mutation.addedNodes.forEach(node => console.log("Added:", node));
      mutation.removedNodes.forEach(node => console.log("Removed:", node));
    }
    if (mutation.type === "attributes") {
      console.log(`Attribute "${mutation.attributeName}" changed`);
    }
    if (mutation.type === "characterData") {
      console.log("Text content changed");
    }
  }
});

observer.observe(document.querySelector(".container"), {
  childList: true,    // watch for added/removed children
  subtree: true,      // watch all descendants, not just direct children
  attributes: true,   // watch attribute changes
  characterData: true // watch text content changes
});

observer.disconnect(); // stop observing
```

---

## 14. ResizeObserver

React to element size changes (not just window resize).

```js
const resizeObserver = new ResizeObserver((entries) => {
  for (const entry of entries) {
    const { width, height } = entry.contentRect;
    console.log(`Element resized to ${width}x${height}`);

    if (width < 600) {
      entry.target.classList.add("compact");
    } else {
      entry.target.classList.remove("compact");
    }
  }
});

resizeObserver.observe(document.querySelector(".panel"));
```

---

## 15. Forms

```js
const form = document.querySelector("#loginForm");
const emailInput = form.querySelector("[name='email']");
const passwordInput = form.querySelector("[name='password']");

// Read values
emailInput.value;
passwordInput.value;

// FormData — easiest way to collect all form fields
form.addEventListener("submit", (e) => {
  e.preventDefault(); // stop browser from submitting/reloading

  const formData = new FormData(form);
  formData.get("email");           // "alice@example.com"
  formData.get("password");        // "secret"
  Object.fromEntries(formData);    // { email: "...", password: "..." }

  // Send as JSON
  fetch("/api/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(Object.fromEntries(formData))
  });

  // Send as multipart/form-data (files)
  fetch("/api/upload", {
    method: "POST",
    body: formData // don't set Content-Type — browser sets boundary automatically
  });
});

// Validation
emailInput.validity.valid;
emailInput.validity.valueMissing;
emailInput.validity.typeMismatch;
emailInput.setCustomValidity("Email already taken"); // custom error message
emailInput.setCustomValidity(""); // clear custom error
form.checkValidity(); // true if all fields valid
form.reportValidity(); // show validation UI
```

---

## 16. Browser APIs (BOM)

### `window`

```js
window.innerWidth;        // viewport width
window.innerHeight;       // viewport height
window.outerWidth;        // browser window width
window.devicePixelRatio;  // 2 on retina screens

window.location.href;     // full URL
window.location.pathname; // /path/to/page
window.location.search;   // ?q=hello
window.location.hash;     // #section
window.location.origin;   // https://example.com

window.location.assign("https://google.com");  // navigate
window.location.replace("https://google.com"); // navigate, no history entry
window.location.reload();                      // refresh

window.history.back();
window.history.forward();
window.history.go(-2);
window.history.pushState({ page: 1 }, "", "/new-url");
window.history.replaceState({ page: 2 }, "", "/replaced-url");
```

### `localStorage` and `sessionStorage`

```js
// localStorage — persists until explicitly cleared
localStorage.setItem("theme", "dark");
localStorage.getItem("theme");     // "dark"
localStorage.removeItem("theme");
localStorage.clear();              // remove everything

// Store objects
localStorage.setItem("user", JSON.stringify({ name: "Alice", age: 30 }));
const user = JSON.parse(localStorage.getItem("user"));

// sessionStorage — cleared when tab is closed
sessionStorage.setItem("token", "abc123");
```

### `URL` and `URLSearchParams`

```js
const url = new URL("https://example.com/search?q=hello&page=2");
url.hostname;  // "example.com"
url.pathname;  // "/search"
url.search;    // "?q=hello&page=2"
url.searchParams.get("q");    // "hello"
url.searchParams.get("page"); // "2"

const params = new URLSearchParams(window.location.search);
params.get("q");
params.set("q", "world");
params.append("filter", "active");
params.toString(); // "q=world&filter=active"

// Build URL from params
const newUrl = `${window.location.pathname}?${params.toString()}`;
window.history.pushState({}, "", newUrl);
```

### `navigator`

```js
navigator.userAgent;       // browser/OS string
navigator.language;        // "en-US"
navigator.onLine;          // boolean
navigator.clipboard.writeText("Copied!");
navigator.clipboard.readText().then(text => console.log(text));

// Geolocation
navigator.geolocation.getCurrentPosition(
  (pos) => {
    pos.coords.latitude;
    pos.coords.longitude;
  },
  (err) => console.error(err),
  { enableHighAccuracy: true, timeout: 5000 }
);
```

---

## 17. DOM Performance Patterns

### Avoid layout thrashing

**Layout thrashing** happens when you read layout properties, then write to DOM, then read again — forcing the browser to recalculate layout repeatedly.

```js
// ❌ Thrashing — read/write/read/write in a loop
const boxes = document.querySelectorAll(".box");
boxes.forEach(box => {
  const width = box.offsetWidth; // read → browser calculates layout
  box.style.width = width * 2 + "px"; // write → invalidates layout
  // next read forces recalculation again
});

// ✅ Batch reads then batch writes
const widths = [...boxes].map(box => box.offsetWidth); // read all first
boxes.forEach((box, i) => {
  box.style.width = widths[i] * 2 + "px"; // write all after
});
```

### `requestAnimationFrame` — sync with render cycle

```js
// ❌ Don't animate with setInterval
setInterval(() => {
  el.style.left = parseFloat(el.style.left) + 1 + "px";
}, 16); // may not sync with screen refresh

// ✅ Use requestAnimationFrame
function animate(timestamp) {
  el.style.left = parseFloat(el.style.left) + 1 + "px";
  requestAnimationFrame(animate); // schedules next frame
}
requestAnimationFrame(animate); // start

// With cancellation
let rafId;
function start() { rafId = requestAnimationFrame(animate); }
function stop() { cancelAnimationFrame(rafId); }
```

### CSS classes over inline styles

```js
// ❌ Don't manage complex state through inline styles
el.style.display = "none";
el.style.opacity = "0";
el.style.transform = "translateY(-10px)";

// ✅ Use CSS classes — browser optimizes transitions
el.classList.add("hidden"); // CSS handles the rest
el.classList.remove("hidden");
el.classList.toggle("active");
```

### `will-change` hint

Tell the browser in advance what will animate, so it can optimize.

```js
// Hint via JS
el.style.willChange = "transform, opacity";
// Remove after animation completes
el.style.willChange = "auto";
```

---

## 18. Template Element

The `<template>` tag holds inert HTML not rendered until cloned into the DOM.

```html
<template id="card-template">
  <div class="card">
    <h2 class="card-title"></h2>
    <p class="card-body"></p>
    <button class="card-btn">Read more</button>
  </div>
</template>
```

```js
const template = document.querySelector("#card-template");

function createCard(title, body) {
  const clone = template.content.cloneNode(true); // deep clone
  clone.querySelector(".card-title").textContent = title;
  clone.querySelector(".card-body").textContent = body;
  return clone;
}

const container = document.querySelector(".container");
container.append(createCard("Hello", "World content here"));
```

---

## Quick Reference Cheatsheet — Day 5

```
Selecting:
  querySelector()      → first match (CSS selector)
  querySelectorAll()   → NodeList of all matches
  getElementById()     → fastest for ID
  closest()            → nearest ancestor matching selector

Inserting:
  parent.append(el)    → end          | parent.prepend(el) → start
  el.before(newEl)     → before el    | el.after(newEl) → after el
  el.replaceWith(newEl)| el.remove()

Events:
  addEventListener(type, fn, options)
  removeEventListener(type, fn)  ← needs same fn reference
  event.target         → clicked element
  event.currentTarget  → listener's element
  event.preventDefault()  → stop default behavior
  event.stopPropagation() → stop bubbling

Event phases: Capture (down) → Target → Bubble (up)
Delegation: one listener on parent, check event.target.closest()

Observers:
  IntersectionObserver  → element enters/leaves viewport
  MutationObserver      → DOM structure/attribute changes
  ResizeObserver        → element dimensions change

Performance:
  DocumentFragment      → batch DOM inserts (1 reflow)
  Batch reads/writes    → avoid layout thrashing
  requestAnimationFrame → sync animation with screen refresh
  CSS classes > inline styles for animations
  event delegation > many individual listeners

Storage:
  localStorage    → persists forever
  sessionStorage  → persists per tab session
  Both: setItem / getItem / removeItem / clear
```