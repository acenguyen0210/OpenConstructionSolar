@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul
title OpenConstructionSolar - Vietnam Solar EPC Edition

cd /d "%~dp0"

echo ==============================================================================
echo             OPENCONSTRUCTION SOLAR - VIETNAM SOLAR EPC
echo ==============================================================================
echo.

:: 1. Thiet lap moi truong ngam
set OE_PACK=vietnam-solar
set OE_LOCALE=vi
set OE_DEFAULT_CURRENCY=VND
set OE_CONNECTORS_BASE_DIR=*
set PYTHONPATH=backend

:: 9router AI Local
set OE_VLLM_URL=http://127.0.0.1:20128/v1
set OE_VLLM_API_KEY=sk-45a61675590eb5f7-1aoo33-1d15d819
set OE_VLLM_MODEL=ag/gemini-3.8-flash

:: Tao thu muc chua nhat ky log neu chua co
if not exist "logs" mkdir "logs"

:: 2. Xac dinh trinh thuc thi CLI
if exist ".venv\Scripts\openconstructionerp.exe" (
    set "CLI_EXE=.venv\Scripts\openconstructionerp.exe"
) else (
    set "CLI_EXE=openconstructionerp"
)

:: Kiem tra neu may chu da dang chay tren cong 8080
curl.exe -s -m 1 http://127.0.0.1:8080/ >nul 2>&1
if !errorlevel! equ 0 (
    echo [*] May chu OpenConstructionSolar da dang hoat dong tren cong 8080.
    goto SERVER_READY
)

echo [*] Dang khoi dong may chu OpenConstructionSolar...
echo     (Nhat ky duoc ghi vao file: logs\solar-server.log)
echo.

:: Lay ky tu Carriage Return (CR) de cap nhat tien trinh tren 1 dong
for /f %%a in ('copy /Z "%~dpf0" nul') do set "CR=%%a"

:: Khoi dong may chu ngam va chuyen toan bo log vao file
start "" /B !CLI_EXE! serve --host 127.0.0.1 --port 8080 > "logs\solar-server.log" 2>&1

:: Vong lap cho kem thoi gian dem giay (toi da 45 giay)
set /a MAX_WAIT=45
set /a ELAPSED=0

:WAIT_LOOP
curl.exe -s -m 1 http://127.0.0.1:8080/ >nul 2>&1
if !errorlevel! equ 0 goto SERVER_READY

set /a ELAPSED+=1
<nul set /p "=  [Tien trinh] Dang khoi dong may chu: !ELAPSED!s / !MAX_WAIT!s (vui long cho...)!CR!"

if !ELAPSED! geq !MAX_WAIT! goto SERVER_TIMEOUT

:: Cho 1 giay
ping -n 2 127.0.0.1 >nul
goto WAIT_LOOP

:SERVER_READY
echo.
echo.
echo ==============================================================================
echo             MAY CHU DA SAN SANG HOAT DONG!
echo ==============================================================================
echo   - Dia chi Web:      http://127.0.0.1:8080
echo   - API Swagger Docs: http://127.0.0.1:8080/docs
echo   - Goi mo rong:      vietnam-solar (Solar EPC Viet Nam)
echo   - Tro ly AI:        9router (ag/gemini-3.8-flash tai port 20128)
echo.
echo   Tai khoan dang nhap:
echo     [1] Quan tri (Admin): admin@solar.vn / admin123
echo     [2] Thu nghiem (Demo): demo@solar.vn  / admin123
echo ==============================================================================
echo.
echo [*] Dang tu dong mo trinh duyet...
start http://127.0.0.1:8080

echo.
echo [*] May chu dang hoat dong.
echo     Nhan phim bat ky de dung may chu va thoat cua so...
pause >nul

echo.
echo [*] Dang dung may chu...
powershell -NoProfile -Command "Get-NetTCPConnection -LocalPort 8080 -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }" >nul 2>&1
echo [OK] Da dung may chu.
goto END

:SERVER_TIMEOUT
echo.
echo.
echo ==============================================================================
echo   [LOI] May chu khong the phan hoi sau !MAX_WAIT! giay!
echo ==============================================================================
echo   Trich xuat 20 dong nhat ky cuoi cung tu logs\solar-server.log:
echo ------------------------------------------------------------------------------
if exist "logs\solar-server.log" (
    powershell -NoProfile -Command "Get-Content -Tail 20 'logs\solar-server.log'"
) else (
    echo   (Khong tim thay file logs\solar-server.log)
)
echo ------------------------------------------------------------------------------
echo   Vui long kiem tra lai hoac xem truc tiep file logs\solar-server.log.
echo.
pause

:END
