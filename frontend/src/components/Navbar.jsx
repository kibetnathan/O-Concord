import React, { useState } from "react";
import { NavLink, useNavigate } from "react-router-dom";
import useAuthStore from "../zustand/authStore";

function Navbar() {
  const [mobileOpen, setMobileOpen] = useState(false);
  const user = useAuthStore((state) => state.user);
  const navigate = useNavigate();

  const handleHome = (e) => {
    e.preventDefault();
    navigate(user ? "/feed" : "/");
    setMobileOpen(false);
  };

  const navLinkClass = ({ isActive }) =>
    `font-coptic text-[0.75rem] uppercase tracking-[0.2em] transition-all px-4 py-2 border-b-2 border-transparent flex items-center h-full ${
      isActive
        ? "text-amber-600 border-amber-500 bg-stone-50/50"
        : "text-stone-700 hover:text-black hover:bg-stone-50/30"
    }`;

  const staticLinkClass = 
    "font-coptic text-[0.75rem] uppercase tracking-[0.2em] transition-all px-4 py-2 border-b-2 border-transparent text-stone-700 hover:text-black hover:bg-stone-50/30 flex items-center h-full cursor-pointer";

  return (
    <div className="fixed w-full top-0 z-50">
      <nav className="w-full flex items-center justify-between bg-porcelain/95 backdrop-blur-md border-b border-stone-200 px-6 sm:px-10 h-20">
        
        {/* Left Side: Logo + Main Nav */}
        <div className="flex items-center h-full gap-8">
          <NavLink
            to="/"
            className="font-cormorant text-2xl font-semibold tracking-[0.15em] text-stone-900 hover:text-amber-600 transition-colors mr-4"
          >
            O<span className="text-amber-500">C</span>M
          </NavLink>

          <ul className="hidden lg:flex items-center h-full gap-1">
            <li className="h-full flex items-center">
              <NavLink to={user ? "/feed" : "/"} className={navLinkClass}>
                Home
              </NavLink>
            </li>
            <li className="h-full flex items-center">
              <NavLink to="/bible" className={navLinkClass}>
                Bible
              </NavLink>
            </li>
            <li className="h-full flex items-center">
              <NavLink to="/reading-plans" className={navLinkClass}>
                Reading Plans
              </NavLink>
            </li>
            <li className="h-full flex items-center">
              <NavLink to="/fellowships" className={navLinkClass}>
                Fellowships
              </NavLink>
            </li>
            <li className="h-full flex items-center">
              <a href="https://mavunochurch.org/give" target="_blank" rel="noopener noreferrer" className={staticLinkClass}>
                Give
              </a>
            </li>
          </ul>
        </div>

        {/* Right side: Auth + CTA */}
        <div className="hidden sm:flex items-center gap-6 h-full">
          {!user ? (
            <>
              <NavLink
                to="/auth/login"
                className="font-coptic text-[0.75rem] uppercase tracking-[0.2em] text-stone-700 hover:text-black transition-colors"
              >
                Sign In
              </NavLink>
              <NavLink
                to="/auth/login"
                className="bg-amber-500 hover:bg-amber-600 text-black font-coptic text-[0.75rem] uppercase tracking-[0.2em] px-6 py-3 transition-all shadow-sm active:scale-95"
              >
                Get Started
              </NavLink>
            </>
          ) : (
            <NavLink
              to="/feed"
              className="bg-amber-500 hover:bg-amber-600 text-black font-coptic text-[0.75rem] uppercase tracking-[0.2em] px-6 py-3 transition-all shadow-sm active:scale-95"
            >
              Go to Feed
            </NavLink>
          )}
        </div>

        {/* Mobile hamburger */}
        <button
          className="lg:hidden flex flex-col gap-1.5 p-2"
          onClick={() => setMobileOpen((v) => !v)}
          aria-label="Toggle menu"
        >
          <span className={`block w-6 h-0.5 bg-stone-700 transition-all duration-300 ${mobileOpen ? "rotate-45 translate-y-[8px]" : ""}`} />
          <span className={`block w-6 h-0.5 bg-stone-700 transition-all duration-300 ${mobileOpen ? "opacity-0" : ""}`} />
          <span className={`block w-6 h-0.5 bg-stone-700 transition-all duration-300 ${mobileOpen ? "-rotate-45 -translate-y-[8px]" : ""}`} />
        </button>
      </nav>

      {/* Mobile menu */}
      <div
        className={`lg:hidden bg-porcelain border-b border-stone-200 flex flex-col transition-all duration-300 ease-in-out overflow-hidden shadow-xl ${
          mobileOpen ? "max-h-[32rem] opacity-100" : "max-h-0 opacity-0 pointer-events-none"
        }`}
      >
        <div className="flex flex-col px-6 py-6 gap-2">
          <NavLink to={user ? "/feed" : "/"} onClick={() => setMobileOpen(false)} className="font-coptic text-[0.8rem] uppercase tracking-[0.2em] text-stone-700 hover:text-black py-4 border-b border-stone-100">
            Home
          </NavLink>
          <NavLink to="/bible" onClick={() => setMobileOpen(false)} className="font-coptic text-[0.8rem] uppercase tracking-[0.2em] text-stone-700 hover:text-black py-4 border-b border-stone-100">
            Bible
          </NavLink>
          <NavLink to="/reading-plans" onClick={() => setMobileOpen(false)} className="font-coptic text-[0.8rem] uppercase tracking-[0.2em] text-stone-700 hover:text-black py-4 border-b border-stone-100">
            Reading Plans
          </NavLink>
          <NavLink to="/fellowships" onClick={() => setMobileOpen(false)} className="font-coptic text-[0.8rem] uppercase tracking-[0.2em] text-stone-700 hover:text-black py-4 border-b border-stone-100">
            Fellowships
          </NavLink>
          <a href="https://mavunochurch.org/give" target="_blank" rel="noopener noreferrer" className="font-coptic text-[0.8rem] uppercase tracking-[0.2em] text-stone-700 hover:text-black py-4 border-b border-stone-100">
            Give
          </a>
          
          <div className="flex flex-col gap-3 pt-6">
            {!user && (
              <NavLink
                to="/auth/login"
                onClick={() => setMobileOpen(false)}
                className="w-full text-center font-coptic text-[0.75rem] uppercase tracking-[0.2em] text-stone-700 border border-stone-200 py-3.5 transition-colors"
              >
                Sign In
              </NavLink>
            )}
            <NavLink
              to={user ? "/feed" : "/auth/login"}
              onClick={() => setMobileOpen(false)}
              className="w-full text-center bg-amber-500 hover:bg-amber-600 text-black font-coptic text-[0.75rem] uppercase tracking-[0.2em] py-3.5 transition-colors shadow-md"
            >
              {user ? "Go to Feed" : "Get Started"}
            </NavLink>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Navbar;
