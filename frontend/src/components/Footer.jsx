import React from "react";

export function FooterTwo() {
  return (
    <footer
      className="footer sm:footer-horizontal bg-stone-950/95 backdrop-blur-md text-stone-300 p-10 font-coptic border-t border-black"
      aria-labelledby="site-footer-heading"
    >
      <h2 id="site-footer-heading" className="sr-only">
        Site footer
      </h2>
      <aside className="max-w-xs">
        <img
          src="/images/mavuno_logo.png"
          alt="Mavuno Church logo"
          className="h-12 mb-4 brightness-0 invert opacity-95"
        />
        <p className="font-cormorant text-xl font-semibold text-stone-50 leading-tight">
          Mavuno Church
        </p>
        <p className="text-sm tracking-[0.12em] text-stone-400 mt-2 leading-relaxed">
          Turning Ordinary People into
          <br />
          Fearless Influencers.
        </p>
      </aside>

      <nav aria-label="Ministries">
        <h3 className="footer-title font-coptic text-sm uppercase tracking-[0.18em] text-amber-400 font-semibold mb-4">
          Ministries
        </h3>
        <a href="#" className="link link-hover text-sm tracking-[0.1em] mb-1.5 text-stone-300 hover:text-white transition-colors">
          Fellowships
        </a>
        <a href="#" className="link link-hover text-sm tracking-[0.1em] mb-1.5 text-stone-300 hover:text-white transition-colors">
          Departments
        </a>
        <a href="#" className="link link-hover text-sm tracking-[0.1em] mb-1.5 text-stone-300 hover:text-white transition-colors">
          Leadership
        </a>
        <a href="#" className="link link-hover text-sm tracking-[0.1em] text-stone-300 hover:text-white transition-colors">
          Volunteers
        </a>
      </nav>

      <nav aria-label="Growth">
        <h3 className="footer-title font-coptic text-sm uppercase tracking-[0.18em] text-amber-400 font-semibold mb-4">
          Growth
        </h3>
        <a href="#" className="link link-hover text-sm tracking-[0.1em] mb-1.5 text-stone-300 hover:text-white transition-colors">
          Bible
        </a>
        <a href="#" className="link link-hover text-sm tracking-[0.1em] mb-1.5 text-stone-300 hover:text-white transition-colors">
          Reading Plans
        </a>
        <a href="#" className="link link-hover text-sm tracking-[0.1em] mb-1.5 text-stone-300 hover:text-white transition-colors">
          Memory Verses
        </a>
        <a href="#" className="link link-hover text-sm tracking-[0.1em] text-stone-300 hover:text-white transition-colors">
          Media Center
        </a>
      </nav>

      <nav aria-label="About">
        <h3 className="footer-title font-coptic text-sm uppercase tracking-[0.18em] text-amber-400 font-semibold mb-4">
          About
        </h3>
        <a href="#" className="link link-hover text-sm tracking-[0.1em] mb-1.5 text-stone-300 hover:text-white transition-colors">
          Our Story
        </a>
        <a href="#" className="link link-hover text-sm tracking-[0.1em] mb-1.5 text-stone-300 hover:text-white transition-colors">
          Locations
        </a>
        <a href="#" className="link link-hover text-sm tracking-[0.1em] mb-1.5 text-stone-300 hover:text-white transition-colors">
          Contact Us
        </a>
        <a href="#" className="link link-hover text-sm tracking-[0.1em] text-stone-300 hover:text-white transition-colors">
          Privacy Policy
        </a>
      </nav>
    </footer>
  );
}

function Footer() {
  return <FooterTwo />;
}

export default Footer;
