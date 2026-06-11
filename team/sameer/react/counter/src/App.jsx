import { useState } from 'react';
function App() {
  const [counter, setCounter] = useState(0);

  function handleIncreament(){
    setCounter(counter+2);
  }

  function handleDecrement(){
    setCounter(counter-2);

  }
  function handleMultiply(){
    setCounter(counter*2);
  }

  function handlePower(){
    setCounter(counter**2);
  }
  function handleDivision(){
    
  }


  return (
    <div>
      <h1>{counter}</h1>
      <button onClick={handleMultiply}>*</button>
      <button onClick={handlePower}>**</button>
      <button onClick={handleIncreament}>+</button>
      <button onClick={handleDecrement}>-</button>
    </div>
  );
}

export default App;