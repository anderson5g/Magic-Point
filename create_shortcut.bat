@echo off
echo Criando atalho na área de trabalho...
set SCRIPT_DIR=%~dp0
set DESKTOP_FOLDER=%USERPROFILE%\Desktop
set SHORTCUT_NAME=PontoMagico.lnk

echo [InternetShortcut] > "%SHORTCUT_NAME%"
echo URL=file:///%SCRIPT_DIR%install.bat >> "%SHORTCUT_NAME%"
echo IconIndex=0 >> "%SHORTCUT_NAME%"
echo IconFile=%SCRIPT_DIR%icone.ico >> "%SHORTCUT_NAME%"

move /y "%SHORTCUT_NAME%" "%DESKTOP_FOLDER%\%SHORTCUT_NAME%"
echo Atalho criado na área de trabalho.
pause
start https://www.python.org/downloads/
exit
