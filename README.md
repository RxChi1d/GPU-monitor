# GPU Monitor

This project provides a Python script for monitoring GPU resources using the `nvitop` library. The script periodically collects resource metrics for all available CUDA devices and logs them to TensorBoard for visualization.

## Installation

To use this project, you will need to have Python 3 installed on your system. You can install the required Python packages using pip:

```
pip install nvitop tensorboardX
```

## Usage

To run the GPU monitor, you need to import the `run_nvitop_logger` from the GPU_monitor.py file.  
To avoid affecting the main program, please use `multiprocessing` to run `run_nvitop_logger`. For example:

```Python
# Assume external_root_pids is either None or a set of pids
external_root_pids = {os.getpid()}  # or {pid1, pid2, ...}
writer = SummaryWriter('runs')
interval = 1 # seconds

nvitop_logger_process = multiprocessing.Process(target=run_nvitop_logger, args=(external_root_pids, writer))
nvitop_logger_process.start()

# ... your main process code
time.sleep(60)

# Ensure the nvitop_logger_process is terminated when the main process exits
nvitop_logger_process.terminate()
```

The script will start logging GPU resource metrics to TensorBoard. You can view the metrics by running TensorBoard and navigating to the appropriate URL in your web browser:

```Shell
tensorboard --logdir=runs
```

## Acknowledgement

Special thanks to the developers of the [nvitop](https://github.com/XuehaiPan/nvitop) and [tensorboardX](https://github.com/lanpa/tensorboardX) libraries for making this project possible. 


