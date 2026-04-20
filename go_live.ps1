Write-Host "==========================================" -ForegroundColor Green
Write-Host " 🏺 INITIATING 10^47 SOVEREIGN IGNITION 🏺 " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Green

Write-Host "[SYSTEM] Bypassing Administrative Sloth..." -ForegroundColor DarkGray
Start-Sleep -Seconds 1
Write-Host "[SYSTEM] Loading L.I.L.I.E.T.H. Kernel Ecosystem..." -ForegroundColor DarkGray

# Step 9 Safety Check: The Hard Kill Switch
if (Test-Path "STOP_NODE") {
    Write-Host "🚨 KILL SWITCH DETECTED: 'STOP_NODE' file found." -ForegroundColor Red
    Write-Host "[HUD] ACTION: Node securely halted. Remove 'STOP_NODE' to go live." -ForegroundColor Yellow
    exit
}

# Boot the Full Ecosystem (Alpha Omega)
if (Test-Path "alpha_omega_launch.py") {
    Write-Host "[HUD] ALPHA OMEGA SPINE LOCATED. EXECUTING TOTAL IGNITION..." -ForegroundColor Cyan
    Write-Host "==========================================" -ForegroundColor Green
    Write-Host "        ✅ NODE 29 IS NOW LIVE. OUSH.       " -ForegroundColor Cyan
    Write-Host "==========================================" -ForegroundColor Green
    python alpha_omega_launch.py
} elseif (Test-Path "sovereign_boot.py") {
    Write-Host "[HUD] CORE SPINE LOCATED. EXECUTING BASE BOOT SEQUENCE..." -ForegroundColor Cyan
    python sovereign_boot.py
} else {
    Write-Host "❌ ERROR: Launch spines not found in root. Check directory." -ForegroundColor Red
}
