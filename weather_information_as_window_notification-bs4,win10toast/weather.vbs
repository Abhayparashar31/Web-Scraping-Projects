Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c C:\Users\abhay\Desktop\articles\projects\weather.bat"
oShell.Run strArgs, 0, false