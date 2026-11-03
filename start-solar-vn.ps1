# OpenConstructionERP - Vietnam Solar EPC Edition Launcher
$Host.UI.RawUI.WindowTitle = "OpenConstructionERP - Vietnam Solar EPC Edition"

Write-Host "==============================================================================" -ForegroundColor Green
Write-Host "   OpenConstructionERP - Vietnam Solar EPC Edition (Solar PV in Vietnam)      " -ForegroundColor Yellow
Write-Host "==============================================================================" -ForegroundColor Green
Write-Host ""

$env:OE_PACK = "vietnam-solar"
$env:OE_LOCALE = "vi"
$env:OE_DEFAULT_CURRENCY = "VND"
$env:PYTHONPATH = "backend"

$cliPath = ".venv\Scripts\openconstructionerp.exe"
if (-not (Test-Path $cliPath)) {
    $cliPath = "openconstructionerp"
}

Write-Host "[1/2] Dang chuan bi may chu va co so du lieu PostgreSQL nhung..." -ForegroundColor Cyan
Write-Host "      - Web App: http://127.0.0.1:8080" -ForegroundColor White
Write-Host "      - Tai lieu API: http://127.0.0.1:8080/docs" -ForegroundColor White
Write-Host "      - Goi cau hinh: vietnam-solar" -ForegroundColor White
Write-Host ""
Write-Host "Tai khoan dang nhap:" -ForegroundColor Green
Write-Host "  [1] Admin:  admin@solar.vn               / admin123" -ForegroundColor Yellow
Write-Host "  [2] Demo:   demo@openconstructionerp.com / admin123" -ForegroundColor Yellow
Write-Host ""
Write-Host "(Vui long doi ~10-15 giay de he thong khoi tao va tu dong mo trinh duyet...)" -ForegroundColor Gray
Write-Host "Nhan Ctrl+C de dung may chu bat ky luc nao." -ForegroundColor DarkGray
Write-Host ""

& $cliPath serve --host 127.0.0.1 --port 8080 --open
