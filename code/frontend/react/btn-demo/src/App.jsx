import './App.css'

function App(){

  function handleOnClick(){
    console.log("btn clicked!!");
  }

  function handleOnMouseEnter(){
    console.log("mouse enter");
  }


  return (

    <button 
      onMouseEnter={handleOnMouseEnter} 
      className="btn" 
      onClick={handleOnClick}
      onMouseLeave={()=>console.log("mouse left!")}
    >Click me</button>

  )
}

export default App;