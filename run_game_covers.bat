@echo off
title TheGamesDB Game Cover Downloader
echo Installing required packages...
python -m pip install --upgrade openpyxl requests pillow
echo.
echo Starting...
python download_game_covers_tgdb.py
echo.
pause
