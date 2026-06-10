import React from 'react'

export default function PreviewCard({profile}) {
  return (
    <div>
      <h2>{profile.name || 'your name'}</h2>
    </div>
  )
}
