```markdown
# React — Day 2
## The 6-Day Plan
| Day | What You're Learning |
|-----|----------------------|
| 1   | Why React, JSX, Components, Props, State |
| **2** | **Events, Lists & Keys, Conditional Rendering** |
| 3 | useEffect, Fetching Data, Loading/Error states |
| 4 | Component design, Lifting state up |
| 5 | useContext, Custom Hooks, React Router |
| 6 | Forms + Mini Project |

---

## Handling Events
React events are very similar to HTML events, but with camelCase naming and JSX syntax.

```jsx
function ButtonDemo() {
  const handleClick = () => {
    alert('Button clicked!')
  }

  const handleSubmit = (e) => {
    e.preventDefault()        // Important: prevent default browser behavior
    console.log('Form submitted')
  }

  return (
    <div>
      <button onClick={handleClick}>Click me</button>
      
      <button onClick={() => alert('Inline handler')}>Inline</button>

      <form onSubmit={handleSubmit}>
        <button type="submit">Submit</button>
      </form>
    </div>
  )
}
```

**Key Points:**
- Use camelCase: `onClick`, `onChange`, `onSubmit`, `onMouseOver`, etc.
- Pass a **function reference**, not the result of calling it: `onClick={handleClick}` (not `onClick={handleClick()}`)
- Event object is passed automatically to your handler

---

## Lists & Keys

Rendering lists is a core React skill. Use `.map()` to turn arrays into JSX.

```jsx
function UserList() {
  const users = [
    { id: 1, name: 'Arjun', role: 'Frontend' },
    { id: 2, name: 'Sneha', role: 'Backend' },
    { id: 3, name: 'Priya', role: 'Designer' }
  ]

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>
          {user.name} — {user.role}
        </li>
      ))}
    </ul>
  )
}
```

**Why do we need `key`?**

- Helps React identify which items changed, were added, or removed
- Improves performance and prevents buggy re-renders
- Should be **unique** and **stable** (usually an `id` from your data)

```jsx
// Bad - avoid using index as key
{users.map((user, index) => <li key={index}>{user.name}</li>)}
// Good
{users.map(user => <li key={user.id}>{user.name}</li>)}
```

---

## Conditional Rendering

Show or hide elements based on conditions.

### 1. `&&` (Logical AND)
```jsx
{isLoggedIn && <WelcomeMessage />}
{items.length > 0 && <ShoppingCart items={items} />}
```

### 2. Ternary Operator
```jsx
{isLoggedIn ? <Dashboard /> : <LoginForm />}
```

### 3. Early Return
```jsx
function Profile({ user }) {
  if (!user) return <p>Loading...</p>
  if (user.role === 'admin') return <AdminPanel />

  return <RegularUserView user={user} />
}
```

### 4. Multiple Conditions
```jsx
function StatusMessage({ status }) {
  if (status === 'loading') return <p>Loading...</p>
  if (status === 'error') return <p>Error occurred</p>
  if (status === 'success') return <p>Success!</p>
  return null
}
```

---

## Putting It All Together

A simple todo list with add, toggle, and delete functionality.

```jsx
import { useState } from 'react'

function TodoApp() {
  const [todos, setTodos] = useState([
    { id: 1, text: 'Learn React', completed: false },
    { id: 2, text: 'Build projects', completed: true }
  ])
  const [inputValue, setInputValue] = useState('')

  const addTodo = (e) => {
    e.preventDefault()
    if (!inputValue.trim()) return
    setTodos([...todos, {
      id: Date.now(),
      text: inputValue,
      completed: false
    }])
    setInputValue('')
  }

  const toggleTodo = (id) => {
    setTodos(todos.map(todo =>
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ))
  }

  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id))
  }

  return (
    <div>
      <h1>My Todos ({todos.length})</h1>
      
      <form onSubmit={addTodo}>
        <input
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="New todo..."
        />
        <button type="submit">Add</button>
      </form>

      <ul>
        {todos.map(todo => (
          <li key={todo.id} style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}>
            <input
              type="checkbox"
              checked={todo.completed}
              onChange={() => toggleTodo(todo.id)}
            />
            {todo.text}
            <button onClick={() => deleteTodo(todo.id)}>Delete</button>
          </li>
        ))}
      </ul>

      {todos.length === 0 && <p>No todos yet! 🎉</p>}
    </div>
  )
}

export default TodoApp
```

---

## Common Mistakes

```jsx
// ❌ Calling function instead of passing reference
<button onClick={handleClick()}>Click</button>
// ✅
<button onClick={handleClick}>Click</button>

// ❌ Missing key in list
{items.map(item => <div>{item.name}</div>)}
// ✅
{items.map(item => <div key={item.id}>{item.name}</div>)}

// ❌ Using index as key when list can reorder/filter
{items.map((item, index) => <div key={index}>{item}</div>)}
// ✅ Use stable unique ID

// ❌ Forgetting to preventDefault in forms
<form onSubmit={handleSubmit}>...</form>  // page refreshes
```

---

## Quick Reference

| Concept              | Syntax / Pattern                              |
|----------------------|-----------------------------------------------|
| Event Handler        | `onClick={handler}`, `onChange={handler}`   |
| List Rendering       | `{array.map(item => <Component key={id} ... />)}` |
| Conditional (AND)    | `{condition && <Element />}`                  |
| Conditional (Ternary)| `{condition ? <A /> : <B />}`                 |
| Event Object         | `e => { e.preventDefault(); ... }`            |

---

## Interview Questions

**Why do we need keys in React lists?**  
Keys help React track which items have changed, been added, or removed, making updates more efficient and predictable.

**What happens if you don't provide keys or use index as key?**  
React may re-render incorrectly, lose component state (e.g., input focus), or have animation bugs.

**Difference between `&&` and ternary for conditional rendering?**  
`&&` is great for "show this if true" (returns falsy values otherwise). Ternary is better when you want to show one thing **or** another.

**How do you pass arguments to an event handler?**  
Use an arrow function: `onClick={() => handleDelete(id)}` or `.bind()` (less common).

---

## Practice

1. **Counter with History** — Button increments count. Show list of past counts below.
2. **Filtered Product List** — Array of products. Search input filters the displayed list.
3. **Toggleable Accordion** — Multiple sections. Clicking one expands/collapses it (bonus: only one open at a time).
4. *(stretch)* **Task Board** — Three columns (To Do, In Progress, Done). Move tasks between them using buttons.

---

*Day 3 — useEffect, Fetching Data, Loading & Error states*
```

Copy and save this as `react-day-2.md`. Let me know if you want any adjustments!