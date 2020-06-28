@echo off

set lang=%1
set folder_name=%2
cd /d %~dp0

If "%1" == "" (
    echo "param: language is missing"
) else if "%2" == "" (
    echo "param: folder name is missing"
) else ( 
    if "%3" == "l" (
        python local.py %lang% %folder_name%
    ) else (
        python remote.py %lang% %folder_name%
    )
)
