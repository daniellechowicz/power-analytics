;NSIS Installer
;Compile the script with nullsoft scriptable install system 3.05

;--------------------------------
;Include Modern UI

	!include "MUI2.nsh"

;--------------------------------
;General

	;Name and file
	Name "Power Analytics"
	OutFile "Power Analytics.exe"
	Unicode True

	;Default installation folder
	InstallDir "$LOCALAPPDATA\Power Analytics"

	;Get installation folder from registry if available
	InstallDirRegKey HKCU "Software\Power Analytics" ""

	;Request application privileges for Windows Vista
	RequestExecutionLevel user

;--------------------------------
;Interface Settings

	!define MUI_ABORTWARNING
	!define MUI_HEADERIMAGE
	!define MUI_HEADERIMAGE_BITMAP "installer\bar.bmp"

;--------------------------------
;Pages

	!insertmacro MUI_PAGE_WELCOME
	!insertmacro MUI_PAGE_COMPONENTS
	!insertmacro MUI_PAGE_DIRECTORY
	!insertmacro MUI_PAGE_INSTFILES
	!insertmacro MUI_PAGE_FINISH

	!insertmacro MUI_UNPAGE_WELCOME
	!insertmacro MUI_UNPAGE_CONFIRM
	!insertmacro MUI_UNPAGE_INSTFILES
	!insertmacro MUI_UNPAGE_FINISH

;--------------------------------
;Languages

	!insertmacro MUI_LANGUAGE "English"

;--------------------------------
;Installer Sections

;Embedding Python installer
Section "Python 3.9.0" SEC01
	
	SetOutPath "$INSTDIR"

	File "installer\python-3.9.0-amd64.exe"
	ExecWait "$INSTDIR\python-3.9.0-amd64.exe"
	
SectionEnd

;Embedding the application
Section "Power Analytics 1.0" SEC02

	SetOutPath "$INSTDIR"
	
	;Files/folders to be added go here...
	File /r "bin"
	File /r "power-analytics"
	File /r "requirements.txt"
	File /r "README.md"

	;Store installation folder
	WriteRegStr HKCU "Software\Power Analytics" "" $INSTDIR

	;Create uninstaller
	WriteUninstaller "$INSTDIR\Uninstall.exe"

	;When done, execute setup commands
	File "setup.bat"
	ExecWait "$INSTDIR\setup.bat"
	
SectionEnd

;--------------------------------
;Descriptions

	;Language strings
	LangString DESC_SEC01 ${LANG_ENGLISH} "Python interpreter - version 3.9.0."
	LangString DESC_SEC02 ${LANG_ENGLISH} "Software to analyze the power consumption of woodworking machines using different tools."

	;Assign language strings to sections
	!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
	!insertmacro MUI_DESCRIPTION_TEXT ${SEC01} $(DESC_SEC01)
	!insertmacro MUI_DESCRIPTION_TEXT ${SEC02} $(DESC_SEC02)
	!insertmacro MUI_FUNCTION_DESCRIPTION_END

;--------------------------------
;Uninstaller Section

Section "Uninstall"

	Delete "$INSTDIR\Uninstall.exe"
	RMDir /r "$INSTDIR"
	DeleteRegKey /ifempty HKCU "Software\Power Analytics"

SectionEnd