import { useState } from "react";

// component
function App() {
  console.log("component is rendered!");

  // state
  const [counter, setCounter] = useState(0);

  // helper functions
  function handleAdd(){
    setCounter(counter+1);
    console.log(handleAdd);
  }

  function handleSub(){
    setCounter(counter-1);
    console.log(handleSub);
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