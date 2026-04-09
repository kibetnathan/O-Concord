import { useEffect } from "react";
import useProfileStore from "../zustand/profileStore";
import useAuthStore from "../zustand/authStore";
import useMainStore from "../zustand/mainStore";
import Sidebar from "../components/Sidebar";

const IconLogout = () => (
  <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" strokeWidth="1.5" viewBox="0 0 24 24">
    <path strokeLinecap="round" strokeLinejoin="round" d="M15.75 9V5.25A2.25 2.25 0 0013.5 3h-6a2.25 2.25 0 00-2.25 2.25v13.5A2.25 2.25 0 007.5 21h6a2.25 2.25 0 002.25-2.25V15M12 9l-3 3m0 0l3 3m-3-3h12.75" />
  </svg>
);

export default function ProfilePage() {
  const token   = useAuthStore((state) => state.token);
  const user    = useAuthStore((state) => state.user);
  const logout  = useAuthStore((state) => state.logout);

  const profile     = useProfileStore((state) => state.profile);
  const fellowships = useMainStore((state) => state.fellowships);

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
    { label: "Campus",    value: profile?.campus },
    { label: "School",    value: profile?.school },
    { label: "Workplace", value: profile?.workplace },
    { label: "Role",      value: user?.groups?.join(", ") },
  ];

  if (!profile)
    return (
      <div
        role="status"
        aria-busy="true"
        className="md:hidden flex h-screen w-full bg-ivory items-center justify-center"
      >
        <Sidebar />
        <p className="text-sm tracking-widest uppercase text-primary animate-pulse">
          Loading…
        </p>
      </div>
    );

  return (
    <>
      <main
        id="main-content"
        className="md:hidden flex flex-col min-h-screen bg-ivory overflow-y-auto pb-20"
      >
        <Sidebar />
        {/* ── Profile Card ── */}
        <section
          aria-labelledby="mobile-profile-name"
          className="flex flex-col items-center px-6 pt-14 pb-7 border-b border-divider"
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
            className="font-cormorant text-3xl font-semibold text-strong tracking-wide text-center leading-tight"
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
                <dd className="text-sm text-strong text-right truncate">
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
                  className="font-coptic text-sm text-strong px-3 py-2.5 border-l-2 border-transparent hover:border-amber-500 hover:text-black hover:bg-amber-50 transition-all duration-150 cursor-default tracking-wide"
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
            onClick={logout}
            className="flex items-center gap-3 w-full px-6 py-4 text-left font-coptic text-sm uppercase tracking-widest text-strong hover:text-red-700 hover:bg-red-50 transition-colors font-semibold"
          >
            <IconLogout />
            Sign Out
          </button>
        </div>
      </main>
    </>
  );
}