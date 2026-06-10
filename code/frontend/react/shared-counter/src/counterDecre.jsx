import React from 'react'
import './App.css'

export default function CounterDecre({counter,setCounter}) {

    function handleCounter(){
        setCounter(counter-1);
        console.log(counter);
    }

  return (
    <div>
      <button className='counter-dec'
        onClick={handleCounter}      
      >-</button>
        {counter}
    </div>
  )
}
