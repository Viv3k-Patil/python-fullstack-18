# React — Day 3
## The 6-Day Plan
| Day | What You're Learning |
|-----|----------------------|
| 1   | Why React, JSX, Components, Props, State |
| 2   | Events, Lists & Keys, Conditional Rendering |
| **3** | **useEffect, Fetching Data, Loading/Error states** |
| 4   | Component design, Lifting state up |
| 5   | useContext, Custom Hooks, React Router |
| 6   | Forms + Mini Project |

---

## useEffect
`useEffect` lets you run side effects after rendering. Typical uses include:
- Fetching API data
- Setting up timers
- Adding event listeners
- Syncing with external systems

### Basic syntax

```jsx
import { useEffect } from 'react'

function Demo() {
  useEffect(() => {
    console.log('Runs after render')
  })

  return <h1>Hello</h1>
}
```

### Dependency array
```jsx
useEffect(() => {
  console.log('Runs once')
}, [])

useEffect(() => {
  console.log('Runs when id changes')
}, [id])
```

Key Points:
- No dependency array → runs after every render
- `[]` → runs once on mount
- `[value]` → runs when that value changes
- Can return a cleanup function

---

## Fetching Data
A common real-world use of `useEffect` is fetching data from an API.

```jsx
import { useEffect, useState } from 'react'

function Users() {
  const [users, setUsers] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    async function fetchUsers() {
      try {
        setLoading(true)
        setError(null)

        const response = await fetch('https://jsonplaceholder.typicode.com/users')

        if (!response.ok) {
          throw new Error('Failed to fetch data')
        }

        const data = await response.json()
        setUsers(data)
      } catch (err) {
        setError(err.message)
      } finally {
        setLoading(false)
      }
    }

    fetchUsers()
  }, [])

  if (loading) return <p>Loading...</p>
  if (error) return <p>Error: {error}</p>

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>
          {user.name} — {user.email}
        </li>
      ))}
    </ul>
  )
}

export default Users
```

---

## Loading and Error States
When fetching data, you should handle three main states:
1. Loading
2. Success
3. Error

```jsx
if (loading) return <p>Loading...</p>
if (error) return <p>Error: {error}</p>
return <div>Data loaded successfully</div>
```

Why this matters:
- Better user experience
- Prevents blank UI
- Makes debugging easier

---

## Cleanup Function
Some effects need cleanup to avoid memory leaks.

```jsx
import { useEffect, useState } from 'react'

function Timer() {
  const [count, setCount] = useState(0)

  useEffect(() => {
    const interval = setInterval(() => {
      setCount(prev => prev + 1)
    }, 1000)

    return () => {
      clearInterval(interval)
    }
  }, [])

  return <h2>{count}</h2>
}
```

Use cleanup for:
- `setInterval`
- `setTimeout`
- Event listeners
- Subscriptions

---

## Common Mistakes

### ❌ Making `useEffect` callback directly async
```jsx
useEffect(async () => {
  const res = await fetch('/api/data')
}, [])
```

### ✅ Use inner async function
```jsx
useEffect(() => {
  async function loadData() {
    const res = await fetch('/api/data')
    const data = await res.json()
    console.log(data)
  }

  loadData()
}, [])
```

### ❌ Forgetting dependency array
```jsx
useEffect(() => {
  console.log('Runs every render')
})
```

### ✅ Add dependencies properly
```jsx
useEffect(() => {
  console.log('Runs once')
}, [])
```

---

## Quick Reference

| Concept | Syntax / Pattern |
|---------|------------------|
| Basic Effect | `useEffect(() => { ... })` |
| Run Once | `useEffect(() => { ... }, [])` |
| Run on Change | `useEffect(() => { ... }, [value])` |
| Cleanup | `return () => { ... }` |
| Loading State | `if (loading) return <p>Loading...</p>` |
| Error State | `if (error) return <p>Error</p>` |

---

## Interview Questions

### What is `useEffect` used for?
It is used for side effects such as fetching data, timers, subscriptions, and DOM-related work.

### Why do we use `[]` in `useEffect`?
It makes the effect run once after the first render.

### What is a cleanup function?
A function returned from `useEffect` that React runs before re-running the effect or unmounting the component.

### How do you handle loading and error states?
By storing separate `loading` and `error` state values and conditionally rendering UI.

### Why should you not make the `useEffect` callback async directly?
Because the effect should return either nothing or a cleanup function, not a Promise.

---

## Practice

1. Fetch Posts  
Create a component that fetches posts from JSONPlaceholder and displays titles.

2. User Card Loader  
Show "Loading..." first, then display user cards after fetch completes.

3. Error Demo  
Use a wrong API URL and display an error message.

4. Timer with Cleanup  
Create a timer that updates every second and stops cleanly when component unmounts.

---

## Mini Challenge
Build a **Weather Search UI**:
- Input for city name
- Button to fetch weather
- Show loading while request is in progress
- Show error if request fails
- Show weather data if success

---

## Day 3 Summary
Today you learned:
- What `useEffect` is
- How to fetch data in React
- How to show loading and error states
- How cleanup functions work

Next: **Day 4 — Component Design and Lifting State Up**