@echo off
cd /d "%~dp0"

git add .
git commit -m "regular commit"
git push origin main