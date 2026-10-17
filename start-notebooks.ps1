# Open the course with its own Python environment, from any current folder.
$ErrorActionPreference = 'Stop'
$coursePython = Join-Path $PSScriptRoot '.venv/Scripts/python.exe'
if (-not (Test-Path -LiteralPath $coursePython)) {
    throw 'The course environment is missing. Follow the one-time setup in README.md.'
}
Set-Location -LiteralPath $PSScriptRoot
$env:JUPYTER_DATA_DIR = Join-Path $PSScriptRoot '.venv/share/jupyter'
$env:JUPYTER_RUNTIME_DIR = Join-Path $PSScriptRoot '.venv/jupyter-runtime'
$env:IPYTHONDIR = Join-Path $PSScriptRoot '.venv/ipython'
& $coursePython -m notebook --ServerApp.root_dir=$PSScriptRoot
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
