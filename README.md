# GPU Monitor

This project provides a Python script for monitoring GPU resources using the `nvitop` library. The script periodically collects resource metrics for all available CUDA devices and logs them to TensorBoard for visualization.

## Installation

To use this project, you will need to have Python 3 installed on your system. You can install the required Python packages using pip:

```shell
pip install nvitop
```
Because it will use the SummaryWriter, you also need to install tensorboardX or torch.utils.tensorboard
```shell
# if you don't want to install pytorch, you can use tensorboardX
pip install tensorboardX
```


## Usage

Download the respository to your project directory:
```shell
git clone https://github.com/RxChi1d/GPU_monitor.git
```
The structure is as follows:
```
- your_project
    - GPU_monitor
        - monitor.py
    - your_main.py
```
Import the `run_nvitop_logger` from GPU_monitor such as `sample.py`:
```python
from GPU_monitor import run_nvitop_logger

if __name__ == "__main__":
    external_root_pids = {os.getpid()}
    writer = SummaryWriter('./runs')

    run_nvitop_logger(external_root_pids, writer)

    # ... your main process code
    for i in range(60):
        print(f"i: {i}")
        time.sleep(1)

    # Exit the program
```

The script will start logging GPU resource metrics to TensorBoard, and it won't interfere with your main process. When your main process exits, the script will automatically stop logging metrics.   
  
You can view the metrics by running TensorBoard and navigating to the appropriate URL in your web browser:

```Shell
tensorboard --logdir=runs
```

## Acknowledgement

Special thanks to the developers of the [nvitop](https://github.com/XuehaiPan/nvitop) and [tensorboardX](https://github.com/lanpa/tensorboardX) libraries for making this project possible. 


