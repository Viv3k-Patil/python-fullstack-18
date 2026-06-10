# React — Day 6

## The 6-Day Plan

| Day | What You're Learning |
|-----|----------------------|
| 1   | Why React, JSX, Components, Props, State |
| 2   | Events, Lists & Keys, Conditional Rendering |
| 3   | useEffect, Fetching Data, Loading/Error states |
| 4   | Component design, Lifting state up |
| 5   | useContext, Custom Hooks, React Router |
| **6** | **Forms + Mini Project** |

***

## What You’ll Learn

- How to build forms in React.
- How to manage form state with controlled inputs.
- How to validate input before submitting.
- How to build and organize a mini project using everything learned so far.

***

## Forms in React

Forms are a very common part of React apps. In React, form inputs are usually **controlled components**, meaning React state stores the current value.

```jsx
import { useState } from 'react'

function SimpleForm() {
  const [name, setName] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    alert(`Hello, ${name}`)
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Enter your name"
      />
      <button type="submit">Submit</button>
    </form>
  )
}
```

### Why controlled inputs?
- React always knows the current value.
- Easy to validate and reset.
- Better for dynamic forms and live previews.

***

## Multiple form fields

A single form can manage many values in one state object.

```jsx
import { useState } from 'react'

function RegistrationForm() {
  const [form, setForm] = useState({
    name: '',
    email: '',
    password: '',
  })

  const handleChange = (e) => {
    const { name, value } = e.target
    setForm(prev => ({
      ...prev,
      [name]: value
    }))
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    console.log(form)
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        name="name"
        value={form.name}
        onChange={handleChange}
        placeholder="Name"
      />
      <input
        name="email"
        value={form.email}
        onChange={handleChange}
        placeholder="Email"
      />
      <input
        name="password"
        type="password"
        value={form.password}
        onChange={handleChange}
        placeholder="Password"
      />
      <button type="submit">Register</button>
    </form>
  )
}
```

***

## Validation basics

Validation helps prevent bad data before submission.

### Common checks
- Required fields.
- Minimum length.
- Valid email format.
- Matching passwords.

```jsx
import { useState } from 'react'

function LoginForm() {
  const [email, setEmail] = useState('')
  const [error, setError] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()

    if (!email.includes('@')) {
      setError('Please enter a valid email')
      return
    }

    setError('')
    console.log('Form submitted')
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
      />
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <button type="submit">Submit</button>
    </form>
  )
}
```

***

## Form patterns

### `preventDefault()`
Use this to stop the browser from refreshing the page.

```jsx
const handleSubmit = (e) => {
  e.preventDefault()
}
```

### Reset form
After successful submit, clear inputs.

```jsx
setName('')
setEmail('')
```

### Disable submit button
Useful when form is incomplete or invalid.

```jsx
<button type="submit" disabled={!name || !email}>
  Submit
</button>
```

***

## Checkbox and select inputs

Not all inputs are text fields.

```jsx
import { useState } from 'react'

function PreferencesForm() {
  const [subscribed, setSubscribed] = useState(false)
  const [role, setRole] = useState('student')

  return (
    <form>
      <label>
        <input
          type="checkbox"
          checked={subscribed}
          onChange={(e) => setSubscribed(e.target.checked)}
        />
        Subscribe to updates
      </label>

      <select value={role} onChange={(e) => setRole(e.target.value)}>
        <option value="student">Student</option>
        <option value="teacher">Teacher</option>
        <option value="developer">Developer</option>
      </select>
    </form>
  )
}
```

***

## Mini Project: Todo App

This mini project combines:
- State
- Events
- Lists and keys
- Conditional rendering
- Forms

### Features
- Add todo
- Mark todo complete
- Delete todo
- Show empty state

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

    setTodos([
      ...todos,
      {
        id: Date.now(),
        text: inputValue,
        completed: false,
      },
    ])
    setInputValue('')
  }

  const toggleTodo = (id) => {
    setTodos(
      todos.map(todo =>
        todo.id === id
          ? { ...todo, completed: !todo.completed }
          : todo
      )
    )
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
          <li
            key={todo.id}
            style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}
          >
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

***

## Better project structure

As your app grows, split it into components.

```jsx
function TodoApp() {
  return (
    <div>
      <TodoForm />
      <TodoList />
    </div>
  )
}
```

Suggested split:
- `TodoApp` → main container
- `TodoForm` → input and add button
- `TodoList` → renders all todos
- `TodoItem` → one todo row

***

## Common mistakes

### ❌ Forgetting `preventDefault()`
```jsx
const handleSubmit = (e) => {
  console.log('Submitted')
}
```

### ✅ Prevent page refresh
```jsx
const handleSubmit = (e) => {
  e.preventDefault()
  console.log('Submitted')
}
```

### ❌ Using uncontrolled inputs by accident
```jsx
<input onChange={(e) => setName(e.target.value)} />
```

### ✅ Controlled input
```jsx
<input value={name} onChange={(e) => setName(e.target.value)} />
```

### ❌ Mutating state directly
```jsx
todos.push(newTodo)
setTodos(todos)
```

### ✅ Create a new array
```jsx
setTodos([...todos, newTodo])
```

***

## Interview Questions

### What is a controlled component?
An input whose value is managed by React state.

### Why do we use `preventDefault()` in forms?
To stop the browser from reloading the page on submit.

### How do you add a new item to a list in React?
By creating a new array and updating state immutably.

### Why is an empty state useful?
It helps users understand that no items exist yet and what to do next.

### What should you focus on in a mini project?
Clear structure, reusable components, clean state management, and working interactions.

***

## Practice

1. **Login Form**  
Build a form with email and password validation.

2. **Profile Form**  
Create a form with name, bio, and role selection.

3. **Todo App**  
Add, complete, and delete tasks.

4. **Form Reset Demo**  
Reset all fields after submission.

***

## Mini Challenge

Build a **Student Feedback App**:
- Name input
- Rating dropdown
- Comment field
- Submit button
- List of submitted feedback entries
- Empty state when no feedback exists

***

## Final Day Summary

Today you learned:
- How forms work in React
- How to manage form state
- How to validate and submit data
- How to build a complete mini project

This completes your 6-day React basics plan.