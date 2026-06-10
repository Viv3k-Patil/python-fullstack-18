import React from 'react'
import TodoItem from './todoItem'

function TodoList({list}) {
    console.log("list in todolist",list);
    return (
        <div>
            <TodoItem
                list={list} 
            />
        </div>
    )
}
export default TodoList;