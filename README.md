# Doc-Locker

Private Citizen Bureaucracy & Document Expiry Locker

Problem Statement
Managing family documents (Aadhaar, PAN, Passport, License, Insurance, etc.) manually is error-prone.  
This system helps track expiry, required actions, and monthly document tasks in one place.

MVP Features
- Family member management
- Expiry status tracking:
  - `VALID`
  - `EXPIRING`
  - `ACTION_REQUIRED`
- Dashboard with monthly action summary
- Filter documents by member/category/status

Tech Stack
- **Frontend:** React + TypeScript
- **Backend:** Django + Django REST Framework
- **Database:** PostgreSQL
- **Auth:** JWT


## 📂Project Structure

```text
doc-locker/
├─ README.md
├─ .gitignore
├─ .env.example
├─ docker-compose.yml
│
├─ backend/
│  ├─ manage.py
│  ├─ requirements.txt
│  ├─ .env
│  │
│  ├─ config/                        # Django project config
│  │  ├─ __init__.py
│  │  ├─ settings.py                 # DB, installed apps, JWT, CORS
│  │  ├─ urls.py                     # root URL router
│  │  ├─ asgi.py
│  │  └─ wsgi.py
│  │
│  ├─ apps/                          # all business apps
│  │  ├─ users/
│  │  │  ├─ __init__.py
│  │  │  ├─ admin.py
│  │  │  ├─ apps.py
│  │  │  ├─ models.py                # custom user (optional) / profile
│  │  │  ├─ serializers.py
│  │  │  ├─ urls.py
│  │  │  ├─ views.py
│  │  │  ├─ permissions.py
│  │  │  └─ migrations/
│  │  │     └─ __init__.py
│  │  │
│  │  ├─ family/
│  │  │  ├─ __init__.py
│  │  │  ├─ admin.py
│  │  │  ├─ apps.py
│  │  │  ├─ models.py                # FamilyMember
│  │  │  ├─ serializers.py
│  │  │  ├─ urls.py
│  │  │  ├─ views.py
│  │  │  └─ migrations/
│  │  │     └─ __init__.py
│  │  │
│  │  ├─ documents/
│  │  │  ├─ __init__.py
│  │  │  ├─ admin.py
│  │  │  ├─ apps.py
│  │  │  ├─ models.py                # Document, category, expiry fields
│  │  │  ├─ serializers.py
│  │  │  ├─ urls.py
│  │  │  ├─ views.py
│  │  │  ├─ services.py              # state machine logic
│  │  │  ├─ constants.py             # VALID/EXPIRING/ACTION_REQUIRED
│  │  │  ├─ signals.py               # auto-status update hooks (optional)
│  │  │  ├─ tasks.py                 # reminder jobs (optional)
│  │  │  └─ migrations/
│  │  │     └─ __init__.py
│  │  │
│  │  └─ dashboard/
│  │     ├─ __init__.py
│  │     ├─ apps.py
│  │     ├─ urls.py
│  │     ├─ views.py                 # monthly timeline API
│  │     ├─ queries.py               # raw SQL / window-function query
│  │     └─ serializers.py
│  │
│  ├─ templates/                     # optional for email templates/admin overrides
│  ├─ static/                        # optional static files
│  ├─ media/                         # uploaded docs (if storing files)
│  │
│  └─ tests/
│     ├─ __init__.py
│     ├─ test_auth.py
│     ├─ test_family.py
│     ├─ test_documents.py
│     └─ test_dashboard.py
│
├─ frontend/
│  ├─ package.json
│  ├─ vite.config.ts
│  ├─ tsconfig.json
│  ├─ index.html
│  │
│  └─ src/
│     ├─ main.tsx
│     ├─ App.tsx
│     ├─ styles/
│     │  └─ globals.css
│     │
│     ├─ api/
│     │  ├─ client.ts                # axios/fetch base client
│     │  ├─ auth.ts
│     │  ├─ family.ts
│     │  ├─ documents.ts
│     │  └─ dashboard.ts
│     │
│     ├─ types/
│     │  ├─ auth.ts
│     │  ├─ family.ts
│     │  ├─ document.ts
│     │  └─ dashboard.ts
│     │
│     ├─ store/
│     │  ├─ authStore.ts
│     │  └─ uiStore.ts               # selected member/category tabs
│     │
│     ├─ hooks/
│     │  ├─ useAuth.ts
│     │  ├─ useFamily.ts
│     │  ├─ useDocuments.ts
│     │  └─ useDashboard.ts
│     │
│     ├─ components/
│     │  ├─ layout/
│     │  │  ├─ Navbar.tsx
│     │  │  └─ Sidebar.tsx
│     │  ├─ family/
│     │  │  ├─ MemberTabs.tsx
│     │  │  └─ MemberCard.tsx
│     │  ├─ documents/
│     │  │  ├─ DocumentForm.tsx
│     │  │  ├─ DocumentTable.tsx
│     │  │  ├─ DocumentCard.tsx
│     │  │  └─ StatusBadge.tsx
│     │  └─ dashboard/
│     │     ├─ MonthlyActions.tsx
│     │     └─ ExpiringSoonList.tsx
│     │
│     └─ pages/
│        ├─ LoginPage.tsx
│        ├─ DashboardPage.tsx
│        ├─ FamilyPage.tsx
│        ├─ DocumentsPage.tsx
│        └─ SettingsPage.tsx
│
└─ .vscode/
   ├─ settings.json
   ├─ extensions.json
   └─ launch.json
```



(Detailed setup steps will be added as implementation progresses.)

 
 Author
Rutuja Nikam
