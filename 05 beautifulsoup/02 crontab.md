# Führen wir die Files automatisch aus

1. Zuerst geben wir in der Command Line ein: ```export EDITOR=nano````

2. Nun starten den Crontab: ```crontab -e```

4. Das virtual environment aktivieren ```workon virtuelenv```. Mit ```lsvirtualenv -l```.
können wir alle aufrufen.

5. Nun den code starten ```python code.py```

6. Und mit den Sternen können dem Computer sagen, wann er die Befehle ausführen soll.
Das ist [eine gute Site dafür](https://crontab.guru/every-20-minutes).

7. In einem nächsten Schritt installieren wir genau so etwas auf einem Server.




Extras: Falls es nicht auf Anhieb funktioniert.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
