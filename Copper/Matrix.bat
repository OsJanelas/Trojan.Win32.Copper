@echo off
title Oxidation
color 0a
cls

:matrix
set /a "num=%random% %% 10"
<nul set /p "=%num% "
set /a "counter+=1"

:: Cria uma quebra de linha aleatória para o efeito de cascata
if %random% LSS 2000 echo.

goto matrix