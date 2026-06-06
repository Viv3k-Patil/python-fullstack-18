import Card from "./Card"
import data from "../data.json"

function CardList(){
    console.log(data)

    return(
        <div>
            <Card />
        </div>
    )
}

export default CardList;