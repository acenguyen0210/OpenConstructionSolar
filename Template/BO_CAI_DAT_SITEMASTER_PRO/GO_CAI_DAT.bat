@echo off
chcp 65001 >nul
title GỠ CÀI ĐẶT BỘ ADD-IN SITEMASTER PRO
color 4F

echo ======================================================================
echo                  GỠ CÀI ĐẶT BỘ CÔNG CỤ SITEMASTER PRO
echo ======================================================================
echo.
set /p confirm="Bạn có chắc chắn muốn gỡ bỏ bộ Add-in này khỏi Excel? (Y/N): "
if /i not "%confirm%"=="Y" exit

taskkill /F /IM excel.exe >nul 2>&1

set "TARGET_DIR=%APPDATA%\Microsoft\AddIns"
if exist "%TARGET_DIR%\SiteMaster.xlam" del /f /q "%TARGET_DIR%\SiteMaster.xlam"
if exist "%TARGET_DIR%\QLVB_MiniTool.xlam" del /f /q "%TARGET_DIR%\QLVB_MiniTool.xlam"
if exist "%TARGET_DIR%\MiniTool" rmdir /s /q "%TARGET_DIR%\MiniTool"

reg delete "HKCU\Software\Microsoft\Office\16.0\Excel\Options" /v "OPEN" /f >nul 2>&1
reg delete "HKCU\Software\Microsoft\Office\16.0\Excel\Options" /v "OPEN1" /f >nul 2>&1
reg delete "HKCU\Software\Microsoft\Office\15.0\Excel\Options" /v "OPEN" /f >nul 2>&1
reg delete "HKCU\Software\Microsoft\Office\15.0\Excel\Options" /v "OPEN1" /f >nul 2>&1
reg delete "HKCU\Software\Microsoft\Office\14.0\Excel\Options" /v "OPEN" /f >nul 2>&1
reg delete "HKCU\Software\Microsoft\Office\14.0\Excel\Options" /v "OPEN1" /f >nul 2>&1

echo.
echo ======================================================================
echo   ĐÃ GỠ CÀI ĐẶT SẠCH SẼ TOÀN BỘ ADD-IN KHỎI PHẦN MỀM EXCEL!
echo ======================================================================
echo.
pause
