@echo off
echo ================================================
echo    AVVIO SERVER BIBLIOGRAFIA CISUI
echo ================================================
echo.
echo Avvio del server locale in corso...
echo.

REM Controlla se Python è installato
python --version >nul 2>&1
if errorlevel 1 (
    echo ERRORE: Python non è installato!
    echo.
    echo Scarica Python da: https://www.python.org/downloads/
    echo IMPORTANTE: Durante l'installazione, spunta "Add Python to PATH"
    echo.
    pause
    exit
)

REM Avvia il server
python avvia_server.py

pause
