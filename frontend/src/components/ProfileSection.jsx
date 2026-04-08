import React, { useEffect, useState } from "react";
import useProfileStore from "../zustand/profileStore";
import useAuthStore from "../zustand/authStore";
import useMainStore from "../zustand/mainStore";
import EditProfileForm from "./EditProfileForm";

const IconEdit = () => (
  <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" strokeWidth="1.5" viewBox="0 0 24 24">
    <path strokeLinecap="round" strokeLinejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10" />
  </svg>
);

function ProfileSection() {
  const token = useAuthStore((state) => state.token);
  const [editOpen, setEditOpen] = useState(false);

  useEffect(() => {
    if (token) useProfileStore.getState().fetchProfile();
  }, [token]);

  useEffect(() => {
    if (token) useMainStore.getState().fetchFellowships();
  }, [token]);

  const profile          = useProfileStore((state) => state.profile);
  const fellowships      = useMainStore((state) => state.fellowships);
  const user             = useAuthStore((state) => state.user);

  const fellowship_group = fellowships?.results ?? (Array.isArray(fellowships) ? fellowships : []);

  const fullName =
    user?.first_name && user?.last_name
      ? `${user.first_name} ${user.last_name}`
      : "Guest User";

  if (!profile)
    return (
      <aside
        aria-label="Profile"
        aria-busy="true"
        className="sticky right-0 top-0 h-screen w-100 bg-porcelain border-l border-stone-200 md:flex hidden items-center justify-center"
      >
        <p className="text-sm tracking-widest uppercase text-stone-700 animate-pulse">
          Loading…
        </p>
      </aside>
    );

  const profileFields = [
    { label: "Campus",    value: profile?.campus },
    { label: "School",    value: profile?.school },
    { label: "Workplace", value: profile?.workplace },
    { label: "Role",      value: user?.groups?.join(", ") },
  ];

  const myGroups = fellowship_group?.filter((g) => g.members?.includes(user?.id));

  return (
    <>
      <aside
        aria-label="Profile"
        className="sticky right-0 top-0 h-screen w-100 bg-porcelain border-l border-stone-200 md:flex hidden flex-col overflow-y-auto"
      >

        {/* ── Profile Card ── */}
        <section
          aria-labelledby="profile-name"
          className="flex flex-col items-center px-6 pt-10 pb-7 border-b border-stone-200"
        >

          {/* Avatar */}
          <div className="relative mb-5">
            <img
              src={profile?.profile_pic_url || "/images/defaultavatar.jpg"}
              alt={`${fullName}'s profile picture`}
              className="w-20 h-20 rounded-full object-cover ring-2 ring-amber-500/30"
            />
            <span
              aria-hidden="true"
              className="absolute bottom-0.5 right-0.5 w-3 h-3 bg-amber-500 rounded-full ring-2 ring-white"
            />
          </div>

          {/* Name & username */}
          <h2
            id="profile-name"
            className="font-cormorant text-2xl font-semibold text-stone-900 tracking-wide text-center leading-tight"
          >
            {fullName}
          </h2>
          <p className="font-coptic text-sm text-stone-700 tracking-widest mt-1">
            @{user?.username}
          </p>

          <div className="w-8 h-px bg-amber-500/40 my-4" aria-hidden="true" />

          {/* Profile fields */}
          <dl className="w-full flex flex-col gap-3">
            {profileFields.map(({ label, value }) => (
              <div key={label} className="flex items-baseline justify-between gap-3">
                <dt className="text-xs uppercase tracking-[0.18em] text-stone-700 font-semibold shrink-0">
                  {label}
                </dt>
                <dd className="text-sm text-stone-800 text-right truncate">
                  {value || "—"}
                </dd>
              </div>
            ))}
          </dl>
        </section>

        {/* ── My Groups ── */}
        <section
          aria-labelledby="my-groups-heading"
          className="flex flex-col flex-1 px-6 py-6"
        >
          <div className="flex items-center gap-2 mb-4">
            <h3
              id="my-groups-heading"
              className="text-xs uppercase tracking-[0.22em] text-stone-700 font-semibold"
            >
              My Groups
            </h3>
            <div className="flex-1 h-px bg-stone-200" aria-hidden="true" />
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
                  className="font-coptic text-sm text-stone-800 px-3 py-2.5 border-l-2 border-transparent hover:border-amber-500 hover:text-black hover:bg-amber-50 transition-all duration-150 cursor-default tracking-wide"
                >
                  {group.name}
                </li>
              ))
            ) : (
              <li className="text-xs text-stone-700 tracking-widest uppercase py-2">
                No groups yet
              </li>
            )}
          </ul>
        </section>

        {/* ── Footer ── */}
        <button
          type="button"
          onClick={() => setEditOpen(true)}
          className="flex items-center gap-3 w-full px-4 py-3 text-left font-coptic text-xs uppercase tracking-widest text-stone-800 hover:text-amber-700 hover:cursor-pointer hover:bg-amber-50 transition-colors group"
        >
          <IconEdit />
          Edit Profile
        </button>

        <div className="px-6 py-4 border-t border-stone-200">
          <p className="text-xs tracking-[0.22em] uppercase text-stone-700">
            Open Church Management
          </p>
        </div>

      </aside>

      {/* Slide-in edit panel — outside aside so it overlays the full page */}
      <EditProfileForm open={editOpen} onClose={() => setEditOpen(false)} />
    </>
  );
}

export default ProfileSection;