@echo off
cd /d "%~dp0"
set "JUPYTER_DATA_DIR=%CD%\.venv\share\jupyter"
set "JUPYTER_RUNTIME_DIR=%CD%\.venv\jupyter-runtime"
set "IPYTHONDIR=%CD%\.venv\ipython"
if not exist ".venv\Scripts\python.exe" (
    echo The course environment is missing. Follow the one-time setup in README.md.
    pause
    exit /b 1
)
".venv\Scripts\python.exe" -m notebook
