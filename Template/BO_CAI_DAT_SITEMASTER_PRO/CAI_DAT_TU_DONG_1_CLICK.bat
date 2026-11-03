@echo off
chcp 65001 >nul
title CÀI ĐẶT BỘ CÔNG CỤ SITEMASTER PRO 2026 (PORTABLE & ALL-IN-ONE)
color 1F

echo ======================================================================
echo          HỆ THỐNG CÀI ĐẶT BỘ CÔNG CỤ KỸ SƯ SITEMASTER PRO 2026
echo         Tích hợp: ITP Solar PV + Quản Lý Văn Bản + CSDL Dự Án
echo         Tác giả: Nguyễn Đức Thắng  -  Hotline: 0962.228.783
echo ======================================================================
echo.

:: 1. Tự động đóng Excel nếu đang chạy để tránh khóa file
echo [1/4] Đang kiểm tra trạng thái phần mềm Excel...
taskkill /F /IM excel.exe >nul 2>&1
echo       -> Đã sẵn sàng.

:: 2. Khởi tạo thư mục đích trong AppData và sao chép TRỌN BỘ CÙNG THƯ MỤC
echo [2/4] Đang đồng bộ trọn bộ Add-in, Template và CSDL vào hệ thống...
set "TARGET_DIR=%APPDATA%\Microsoft\AddIns"
if not exist "%TARGET_DIR%" mkdir "%TARGET_DIR%"

copy /y "%~dp0SiteMaster.xlam" "%TARGET_DIR%\" >nul
copy /y "%~dp0QLVB_MiniTool.xlam" "%TARGET_DIR%\" >nul
copy /y "%~dp0Template_ITP_Pro.xlsx" "%TARGET_DIR%\" >nul
copy /y "%~dp0Template_QLVB.xlsx" "%TARGET_DIR%\" >nul
copy /y "%~dp0SiteMaster_Projects.json" "%TARGET_DIR%\" >nul

echo [3/4] Đang sao chép thư viện phụ trợ MiniTool...
if not exist "%TARGET_DIR%\MiniTool" mkdir "%TARGET_DIR%\MiniTool"
xcopy /s /e /y /i "%~dp0MiniTool" "%TARGET_DIR%\MiniTool" >nul

:: 3. Tự động đăng ký Registry để Excel nạp ngay lập tức
echo [4/4] Đang tự động đăng ký kích hoạt thanh công cụ trên Excel...

:: Đăng ký cho Office 365 / 2021 / 2019 / 2016 (v16.0)
reg add "HKCU\Software\Microsoft\Office\16.0\Excel\Options" /v "OPEN" /t REG_SZ /d "\"%TARGET_DIR%\SiteMaster.xlam\"" /f >nul 2>&1
reg add "HKCU\Software\Microsoft\Office\16.0\Excel\Options" /v "OPEN1" /t REG_SZ /d "\"%TARGET_DIR%\QLVB_MiniTool.xlam\"" /f >nul 2>&1

:: Tự động cấp quyền tin cậy (Trusted Location) để macro chạy 100% không bị chặn
reg add "HKCU\Software\Microsoft\Office\16.0\Excel\Security\Trusted Locations\SiteMasterAddIns" /v "Path" /t REG_SZ /d "%TARGET_DIR%" /f >nul 2>&1
reg add "HKCU\Software\Microsoft\Office\16.0\Excel\Security\Trusted Locations\SiteMasterAddIns" /v "AllowSubFolders" /t REG_DWORD /d 1 /f >nul 2>&1
reg add "HKCU\Software\Microsoft\Office\16.0\Excel\Security\Trusted Locations\SiteMasterAddIns" /v "Description" /t REG_SZ /d "SiteMaster Pro Suite" /f >nul 2>&1

:: Đăng ký dự phòng cho Office 2013 (v15.0)
reg add "HKCU\Software\Microsoft\Office\15.0\Excel\Options" /v "OPEN" /t REG_SZ /d "\"%TARGET_DIR%\SiteMaster.xlam\"" /f >nul 2>&1
reg add "HKCU\Software\Microsoft\Office\15.0\Excel\Options" /v "OPEN1" /t REG_SZ /d "\"%TARGET_DIR%\QLVB_MiniTool.xlam\"" /f >nul 2>&1
reg add "HKCU\Software\Microsoft\Office\15.0\Excel\Security\Trusted Locations\SiteMasterAddIns" /v "Path" /t REG_SZ /d "%TARGET_DIR%" /f >nul 2>&1
reg add "HKCU\Software\Microsoft\Office\15.0\Excel\Security\Trusted Locations\SiteMasterAddIns" /v "AllowSubFolders" /t REG_DWORD /d 1 /f >nul 2>&1

echo.
echo ======================================================================
echo                  CÀI ĐẶT HOÀN TẤT THÀNH CÔNG 100%!
echo.
echo   • Thư mục bộ cài này có thể COPY SANG MÁY KHÁC HOẶC USB bất cứ lúc nào!
echo   • Toàn bộ Add-in, Biểu mẫu và CSDL dự án đều nằm chung trong 1 thư mục.
echo   • Mở Microsoft Excel: Thanh Ribbon [SITEMASTER PRO] đã sẵn sàng!
echo ======================================================================
echo.
pause
