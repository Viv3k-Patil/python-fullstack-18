import React from 'react'
import { useState } from 'react';

function CreateTodo() {
 //here state are defined
  const [todoList,setTodoList]=useState([])
  const [todoText,setTodoText]=useState('');

   console.log("rendering createTodo component");
     console.log(todoList);

  function handleClick(){
      setTodoList([...todoList,todoText]);
      setTodoText('');
   }

   function handleInputText(e){
      //e.target.value
      setTodoText(e.target.value);
   }

   function handleDeleteClick(t){
    console.log("delete clicked",t)

    const filterList=todoList.filter((item)=>{
      return item !==t;
    });
    setTodoList(filterList);
   }

  return (
        <>
            <input 
              type="text" 
              placeholder='enter todo here'
              value={todoText}
              onChange={handleInputText}
              
            />
            <button onClick={handleClick}>click</button>

            <div>
              {
                todoList.map((t)=>{
                  return(
                    <div>
                      <input type="checkbox" />
                      {t}
                      <button onClick={()=>handleDeleteClick(t)}>Delete</button> 
                    </div>  
                  )
                })
              }  
            </div>

        </>
   
  )
}

export default CreateTodo;