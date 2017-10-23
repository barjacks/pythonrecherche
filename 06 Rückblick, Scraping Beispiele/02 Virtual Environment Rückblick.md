# Wer versteht was Virtual Environments sind?

Eine Erkundung der VEs auf der Command Line.

1. Macht das Terminal auf.
2. Prüft mit ```pip freeze``` alle Pakete, die ihr mit **Pip** installiert habt.
3. Prüft mit ```brew freeze```, die ihr mit Homebrew installiert habt. Linux-Nutzer prüfen ```apt list --installed```, was sie installiert haben.
4. Weitere nützliche Befehle:
  - ```lsvirtualenv``` listet alle virtual envs auf
  - Mit ```workon NameVE```in das jeweilige VirtualEnv springen.
  - ```cdvirtualenv```springt man in das Verzeichnis ders VEs. Hier sieht man, was hier alles installiert.
  - ```cdsitepackages```springt man direkt in den Ordner der Packages.
  - ```lssitepackages```springt man direkt zu den packages
5. Nun verschaffen wir uns mit einem simplen Befehl eine Übersicht über alle Packages die einem VE geladen sind. Dafür mit ```cd ~``` (Das Tilde Zeichen ist "Alt" und die "N"-Taste) ins Homeverzeichnis zurück. Dann zum Beispiel auf den Desktop. ```pip freeze > requirements.txt```. Auf dem Desktop sollte nun ein Text-File erscheinen, in dem die Requirements gelistet sind.
6. Um Virtualenvs zu deaktivieren, tippt einfach ```deactivate``` in das Terminal.
7. Um Virtualenvs zu löschen, tippt ```rmvirtualenv```. Funktioniert nur, wenn das jeweilige Virtualenv deaktiviert ist.
