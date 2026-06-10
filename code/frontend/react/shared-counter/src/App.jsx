import React, { useState } from 'react'
import CounterDecre from './counterDecre'
import CounterIncre from './counterIncre';


export default function App() {
  const[counter,setCounter]=useState(0);

  return (
    <div className="app">
      <div className="button-row">
        <CounterDecre
          counter={counter}
          setCounter={setCounter}
        />

        <CounterIncre
          counter={counter}
          setCounter={setCounter}
        />
      </div>
    </div>
  )
}
