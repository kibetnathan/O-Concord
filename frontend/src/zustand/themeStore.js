import { create } from "zustand";

function getInitialTheme() {
  const stored = localStorage.getItem("ocm-theme");
  if (stored === "dark" || stored === "light") return stored;
  return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

function applyTheme(theme) {
  const html = document.documentElement;
  html.classList.toggle("dark", theme === "dark");
  html.classList.toggle("light", theme === "light");
}

const useThemeStore = create((set) => {
  const initial = getInitialTheme();
  applyTheme(initial);
  return {
    theme: initial,
    toggleTheme: () =>
      set((state) => {
        const next = state.theme === "dark" ? "light" : "dark";
        localStorage.setItem("ocm-theme", next);
        applyTheme(next);
        return { theme: next };
      }),
  };
});

export default useThemeStore;
