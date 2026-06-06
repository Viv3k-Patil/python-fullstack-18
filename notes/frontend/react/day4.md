# React — Day 4

## The 6-Day Plan

| Day | What You're Learning |
|-----|----------------------|
| 1   | Why React, JSX, Components, Props, State |
| 2   | Events, Lists & Keys, Conditional Rendering |
| 3   | useEffect, Fetching Data, Loading/Error states |
| **4** | **Component design, Lifting state up** |
| 5   | useContext, Custom Hooks, React Router |
| 6   | Forms + Mini Project |

***

## What You’ll Learn

- How to split a UI into reusable components.
- How to decide what each component should own.
- How to move state to a common parent when multiple components need it.
- How to pass data and actions between parent and child components.

***

## Component Design

Good React apps are built by breaking the UI into small, focused components.

### A good component:
- Does one job.
- Has a clear name.
- Receives data through props.
- Reuses logic only when it actually helps.

### Example component breakdown
For a todo app:
- `TodoApp` → main container
- `TodoForm` → input + add button
- `TodoList` → renders all todos
- `TodoItem` → single todo row

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

### Thinking in components
Ask these questions:
- What parts of the UI repeat?
- What parts change independently?
- What data belongs together?
- Which part should own the state?

***

## Props in component design

Props let parent components pass data and functions to child components.

```jsx
function Greeting({ name }) {
  return <h2>Hello, {name}</h2>
}

function App() {
  return <Greeting name="Arjun" />
}
```

Props are useful when:
- A child only needs to display data.
- A child needs to trigger an action in the parent.
- The same component is reused in multiple places.

***

## Lifting state up

When two or more components need the same state, move that state to their closest common parent. This is called lifting state up.

### Example
Suppose an input box and display box both need the same text.

```jsx
import { useState } from 'react'

function Parent() {
  const [text, setText] = useState('')

  return (
    <div>
      <TextInput text={text} setText={setText} />
      <TextPreview text={text} />
    </div>
  )
}

function TextInput({ text, setText }) {
  return (
    <input
      value={text}
      onChange={(e) => setText(e.target.value)}
      placeholder="Type here"
    />
  )
}

function TextPreview({ text }) {
  return <p>You typed: {text}</p>
}
```

### Why lift state up?
- Keeps data in one place.
- Avoids duplicate state.
- Makes sibling components stay in sync.
- Reduces bugs caused by mismatched values.

***

## One-way data flow

React follows a top-down data flow.

- Parent passes data down through props.
- Child triggers actions by calling functions passed from parent.
- State changes happen in the component that owns the state.

```jsx
function Child({ onSave }) {
  return <button onClick={onSave}>Save</button>
}

function Parent() {
  const handleSave = () => {
    console.log('Saved!')
  }

  return <Child onSave={handleSave} />
}
```

This pattern keeps your app predictable and easier to debug.

***

## Controlled components

A controlled component is an input whose value is managed by React state.

```jsx
import { useState } from 'react'

function NameForm() {
  const [name, setName] = useState('')

  return (
    <input
      value={name}
      onChange={(e) => setName(e.target.value)}
      placeholder="Enter your name"
    />
  )
}
```

### Why controlled components matter
- React always knows the input value.
- Easier to validate and reset.
- Needed for forms and shared state patterns.

***

## Example: shared counter

Two buttons can control the same counter only if the count lives in the parent.

```jsx
import { useState } from 'react'

function CounterApp() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <CounterDisplay count={count} />
      <CounterControls count={count} setCount={setCount} />
    </div>
  )
}

function CounterDisplay({ count }) {
  return <h2>Count: {count}</h2>
}

function CounterControls({ count, setCount }) {
  return (
    <div>
      <button onClick={() => setCount(count - 1)}>-</button>
      <button onClick={() => setCount(count + 1)}>+</button>
    </div>
  )
}
```

***

## Example: temperature converter

This is a classic lifting-state-up example.

```jsx
import { useState } from 'react'

function TemperatureConverter() {
  const [celsius, setCelsius] = useState('')

  const fahrenheit = celsius === '' ? '' : ((Number(celsius) * 9) / 5 + 32).toFixed(1)

  return (
    <div>
      <label>
        Celsius:
        <input
          value={celsius}
          onChange={(e) => setCelsius(e.target.value)}
        />
      </label>

      <p>Fahrenheit: {fahrenheit}</p>
    </div>
  )
}
```

Here, the Celsius value is the single source of truth.

***

## Common patterns

### Parent owns state
Use this when:
- Multiple children need the same value.
- One child updates state, another shows it.
- Data must stay synchronized.

### Child owns state
Use this when:
- The state is only used inside that child.
- No other component needs it.

### Shared state in a feature
Use this when:
- A set of sibling components depend on each other.
- A form, filter bar, or dashboard panel needs shared values.

***

## Common mistakes

### ❌ Duplicating the same state in two components
```jsx
function A() {
  const [value, setValue] = useState('')
}

function B() {
  const [value, setValue] = useState('')
}
```

### ✅ Keep one source of truth
```jsx
function Parent() {
  const [value, setValue] = useState('')
}
```

### ❌ Mutating props
Props should be treated as read-only.

```jsx
function Child({ user }) {
  user.name = 'New Name'
}
```

### ✅ Pass functions to request changes
```jsx
function Child({ onRename }) {
  return <button onClick={() => onRename('New Name')}>Rename</button>
}
```

***

## Interview Questions

### What does “lifting state up” mean?
It means moving shared state to the nearest common parent so multiple components can use it.

### When should you create a new component?
When a section of UI is reusable, has a clear responsibility, or makes the code easier to read.

### What is the benefit of one-way data flow?
It makes the app predictable because data always flows from parent to child.

### What is a controlled component?
An input whose value is controlled by React state.

### When should state stay local?
When only one component needs it and no other part of the UI depends on it.

***

## Practice

1. **Shared Counter**  
Build two buttons that increment and decrement a counter shown in a separate component.

2. **Live Name Preview**  
Create an input and a preview card that both use the same value.

3. **Temperature Converter**  
Keep Celsius in parent state and display Fahrenheit in a child component.

4. **Todo Split**  
Split a todo app into `TodoForm`, `TodoList`, and `TodoItem`.

***

## Mini Challenge

Build a **small profile editor**:
- Input for name
- Input for bio
- Preview card that updates live
- Reset button that clears both fields

***

## Day 4 Summary

Today you learned:
- How to design components clearly
- How to think in reusable UI pieces
- How to lift state up
- How to share state between components using props and parent state

Next: **Day 5 — useContext, Custom Hooks, React Router**