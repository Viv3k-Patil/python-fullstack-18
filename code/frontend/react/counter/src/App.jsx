import { useState } from "react";

function App() {
  const [counter, setCounter] = useState(0);  // state management for counter

  function handleAdd(){
    setCounter(counter+1);
  }

  function handleSub(){
    setCounter(counter-1);
  }

  return (
    <div>
      <div>{counter}</div>
      <button onClick={handleAdd}>+</button>
      <button onClick={handleSub}>-</button>
    </div>
  );
}

export default App;