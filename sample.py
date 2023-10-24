import os
import time
from monitor import run_nvitop_logger

# from torch.utils.tensorboard import SummaryWriter
from tensorbaordX import SummaryWriter

if __name__ == "__main__":
    external_root_pids = {os.getpid()}
    writer = SummaryWriter('./runs')

    run_nvitop_logger(external_root_pids, writer)

    # ... your main process code
    for i in range(60):
        print(f"i: {i}")
        time.sleep(1)

    # Exit the program