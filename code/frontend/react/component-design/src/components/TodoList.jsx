import TodoItem from "./TodoItem";
function TodoList({list}){

    console.log("list in todolist", list)
    return (
        <div>
            <TodoItem 
                list = {list}
            />
        </div>
    )
}

export default TodoList;