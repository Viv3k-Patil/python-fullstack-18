import React from 'react';

import { useState } from "react";

export default function todoForm({list,setList}) {

  const [text,setText]=useState('');

  function handleClick(){

      setList([...list,text]);
      console.log("rendering console");
      console.log(list)
  }


  return (
    <div>
      <input
          type="text" 
          placeholder="enter the todo" 
          onChange={(e)=>{
             setText(e.target.value);
          }}
      />
        <button onClick={handleClick}>add</button>
          
    </div>
  )
}
