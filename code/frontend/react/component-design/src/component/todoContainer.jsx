import React from 'react'
import { useState } from 'react';
import TodoForm from './todoForm';
import TodoList from './todoList';

function todoContainer() {
  const[list,setList]=useState([]);

  return (
    <div>
      hello
      <TodoForm
        list={list}
        setList={setList}
      />
      <TodoList
        list={list}
      />
    </div>
  )
}

export default todoContainer;