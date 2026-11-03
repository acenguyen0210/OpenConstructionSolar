@echo off
chcp 65001 >nul
title OpenConstructionSolar - Day du lieu len GitHub
cd /d "%~dp0"

echo ==============================================================================
echo    OpenConstructionSolar - Dong bo va Day du lieu len GitHub
echo    Kho luu tru: https://github.com/acenguyen0210/OpenConstructionSolar.git
echo ==============================================================================
echo.

:: 1. Kiem tra Git
where git >nul 2>&1
if %ERRORLEVEL% NEQ 0 goto :no_git

:: 2. Cau hinh remote origin
echo [1/4] Kiem tra ket noi GitHub repository...
git remote get-url origin >nul 2>&1
if %ERRORLEVEL% EQU 0 goto :origin_ok
git remote add origin https://github.com/acenguyen0210/OpenConstructionSolar.git
goto :origin_done

:origin_ok
git remote set-url origin https://github.com/acenguyen0210/OpenConstructionSolar.git

:origin_done
echo       - Remote: https://github.com/acenguyen0210/OpenConstructionSolar.git

:: Cau hinh danh tinh Git co ban neu chua co
git config user.name >nul 2>&1
if %ERRORLEVEL% NEQ 0 git config user.name "acenguyen0210"
git config user.email >nul 2>&1
if %ERRORLEVEL% NEQ 0 git config user.email "acenguyen0210@gmail.com"

:: Xac dinh nhanh hien tai
set CURRENT_BRANCH=main
for /f "tokens=*" %%i in ('git rev-parse --abbrev-ref HEAD 2^>nul') do set CURRENT_BRANCH=%%i
echo       - Nhanh hien tai: %CURRENT_BRANCH%
echo.

:: 3. Them file va commit
echo [2/4] Kiem tra va dong goi cac thay doi moi nhat...
git add -A
git commit -m "feat(solar): update OpenConstructionSolar - branding and configs" 2>nul
echo       - Cac thay doi da duoc dong goi vao commit san sang.
echo.

:: 4. Lua chon phuong thuc day du lieu
echo [3/4] Chon phuong thuc day du lieu len GitHub:
echo       [1] Day truc tiep (Xac thuc qua trinh duyet / Git Credential Manager)
echo       [2] Day bang GitHub Personal Access Token (Khuyen dung neu gap loi)
echo       [3] Day sach kho Solar toi uu (~180MB)
echo.
set PUSH_METHOD=1
set /p PUSH_METHOD="Nhap lua chon [1, 2 hoac 3] (mac dinh la 1): "

if "%PUSH_METHOD%"=="2" goto :push_token
if "%PUSH_METHOD%"=="3" goto :push_clean

:push_normal
echo.
echo [4/4] Dang day du lieu len GitHub tren nhanh %CURRENT_BRANCH%...
echo       Neu trinh duyet bat cua so dang nhap, quy khach vui long xac thuc.
echo.
git push -u origin %CURRENT_BRANCH%
if %ERRORLEVEL% EQU 0 goto :push_success
goto :push_failed

:push_token
echo.
echo ==============================================================================
echo    HUONG DAN LAY GITHUB PERSONAL ACCESS TOKEN:
echo    1. Mo trinh duyet vao: https://github.com/settings/tokens
echo    2. Chon Generate new token -^> Generate new token (classic)
echo    3. Dat ten tuy y, tich chon o [repo] de cap quyen ghi
echo    4. Nhan Generate token va sao chep ma bat dau bang ghp_...
echo ==============================================================================
echo.
set GH_TOKEN=
set /p GH_TOKEN="Dan ma Token vao day va nhan Enter: "
if "%GH_TOKEN%"=="" goto :token_empty
echo.
echo [4/4] Dang day du lieu len GitHub bang Token...
git push -u https://%GH_TOKEN%@github.com/acenguyen0210/OpenConstructionSolar.git %CURRENT_BRANCH%
if %ERRORLEVEL% EQU 0 goto :push_success
goto :push_failed

:push_clean
echo.
echo [4/4] Dang tao nhanh phat hanh toi uu gon nhe...
git checkout --orphan solar-deploy 2>nul
git add -A
git commit -m "feat: OpenConstructionSolar - Vietnam Solar EPC Edition" 2>nul
echo.
set TOKEN_CLEAN=
set /p TOKEN_CLEAN="Nhap Token GitHub (hoac nhan Enter de dung trinh duyet): "
if "%TOKEN_CLEAN%"=="" goto :clean_direct
git push -u https://%TOKEN_CLEAN%@github.com/acenguyen0210/OpenConstructionSolar.git solar-deploy:main --force
goto :clean_finish

:clean_direct
git push -u origin solar-deploy:main --force

:clean_finish
set RES_CLEAN=%ERRORLEVEL%
git checkout %CURRENT_BRANCH% 2>nul
git branch -D solar-deploy 2>nul
if %RES_CLEAN% EQU 0 goto :push_success
goto :push_failed

:push_success
echo.
echo ==============================================================================
echo    [THANH CONG] DA DAY DU LIEU LEN GITHUB!
echo    Xem kho tai: https://github.com/acenguyen0210/OpenConstructionSolar
echo ==============================================================================
goto :finish

:push_failed
echo.
echo ==============================================================================
echo    [THONG BAO] Khong the day du lieu len GitHub.
echo.
echo    Nguyen nhan va huong xu ly:
echo    1. Kho GitHub chua cap quyen ghi hoac chua dang nhap:
echo       -^> Hay chay lai file .bat nay va chon phuong an [2] de dung Token.
echo    2. Neu kho GitHub tren web da co commit tu truoc:
echo       -^> Chay lenh: git push -u origin %CURRENT_BRANCH% --force
echo ==============================================================================
goto :finish

:token_empty
echo [LOI] Token khong duoc de trong!
goto :finish

:no_git
echo [LOI] Khong tim thay Git trong may tinh.
echo Vui long cai dat Git tai https://git-scm.com/download/win va thu lai.
goto :finish

:finish
echo.
pause
