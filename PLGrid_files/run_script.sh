#!/bin/bash -l

# Nazwa zlecenia
#SBATCH -J helloworld_test
# Liczba alokowanych węzłów
#SBATCH -N 1
# Liczba zadań per węzeł (domyślnie jest to liczba alokowanych rdzeni na węźle)
#SBATCH --ntasks-per-node=1
# Ilość pamięci przypadającej na jeden rdzeń obliczeniowy (domyślnie 4GB na rdzeń)
#SBATCH --mem-per-cpu=1GB
# Maksymalny czas trwania zlecenia (format DD-HH:MM:SS)
#SBATCH --time=00:01:00 
# Nazwa grantu do rozliczenia zużycia zasobów
#SBATCH -A plg-dspmwitkowski
# Specyfikacja partycji
#SBATCH -p plgrid-testing
# Plik ze standardowym wyjściem
#SBATCH --output="output-%A_%a.out"
# Plik ze standardowym wyjściem błędów
#SBATCH --error="error-%A_%a.err"

# przejscie do katalogu z ktorego wywolany zostal sbatch
cd $SLURM_SUBMIT_DIR

./test.py