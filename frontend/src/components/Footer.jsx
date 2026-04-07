import React from "react";

export function FooterTwo() {
  return (
    <footer className="footer sm:footer-horizontal bg-stone-950/90 backdrop-blur-md text-stone-300 p-10 font-coptic border-t border-stone-800">
      <aside className="max-w-xs">
        <img 
          src="/images/mavuno_logo.png" 
          alt="Mavuno Logo" 
          className="h-12 mb-4 brightness-0 invert opacity-90" 
        />
        <p className="font-cormorant text-xl font-semibold text-stone-100 leading-tight">
          Mavuno Church
        </p>
        <p className="text-[0.6rem] uppercase tracking-[0.2em] opacity-50 mt-2 leading-relaxed">
          Turning Ordinary People into<br />Fearless Influencers.
        </p>
      </aside>
      <nav>
        <h6 className="footer-title font-coptic text-[0.7rem] uppercase tracking-[0.2em] text-amber-500 opacity-100 mb-4">Ministries</h6>
        <a className="link link-hover text-[0.65rem] uppercase tracking-[0.15em] mb-1.5 hover:text-white transition-colors">Fellowships</a>
        <a className="link link-hover text-[0.65rem] uppercase tracking-[0.15em] mb-1.5 hover:text-white transition-colors">Departments</a>
        <a className="link link-hover text-[0.65rem] uppercase tracking-[0.15em] mb-1.5 hover:text-white transition-colors">Leadership</a>
        <a className="link link-hover text-[0.65rem] uppercase tracking-[0.15em] hover:text-white transition-colors">Volunteers</a>
      </nav>
      <nav>
        <h6 className="footer-title font-coptic text-[0.7rem] uppercase tracking-[0.2em] text-amber-500 opacity-100 mb-4">Growth</h6>
        <a className="link link-hover text-[0.65rem] uppercase tracking-[0.15em] mb-1.5 hover:text-white transition-colors">Bible</a>
        <a className="link link-hover text-[0.65rem] uppercase tracking-[0.15em] mb-1.5 hover:text-white transition-colors">Reading Plans</a>
        <a className="link link-hover text-[0.65rem] uppercase tracking-[0.15em] mb-1.5 hover:text-white transition-colors">Memory Verses</a>
        <a className="link link-hover text-[0.65rem] uppercase tracking-[0.15em] hover:text-white transition-colors">Media Center</a>
      </nav>
      <nav>
        <h6 className="footer-title font-coptic text-[0.7rem] uppercase tracking-[0.2em] text-amber-500 opacity-100 mb-4">About</h6>
        <a className="link link-hover text-[0.65rem] uppercase tracking-[0.15em] mb-1.5 hover:text-white transition-colors">Our Story</a>
        <a className="link link-hover text-[0.65rem] uppercase tracking-[0.15em] mb-1.5 hover:text-white transition-colors">Locations</a>
        <a className="link link-hover text-[0.65rem] uppercase tracking-[0.15em] mb-1.5 hover:text-white transition-colors">Contact Us</a>
        <a className="link link-hover text-[0.65rem] uppercase tracking-[0.15em] hover:text-white transition-colors">Privacy Policy</a>
      </nav>
    </footer>
  );
}

function Footer() {
  return <FooterTwo />;
}

export default Footer;
