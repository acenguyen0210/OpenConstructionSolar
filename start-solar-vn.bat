@echo off
setlocal enabledelayedexpansion
title OpenConstructionSolar - Vietnam Solar EPC Edition

cd /d "%~dp0"

echo ==============================================================================
echo    OpenConstructionSolar - Vietnam Solar EPC Edition (Solar PV in Vietnam)
echo ==============================================================================
echo.
echo [1/3] Setting Vietnam Solar environment and 9router AI...
set OE_PACK=vietnam-solar
set OE_LOCALE=vi
set OE_DEFAULT_CURRENCY=VND
set OE_CONNECTORS_BASE_DIR=*
set PYTHONPATH=backend

:: 9router AI Local Configuration
set OE_VLLM_URL=http://127.0.0.1:20128/v1
set OE_VLLM_API_KEY=sk-45a61675590eb5f7-1aoo33-1d15d819
set OE_VLLM_MODEL=ag/gemini-3.8-flash

if exist ".venv\Scripts\openconstructionerp.exe" (
    set CLI_EXE=.venv\Scripts\openconstructionerp.exe
    echo [2/3] Using CLI from virtualenv: !CLI_EXE!
) else (
    set CLI_EXE=openconstructionerp
    echo [2/3] Using system CLI: !CLI_EXE!
)

echo [3/3] Starting OpenConstructionSolar server with embedded PostgreSQL...
echo       - Web UI: http://127.0.0.1:8080
echo       - API Docs: http://127.0.0.1:8080/docs
echo       - Active Pack: vietnam-solar (Vietnam Solar EPC)
echo       - AI Router: 9router at http://127.0.0.1:20128/v1 (ag/gemini-3.8-flash)
echo.
echo Dang nhap / Login Accounts:
echo   [1] Admin:  admin@solar.vn               / admin123
echo   [2] Demo:   demo@openconstructionerp.com / admin123
echo.
echo (He thong khoi dong trong khoang 10-15 giay va tu dong mo trinh duyet...)
echo Nhan Ctrl+C de dung may chu.
echo.

!CLI_EXE! serve --host 127.0.0.1 --port 8080 --open
pause
