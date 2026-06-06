import React from "react";
import "./Card.css";
{/* <div class="card">
    <span>Account Overview</span>
    <h2>Welcome Back</h2>
    <p>Your system is up to date and running smoothly.</p>
    <div class="footer">Last updated 2 mins ago</div>
  </div> */}
function Card(){
    return (
        <div>
            <div className="card">
                <span>Storage Alert</span>
                <h2>System Warning</h2>
                <p>Your cloud storage is at 95% capacity. Clean up files to free up space.</p>
                <div className="footer">Action required</div>
            </div>
            <div className="card">
                <span>Payment Received</span>
                <h2>Billing Update</h2>
                <p>Invoice #2026-04 has been successfully paid via your linked card.</p>
                <div className="footer">Receipt emailed</div>
            </div>
            <div className="card">
                <span>New Device Detected</span>
                <h2>System Warning</h2>
                <p>Your cloud storage is at 95% capacity. Clean up files to free up space.</p>
                <div className="footer">Action required</div>
            </div>
            <div className="card">
                <span>Storage Alert</span>
                <h2>System Warning</h2>
                <p>Your cloud storage is at 95% capacity. Clean up files to free up space.</p>
                <div className="footer">Action required</div>
            </div>
        </div>
        
    )
}

export default Card;