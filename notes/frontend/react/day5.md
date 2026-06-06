# React — Day 5

## The 6-Day Plan

| Day | What You're Learning |
|-----|----------------------|
| 1   | Why React, JSX, Components, Props, State |
| 2   | Events, Lists & Keys, Conditional Rendering |
| 3   | useEffect, Fetching Data, Loading/Error states |
| 4   | Component design, Lifting state up |
| **5** | **useContext, Custom Hooks, React Router** |
| 6   | Forms + Mini Project |

***

## What You’ll Learn

- How to share state globally with `useContext`.
- How to build reusable logic with custom hooks.
- How client-side routing works in React.
- How to create multi-page experiences without full page reloads.

***

## `useContext`

`useContext` helps you share data across components without passing props through many levels. It is useful for app-wide values like theme, user, language, or auth status.

### Why use it?
- Avoids prop drilling.
- Makes global data easier to access.
- Keeps related app-wide state in one place.

```jsx
import { createContext, useContext, useState } from 'react'

const ThemeContext = createContext()

function App() {
  const [theme, setTheme] = useState('light')

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <Dashboard />
    </ThemeContext.Provider>
  )
}

function Dashboard() {
  return <ThemeToggle />
}

function ThemeToggle() {
  const { theme, setTheme } = useContext(ThemeContext)

  return (
    <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
      Current theme: {theme}
    </button>
  )
}
```

***

## When to use Context

Use context when:
- Many components need the same value.
- The value changes occasionally.
- You want to avoid passing props through many layers.

Do not use context for:
- Very local state.
- Fast-changing values that update every second.
- Complex app state that is better handled with a reducer or store.

***

## Common context pattern

A context usually has three parts:
- `createContext()`
- `Provider`
- `useContext()`

```jsx
const UserContext = createContext()

function App() {
  const user = { name: 'Arjun', role: 'admin' }

  return (
    <UserContext.Provider value={user}>
      <Profile />
    </UserContext.Provider>
  )
}

function Profile() {
  const user = useContext(UserContext)
  return <p>Welcome, {user.name}</p>
}
```

***

## Custom Hooks

A custom hook is a JavaScript function that starts with `use` and lets you reuse stateful logic.

### Why custom hooks?
- Reuse logic across components.
- Keep components small and readable.
- Separate behavior from UI.

```jsx
import { useState } from 'react'

function useCounter(initialValue = 0) {
  const [count, setCount] = useState(initialValue)

  const increment = () => setCount(c => c + 1)
  const decrement = () => setCount(c => c - 1)
  const reset = () => setCount(initialValue)

  return { count, increment, decrement, reset }
}

function Counter() {
  const { count, increment, decrement, reset } = useCounter(10)

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={decrement}>-</button>
      <button onClick={increment}>+</button>
      <button onClick={reset}>Reset</button>
    </div>
  )
}
```

***

## Rules for custom hooks

- Must start with `use`.
- Must follow the Rules of Hooks.
- Can call other hooks inside them.
- Should hide logic, not UI.

```jsx
function useToggle(initial = false) {
  const [value, setValue] = useState(initial)
  const toggle = () => setValue(v => !v)

  return [value, toggle]
}
```

***

## React Router

React Router lets you create navigation between views without full page reloads. It is the standard way to build single-page app routing in React.

### Main idea
- `BrowserRouter` wraps the app.
- `Routes` groups route definitions.
- `Route` maps a URL path to a component.
- `Link` replaces `<a>` for internal navigation.

```jsx
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </BrowserRouter>
  )
}

function Home() {
  return <h2>Home Page</h2>
}

function About() {
  return <h2>About Page</h2>
}
```

***

## Why React Router is useful

- Keeps navigation fast.
- Prevents full page reloads.
- Makes app views feel like real pages.
- Supports nested routes, route params, and layouts.

***

## `Link` vs `<a>`

Use `Link` for internal navigation inside your React app.

```jsx
<Link to="/profile">Profile</Link>
```

Use `<a>` for external links.

```jsx
<a href="https://example.com" target="_blank" rel="noreferrer">
  Visit site
</a>
```

***

## Route params

Route params let you read values from the URL.

```jsx
import { BrowserRouter, Routes, Route, useParams } from 'react-router-dom'

function UserProfile() {
  const { id } = useParams()
  return <h2>User ID: {id}</h2>
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/users/:id" element={<UserProfile />} />
      </Routes>
    </BrowserRouter>
  )
}
```

***

## Nested routes

Nested routes are useful for dashboards, account pages, and layouts.

```jsx
import { BrowserRouter, Routes, Route, Outlet, Link } from 'react-router-dom'

function Layout() {
  return (
    <div>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/dashboard">Dashboard</Link>
      </nav>
      <Outlet />
    </div>
  )
}
```

***

## Common mistakes

### ❌ Using `<a>` for internal routes
```jsx
<a href="/about">About</a>
```

### ✅ Use `Link`
```jsx
<Link to="/about">About</Link>
```

### ❌ Forgetting to wrap in `BrowserRouter`
```jsx
function App() {
  return <Routes>...</Routes>
}
```

### ✅ Wrap routing properly
```jsx
function App() {
  return (
    <BrowserRouter>
      <Routes>...</Routes>
    </BrowserRouter>
  )
}
```

### ❌ Creating context but not using provider
```jsx
const ThemeContext = createContext()
```

### ✅ Provide a value
```jsx
<ThemeContext.Provider value={{ theme, setTheme }}>
  <App />
</ThemeContext.Provider>
```

***

## Quick Reference

| Concept | Pattern |
|---------|---------|
| Context creation | `createContext()` |
| Context usage | `useContext(MyContext)` |
| Provider | `<MyContext.Provider value={...}>` |
| Custom hook | `function useSomething() { ... }` |
| Router setup | `<BrowserRouter><Routes>...</Routes></BrowserRouter>` |
| Internal link | `<Link to="/path">` |
| Dynamic route | `<Route path="/users/:id" ... />` |

***

## Interview Questions

### What problem does context solve?
It solves prop drilling by letting you share values across many components without passing props manually at every level.

### What is a custom hook?
A reusable function that starts with `use` and contains hook-based logic.

### Why use React Router?
To manage navigation between views in a single-page app without full page reloads.

### What is the difference between `Link` and `<a>`?
`Link` handles client-side navigation; `<a>` reloads the page.

### When should you avoid context?
When the state is only needed in one small part of the app or changes too frequently.

***

## Practice

1. **Theme Context**  
Create a light/dark theme toggle using context.

2. **Counter Hook**  
Build a reusable `useCounter` hook and use it in two components.

3. **Simple Router**  
Create Home, About, and Contact pages with React Router.

4. **User Detail Page**  
Use route params to show a user ID from the URL.

***

## Mini Challenge

Build a **small dashboard app**:
- Shared theme using context
- Reusable card counter using a custom hook
- Navigation between Home and Profile pages using React Router
- A route like `/users/:id` to show dynamic data

***

## Day 5 Summary

Today you learned:
- How to share state with `useContext`
- How to create reusable logic with custom hooks
- How React Router powers navigation
- How to build route-based React apps

Next: **Day 6 — Forms + Mini Project**