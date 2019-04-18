ControlFocus("Open","","Edit1")
WinWait("[CLASS:#32770]","","5")
ControlSetText("Open","","Edit1","C:\Users\ml980245\PycharmProjects\learning\appendix\test.csv")
Sleep(1000)
ControlClick("Open","","Button1");
