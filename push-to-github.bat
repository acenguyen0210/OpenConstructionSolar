@echo off
title OpenConstructionSolar - Push to GitHub
cd /d "%~dp0"

echo ==============================================================================
echo    OpenConstructionSolar - Day du lieu len GitHub
echo    Repository: https://github.com/acenguyen0210/OpenConstructionSolar.git
echo ==============================================================================
echo.

:: 1. Kiem tra Git
where git >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [LOI] Khong tim thay Git trong he thong PATH.
    echo Vui long cai dat Git tu https://git-scm.com/download/win va thu lai.
    echo.
    pause
    exit /b 1
)

:: 2. Cau hinh remote origin
echo [1/4] Kiem tra cau hinh remote origin...
git remote get-url origin >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    git remote set-url origin https://github.com/acenguyen0210/OpenConstructionSolar.git
) else (
    git remote add origin https://github.com/acenguyen0210/OpenConstructionSolar.git
)
echo       - Remote origin: https://github.com/acenguyen0210/OpenConstructionSolar.git

:: Cau hinh danh tinh Git neu chua co
git config user.name >nul 2>&1
if %ERRORLEVEL% NEQ 0 git config user.name "acenguyen0210"
git config user.email >nul 2>&1
if %ERRORLEVEL% NEQ 0 git config user.email "acenguyen0210@gmail.com"

:: 3. Kiem tra nhanh
for /f "tokens=*" %%i in ('git rev-parse --abbrev-ref HEAD 2^>nul') do set CURRENT_BRANCH=%%i
if "%CURRENT_BRANCH%"=="" set CURRENT_BRANCH=main
echo       - Nhanh lam viec: %CURRENT_BRANCH%
echo.

:: 4. Commit cac thay doi neu co
echo [2/4] Kiem tra va commit cac thay doi moi nhat...
git add -A
git commit -m "feat: Vietnam Solar EPC Edition - 12 nhom ho so SOP va catalog gia Solar VN" 2>nul
echo       - Code da duoc commit san sang.
echo.

:: 5. Lua chon phuong thuc day du lieu
echo [3/4] Chon phuong thuc day du lieu len GitHub:
echo       [1] Day truc tiep (Dung trinh duyet / Git Credential Manager)
echo       [2] Day bang GitHub Personal Access Token (Khuyen dung neu gap loi dang nhap)
echo       [3] Day kho sach Clean (~180MB ma khong kem 4GB lich su cu cua ban goc)
echo.
set /p PUSH_CHOICE="Chon [1, 2 hoac 3] (mac dinh la 1): "

if "%PUSH_CHOICE%"=="2" goto :push_with_token
if "%PUSH_CHOICE%"=="3" goto :clean_push

:push_direct
echo.
echo [4/4] Dang day du lieu len GitHub (Nhanh %CURRENT_BRANCH%)...
echo       (Neu trinh duyet mo cua so dang nhap, vui long xac thuc tai khoan)...
echo.
git push -u origin %CURRENT_BRANCH%
if %ERRORLEVEL% EQU 0 goto :success
goto :push_failed

:push_with_token
echo.
echo ==============================================================================
echo    HUONG DAN LAY GITHUB TOKEN (PERSONAL ACCESS TOKEN):
echo    1. Truy cap: https://github.com/settings/tokens
echo    2. Bam 'Generate new token' -^> 'Generate new token (classic)'
echo    3. Dat ten (Note: Solar), tich chon o [x] repo (Full control)
echo    4. Cuon xuong duoi cung bam 'Generate token' va COPY doan ma bat dau bang 'ghp_...'
echo ==============================================================================
echo.
set /p GH_TOKEN="Dan GitHub Token (ghp_...) vao day: "
if "%GH_TOKEN%"=="" (
    echo [LOI] Token khong duoc de trong.
    goto :end
)
echo.
echo [4/4] Dang day du lieu len GitHub bang Token...
git push -u https://%GH_TOKEN%@github.com/acenguyen0210/OpenConstructionSolar.git %CURRENT_BRANCH%
if %ERRORLEVEL% EQU 0 goto :success
goto :push_failed

:clean_push
echo.
echo [4/4] Dang tao nhanh moi gon nhe (chi chua ma nguon Solar hien tai ~180MB)...
git checkout --orphan solar-deploy 2>nul
git add -A
git commit -m "feat: OpenConstructionSolar - Vietnam Solar EPC Edition (12 nhom ho so SOP, catalog gia Solar VN)" 2>nul
echo.
set /p CLEAN_TOKEN="Nhap GitHub Token (hoac nhan Enter de dung xac thuc trinh duyet): "
if "%CLEAN_TOKEN%"=="" (
    git push -u origin solar-deploy:main --force
) else (
    git push -u https://%CLEAN_TOKEN%@github.com/acenguyen0210/OpenConstructionSolar.git solar-deploy:main --force
)
set PUSH_RES=%ERRORLEVEL%
git checkout %CURRENT_BRANCH% 2>nul
git branch -D solar-deploy 2>nul
if %PUSH_RES% EQU 0 goto :success
goto :push_failed

:success
echo.
echo ==============================================================================
echo    DA DAY DU LIEU LEN GITHUB THANH CONG!
echo    Xem truc tiep tai: https://github.com/acenguyen0210/OpenConstructionSolar
echo ==============================================================================
goto :end

:push_failed
echo.
echo ==============================================================================
echo    [CANH BAO] Lenh git push gap su co.
echo    Nguyen nhan thuong gap nhat:
echo      1. GitHub khong chap nhan mat khau tai khoan, can dung Personal Access Token.
echo         -^> Hay chay lai file bat nay va chon [2] de nhap Token.
echo      2. Neu kho chua lich su qua nang (4GB), hay chon [3] de day ban sach (~180MB).
echo ==============================================================================

:end
echo.
pause
