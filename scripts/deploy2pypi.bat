@echo off

setlocal

set /p TOKEN=<C:\Users\r.brecheisen\pypi-token.txt

poetry build
poetry publish --username __token__ --password %TOKEN%

endlocal