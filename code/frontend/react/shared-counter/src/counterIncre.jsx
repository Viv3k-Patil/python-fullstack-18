import React from 'react'
import './App.css'

export default function CounterIncre({counter,setCounter}) {
    function handleDecrement(){
        setCounter(counter+1)
        console.log(counter);
    }
  return (
    <div>
      <button className='counter-dec'
        onClick={handleDecrement}
      >+</button>
    </div>
  )
}
