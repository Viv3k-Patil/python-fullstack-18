
import "./App.css"

function App(){
  function handleOnClick(){
    console.log("btn clicked!!")
  }
  return(
    <button onClick={handleOnClick}>click me </button>

  )  
}

export default App;