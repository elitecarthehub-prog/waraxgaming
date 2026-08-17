@echo off
title Accurate TheGamesDB Cover Downloader
echo Installing required Python packages...
python -m pip install --upgrade openpyxl requests pillow
echo.
echo ==========================================
echo Starting accurate game cover downloader...
echo ==========================================
echo.
python download_game_covers_tgdb_v3.py
