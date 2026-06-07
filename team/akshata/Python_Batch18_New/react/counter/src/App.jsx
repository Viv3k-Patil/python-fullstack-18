import { useState } from "react";

function App() {
    const [counter, setcounter]= useState(0); // state management for counter

    function handleAdd(){
        setcounter(counter+1);
    }
    function handleSub(){
        setcounter(counter-1);
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