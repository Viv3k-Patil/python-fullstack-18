import Card from "./Card"
import data from "../data.json"
import "./CardList.css"

function CardList(){
    const returnedData = data.map((item)=>{
        return <Card 
            title={item.title}
            subtitle={item.subtitle}
            description={item.description}
            footer={item.footer}
        />
    });
    console.log(returnedData);

    return(
        <div className="card-list">
           {returnedData}
        </div>
    )
}

export default CardList;




// import React from 'react';
// import Data from "../data.json"
// import Card from './Card'
// import "./CardList.css"

// function CardList() {
//             const returnedData=Data.map((data)=>{
//                 return <Card
//                     tittle={data.title}
//                     subtittle={data.subtitle}
//                     description={data.description}
//                     footer={data.footer}
//                 />
//             });
//         console.log(returnedData);
        

//         return(
//             <div className='Card-List'>
//                 {returnedData}
//             </div>
//         )
//     }
// export default CardList;