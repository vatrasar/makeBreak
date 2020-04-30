# Projekt makeBreak

Program słóży do organizacji i wymuszania przerw podczas pracy przy komputerze. Działa analgoicznie jak safeYourEyes. Różnica jest taka, że udostępnia przycisk za pomocą którego potwierdzamy zakończenie przerwy. Dzięki temu program lepiej wwyznacza czas pracy użytkownika.

## Wersja exe
Plik exe powinien być tworzony za pomocą pyinstaller. W folderu z exe musi znaleźć się plik exe oraz ikona.png z folderu resources

## UStawienie jako program startowy ubuntu
Aby ustawić program jako startowy należy wejść do aplikacji programy startowe i dać tam polecenie:

/bin/bash -c "cd /sciezka/do/exe && sleep 15 && /sciezka/do/exe"
