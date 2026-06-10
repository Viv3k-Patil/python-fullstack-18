import { useState } from "react";


function TodoForm({ setList, list }){
    const [value, setValue] = useState('');
    
     
    function handleAddTask(){
        setList([...list, value]);
        console.log("button clicked")
    }

    return (
        <div>
            <input 
                type="text"
                placeholder="please enter task"
                onChange={(e)=>{
                    setValue(e.target.value);
                }} 
            />
            <button onClick={handleAddTask}>Add</button>
        </div>
    )
}

export default TodoForm;