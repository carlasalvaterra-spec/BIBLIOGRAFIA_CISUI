@echo off
REM ============================================================================
REM Script Windows per conversione Bibliografia CISUI
REM Trascina il file Excel su questo batch file per convertirlo
REM ============================================================================

echo ================================================
echo   CONVERSIONE BIBLIOGRAFIA CISUI
echo   Excel --^> CSV
echo ================================================
echo.

REM Controlla se Python è installato
python --version >nul 2>&1
if errorlevel 1 (
    echo ERRORE: Python non installato!
    echo.
    echo Scarica Python da: https://www.python.org/downloads/
    echo IMPORTANTE: Durante l'installazione, spunta "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

REM Controlla se pandas è installato
python -c "import pandas" >nul 2>&1
if errorlevel 1 (
    echo Pandas non installato. Installazione in corso...
    pip install pandas openpyxl
    if errorlevel 1 (
        echo.
        echo ERRORE: Impossibile installare pandas
        echo Prova manualmente: pip install pandas openpyxl
        pause
        exit /b 1
    )
)

REM Se è stato trascinato un file
if "%~1"=="" (
    echo Nessun file specificato!
    echo.
    echo UTILIZZO:
    echo   1. Trascina il file Excel su questo file .bat
    echo   2. Oppure: converti_excel.bat tuo_file.xlsx
    echo.
    pause
    exit /b 1
)

REM Imposta nomi file
set INPUT_FILE=%~1
set OUTPUT_FILE=%~dpn1_convertito.csv

echo File input:  %INPUT_FILE%
echo File output: %OUTPUT_FILE%
echo.

REM Esegui conversione
python converti_bibliografia.py "%INPUT_FILE%" "%OUTPUT_FILE%"

if errorlevel 1 (
    echo.
    echo CONVERSIONE FALLITA!
    pause
    exit /b 1
)

echo.
echo ================================================
echo   CONVERSIONE COMPLETATA!
echo ================================================
echo.
echo File CSV creato: %OUTPUT_FILE%
echo.
echo Prossimi passi:
echo   1. Apri il CSV per verificare
echo   2. Testa con bibliografia_ricercabile_completo.html
echo   3. Carica su GitHub
echo.
pause
