import React from 'react';
import "./App.css"

 function Todo({text,owner,is_completed}) {
  return (
    <div className='todo-container'>
        <p>{text}</p>
        <p>{owner}</p>
        <p>{is_completed ? "Completed" :"Pending"}</p>
    </div>
  )
}

export default Todo;