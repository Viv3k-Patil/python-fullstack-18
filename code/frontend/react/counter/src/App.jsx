import { useState } from "react";

// component
function App() {
  console.log("component is rendered!");

  // state
  const [counter, setCounter] = useState(0);

  // helper functions
  function handleAdd(){
    setCounter(counter+1);
  }

  function handleSub(){
    setCounter(counter-1);
  }

  // returning jsx
  return (
    <div>
      <div>{counter}</div>
      <button onClick={handleAdd}>+</button>
      <button onClick={handleSub}>-</button>
    </div>
  );
}

export default App;