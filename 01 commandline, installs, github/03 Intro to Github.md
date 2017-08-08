# 03 Intro to Github

Github is eines von mehreren Plattformen, auf der Open-Source-Entwickler
ihren Code tauschen und gemeinsam weiterentwickeln. Wir wollen diese
Plattform genauso nutzten.

- Zuerst müssen wir uns registrieren.

- Dann steuern wir die [Python-Recherche-Repo](https://github.com/barjacks/pythonrecherche)
an.

- Nun wählen wir rechts oben Fork. Nun hast Du Deine "gegabelte" Version der
Repo. Gratuliere! Gehen wir zurück auf die Commandline und geben Folgendes ein,
um Deine Kopie der Repo (Repository) auf Deinem Gerät zu haben:```git clone
'Link auf Deinen Fork'```

- Wenn Du nur für Dich an diesem Projekt arbeiten möchtest, wäre das Setup
nun zu Ende. Wir können Änderungen vornehmen. Und dann mit folgenden Befehlen
auf der Kommandozeile ausführen.

    + Zuerst steuern wir mit ```cd``` in die Repo
    + Dann geben wir folgendes ein ```git add .```, das ergänzt alles, was wir
    verändert haben
    + Dann schreiben wir dazu eine Mitteilung. ```git commit -m 'hello'```
    + Und dann schieben wir das auf Github. ```git push```

- Doch wir wollen Code teilen, deshalb sind noch ein paar Schritte nötig. Und
das sieht komplizierter aus, als es ist. Zuerst müssen wir dem Computer sagen,
wo die Original-Repo ist. Das tun wir mit folgender Eingabe in die
Commandline: ```git remote add upstream 'link auf Orginal-Repo'```.

- Du könntest nun einfach Änderungen vornehmen und abspeichern und mit der
Original-Repo machen. Aber das wäre nicht sehr gut, weil wir ja alle daran
arbeiten. Das führt zwangsweise zu Konflikten. Damit die nicht passieren, ist
es deshalb besser mit Branches zu arbeiten. Seitenarme, die man nach
der Arbeit wieder dem Hauptprojekt hinzufügen kann. Wir werden folgendes tun:
    + Branch kreieren: ```git checkout -b <new branch name>```
    + Files ändern: Änderungen vornehmen, wenn wir welche haben
    + Änderungen eingeben:
        - ```git add .```, um die Änderungen einzugeben
        - ```git commit -m 'hello'``` um die Änderungen einen Namen zu geben
        - ```git push origin <new branch name>```
    + Nun auf der Github-Website einen so genannten Pull-Request kreieren, und
    darauf warten, dass der Verwalter der Orginial-Repo die Änderungen absegnet
    und merged

- Sobald die Änderungen gemerged sind, kann man auf dem eigenen System für etwas
Ordnung sorgen.
    + Mit  ```git pull upstream master```sorgt man dafür, dass alles auf
    demselben Stand ist.
    + Mit diesem Befehl löschen wir den Branch, den wir nicht mehr
    brauche ```git branch -d <branch name>```
    + Dann updaten wir den Master Branch in unserer eigenen
    Repo: ```git push origin master```
    + Und dann führen wir die Löschung wirklich durch: ```git push --delete
    origin <branch name>```

- Um Dein Fork schnell immer auf den neuesten Stand zu bringen, folgende
Befehle eingeben:
    +```git pull upstream master```
    +```git push origin master```

So, jetzt hast Du eine Repo kopiert, auf Deinem System abgespeichert, einen
Branch geschaffen, Änderungen gemacht und diese dann dem Haupt-Repo übergeben.
Und schliesslich hast Du Dein eigenes System aufgeräumt. Gratuliere!
