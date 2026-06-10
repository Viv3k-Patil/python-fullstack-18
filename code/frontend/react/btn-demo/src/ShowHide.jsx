import { useState } from "react";
import "./ShowHide.css"

function ShowHide(){
    const [ShowHide, setShowHide] = useState(true);

    function handleShow(){
        setShowHide(true)
    }

    function handleHide(){
        setShowHide(false)
    }
    return (
        <div>
            {ShowHide && <p>This is text to hide/show.</p>}

            {ShowHide ? <p>text is visible</p> : <p>text is hidden</p>}
            <div className="control-pane">
                <button onClick={handleShow}>show</button>
                <button onClick={handleHide}>hide</button>
            </div>
        </div>
    )
}

export default ShowHide;