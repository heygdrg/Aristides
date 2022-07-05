
python -m pip install pystyle
python -m pip install requests
python -m pip install os
python -m pip install json
cls
echo python token_spammer.py >> start.bat
start start.bat
start /b "" cmd /c del "%~f0"&exit /b