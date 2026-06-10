import React from 'react'
import "./todoItem.css";

export default function TodoItem({list}){
        function handleDelete(item){
        const filterItem=list.filter(i => i!==item);
        }
     const  items= list.map((item)=>{
       return (
            <div className="todoitem">
                <input type="checkbox" />
                <p>{item}</p>
                <button onClick={()=>handleDelete(item)}>delete</button>
            </div>
        )
    });



  return(
    <div>
        {items}
    </div>
  )
}
