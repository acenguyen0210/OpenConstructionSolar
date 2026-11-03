# OpenConstructionSolar - Git Sync & Push Script
$Host.UI.RawUI.WindowTitle = "OpenConstructionSolar - Push to GitHub"

Write-Host "==============================================================================" -ForegroundColor Green
Write-Host "   OpenConstructionSolar - Day du lieu len GitHub                             " -ForegroundColor Yellow
Write-Host "   Repository: https://github.com/acenguyen0210/OpenConstructionSolar.git     " -ForegroundColor Cyan
Write-Host "==============================================================================" -ForegroundColor Green
Write-Host ""

# 1. Kiem tra Git
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "[LOI] Khong tim thay Git trong he thong PATH." -ForegroundColor Red
    Write-Host "Vui long cai dat Git tu https://git-scm.com/download/win va thu lai." -ForegroundColor Yellow
    Read-Host "Nhan Enter de thoat..."
    exit 1
}

# 2. Cau hinh remote origin
Write-Host "[1/4] Kiem tra cau hinh remote origin..." -ForegroundColor Cyan
$remotes = git remote
if ($remotes -contains "origin") {
    git remote set-url origin https://github.com/acenguyen0210/OpenConstructionSolar.git
} else {
    git remote add origin https://github.com/acenguyen0210/OpenConstructionSolar.git
}
Write-Host "      - Remote origin: https://github.com/acenguyen0210/OpenConstructionSolar.git" -ForegroundColor White

# Cau hinh danh tinh Git neu chua co
$gitName = git config user.name
if ([string]::IsNullOrWhiteSpace($gitName)) { git config user.name "acenguyen0210" }
$gitEmail = git config user.email
if ([string]::IsNullOrWhiteSpace($gitEmail)) { git config user.email "acenguyen0210@gmail.com" }

# 3. Nhanh hien tai
$currentBranch = (git rev-parse --abbrev-ref HEAD).Trim()
if ([string]::IsNullOrWhiteSpace($currentBranch)) { $currentBranch = "main" }
Write-Host "      - Nhanh lam viec: $currentBranch" -ForegroundColor White
Write-Host ""

# 4. Stage & Commit
Write-Host "[2/4] Kiem tra va commit cac thay doi moi nhat..." -ForegroundColor Cyan
git add -A
git commit -m "feat: Vietnam Solar EPC Edition - 12 nhom ho so SOP va catalog gia Solar VN" 2>$null
Write-Host "      - Code da duoc commit san sang." -ForegroundColor DarkGray
Write-Host ""

# 5. Lua chon phuong thuc
Write-Host "[3/4] Chon phuong thuc day du lieu len GitHub:" -ForegroundColor Cyan
Write-Host "      [1] Day truc tiep (Dung trinh duyet / Git Credential Manager)" -ForegroundColor White
Write-Host "      [2] Day bang GitHub Personal Access Token (Khuyen dung neu gap loi dang nhap)" -ForegroundColor Yellow
Write-Host "      [3] Day kho sach Clean (~180MB ma khong kem 4GB lich su cu cua ban goc)" -ForegroundColor Green
Write-Host ""
$choice = Read-Host "Chon [1, 2 hoac 3] (mac dinh la 1)"

if ($choice -eq "2") {
    Write-Host ""
    Write-Host "==============================================================================" -ForegroundColor Yellow
    Write-Host "   HUONG DAN LAY GITHUB TOKEN (PERSONAL ACCESS TOKEN):" -ForegroundColor White
    Write-Host "   1. Truy cap: https://github.com/settings/tokens" -ForegroundColor Gray
    Write-Host "   2. Bam 'Generate new token' -> 'Generate new token (classic)'" -ForegroundColor Gray
    Write-Host "   3. Dat ten (Note: Solar), tich chon o [x] repo (Full control)" -ForegroundColor Gray
    Write-Host "   4. Cuon xuong duoi cung bam 'Generate token' va COPY doan ma bat dau bang 'ghp_...'" -ForegroundColor Gray
    Write-Host "==============================================================================" -ForegroundColor Yellow
    Write-Host ""
    $token = Read-Host "Dan GitHub Token (ghp_...) vao day"
    if ([string]::IsNullOrWhiteSpace($token)) {
        Write-Host "[LOI] Token khong duoc de trong." -ForegroundColor Red
        Read-Host "Nhan Enter de thoat..."
        exit 1
    }
    Write-Host ""
    Write-Host "[4/4] Dang day du lieu len GitHub bang Token..." -ForegroundColor Cyan
    git push -u "https://$($token)@github.com/acenguyen0210/OpenConstructionSolar.git" $currentBranch
} elseif ($choice -eq "3") {
    Write-Host ""
    Write-Host "[4/4] Dang tao nhanh moi gon nhe (chi chua ma nguon Solar hien tai ~180MB)..." -ForegroundColor Cyan
    git checkout --orphan solar-deploy 2>$null
    git add -A
    git commit -m "feat: OpenConstructionSolar - Vietnam Solar EPC Edition (12 nhom ho so SOP, catalog gia Solar VN)" 2>$null
    Write-Host ""
    $cleanToken = Read-Host "Nhap GitHub Token (hoac nhan Enter de dung xac thuc trinh duyet)"
    if ([string]::IsNullOrWhiteSpace($cleanToken)) {
        git push -u origin solar-deploy:main --force
    } else {
        git push -u "https://$($cleanToken)@github.com/acenguyen0210/OpenConstructionSolar.git" solar-deploy:main --force
    }
    git checkout $currentBranch 2>$null
    git branch -D solar-deploy 2>$null
} else {
    Write-Host ""
    Write-Host "[4/4] Dang day du lieu len GitHub ($currentBranch)..." -ForegroundColor Cyan
    Write-Host "      (Neu trinh duyet mo cua so dang nhap, vui long xac thuc tai khoan)..." -ForegroundColor Gray
    Write-Host ""
    git push -u origin $currentBranch
}

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "==============================================================================" -ForegroundColor Green
    Write-Host "   DA DAY DU LIEU LEN GITHUB THANH CONG!                                      " -ForegroundColor Green
    Write-Host "   Xem truc tiep tai: https://github.com/acenguyen0210/OpenConstructionSolar  " -ForegroundColor Yellow
    Write-Host "==============================================================================" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "[CANH BAO] Lenh git push gap su co." -ForegroundColor Red
    Write-Host "Nguyen nhan thuong gap nhat:" -ForegroundColor Yellow
    Write-Host "  1. GitHub khong chap nhan mat khau tai khoan, can dung Personal Access Token." -ForegroundColor White
    Write-Host "     -> Chay lai script va chon [2] de nhap Token." -ForegroundColor Gray
    Write-Host "  2. Neu kho chua lich su qua nang (4GB), hay chon [3] de day ban sach (~180MB)." -ForegroundColor Gray
}

Write-Host ""
Read-Host "Nhan Enter de ket thuc..."
