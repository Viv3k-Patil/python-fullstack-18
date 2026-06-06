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