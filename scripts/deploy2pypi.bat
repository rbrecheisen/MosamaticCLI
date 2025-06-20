@echo off

setlocal

poetry run pytest

set /p CONFIRM="Did the tests run without errors? (y/n) "
if /I NOT "%CONFIRM%"=="y" (
    echo Aborting deployment
    exit /b 1
)

poetry version minor

FOR /F %%v IN ('poetry version --short') DO SET VERSION=%%v
echo Deploying version %VERSION% to PyPI...
set /p CONFIRM="Is this correct? (y/n) "
if /I NOT "%CONFIRM%"=="y" (
    echo Aborting deployment
    exit /b 1
)

set /p TOKEN=<C:\Users\r.brecheisen\pypi-token.txt

poetry build
poetry publish --username __token__ --password %TOKEN%

git tag v%VERSION%
git push origin v%VERSION%

endlocal