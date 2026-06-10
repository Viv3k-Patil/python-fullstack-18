import React, { useState } from 'react'
import InputForm from './inputForm'
import PreviewCard from './previewCard';

export default function LiveName() {
    const [profile,setProfile]=useState({name:'',role:'',Bio:''});
    const update=(field,val)=>setProfile(p=>({...p,[field]:val}))


  return (
    <div>
        <InputForm
            profile={profile}
            onChange={update}
        />
        <PreviewCard
            profile={profile}
        />
    </div>
  )
}
