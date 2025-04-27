@echo off
setlocal EnableDelayedExpansion
title Discord Giveaway Calculator
color 0b

:: Set window size to match the desired dimensions
mode con: cols=72 lines=30

:: Animation effect
echo Loading Discord Giveaway Calculator...
echo.
ping -n 2 127.0.0.1 > nul

echo =================================================
echo           DISCORD GIVEAWAY CALCULATOR
echo =================================================
echo.
echo A simple tool to calculate your odds of winning
echo Discord giveaways with various requirements.
echo.
ping -n 3 127.0.0.1 > nul

:: Check if Python is installed
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH.
    echo Please install Python 3.6 or higher before using this tool.
    echo.
    echo Press any key to open the HTML interface...
    pause > nul
    start "" "%~dp0..\index.html"
) else (
    echo Python detected. Checking dependencies...
    
    :: Check if required packages are installed
    python -c "import argparse, colorama" > nul 2>&1
    if %errorlevel% neq 0 (
        echo Installing required packages...
        pip install -r "%~dp0requirements.txt"
    ) else (
        echo Dependencies satisfied.
    )
    
    echo.
    echo Starting Discord Giveaway Calculator...
    
    :: Start the calculator with web UI
    cd ..
    python giveaway_odds_calculator.py --web-ui
)

exit 