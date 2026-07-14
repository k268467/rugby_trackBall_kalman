#!/bin/bash
#SBATCH --job-name demo-kalman
#SBATCH --output logs/%x-%j.log
#SBATCH --error logs/%x-%j.err
#SBATCH --nodes 1
#SBATCH --cpus-per-task 8
#SBATCH --gpus tesla:1

SIF_PATH='./singularity/env.sif'
date
singularity exec --nv $SIF_PATH python3 check_cuda.py
singularity exec --nv $SIF_PATH python3 demo_kalman.py
date