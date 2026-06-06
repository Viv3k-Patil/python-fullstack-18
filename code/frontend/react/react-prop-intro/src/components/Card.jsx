// import React from "react";
// import "./Card.css";

// function Card(props){
//     console.log("props", props);
//     return (
//         <div>
//             <div className="card">
//                 <span>{props.title}</span>
//                 <h2>{props.subtitle}</h2>
//                 <p>{props.description}</p>
//                 <div className="footer">{props.footer}</div>
//             </div>
//         </div> 
//     )
// }

// export default Card;

import React from "react";
import "./Card.css";

function Card(props){
    console.log("props",props);
    return(
        <>
            <div className="card">
              <span>{props.tittle}</span>
              <h2>{props.subtittle}</h2>
              <p>{props.description}</p>
              <div className="footer">{props.footer}</div>
            </div>
        </>   
    )
    
 }


export default Card;