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

Rendering in React is the process where React calls your component functions to discover what the user interface (UI) should look like based on current props and state.

all the hooks always starts with "use"

Hooks:

React Hooks are built-in JavaScript functions that allow functional components to manage state, handle side effects, and access other core React features without writing class components

The JavaScript  function is a built-in global method used to make asynchronous HTTP network requests. It provides a modern, Promise-based alternative to the older  API, enabling clean communication with servers, endpoints, and databases. [1, 2, 3, 4, 5]  
Basic Syntax 
The function requires at least one parameter (the URL target) and accepts an optional configuration object: [1, 6]  
Key Concepts to Remember 

• Two-Step Resolution:  returns a  resolving to a  object. This initial resolution occurs as soon as HTTP headers are read. To access the actual data body, you must call a secondary async method like  or . 
• HTTP Error Handling: A  promise does not reject on HTTP error statuses (like  or ). The promise only rejects due to true network failures or malformed URLs. You must manually inspect the  flag. [1, 2, 9]  

Common Implementation Patterns 
1. Making a GET Request (Async/Await) This pattern is widely preferred for clean, linear syntax that reads like synchronous code. [2]  
2. Making a POST Request (Sending Data) To send data, pass an options object defining the , custom , and a stringified payload . [1, 10]  
3. Classic Promise Chaining Syntax ( / ) If your project avoids , use standard promise chaining to process data streams sequentially. [11, 12]  
Summary of Core Response Methods 
Once you receive the initial network response, use these built-in stream-consumers to parse data safely: 

• : Parses payload directly into a JavaScript object. 
• : Returns raw string content (ideal for HTML or plain text). 
• : Extracts binary object data (useful for processing images or file downloads). [1, 2, 6, 8, 9]  

For deep dives into configurations like CORS policies or session management, review the comprehensive MDN Web Docs Fetch API Guide or the W3Schools Fetch API Reference. [1, 7, 13]  
Would you like to build an example for a specific type of request, like handling file uploads via FormData, or configuring request timeouts? [14, 15]  

AI responses may include mistakes.

[1] https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
[2] https://www.geeksforgeeks.org/javascript/javascript-fetch-method/
[3] https://danielyankiver.medium.com/how-to-use-fetch-in-javascript-baab7491edff
[4] https://mimo.org/glossary/javascript/fetch-api
[5] https://www.youtube.com/watch?v=32tJEJbxUS8
[6] https://learnjavascript.online/topics/fetch.html
[7] https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
[8] https://codingnomads.com/intro-javascript-fetch
[9] https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch
[10] https://nodejs.org/learn/getting-started/fetch
[11] https://www.topcoder.com/thrive/articles/fetch-api-javascript-how-to-make-get-and-post-requests
[12] https://www.freecodecamp.org/news/javascript-fetch-api-for-beginners/
[13] https://www.w3schools.com/jsref/api_fetch.asp
[14] https://www.turing.com/blog/javascript-fetch-api-guide
[15] https://www.youtube.com/watch?v=6JR8HI9Ymd8

 and  are JavaScript's native methods for scheduling code execution asynchronously. They are part of the global  object in browsers and the  object in Node.js. [1, 2, 3, 4, 5]  
⏱️ Quick Summary Comparison 

| Feature [3, 6, 7, 8, 9] |  |   |
| --- | --- | --- |
| Execution | Runs a callback function once after a delay. | Runs a callback function repeatedly at fixed intervals.  |
| Cancellation | Stopped using . | Stopped using .  |
| Use Cases | Splash screens, delayed UI alerts, debouncing. | Clocks, stopwatches, polling data, animations.  |

1.  
Executes a function exactly once after the specified number of milliseconds has passed. [6, 10]  
Syntax • : The callback function to execute. 
• : Time in milliseconds (e.g.,  = 1 second). Defaults to  if omitted. 
• : Optional parameters passed directly into the callback function. [6, 10, 11, 12, 13]  

Example 2.  
Repeatedly executes a function, waiting for the designated time interval between each cycle. [6, 9]  
SyntaxExample 3. Critical Behavioral Dynamics 
Zero-Delay Trick () Setting a delay of  does not run the function immediately. Instead, it schedules the task to run as soon as possible after the current execution stack (synchronous script) has completed. [6]  
Why Timers Are Not 100% Precise JavaScript is single-threaded. Timers are handled by the browser environment (Web APIs) and queued up in the event loop. If the main thread is busy calculating heavy logic or rendering elements, your timer will wait, causing a slight drift. 

• The 4ms Limitation: Browsers automatically clamp the minimum delay to 4 milliseconds for heavily nested timers (5+ iterations) or active intervals to preserve CPU performance. [1, 6]  

Memory Leak Warning Passing a function to these methods creates an internal reference inside the scheduler. This prevents garbage collection. For , the function—and any outer variables it references via closures—stays stuck in memory forever unless explicitly cleared with . [3, 6]  
4. Nested  vs.  
When dealing with recurring execution, it is often recommended by platforms like MDN Web Docs to use a recursive/nested  instead of . [6, 17]  
Key Differences in Execution Flow: • : The interval includes the time spent running the code. If your function takes  to execute and your interval is , the actual pause between cycles is only . If your function takes longer than the interval itself, executions will run back-to-back with zero delay. 
• Nested : Guarantees a exact fixed delay between the end of one execution and the start of the next. The timer for the next cycle is only initialized after the current code finishes running. [6]  

If you are currently debugging or building a feature with these methods, let me know: 

• Are you trying to build a specific feature (like a countdown timer, search debounce, or API polling)? 
• Do you want to see how these play nicely (or poorly) with frameworks like React hooks ()? 

I can tailor a specific code recipe or fix any bugs you are facing. 

AI responses may include mistakes.

[1] https://www.geeksforgeeks.org/javascript/java-script-settimeout-setinterval-method/
[2] https://www.youtube.com/watch?v=kTg-5HBqiyQ
[3] https://www.scaler.com/topics/javascript-settimeout-and-setinterval-method/
[4] https://www.youtube.com/watch?v=0ewbT5YJdR8
[5] https://www.angulartraining.com/daily-newsletter/rxjs-timer-for-recurring-tasks/
[6] https://javascript.info/settimeout-setinterval
[7] https://thequeenbeebs.medium.com/taking-some-time-out-to-explain-settimeout-and-setinterval-in-javascript-38f12379ef7e
[8] https://dev.to/parthvirgoz/understanding-setinterval-and-settimeout-a-comprehensive-guide-9jb
[9] https://www.geeksforgeeks.org/javascript/difference-between-settimeout-setinterval/
[10] https://www.freecodecamp.org/news/javascript-timing-events-settimeout-and-setinterval/
[11] https://www.scribd.com/document/921644179/JS-Notes
[12] https://zerotomastery.io/blog/javascript-settimeout/
[13] https://dev.to/muthuraja_r/settimeout-setinterval-setimmediate-eib
[14] https://medium.com/@mohitsharma93/scheduling-mastering-settimeout-and-setinterval-javascript-48b403728233
[15] https://www.youtube.com/watch?v=HRHoI0uCMOc
[16] https://mimo.org/glossary/javascript/settimeout
[17] https://developer.mozilla.org/en-US/docs/Web/API/Window/setInterval


___
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