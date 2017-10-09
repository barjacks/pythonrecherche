# 02 Installs

Hier installieren wir Zusatzprogramme und bereiten den Computer darauf vor, dass
er in Zukunft einfacher Zusatzpakete installieren kann. Den Terminal öffnen und
mit folgenden Befehlen die Software installieren. Manchmal dauern die Installs
etwas lange. Geduld. Es funktioniert alles richtig. Und all das müssen wir
nur einmal machen. Nicht mehr, aber auch nicht weniger.


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
installieren wird noch ```pip install -U pip```. Wenn das nicht funktioniert hat
versuche es mit ```sudo pip install -U pip```.

## Virtual Environments

- Wenn Du joggen gehst, ziehst Du Dich anders an, als wenn Du schwimmen gehst.
Dasselbe gilt für Python. Um die unterschiedlichen Installationen von einander
zu trennen, installieren wir sogenannte virtual environments.
So: ```pip3 install virtualenv``` wenn es eine Fehlermeldung gegeben hat: ```sudo pip3 install virtualenv```
- Wir müssen dem Computer zudem sagen, dass er virtual environments in Python3
verwendet, und nicht Python2. Das machen wir diesem extrem kompliziert anzusehenden
Befehl ```echo 'export VIRTUALENV_PYTHON=`which python3`' >> ~/.bash_profile```
und ```source ~/.bash_profile```.
- Jetzt noch ein paar Zusätze: ```pip3 install virtualenvwrapper```, und dann
wieder eine ganze Reihe komplizierter Befehle:
- ```echo 'export VIRTUALENVWRAPPER_PYTHON=$VIRTUALENV_PYTHON' >> ~/.bash_profile```
- ```echo 'export WORKON_HOME=$HOME/.virtualenvs' >> ~/.bash_profile```
- ```export VIRTUALENVWRAPPER_SH_PATH=`which virtualenvwrapper.sh` ```
- ```echo "source $VIRTUALENVWRAPPER_SH_PATH" >> ~/.bash_profile```
- ```source ~/.bash_profile```

- So, und jetzt können wir virtuelle Umgebungen, virtual environments, kreieren.
Versuche wir es mit diesem Befehl ```mkvirtualenv erstesVE```
- Und dann ```workon erstesVE```. Nun sollte in der Kommandozeile eine Anzeige
auftauchen, dass Du Dich in einem virtual environment aufhälts, mit dem Namen
VE. Von jetzt an brauchst Du auch nicht mehr ```pip3```zu schreiben, da ```pip```
weiss, was er zu tun hat.

## Erste Zusatzpakete

- Installieren wir also BeautifulSoup, eine Python-Library, die wir später
brauchen werden, um Websites zu lesen. Also: ```pip install beautifulsoup4```.
- In diesem Library
- Und dann installieren wir noch Jupyter Notebook: ```pip install jupyter notebook```.

## Letzter Install (vorerst)

- Jetzt, ganz am Ende, installieren wir noch eine letzte Software: Den Texteditor
[Atom](https://atom.io/). Das tun wir ganz normal. So, wie ihr es gewohnt seid,
Software zu installieren.
