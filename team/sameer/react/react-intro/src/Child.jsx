import React from 'react';

export default function Child(prop) {
  console.log(prop);
  console.log("inside child component");

  return(
    <div>
        hiiiii,{prop.name},i belong to batch {prop.batch} 
        
    </div>
  )
}
