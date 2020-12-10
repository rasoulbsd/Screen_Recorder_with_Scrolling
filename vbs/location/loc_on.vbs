
RunAsAdmin()
Set objwsh = CreateObject("WScript.Shell")

objwsh.RegWrite "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\location\Value","Allow","REG_SZ"

Function RunAsAdmin()
 Dim objAPP
  If WScript.Arguments.length = 0 Then
  Set objAPP = CreateObject("Shell.Application")
  objAPP.ShellExecute "wscript.exe", """" & _
  WScript.ScriptFullName & """" & " RunAsAdministrator",,"runas", 1
  WScript.Quit
  End If
End Function