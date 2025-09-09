import React from 'react';

export default function Header({ onHelp }) {
  return (
    <header className="bg-white p-4 shadow-md sticky top-0 z-50 flex items-center justify-between relative">
      <h1 className="text-2xl font-bold font-['Poppins'] absolute left-1/2 transform -translate-x-1/2 header-title">Complain Box</h1>
      <button onClick={onHelp} className="py-2 px-4 font-semibold rounded-full hover:bg-gray-100 transition-all duration-300 ml-auto help-btn">Help</button>
    </header>
  );
}
