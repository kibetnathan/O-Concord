import { useEffect, useState } from "react";
import useProfileStore from "../zustand/profileStore";
import useAuthStore from "../zustand/authStore";
import useMainStore from "../zustand/mainStore";
import useThemeStore from "../zustand/themeStore";
import Sidebar from "../components/Sidebar";
import EditProfileForm from "../components/EditProfileForm";

const IconLogout = () => (
  <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" strokeWidth="1.5" viewBox="0 0 24 24">
    <path strokeLinecap="round" strokeLinejoin="round" d="M15.75 9V5.25A2.25 2.25 0 0013.5 3h-6a2.25 2.25 0 00-2.25 2.25v13.5A2.25 2.25 0 007.5 21h6a2.25 2.25 0 002.25-2.25V15M12 9l-3 3m0 0l3 3m-3-3h12.75" />
  </svg>
);

const IconEdit = () => (
  <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" strokeWidth="1.5" viewBox="0 0 24 24">
    <path strokeLinecap="round" strokeLinejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10" />
  </svg>
);

const IconSun = () => (
  <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" strokeWidth="1.5" viewBox="0 0 24 24">
    <path strokeLinecap="round" strokeLinejoin="round" d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z" />
  </svg>
);

const IconMoon = () => (
  <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" strokeWidth="1.5" viewBox="0 0 24 24">
    <path strokeLinecap="round" strokeLinejoin="round" d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z" />
  </svg>
);

export default function ProfilePage() {
  const token = useAuthStore((state) => state.token);
  const user = useAuthStore((state) => state.user);
  const logout = useAuthStore((state) => state.logout);
  const [editOpen, setEditOpen] = useState(false);

  const profile = useProfileStore((state) => state.profile);
  const fellowships = useMainStore((state) => state.fellowships);
  const { theme, toggleTheme } = useThemeStore();

  useEffect(() => {
    if (token) useProfileStore.getState().fetchProfile();
  }, [token]);

  useEffect(() => {
    if (token) useMainStore.getState().fetchFellowships();
  }, [token]);

  const fellowship_group = fellowships?.results ?? (Array.isArray(fellowships) ? fellowships : []);
  const myGroups = fellowship_group?.filter((g) => g.members?.includes(user?.id));

  const fullName =
    user?.first_name && user?.last_name
      ? `${user.first_name} ${user.last_name}`
      : "Guest User";

  const profileFields = [
    { label: "Campus", value: profile?.campus },
    { label: "School", value: profile?.school },
    { label: "Workplace", value: profile?.workplace },
    { label: "Role", value: user?.groups?.join(", ") },
  ];

  if (!profile)
    return (
      <div className="flex h-screen w-full bg-ivory">
        <Sidebar />
        <div
          role="status"
          aria-busy="true"
          className="flex-1 flex items-center justify-center"
        >
          <p className="text-sm tracking-widest uppercase text-primary animate-pulse">
            Loading…
          </p>
        </div>
      </div>
    );

  return (
    <>
      <main
        id="main-content"
        className="flex flex-row bg-ivory min-h-screen"
      >
        <Sidebar />

        {/* Profile content - desktop */}
        <div
          className="hidden md:flex flex-1 overflow-y-auto px-6 md:px-10 lg:px-16 py-8 md:py-10"
        >
          <div className="max-w-3xl w-full">
            {/* Header */}
            <div className="mb-8">
              <h1 className="font-cormorant text-4xl md:text-5xl font-semibold text-primary tracking-wide leading-tight">
                My Profile
              </h1>
              <div className="w-8 h-0.5 bg-amber-500 mt-4" />
            </div>

            {/* ── Profile Card ── */}
            <section
              aria-labelledby="profile-name"
              className="flex flex-col items-start px-0 pt-8 md:pt-10 pb-8 md:pb-10 border-b border-divider"
            >

              {/* Avatar */}
              <div className="relative mb-6">
                <img
                  src={profile?.profile_pic_url || "/images/defaultavatar.jpg"}
                  alt={`${fullName}'s profile picture`}
                  className="w-24 md:w-28 h-24 md:h-28 rounded-full object-cover ring-2 ring-amber-500/30"
                />
                <span
                  aria-hidden="true"
                  className="absolute bottom-0.5 right-0.5 w-3.5 h-3.5 bg-amber-500 rounded-full ring-2 ring-white"
                />
              </div>

              {/* Name & username */}
              <h2
                id="profile-name"
                className="font-cormorant text-3xl md:text-4xl font-semibold text-primary tracking-wide leading-tight"
              >
                {fullName}
              </h2>
              <p className="font-coptic text-sm text-primary tracking-widest mt-2">
                @{user?.username}
              </p>

              <div className="w-8 h-px bg-amber-500/40 my-6" aria-hidden="true" />

              {/* Profile fields */}
              <dl className="w-full flex flex-col gap-4">
                {profileFields.map(({ label, value }) => (
                  <div key={label} className="flex items-baseline justify-between gap-4">
                    <dt className="text-xs uppercase tracking-[0.18em] text-primary font-semibold shrink-0">
                      {label}
                    </dt>
                    <dd className="text-sm text-primary text-right">
                      {value || "—"}
                    </dd>
                  </div>
                ))}
              </dl>
            </section>

            {/* ── My Groups ── */}
            <section
              aria-labelledby="my-groups-heading"
              className="flex flex-col px-0 py-8 md:py-10 border-b border-divider"
            >
              <div className="flex items-center gap-2 mb-4">
                <h3
                  id="my-groups-heading"
                  className="text-xs uppercase tracking-[0.22em] text-primary font-semibold"
                >
                  My Groups
                </h3>
                <div className="flex-1 h-px bg-divider" aria-hidden="true" />
                {myGroups?.length > 0 && (
                  <span className="text-xs text-amber-700 tabular-nums font-semibold">
                    {myGroups.length}
                  </span>
                )}
              </div>

              <ul className="flex flex-col gap-1">
                {myGroups?.length > 0 ? (
                  myGroups.map((group) => (
                    <li
                      key={group.id}
                      className="font-coptic text-sm text-primary px-3 py-2.5 border-l-2 border-transparent hover:border-amber-500 hover:text-black hover:bg-amber-50 transition-all duration-150 cursor-default tracking-wide"
                    >
                      {group.name}
                    </li>
                  ))
                ) : (
                  <li className="text-xs text-primary tracking-widest uppercase py-2">
                    No groups yet
                  </li>
                )}
              </ul>
            </section>

            {/* ── Action Buttons ── */}
            <div className="flex flex-col gap-3 px-0 py-8 md:py-10">
              <button
                type="button"
                onClick={() => setEditOpen(true)}
                className="flex items-center gap-3 px-4 py-3 text-left font-coptic text-xs uppercase tracking-widest text-primary hover:text-amber-700 hover:bg-amber-50 transition-colors"
              >
                <IconEdit />
                Edit Profile
              </button>

              <button
                type="button"
                onClick={toggleTheme}
                aria-label={theme === "dark" ? "Switch to light mode" : "Switch to dark mode"}
                className="flex items-center gap-3 px-4 py-3 text-left font-coptic text-xs uppercase tracking-widest text-primary hover:text-amber-700 hover:bg-amber-50 transition-colors"
              >
                {theme === "dark" ? <IconSun /> : <IconMoon />}
                {theme === "dark" ? "Light Mode" : "Dark Mode"}
              </button>

              <button
                type="button"
                onClick={logout}
                className="flex items-center gap-3 px-4 py-3 text-left font-coptic text-xs uppercase tracking-widest text-primary hover:text-red-700 hover:bg-red-50 transition-colors"
              >
                <IconLogout />
                Sign Out
              </button>
            </div>
          </div>
        </div>

        {/* Profile content - mobile */}
        <div className="md:hidden flex-1 flex flex-col overflow-y-auto pb-20">
          <section
            aria-labelledby="mobile-profile-name"
            className="flex flex-col items-center px-6 pt-8 pb-7 border-b border-divider"
          >

            {/* Church label */}
            <p className="font-coptic text-xs tracking-[0.22em] uppercase text-primary font-semibold mb-6">
              Open Church Management
            </p>

            {/* Avatar */}
            <div className="relative mb-5">
              <img
                src={profile?.profile_pic_url || "/images/defaultavatar.jpg"}
                alt={`${fullName}'s profile picture`}
                className="w-24 h-24 rounded-full object-cover ring-2 ring-amber-500/30"
              />
              <span
                aria-hidden="true"
                className="absolute bottom-0.5 right-0.5 w-3.5 h-3.5 bg-amber-500 rounded-full ring-2 ring-white"
              />
            </div>

            {/* Name & username */}
            <h1
              id="mobile-profile-name"
              className="font-cormorant text-3xl font-semibold text-primary tracking-wide text-center leading-tight"
            >
              {fullName}
            </h1>
            <p className="font-coptic text-sm text-primary tracking-widest mt-1">
              @{user?.username}
            </p>

            <div className="w-8 h-px bg-amber-500/40 my-4" aria-hidden="true" />

            {/* Profile fields */}
            <dl className="w-full flex flex-col gap-3">
              {profileFields.map(({ label, value }) => (
                <div key={label} className="flex items-baseline justify-between gap-3">
                  <dt className="text-xs uppercase tracking-[0.18em] text-primary font-semibold shrink-0">
                    {label}
                  </dt>
                  <dd className="text-sm text-primary text-right truncate">
                    {value || "—"}
                  </dd>
                </div>
              ))}
            </dl>
          </section>

          {/* ── My Groups ── */}
          <section
            aria-labelledby="mobile-groups-heading"
            className="flex flex-col px-6 py-6 border-b border-divider"
          >
            <div className="flex items-center gap-2 mb-4">
              <h2
                id="mobile-groups-heading"
                className="text-xs uppercase tracking-[0.22em] text-primary font-semibold"
              >
                My Groups
              </h2>
              <div className="flex-1 h-px bg-divider" aria-hidden="true" />
              {myGroups?.length > 0 && (
                <span className="text-xs text-amber-700 tabular-nums font-semibold">
                  {myGroups.length}
                </span>
              )}
            </div>

            <ul className="flex flex-col gap-1">
              {myGroups?.length > 0 ? (
                myGroups.map((group) => (
                  <li
                    key={group.id}
                    className="font-coptic text-sm text-primary px-3 py-2.5 border-l-2 border-transparent hover:border-amber-500 hover:text-black hover:bg-amber-50 transition-all duration-150 cursor-default tracking-wide"
                  >
                    {group.name}
                  </li>
                ))
              ) : (
                <li className="text-xs text-primary tracking-widest uppercase py-2">
                  No groups yet
                </li>
              )}
            </ul>
          </section>

          {/* ── Footer Actions ── */}
          <div className="flex flex-col mt-auto">
            <button
              type="button"
              onClick={() => setEditOpen(true)}
              className="flex items-center gap-3 w-full px-6 py-4 text-left font-coptic text-sm uppercase tracking-widest text-primary hover:text-amber-700 hover:bg-amber-50 transition-colors font-semibold"
            >
              <IconEdit />
              Edit Profile
            </button>

            <button
              type="button"
              onClick={toggleTheme}
              aria-label={theme === "dark" ? "Switch to light mode" : "Switch to dark mode"}
              className="flex items-center gap-3 w-full px-6 py-4 text-left font-coptic text-sm uppercase tracking-widest text-primary hover:text-amber-700 hover:bg-amber-50 transition-colors font-semibold"
            >
              {theme === "dark" ? <IconSun /> : <IconMoon />}
              {theme === "dark" ? "Light Mode" : "Dark Mode"}
            </button>

            <button
              type="button"
              onClick={logout}
              className="flex items-center gap-3 w-full px-6 py-4 text-left font-coptic text-sm uppercase tracking-widest text-primary hover:text-red-700 hover:bg-red-50 transition-colors font-semibold"
            >
              <IconLogout />
              Sign Out
            </button>
          </div>
        </div>
      </main>

      {/* Edit profile modal */}
      <EditProfileForm open={editOpen} onClose={() => setEditOpen(false)} />
    </>
  );
}
