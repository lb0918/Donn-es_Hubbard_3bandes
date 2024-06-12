#!/bin/bash
#SBATCH --job-name=boucle
#SBATCH --time=0-24:00
#SBATCH --account=def-dsenech
#SBATCH --cpus-per-task=4
#SBATCH --mem 8g
#SBATCH --partition c-apc
#SBATCH --mail-user=lbstc@ulaval.ca
#SBATCH --mail-type=ALL
# SBATCH --array=12,13,15
ulimit -c 0
export OMP_NUM_THREADS=4
python boucle_sur_mu.py 
