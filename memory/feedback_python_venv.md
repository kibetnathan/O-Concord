---
name: Always use venv for Python commands
description: All backend Python/Django commands must be run with the venv activated at backend/venv/
type: feedback
---

Always activate the virtual environment before running any Python or Django management commands in the backend.

**Why:** User explicitly requires it — the project uses a venv at `backend/venv/`.

**How to apply:** Prefix all backend Python commands with `source venv/bin/activate &&`, e.g.:
```bash
source venv/bin/activate && python manage.py migrate
source venv/bin/activate && python manage.py collectstatic --no-input
source venv/bin/activate && python manage.py runserver
```
The venv is located at `/Users/nero/Projects/ocm-fullstack/backend/venv/bin/activate`.
