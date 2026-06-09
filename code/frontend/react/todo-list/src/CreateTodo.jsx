import { useState } from "react";


function CreateTodo(){
    const [todoList, setTodoList] = useState([])
    const [todotext, setTodoText] = useState('');
    

    // function handleAdd(){
    //     setTodoList([...todolist, "new item"])
    //     console.log(todolist)
    // }
    console.log(todoList);
    console.log("rendering createtodo component!!");

    function handleClick(){
        setTodoList([...todoList, todotext]);
        setTodoText('');
    }

    function handleInputText(e){
        // e.target.value
        setTodoText(e.target.value);
    }
    
    function handleDelete(t){
      console.log("delete clicked", t)
      // 
      const filteredList = todoList.filter((item)=>{
        return item != t;
      });
      setTodoList(filteredList);
    }

    return (
        <>
            <input 
                type="text"
                placeholder="enter todo"
                value={todotext}
                onChange={handleInputText}
            />
            <button onClick={handleClick}>click</button>
            <div>
                {
                    todoList.map((t)=>{
                        return (
                            <div>
                                <input type="checkbox" />
                                {t}
                                <button onClick={()=> handleDelete(t)}>delete</button>
                            </div>
                        )
                    })
                }
            </div>
        </>
    )
}

export default CreateTodo;