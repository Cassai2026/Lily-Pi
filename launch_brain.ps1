Write-Host "--- 🏺 INITIALIZING ENKI BRAIN: NODE 29 ---" -ForegroundColor Cyan
Write-Host "Entering lil-pi/brain_node..." -ForegroundColor Gray

# Navigate, Execute, and Return
Set-Location -Path "lil-pi/brain_node"
python main.py
Set-Location -Path "../../"

Write-Host "--- 🛡️ NODE SECURED. RETURNED TO ROOT. ---" -ForegroundColor Green
