# Kurs

1. Navigiere zum Desktop mit cd oder cd ..
2. Shift = Autocomplete
3. Pfeile rauf und runter
4. Drag and Drop auf dem Mac
5. Zeige an, was Du alles auf dem Desktop hast mit ls
6. mit ls -lah kannst Du alle Informationen der Files anzeigen
7. Kreiere einen Ordner: mkdir daten
8. speichern wir die Metadaten des Inhalts des Desktops in diesen Ordner: ls -lah > daten/desktopdaten.txt [Hier mehr zu den Permissions]/https://www.pluralsight.com/blog/it-ops/linux-file-permissions)
9. Navigiere in diesen Ordner und prüfe, was drin is mit ls
10. Lesen wir dieses File mit cat desktopdaten.txt

11. Laden wir diese Daten in unseren [Folder](https://lobbyfacts.eu/transparency_meetings)
12. Das tun wir am besten mit wget. Zuerst müssen wir etwas installieren:
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
Und dann:
brew install wget
13. Und jetzt den einfachen Befehl:
wget https://lobbyfacts.eu/transparency_meetings. Darauf achten, dass ihr im richten Folder seid.

14. Nun schauen wir dieses File an.
head -n 10
15. Speichern wir diese top 10 mal ab.
head -n 10 > topten.csv
16. Cat topten.csv ist nicht sehr hübsch. Laden wir deshalb ein neues Package herunter. csvkit. Dafür müssen wir aber zuerst Pip haben: also
sudo easy_install pip
17. Und nun pip install csvkit
18. csvlook topten.csv
19. Schauen wir uns einml die Zusammenfassung des ganzen Files an.
csvstat transparency_meetings
20. Welche Firma hat die meisten Lobbyisten? -> 'Participants' Ja, Google. Schauen wir uns die mal näher an.
21. grep Google transparency_meetings > google.csv
22. Das Problem hier, ist, dass die erste Reihe nicht mitkommt. Natürlich gibt es Wege dazu, aber die sind jetzt etwas kompliziert Machen wir es von hand
23. open google.csv, verändern wir die oberste Zelle, speichern es ab.
24. Und nun schauen wir das File nochmals an csvstat google.csv

25. Und als letztes schauen wir uns an, wo überall Schweiz zu finden ist?
grep Switzerland|switzerland transparency_meetings 
