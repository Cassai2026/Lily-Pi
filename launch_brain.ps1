Write-Host "--- 🏺 IGNITING THE 29TH NODE ---" -ForegroundColor Cyan
if (Test-Path "lil-pi/brain_node") {
    Set-Location -Path "lil-pi/brain_node"
    python main.py
    Set-Location -Path "../../"
} else {
    Write-Host "❌ ERROR: Path not found. Stay in root." -ForegroundColor Red
}
