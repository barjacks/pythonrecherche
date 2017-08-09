# 01 Command Line

## Start

Bevor wir loslegen, müssen wir die Arbeit mit der Commandline kennenlernen. Sie
ist so etwas wie unsere Hauptsteuerungszentrum. Von hier aus starten wir Programme,
auch unsere eigenen.

In dieser Erklärung braucht ihr [] nicht anzuschrieben. Also ```cd [dirname]```
bedeutet, dass ihr einfach ```cd documents```schreibt.

## Wir sind faul

* ↑ und ↓ scrollen uns zu alten Eingaben. Sehr nützlich.
* Mit ```Tab``` können Sachen autocompleted werden. Probiert es aus.
* Auf einem Mac könnte ihr auch mit Drag und Drop arbeiten, um Files und Folders
hin und her zu bewegen.

## Navigation

* ```pwd```: prints working directory — zeigt uns an, wo wir uns gerade befinden.
* ```cd [dirname]```: changes directory, bewegt uns ins jeweilige Directory.
* ``cd ..``: Bewegt uns eine Stuff rauf.
* ``ls``: zeigt alle subdirectories an. ``ls -lah`` zeigt uns alles an.
* ```locate [filename]```: versucht Files zu finden. Wenn es etwas nicht findet,
bedeutet es nicht, das es auf dem Gerät nicht ist.
* ```find```: Dauert länger als locate, findet aber alles.

* ```mv [source] [destination]``` moves a file from one place to another
* ```cp [source] [destination]``` copies a file from one place to another (so now you have two)
* ```rm [file] deletes``` (removes) a file
* ```mkdir [directoryname]``` creates a directory
* ```rmdir [directoryname]``` deletes (removes) a directory
* ```tar cvf [filename] [filename] [filename]...``` compresses (zips) files up into a .tar.gz file
* ```tar xvf [filename]``` extracts (unzips) a .tar.gz file
* ```curl [url]``` downloads a file, but streams it into your terminal window
* ```curl -O [url]``` downloads a file, saving it
* ```wget [url]``` downloads a file, saving it (yes, curl and wget are pretty similar)

## Individuelle Files

* ```cat [filename]```: displays the contents of a file
* ```wc [filename]```: displays the word count of a file
* ```wc -l [filename]```: displays the line count of a file
* ```head -n 10 [filename]```: displays the first 10 lines of a file
* ```tail -n 20 [filename]```: displays the last 20 lines of a file
* ```more [filename]```: displays the contents of a file one screen at a time (spacebar to continue)
* ```grep [text] [filename]```: show all of the lines in filename that contain text.
* ```sort```: sorts the lines of a file
* ```uniq```: removes duplicate adjacent lines of a file

* Und **wichtig**: Mit diesem wunderbaren Zeichen kann man Befehle kombinieren: ```|```

## Lustiges

* ```banner```
* ```cowsay```
* ```say```

## Abspeichern und Kombinieren

* ```grep xyz 'file' > output.txt```
* ```grep -E 'MyVariable = False|MyVariable = True' FormA.frm```

## Escaping commands

Has something gone wrong? Taking too long? Hold down Control and hit C, a.k.a. Ctrl+C.

## Mehr zu den einzelnen Befehlen lernen

* ```man``` pages are manuals that you can use from the command line.

* ```man grep``` would give you the entry for grep, and then you’d use the d and u to navigate up and down. You should probably just googlegrep man page or grep examples, though.
