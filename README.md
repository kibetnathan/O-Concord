# Open Church Management (OCM)

A fullstack church management system built for Mavuno Young & Fearless and similar low-church structures (non-denominational, Baptist, Pentecostal). Supports congregationalist, elder-led, and Moses model organisations.

## Stack

| Layer | Tech |
|---|---|
| Frontend | React 19, Vite, React Router v7, Zustand |
| UI | Tailwind CSS 4, DaisyUI 5, MUI Material 7 |
| Backend | Django 6, Django REST Framework |
| Auth | Firebase Authentication |
| Real-time | Firebase Firestore (chat) |
| Database | PostgreSQL (prod), SQLite (local) |
| Media | Cloudinary |
| Payments | Paystack |
| Deployment | Vercel (frontend), Render (backend) |

## Features

- **Role-based access** — Pastors, Leaders, DG Leaders, Members each get a tailored dashboard and scoped API permissions
- **Serving teams** — Department management with crew assignments to services
- **Fellowship groups** — Discipleship/small group management with embedded chat
- **Leadership teams** — Named leadership groups across the church structure
- **Courses (ROPES classes)** — Training courses with member enrollment
- **Church services** — Service scheduling with crew and equipment tracking
- **Bible memorisation** — Spaced repetition verse review (5 translations: BSB, KJV, NIV, ESV, NASB)
- **Reading plans** — YouVersion plan integration scoped to groups, departments, or church-wide
- **Social feed** — Posts, comments, likes, and tags with role-based moderation
- **Real-time chat** — Firestore-backed chat rooms per group/department/course/leadership team
- **Outreach** — Charity organisation listings with Paystack donation links
- **Streaming** — YouTube live stream viewer with admin controls
- **Payments** — Paystack integration with server-side verification

## Project Structure

```
ocm-fullstack/
├── frontend/          # React 19 SPA (Vercel)
└── backend/           # Django 6 REST API (Render)
```

## Getting Started

### Prerequisites

- Node.js 18+
- Python 3.12+
- PostgreSQL (or use SQLite locally)
- Firebase project with Auth + Firestore enabled

---

### Frontend

```bash
cd frontend
npm install
cp .env.example .env   # configure env vars
npm run dev            # http://localhost:5174
```

**Environment variables** (`frontend/.env`):
```
VITE_API_URL=http://localhost:8000/api/
VITE_YOUTUBE_API_KEY=
VITE_PAYSTACK_PUBLIC_KEY=
```

`VITE_API_URL` defaults to the production backend if unset.

---

### Backend

```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env         # configure env vars
# place firebase-key.json in backend/
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver   # http://localhost:8000
```

**Environment variables** (`backend/.env`):
```
SECRET_KEY=
DATABASE_URL=              # omit to use SQLite locally
ALLOWED_HOSTS=
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=
PAYSTACK_SECRET_KEY=
BACKEND_ADMIN_EMAIL=
BACKEND_ADMIN_PASSWORD=
```

Firebase service account key must be placed at `backend/firebase-key.json`.

---

## Architecture

### Authentication

Firebase Auth is the identity source of truth. The frontend signs users in via Firebase, then attaches the ID token to every API request via an Axios interceptor. The Django backend validates tokens using a custom `FirebaseAuthentication` backend (`userapp/authentication.py`), which creates or syncs a `CustomUser` record on first login.

### Frontend State (Zustand)

| Store | Manages |
|---|---|
| `authStore` | Firebase session, token refresh, login/logout |
| `mainStore` | All church data — teams, groups, services, posts, etc. |
| `chatStore` | Firestore real-time chat rooms and messages |
| `profileStore` | Current user profile |
| `groupStore` | User group memberships |
| `useMemoriseStore` | Verse queue, due reviews, spaced repetition stats |
| `useReadingPlanStore` | Reading plans, joined plans |

### Backend Apps

#### `userapp`
- `CustomUser` — extended user model with `firebase_uid`
- `Profile` — date of birth, school, workplace, phone, campus, profile picture

#### `mainapp`
- `LeadershipTeam` — named leadership groups with members
- `Department` — serving teams led by a leader
- `Services` — church services with crew (departments) and pastor
- `Equipment` — audio/visual equipment linked to services or departments
- `FellowshipGroup` — discipleship/small groups; leader auto-added as member
- `Course` — ROPES training courses
- `MemorizeVerse` — verse queue with spaced repetition (intervals: 1→3→7→14 days)
- `MemorizationAttempt` — review history (4 difficulty levels, scores 0–3)
- `ReadingPlan` — YouVersion plans scoped to groups, departments, courses, or church-wide
- `CharityOrganisation` — outreach initiatives with donation links

#### `communication`
- `Post` — social feed posts with image, tags (django-taggit), and likes
- `Comment` — threaded comments on posts

### API Endpoints

Base URL: `/api/`

| Resource | Endpoints |
|---|---|
| Auth | `POST /register/`, `GET /users/me/`, `GET /check-username/` |
| Profile | `GET/PATCH /profile/{user_id}/` |
| Users | `GET /users/`, `GET /groups/` |
| Leadership | `GET/POST /leadership-team/` |
| Departments | `GET/POST /department/` |
| Services | `GET/POST /services/` |
| Equipment | `GET/POST /equipment/` |
| Fellowships | `GET/POST /fellowship-group/` |
| Courses | `GET/POST /course/` |
| Memorisation | `GET/POST /memorize/`, `GET /memorize/due/`, `POST /memorize/{id}/review/`, `GET /memorize/stats/` |
| Reading Plans | `GET/POST /reading-plans/`, `POST /reading-plans/{id}/join/`, `POST /reading-plans/{id}/leave/`, `GET /reading-plans/my/` |
| Charity | `GET/POST /charity-organisations/` |
| Feed | `GET/POST /post/`, `POST /posts/{id}/toggle_like/` |
| Comments | `GET/POST /comment/` |
| Payments | `POST /verify-payment/` |
| JWT | `POST /token/`, `POST /token/refresh/` |

### Roles & Permissions

| Role | Access |
|---|---|
| Pastor / Head Pastor | Full access; can create chat rooms |
| Leader / Jr Leader | Group and department management; can create chat rooms |
| Staff | Administrative access; can create chat rooms |
| Member | Read access; personal profile and group participation |

Permission classes: `IsAuthorOrPastor` (post moderation), `IsLeaderOrReadOnly` (resource management), `IsAuthenticated` (general access).

### Real-time Chat

Chat is backed by Firebase Firestore rather than Django Channels. Rooms are created per fellowship group, department, course, or leadership team. Messages support emoji reactions. Room creation is gated to leadership roles.

## Pages

| Route | Page |
|---|---|
| `/` | Home / landing |
| `/feed` | Social feed |
| `/feed/post/:postId` | Post detail |
| `/feed/upload` | Create post |
| `/threads` | Discussion threads |
| `/bible` | Bible search |
| `/plans/verses` | Verse memorisation |
| `/plans/reading` | Reading plans |
| `/streaming` | Live stream |
| `/outreach/charity` | Charity organisations |
| `/profile` | User profile |
| `/auth/login` | Login |
| `/auth/signup` | Sign up |
| `/dashboard` | Admin/leader dashboard |
| `/dashboard/groups/fellowship` | Fellowship group management |
| `/dashboard/groups/courses` | Course management |
| `/dashboard/groups/departments` | Department management |
| `/dashboard/groups/services` | Service management |
| `/dashboard/users/all` | User management |
| `/dashboard/users/leadership` | Leadership team management |
| `/dashboard/outreach/charity` | Charity management |
| `/dashboard/streaming` | Stream admin |

## Deployment

| Target | Config | URL |
|---|---|---|
| Frontend | `frontend/vercel.json` | `https://opencms.vercel.app` |
| Backend | `backend/render.yaml` + `build.sh` | `https://opencms-q36g.onrender.com` |

The backend runs as `gunicorn church.asgi:application -k uvicorn.workers.UvicornWorker`. Static files are served by WhiteNoise. CORS origins are configured in `church/settings.py`.

## Available Commands

### Frontend
```bash
npm run dev       # dev server
npm run build     # production build
npm run lint      # ESLint
npm run preview   # preview production build
```

### Backend
```bash
python manage.py runserver        # dev server
python manage.py migrate          # apply migrations
python manage.py makemigrations   # create migrations
python manage.py createsuperuser  # create admin user
pip install -r requirements.txt   # install dependencies
```

## Contact

Bugs, feedback, or feature requests: [bg1b9xany@mozmail.com](mailto:bg1b9xany@mozmail.com)
