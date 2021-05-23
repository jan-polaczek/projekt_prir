# Równoległe symulowane wyżarzanie rozwiązujące TSP

## Główny program
Uruchamiamy przy pomocy `mpiexec -n <liczba procesów> python main.py`
### Opcjonalne argumenty:
 - nazwa pliku wejściowego, domyślnie 'data.dat'
 - liczba różnych miast w problemie (konieczne do zainicjowania tablic np), domyślnie 5
 
 ## Generator grafów
 Plik `graph_generator.py` służy oczywiście do wygenerowania losowego grafu. Uruchamiamy go po prostu `python graph_generator.py`.
 ### Opcjonalne argumenty:
 - liczba miast, domyślnie 5
 - minimalny dystans między miastami, domyślnie 1
 - maksymalny dystans między miastami, domyślnie 15
 - nazwa pliku wyjściowego, domyślnie 'data.dat'  
 <a/>
 Skrypt generuje ścieżkę pomiędzy każdą parą miast - jest to proste rozwiązanie, które zapewnia, że będzie się dało utworzyć cykl Hamiltona.
