#!/bin/bash
#SBATCH --job-name=boucle
#SBATCH --time=0-24:00
#SBATCH --account=def-dsenech
#SBATCH --cpus-per-task=4
#SBATCH --mem 2g
#SBATCH --partition c-iq
#SBATCH --mail-user=lbstc@ulaval.ca
#SBATCH --mail-type=ALL
ulimit -c 0
export OMP_NUM_THREADS=4
python densité_états.py 