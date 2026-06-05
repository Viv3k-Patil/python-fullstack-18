# React — Day 1

## The 6-Day Plan

| Day | What You're Learning |
|-----|----------------------|
| **1** | Why React, JSX, Components, Props, State |
| 2 | Events, Lists & Keys, Conditional Rendering |
| 3 | useEffect, Fetching Data, Loading/Error states |
| 4 | Component design, Lifting state up |
| 5 | useContext, Custom Hooks, React Router |
| 6 | Forms + Mini Project |

---

## Why React?

Vanilla JS gets messy fast. You're constantly querying the DOM, updating elements manually, and keeping data in sync yourself.

```js
// Vanilla
let count = 0
document.getElementById('btn').addEventListener('click', () => {
  count++
  document.getElementById('display').innerText = count  // manual sync
})
```

React flips this around — you describe *what the UI should look like* for a given state, and React handles the DOM updates.

```jsx
function Counter() {
  const [count, setCount] = useState(0)
  return <button onClick={() => setCount(count + 1)}>{count}</button>
}
```

No querying. No manual updates. Just: "when count is X, show this."

---

## Project Setup

```bash
npm create vite@latest my-app -- --template react
cd my-app
npm install
npm run dev
```

Open `src/App.jsx`, delete everything, and start fresh. Vite is the current standard — Create React App is deprecated.

---

## JSX

JSX looks like HTML but it compiles to JavaScript. Babel turns this:

```jsx
const el = <h1 className="title">Hello</h1>
```

into this:

```js
const el = React.createElement('h1', { className: 'title' }, 'Hello')
```

You don't write `createElement` yourself, but knowing this explains why JSX has its rules.

**The rules:**

```jsx
// Must return one root element — use a Fragment if you don't want an extra div
return (
  <>
    <h1>Title</h1>
    <p>Subtitle</p>
  </>
)

// class is a reserved JS word, so JSX uses className
<div className="card">

// Embed any JS expression with curly braces
<p>{user.name}</p>
<p>{isLoggedIn ? 'Welcome' : 'Log in'}</p>

// Tags with no children must self-close
<img src="photo.jpg" />
<input type="text" />
```

---

## Components

A component is a function that returns JSX. That's it.

```jsx
function Greeting() {
  return <h1>Hello, world!</h1>
}

function App() {
  return (
    <div>
      <Greeting />
      <Greeting />
    </div>
  )
}
```

Two rules that trip people up:
- Name must start with a **capital letter** — `<greeting />` renders an unknown HTML tag, `<Greeting />` renders your component
- Must return JSX or `null` — never `undefined`

---

## Props

Props are how you pass data into a component. Think of them as function arguments.

```jsx
function UserCard({ name, role }) {
  return (
    <div>
      <h2>{name}</h2>
      <p>{role}</p>
    </div>
  )
}

function App() {
  return (
    <>
      <UserCard name="Arjun" role="Frontend Dev" />
      <UserCard name="Sneha" role="Backend Dev" />
    </>
  )
}
```

Props only flow **one way — parent to child**. A component can never modify its own props. If data needs to change, that's what state is for.

```jsx
// Both are the same, destructuring is just cleaner
function Card(props) { return <h1>{props.title}</h1> }
function Card({ title }) { return <h1>{title}</h1> }
```

---

## State

State is a component's internal memory. `useState` gives you the current value and a setter function.

```jsx
import { useState } from 'react'

function Counter() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <p>{count}</p>
      <button onClick={() => setCount(count + 1)}>+</button>
      <button onClick={() => setCount(count - 1)}>-</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  )
}
```

Every time you call the setter, React re-renders the component with the new value.

**Never mutate state directly:**

```jsx
// ❌ React doesn't know anything changed
count = count + 1

// ✅ React sees the setter call, re-renders
setCount(count + 1)
```

**For object state, always spread:**

```jsx
const [user, setUser] = useState({ name: 'Arjun', age: 25 })

// ❌ Mutating the object
user.age = 26

// ✅ New object with the change
setUser({ ...user, age: 26 })
```

---

## Putting It All Together

A profile card that toggles bio visibility — uses props for data, state for the toggle.

```jsx
import { useState } from 'react'

function ProfileCard({ name, bio }) {
  const [expanded, setExpanded] = useState(false)

  return (
    <div style={{ border: '1px solid #ccc', padding: '16px', width: '300px' }}>
      <h2>{name}</h2>
      {expanded && <p>{bio}</p>}
      <button onClick={() => setExpanded(!expanded)}>
        {expanded ? 'Show less' : 'Read more'}
      </button>
    </div>
  )
}

function App() {
  return (
    <div>
      <ProfileCard name="Arjun Sharma" bio="Self-taught dev. Loves clean code and chai." />
      <ProfileCard name="Sneha Patil" bio="Backend engineer who accidentally learned React." />
    </div>
  )
}

export default App
```

Each card manages its own `expanded` state independently. Toggling one doesn't affect the other — this is component isolation.

---

## Common Mistakes

```jsx
// ❌ Forgot to import useState
const [x, setX] = useState(0)  // ReferenceError

// ✅
import { useState } from 'react'


// ❌ Lowercase component name
function myCard() { return <div /> }
<myCard />  // React treats this as a custom HTML element, not your component

// ✅
function MyCard() { return <div /> }
<MyCard />


// ❌ Multiple root elements with no wrapper
return (
  <h1>Hello</h1>
  <p>World</p>  // Syntax error
)

// ✅
return (
  <>
    <h1>Hello</h1>
    <p>World</p>
  </>
)
```

---

## Quick Reference

| Concept | One-liner |
|---------|-----------|
| Component | Function that returns JSX |
| Props | Data passed in from parent — read-only |
| State | Internal memory — triggers re-render when updated |
| Re-render | React calls your function again with new state |
| JSX | HTML-like syntax that compiles to `React.createElement` |

---

## Interview Questions

**What's the difference between props and state?**
Props come from the parent and are read-only. State is managed inside the component and can be updated with the setter.

**Why can't you mutate state directly?**
React only knows to re-render when you call the setter. Directly mutating a variable bypasses that, so the UI stays stale.

**What is a re-render?**
React calls your component function again with the new state value, produces new JSX, and updates only the parts of the DOM that changed.

**What is JSX?**
Syntax sugar for `React.createElement`. Babel compiles it before the browser sees it.

---

## Practice

1. `LikeButton` — starts at 0, increments on click
2. `ToggleTheme` — clicking a button switches displayed text between `"light"` and `"dark"`
3. *(stretch)* `TemperatureCard` — takes a `celsius` prop, displays both Celsius and the Fahrenheit conversion

---

*Day 2 — Events, rendering lists, conditional rendering*