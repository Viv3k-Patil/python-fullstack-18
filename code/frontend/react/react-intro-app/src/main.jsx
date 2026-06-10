import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import Introduction from './Introduction.jsx'
import ReactIntro from './ReactIntro.jsx'

// createRoot(document.getElementById('root')).render(
//   <StrictMode>
//     <App />
//   </StrictMode>,
// )

createRoot(
  document.getElementById('root')
).render(<ReactIntro />);