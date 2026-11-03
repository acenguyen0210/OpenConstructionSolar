# ==============================================================================
# OpenConstructionSolar - PowerShell GitHub Push Utility
# ==============================================================================
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$Host.UI.RawUI.WindowTitle = "OpenConstructionSolar - Day du lieu len GitHub"

Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host "   OpenConstructionSolar - Dong bo va Day du lieu len GitHub" -ForegroundColor Green
Write-Host "   Repository: https://github.com/acenguyen0210/OpenConstructionSolar.git" -ForegroundColor Yellow
Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host ""

# 1. Kiem tra Git
$gitCmd = Get-Command git -ErrorAction SilentlyContinue
if (-not $gitCmd) {
    Write-Host "[LOI] Khong tim thay Git trong he thong PATH." -ForegroundColor Red
    Write-Host "Vui long cai dat Git tu https://git-scm.com/download/win" -ForegroundColor White
    Read-Host "Nhan Enter de thoat..."
    exit 1
}

# 2. Cau hinh Remote
Write-Host "[1/4] Kiem tra ket noi GitHub repository..." -ForegroundColor Cyan
$remoteUrl = "https://github.com/acenguyen0210/OpenConstructionSolar.git"
$remotes = git remote
if ($remotes -contains "origin") {
    git remote set-url origin $remoteUrl
} else {
    git remote add origin $remoteUrl
}
Write-Host "      - Remote origin: $remoteUrl" -ForegroundColor Gray

# Git identity
$userName = git config user.name
if (-not $userName) { git config user.name "acenguyen0210" }
$userEmail = git config user.email
if (-not $userEmail) { git config user.email "acenguyen0210@gmail.com" }

$branch = (git rev-parse --abbrev-ref HEAD 2>$null)
if (-not $branch) { $branch = "main" }
Write-Host "      - Nhanh hien tai: $branch" -ForegroundColor Gray
Write-Host ""

# 3. Commit
Write-Host "[2/4] Kiem tra va dong goi ma nguon..." -ForegroundColor Cyan
git add -A
git commit -m "feat(solar): update OpenConstructionSolar - branding and configs" 2>$null
Write-Host "      - Ma nguon da san sang push." -ForegroundColor Gray
Write-Host ""

# 4. Lua chon
Write-Host "[3/4] Chon phuong thuc day du lieu:" -ForegroundColor Cyan
Write-Host "      [1] Day truc tiep (Trinh duyet / Git Credential Manager)" -ForegroundColor White
Write-Host "      [2] Day bang GitHub Personal Access Token" -ForegroundColor White
Write-Host "      [3] Day toi uu sach (~180MB, force push)" -ForegroundColor White
Write-Host ""
$choice = Read-Host "Nhap lua chon [1, 2 hoac 3] (mac dinh: 1)"
if (-not $choice) { $choice = "1" }

if ($choice -eq "2") {
    Write-Host ""
    Write-Host "==============================================================================" -ForegroundColor Yellow
    Write-Host "   HUONG DAN LAY GITHUB TOKEN (PERSONAL ACCESS TOKEN):" -ForegroundColor Yellow
    Write-Host "   1. Mo https://github.com/settings/tokens" -ForegroundColor White
    Write-Host "   2. Bam Generate new token -> Generate new token (classic)" -ForegroundColor White
    Write-Host "   3. Tich chon [repo] de cap quyen push code" -ForegroundColor White
    Write-Host "   4. Copy ma bat dau bang ghp_..." -ForegroundColor White
    Write-Host "==============================================================================" -ForegroundColor Yellow
    Write-Host ""
    $token = Read-Host "Dan Token vao day va nhan Enter"
    if (-not $token) {
        Write-Host "[LOI] Token khong duoc de trong!" -ForegroundColor Red
        Read-Host "Nhan Enter de tiep tuc..."
        exit 1
    }
    Write-Host ""
    Write-Host "[4/4] Dang day du lieu bang Token..." -ForegroundColor Cyan
    $pushUrl = "https://${token}@github.com/acenguyen0210/OpenConstructionSolar.git"
    git push -u $pushUrl $branch
} elseif ($choice -eq "3") {
    Write-Host ""
    Write-Host "[4/4] Dang tao ban day gon nhe toi uu..." -ForegroundColor Cyan
    git checkout --orphan solar-deploy 2>$null
    git add -A
    git commit -m "feat: OpenConstructionSolar - Vietnam Solar EPC Edition" 2>$null
    $token = Read-Host "Nhap Token GitHub (hoac nhan Enter de dung xac thuc trinh duyet)"
    if ($token) {
        $pushUrl = "https://${token}@github.com/acenguyen0210/OpenConstructionSolar.git"
        git push -u $pushUrl solar-deploy:main --force
    } else {
        git push -u origin solar-deploy:main --force
    }
    git checkout $branch 2>$null
    git branch -D solar-deploy 2>$null
} else {
    Write-Host ""
    Write-Host "[4/4] Dang day du lieu len GitHub (Nhanh $branch)..." -ForegroundColor Cyan
    git push -u origin $branch
}

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "==============================================================================" -ForegroundColor Green
    Write-Host "   [THANH CONG] DA DAY DU LIEU LEN GITHUB!" -ForegroundColor Green
    Write-Host "   Xem kho tai: https://github.com/acenguyen0210/OpenConstructionSolar" -ForegroundColor Yellow
    Write-Host "==============================================================================" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "==============================================================================" -ForegroundColor Red
    Write-Host "   [THONG BAO] Git push gap loi xac thuc hoac xung dot kho." -ForegroundColor Red
    Write-Host "   Giai phap:" -ForegroundColor Yellow
    Write-Host "   1. Chay lai va chon [2] de dung Personal Access Token." -ForegroundColor White
    Write-Host "   2. Neu kho tren GitHub da co san commit, dung lenh: git push -u origin $branch --force" -ForegroundColor White
    Write-Host "==============================================================================" -ForegroundColor Red
}

Write-Host ""
Read-Host "Nhan Enter de hoan tat..."
