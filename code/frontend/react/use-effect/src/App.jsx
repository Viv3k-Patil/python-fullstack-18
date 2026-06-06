import { useEffect, useState } from "react";
import './App.css'

function App() {
  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(()=>{
    setTimeout(()=>{
      fetchData();

    }, 5000);
    async function fetchData() {
        const response = await fetch('https://jsonplaceholder.typicode.com/users');
        const datafinal = await response.json();
        
        setData(datafinal);
        
        setIsLoading(false);
        // Put the log here! It executes immediately after the data arrives.
        console.log(datafinal); 
    }
    
  },[]);

  return (
    <>
      <h1>hey there!</h1>
      {isLoading && <div className="line-loader"></div>}
      {error != null && <div>{error}</div>}
      <div class="marquee-container">
        <div class="marquee-content">
          🔥 Breaking News: This is a modern, smooth, high-performance scrolling text banner!
        </div>
      </div>
      {/* {data} */}
      {/* <button onClick={fetchData}>click</button> */}
    </>
  );
}

export default App;
