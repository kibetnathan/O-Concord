import { React} from 'react'
import Sidebar from '../components/Sidebar'
import Footer from '../components/Footer'
import { Outlet } from 'react-router-dom'

function Feed() {
  return (
    <>
    <div className='flex flex-row bg-light w-full min-h-screen'>
      <Sidebar />
        <Outlet />
    </div>
      <Footer />
    </>
  )
}

export default Feed