# Temat: Słonie

> Treści zadania, Opracowanie : Jakub Radoszewski, Wojciech Rytter
> zrodlo: https://oi.edu.pl/static/attachment/20110704/oi16.pdf - str 71

##### Program, który: 

- wczytuje ze standardowego wejścia masy wszystkich słoni z zoo oraz aktualną i docelową kolejność słoni w rzędzie
- wyznacza sposób poprzestawiania słoni, który prowadzi od kolejności początkowej do docelowej i minimalizuje sumę wysiłków związanych ze wszystkimi wykonanymi zamianami pozycji słoni, 
- wypisuje sumę wartości tych wysiłków na standardowe wyjście.

- ✨
##### INPUT:
First line:
```sh
n - liczba słoni - liczba całkowita n (2 <=n <=1 000 000)
```
Second line:
```sh
mi - masa poszczególnych słoni [kg] - n liczb całkowitych mi (100 <= mi <= 6 500 dla 1 <= i <= n), separator spacja
```
Third line:
```sh
ciąg ai - numery kolejnych słoni w aktualnym ustawieniu- n różnych liczb całkowitych ai (1<= ai <= n), separator spacja
```
Fourth line:
```sh
ciąg bi - numery kolejnych słoni w docelowym ustawieniu- n różnych liczb całkowitych bi (1<= bi <= n), separator spacja
```

##### OUTPUT:
One line:
```sh
liczba całkowita, oznaczająca minimalny łączny wysiłek związany z przestawianiem słoni, w wyniku którego z ustawienia reprezentowanego przez (ai) uzyskuje się ustawienie (bi)
```




| EXAMPLE INPUT | 
| ------ | 
| 6 | 
| 2400 2000 1200 2400 1600 4000  | 
| 1 4 5 3 6 2 | 
| 5 3 2 4 6 1  | 

| OUTPUT | 
| ------ | 
| 11200 | 



| Plik | nazwa |
| ------ | ------ |
| zrodlowy | Elephans_solution.py|
| testy | Elephans_solution_test.py |
| automatyczna kontrola - wyniki z plikow out z wynikami otrzymanymi z kodu | check_output_from_code_and_from_files_out.py|

| Oprogramowanie | version |
| ------ | ------ |
| Python | 3.7.6 64 bit |
| IDE: Visual Studio Code | 1.53.2 |
| macOS Big Sure|  11.2.1 |

##### Inne: 

- Zlozonosc obliczeniowa  O(n)
-  metodyka: TDD - Test-driven development


##### Uwagi : 

- KOMENTARZE
        zastosowano celowe przesadne komentarze, opisujące metody klasy 

- OPTYMALIZACJA
        zoptymalizowano przepływ dla metody "calculate_chose_method1_or_method2" - 
        tak aby uproscic i zredukowac obliczenia dla przypadkow:
                1 - gdy slon nie zmienia podejscia
                2 - gdy przemieszczamy 2 slonie ze soba tylko raz , i zajmuja one docelowa pozycje
        
        metode Pythona .index() - zastapiono wyszukiwaniem w slowniku - aby zminimalizowac zlozonosc obliczeniowa

-  MOZLIWOSC ROZBUDOWY
        stworzenie listy "whole_cycle" wypelnionej "single_cycle" otwiera mozliwosc do refaktoryzacji kodu i
        w przypadku duzych tabel, umozliwia mapowanie na wiele komputerow i
        decelowo redukcje wynikow czastkowych (kazdej pojedynczej maszyny) do poj, docelowej wartosci 


##### Autor : 

- Monika Klimek
