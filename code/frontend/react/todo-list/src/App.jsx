import "./App.css"
import Todo from "./Todo";
import data from "./data.json"
import CreateTodo from "./CreateTodo";

function App(){


  const todos = data.map((todo)=>{
    return (
      <Todo 
        text={todo.text}
        owner={todo.owner}
        is_completed={todo.is_completed}
      />
    )
  });

  return (
    // <div>
    //   <section>
    //     <p>create new todo</p>
    //   </section>

    //   <section className="todolist-section">
    //     {todos}
    //   </section>

    // </div>
    <CreateTodo />
  )
}

export default App;
