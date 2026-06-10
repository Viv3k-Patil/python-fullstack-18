import './TodoItem.css'

function TodoItem({list}){

    function handleDelete(item){
        const filteredList = list.filter(i => i != item);

    }

    const items = list.map((item)=>{
       return (
            <div className="todoitem">
                <input type="checkbox" />
                <p>{item}</p>
                <button onClick={()=>handleDelete(item)}>delete</button>
            </div>
        )
    });

    return (
        <div>
            {items}
        </div>
    )
}

export default TodoItem;