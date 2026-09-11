@echo off
echo === BIS Standards Intelligence - Development Server ===
echo.
echo Starting backend on port 8000...
start "BIS Backend" cmd /k "cd backend && pip install -r requirements.txt >nul 2>&1 && python -m uvicorn main:app --reload --port 8000"
echo Starting frontend on port 3000...
timeout /t 3 >nul
start "BIS Frontend" cmd /k "cd frontend && npm run dev"
echo.
echo Both servers are starting...
echo   Backend:  http://localhost:8000
echo   Frontend: http://localhost:3000
echo   Health:   http://localhost:8000/api/health
