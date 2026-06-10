import TodoForm from "./TodoForm";
import TodoList from "./TodoList";
import { useState } from "react";

function TodoContainer(){
    const [list, setList] = useState([]);

    return (
        <div>
            todocontainer
            <TodoForm 
                setList = {setList}
                list = {list}
            />
            <TodoList 
                list = {list}
            />
        </div>
    )
}

export default TodoContainer;