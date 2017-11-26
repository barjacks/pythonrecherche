# Servers


1. Öffne digital ocean
2. Kreiere ein Droplet
   Ubuntu 14.04.4 x64
   $5/mo
   Am besten einen europäischen Standort wählen
   New SSH Key
   Den SSH public key reinpasten, nenne es "do-droplet" (wie wir den Schlüssel bauen, kommt weiter unten)
   Nachdem Schritt 3 ausgeführt wurde, "Create" anklicken und warten

3. How to create an SSH key
   Geben folgendes in die Commandline ein: ```ssh-keygen -t rsa -b 4096 -C "YOUR_EMAIL@EXAMPLE.COM"```

   Das System fragt: ```Enter a file in which to save the key (/Users/YOUR_USERNAME/.ssh/id_rsa):```
   Wir geben folgendes ein: ``~/.ssh/do-droplet```
   Keinen passphrase eingeben, sondern einfach zweimal Enter drücken

   Mit cat kannst Du nun Deinen private Key anschauen. Das darfst Du nie, nie,
   nie mit jemanden teilen: ```cat ~/.ssh/do-droplet```

   Jetzt sehen wir den public Key an: ```cat ~/.ssh/do-droplet.pub```
   Diesen Schlüssel kopieren wir.

4. Jetzt verbinden wir uns mit dem Server
   Öffne die Seite Deines Droplet und notiere Dir die IP Nummer.
   Jetzt verbinden wir uns mit ssh zum Server. Wir geben folgendes ein: ```ssh root@YOUR_IP```

   Sage: "yes". Nun kommen Deine public und private Keys zum Zug.
   Drücke Ctrl+C. Und nun loggen wir uns mit unseren Keys ein

   Also: ```ssh -i ~/.ssh/do-droplet root@YOUR_IP```

5. Nun sollten wir mit dem Server verbunden sein.
   Testen wir: ```pwd```, ``ls```
   - ```curl http://www.tagesanzeiger.ch```
   - ```curl http://www.nytimes.com > tagi.text```
   - ``ls``
   - ```cat tagi.txt```
   - ```python --version```
   - ```python3 --version```
   - ```apt-get update```
   - ```apt-get upgrade```
   - ```apt-get install mailutils```
   - Wenn ein pinker Screen angezeigt wird, wähle "Internet" aus.
   - ```python3 get-pip.py```
   - ```apt-get install build-essential```
   - ```apt-get install python3-dev```
   - ```apt-get install python3-numpy```
   - ```apt-get install python3-scipy```
   - ```apt-get install libatlas-dev```
   - ```apt-get install ipython3```
   - ```apt-get install python3-pandas```
   - ```apt-get install libxml2-dev libxslt1-dev```
   - ```apt-get install python3-matplotlib```
   - ```pip3 install requests```
   - ```pip3 install bs4```

6. So, jetzt sollte der Server bereit sein. Spielen wir unseren Scraper auf Den
   Server:
   - ```ssh -i ~/.ssh/do-droplet root@DEINEIP```
   - Den Scraper auf den Server spielen, dabei mit Deiner Commandline
   im Ordner auf Deinem Computer sein: ```scp -i ~/.ssh/do-droplet DAPHNESCRAPER.py root@DEINEIP:~/```
   - Vom Server nehmen: ```scp -i ~/.ssh/do-droplet root@46.101.231.162:~/daphne.csv .```
   - Den Scraper startet: ```python3 DAPHNESCRAPER.py```
   - Das geht ziemlich lange. Und wenn unsere Verbindung zum Server abbricht,
   bekommen wir Probleme. Also, arbeiten wir mit tmux:
   - ```tmux```
   - Dann den Code starten: ```python3 DAPHNESCRAPER.py```
   - Und, den Fortschritt zu prüfen, geben wir folgendes ein: ```tmux attach```


EXTRAS:
- eval "$(ssh-agent -s)"
 ssh-add ~/.ssh/do-droplet
