# 01 Installs

Hier installieren wir Zusatzprogramme und bereiten den Computer darauf vor, dass
er in Zukunft einfacher Zusatzpakete installieren kann. Den Terminal öffnen und
mit folgenden Befehlen die Software installieren. Manchmal dauern die Installs
etwas lange. Geduld. Es funktioniert alles richtig.


## Install-Programme und Python 3

**Mac OS X** (auf Linux sollte Python 3 schon installiert sein)

- Diese Install-Programme sind auf manchen Macs bereits vorinstalliert. Auf
anderen nicht. Zur Sicherheit einfach diesen Befehl eingeben: ```xcode-select --installs```

- Mit **Homebrew** ist es einfacher, Pakete zu installieren. Der Befehl zum
Initialsetup ist etwas kompliziert. Müssen wir aber nur einmal
eingeben. ```ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"```

- Und, damit alles etwas runde läuft, diesen Befehl:
- ```echo 'export PATH=/usr/local/bin:$PATH' >> ~/.bash_profile```
- ```source ~/.bash_profile```

- Und jetzt können wir mit Befehl Python 3 installieren: ```brew install python3```

## Weitere Install-Programme, jetzt auch für Linux

- **Pip3** ist das gängigst Install-Modul, das wir verwenden werden. Es lässt
sich folgendermassen installieren: ```pip3 install -U pip``` zur Sicherheit
installieren wird noch ```pip install -U pip```.

## Virtual Environments

- Wenn Du joggen gehst, ziehst Du Dich anders an, als wenn Du schwimmen gehst.
Dasselbe gilt für Python. Um die unterschiedlichen Installationen von einander
zu trennen, installieren wir sogenannte virtual environments.
So: ```pip3 install virtualenv``` wenn es eine Fehlermeldung gegeben hat: ```sudo pip3 install virtualenv```
- Wir müssen dem Computer zudem sagen, dass er virtual environments in Python3
verwendet, und nicht Python2.
