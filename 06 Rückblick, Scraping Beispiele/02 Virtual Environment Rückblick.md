# Wer versteht was Virtual Environments sind?

Eine Erkundung der VEs auf der Command Line.

1. Macht das Terminal auf.
2. Prüft mit ```pip freeze``` alle Pakete, die ihr mit **Pip** installiert habt.
3. Prüft mit ```brew freeze```, die ihr mit Homebrew installiert habt. Linux-Nutzer prüfen ```apt list --installed```, was sie installiert haben.
4. Weitere nützliche Befehle:
  - ```lsvirtualenv``` listet alle virtual envs auf
  - ```cdvirtualenv name_VE```springt man in das Verzeichnis ders VEs. Hier sieht man, was hier alles installiert.
  - ```cdsitepackages name_VE```springt man direkt in den Ordner der Packages.
  - ```lssitepackages name_VE```springt man direkt zu den packages
5. Nun verschaffen wir uns mit einem simplen Befehl eine Übersicht über alle Packages die einem VE geladen sind. ```pip freeze > requirements.txt```. Auf der Ebene, auf den ihr euch eben befindet sollte nun ein Text-File erscheinen, in dem die Requirements gelistet sind.
