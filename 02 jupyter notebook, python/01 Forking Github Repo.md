# Creating a Github Repository and Forking the course Repository

Bei der Arbeit mit Github fangen wir nochmals an, und wählen einen einfacheren
Weg, um damit zu arbeiten. Den komplexeren, doch effizenteren Arbeitsflow
lernen wir später. Wenn alle Github lieben.

# Erstes eigenes Repo

1. Auf Github gehen, das Plus klick, und neue Repo eröffnen.

2. Name eingeben, Beschreibung, Public, Initialise with ReadMe. Add gitignore
Python. Licences MIT.

3. Auf der Command Line: ```git clone https://github.com/username/.git ```

4. Von nun an arbeitet ihr einfach von der Command Line auf Git. Mit folgenden Befehlen ladet ihr Sachen hoch.

5. ```git add .```

6. ```git commit -m 'deine Meldung'```

7. ```git push```


# Kurs Repo Clonen


1. Auf Fork klicken in der Repo des jeweiligen Nutzers. Also [hier](https://github.com/barjacks/pythonrecherche).

2. Dann ```git clone https://github.com/deinusername/pythonrecherche.git```

3. Jetzt prüfen wir, wo Informationen hin und her geschickt werden. ```git remote -v```

4. Dann sagen wir Git sagen, dass es eigentlich eine Haupt Repo gibt, von der diese geklont wurde. Geht dafür zurück ins Original-Repo und kopiere den Link. Und dann gebe Folgendes in das Terminal ein. ```git remote add upstream https://github.com/originalusername/repo.git```
Wenn Du den Link falsch setztes, kann Du den UpStream folgendermassen neu setzen: ```git remote rm upstream```

5. Jetzt synchron halten mit dem Original-Repo. Dafür gehst Du im Terminal in die Repo, die Du auf Deinem Gerät gecloned hast.

6. Dann wechselst Du zum Upstream. ```git fetch upstream```

7. Und checkst den Master Branch aus ```git checkout master```

8. Und dann machst Du mit ```git merge upstream/master``` das Update.

9. Nun die Kurs-Materialien in euren eigenen Repo laden. Nicht in dieser Repo arbeiten!!!
