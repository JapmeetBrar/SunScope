import React, { useState } from 'react'

enum navItemType {
    Home = 'Home',
    About = 'About Us',
    Contact = 'Contact',
    Estimate = 'Estimate',
}


function NavBar() {
const [selected, setSelected] = useState(navItemType.Home)
const navItemsArray = [navItemType.Home, navItemType.About, navItemType.Contact, navItemType.Estimate];
    
    return (
        <div className='h-20 flex gap-20 items-center px-10 py-6 shadow-lg font-roboto rounded-b-lg' >
            <div className="title text-4xl font-bold text-orange-500">SunScope</div>
            <div className='grow'>
                <ul className='flex gap-3 font-bold justify-around text-xl'>
                    {navItemsArray.map((item) => {
                        return <button className={ item === selected ? 'underline decoration-slate-800 underline-offset-8 text-orange-500': 'hover:text-orange-500'} onClick={() => setSelected(item)}>{item}</button>
                    })}
                </ul>
            </div>
        </div>
  )
}

export default NavBar