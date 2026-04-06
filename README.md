# Open Church Management (OCM)

A fullstack church management system for Mavuno Young & Fearless and other low-church structures (non-denominational, Baptist, Pentecostal). Supports congregationalism, elder-led, and Moses model organisations.

## Stack

| Layer | Tech |
|---|---|
| Frontend | React 19, Vite, Tailwind CSS 4, MUI, DaisyUI |
| Backend | Django 6, Django REST Framework, Django Channels |
| Auth | Firebase Authentication |
| Database | PostgreSQL (Cloudinary for media) |
| Deployment | Vercel (frontend), Render (backend) |

## Features

- **Role-based access** — Pastors, Leaders, DG Leaders, Members each get a tailored dashboard and scoped API permissions
- **Member groups** — Serving teams, discipleship groups, age groups, leadership teams, ropes classes, campus trend
- **Messaging board** — Forum-style posts and comments with role-based permissions
- **Bible tools** — Memorisation plans and reading plans
- **Real-time** — Firebase Firestore for chat; Django Channels for WebSocket support
- **Payments** — Paystack integration

## Getting Started

### Frontend

```bash
cd frontend
npm install
cp .env.example .env        # set VITE_API_URL if pointing to local backend
npm run dev                 # runs on http://localhost:5174
```

### Backend

```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
# add firebase-key.json to backend/ and configure .env
python manage.py migrate
python manage.py runserver
```

**Required backend env vars:**
```
SECRET_KEY=
DATABASE_URL=
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=
PAYSTACK_SECRET_KEY=
```

Firebase service account key must be placed at `backend/firebase-key.json`.

## Deployment

- Frontend deploys via `vercel.json` to `https://opencms.vercel.app`
- Backend deploys via `render.yaml` + `build.sh` to `https://opencms-q36g.onrender.com`

## Contact

Bugs, feedback, or feature requests: [bg1b9xany@mozmail.com](mailto:bg1b9xany@mozmail.com)
