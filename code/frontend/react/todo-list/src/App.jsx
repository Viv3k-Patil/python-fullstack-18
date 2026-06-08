import React from 'react'
import Todo from './Todo';
import data from './data.json';
import CreateTodo from './CreateTodo';
///import "./App.css";

 function App() {

  const todos=data.map((todo)=>{
      return(
        <Todo
          text={todo.text}
          owner={todo.owner}
          is_completed={todo.is_completed}
        />
    )
  });
        // console.log(todos);

  return (
    // <div>
    //   <section className='todolist-section'>
    //     <div>
    //        {todos}
       
    //     </div>
    
    //   </section>
    // </div>
    <CreateTodo/>
  )
}

export default App;
