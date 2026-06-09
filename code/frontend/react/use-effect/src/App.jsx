// import { useEffect, useState } from "react";
// import './App.css'

// function App() {
//   const [data, setData] = useState([]);
//   const [isLoading, setIsLoading] = useState(true);
//   const [error, setError] = useState('');

//   useEffect(()=>{
//     setTimeout(()=>{
//       fetchData();

//     }, 5000);
//     async function fetchData() {
//         const response = await fetch('https://jsonplaceholder.typicode.com/users');
//         const datafinal = await response.json();
        
//         setData(datafinal);
        
//         setIsLoading(false);
//         // Put the log here! It executes immediately after the data arrives.
//         console.log(datafinal); 
//     }
    
//   },[]);

//   return (
//     <>
//       <h1>hey there!</h1>
//       {isLoading && <div className="line-loader"></div>}
//       {error != null && <div>{error}</div>}
//       <div class="marquee-container">
//         <div class="marquee-content">
//           🔥 Breaking News: This is a modern, smooth, high-performance scrolling text banner!
//         </div>
//       </div>
//       {/* {data} */}
//       {/* <button onClick={fetchData}>click</button> */}
//     </>
//   );
// }

// export default App;


import React from 'react'
import { useState,useEffect } from 'react';
import "./App.css"

 function App() {
    const [data,setData]=useState([])
    const [is_loading,setIsLoading]=useState(true);
    const [error,setError]=useState('');


     useEffect(()=>{
      setTimeout(()=>{
        fetchData()
        console.log("run this");

    }, 5000);

        async function fetchData(){
          const response=await fetch('https://api.open-meteo.com/v1/forecast?latitude=18.65&longitude=73.85&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m')
          const finalData=await response.text()
          
          setData(finalData);
          
          setIsLoading(false);
           // Put the log here! It executes immediately after the data arrives.
          console.log(finalData);

        }
 },[]);

  return (  

      <div>
        <h1>Hello</h1>
            {is_loading && <div className='line-loader'></div>}
            {error !=null && <div>{error}</div>}
            <div className="marquee-container">

                <div className="marquee-content">🔥 Breaking News: This is a modern, smooth, high-performance scrolling text banner!
                </div>
            </div>

            <div>  
                  {/* {data} 
                <button onClick={fetchData}>click</button> */}
            </div>
      </div>
 
  );
}

export default App;
