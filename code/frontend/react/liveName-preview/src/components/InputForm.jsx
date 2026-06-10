import React from 'react'

export default function InputForm({profile,onChange}) {
        console.log(profile);
  return (
    <div>
      <input
         type="text"
         placeholder='enter input here'
         value={profile.name}
         onChange={e=>onChange('name',e.target.value)} />
        
    </div>
  )
   
}
