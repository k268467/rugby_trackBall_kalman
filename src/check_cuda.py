import torch 
import sys

def check_cuda():
    if not torch.cuda.is_available():
        print("WARNING: CUDA is not available.")
        sys.exit(1)
    else:
        print("CUDA is available.")