Write-Host "--- 🏺 IGNITING THE 29TH NODE ---" -ForegroundColor Cyan
Set-Location -Path "lil-pi/brain_node"

# Run the Brain
python main.py

# When finished, return and show the logs
Set-Location -Path "../../"
Write-Host "--- 🛡️ SESSION COMPLETE. OPENING AUDIT TRAIL... ---" -ForegroundColor Yellow
if (Test-Path "audit_logs/sovereign_audit_trail.txt") {
    notepad "audit_logs/sovereign_audit_trail.txt"
}
