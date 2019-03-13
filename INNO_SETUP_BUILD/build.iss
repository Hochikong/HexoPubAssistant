; Script generated by the Inno Script Studio Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{B44801BD-CE0D-4606-83C6-1A4DECA75336}
AppName=HexoPubAssistant
AppVersion=1.0
;AppVerName=HexoPubAssistant 1.0
AppPublisher=Hochikong
AppPublisherURL=https://github.com/Hochikong/HexoPubAssistant
AppSupportURL=https://github.com/Hochikong/HexoPubAssistant
AppUpdatesURL=https://github.com/Hochikong/HexoPubAssistant
DefaultDirName={pf}\HexoPubAssistant
DefaultGroupName=HexoPubAssistant
DisableProgramGroupPage=yes
LicenseFile=C:\Users\ckhoi\Desktop\hpa\LICENSE
InfoAfterFile=C:\Users\ckhoi\Desktop\hpa\help.rtf
OutputDir=C:\Users\ckhoi\Desktop
OutputBaseFilename=HPA_1.0_setup
SetupIconFile=C:\Users\ckhoi\Desktop\hpa\ICON\hexo logo.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "chinesesimplified"; MessagesFile: "compiler:Languages\ChineseSimplified.isl"
Name: "chinesetraditional"; MessagesFile: "compiler:Languages\ChineseTraditional.isl"
Name: "japanese"; MessagesFile: "compiler:Languages\Japanese.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 0,6.1

[Files]
Source: "C:\Users\ckhoi\Desktop\hpa\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\HexoPubAssistant"; Filename: "{app}\hpa.exe"
Name: "{group}\{cm:UninstallProgram,HexoPubAssistant}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\HexoPubAssistant"; Filename: "{app}\hpa.exe"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\HexoPubAssistant"; Filename: "{app}\hpa.exe"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\hpa.exe"; Description: "{cm:LaunchProgram,HexoPubAssistant}"; Flags: nowait postinstall skipifsilent