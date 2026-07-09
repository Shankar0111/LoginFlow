# Seeded Test Users

Use these credentials for login testing after running `backend/seed_users.py`.

1. admin / admin123
2. user1 / pass1
3. user2 / pass2
4. user3 / pass3
5. tester / test123
6. guest / guest123
7. shankar / RATbat@1

## How to seed the users

1. Open a terminal in your project root.
2. Run:

```powershell
cd backend
python seed_users.py
```

3. Then start the backend and frontend:

```powershell
uvicorn main:app --reload
```

In another terminal:

```powershell
cd ..\frontend
npm start
```
