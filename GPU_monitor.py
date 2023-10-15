import multiprocessing
import os
import time
from nvitop import CudaDevice, ResourceMetricCollector
from nvitop.callbacks.tensorboard import add_scalar_dict
from tensorboardX import SummaryWriter


class NvitopLogger:
    def __init__(self, root_pids=None, summary_writer=None, log_interval=1):
        self.log_interval = log_interval
        self.summary_writer = summary_writer or SummaryWriter()
        self.root_pids = root_pids or {os.getpid()}
        self.collector = ResourceMetricCollector(
            devices=CudaDevice.all(),
            root_pids=self.root_pids,
            interval=log_interval
        )
        self.global_step = 0

    def monitor(self):
        while True:
            with self.collector(tag='interval'):
                # Increment the global_step by log_interval at each interval
                self.global_step += self.log_interval
                metrics = self.collector.collect()
                self.log_to_tensorboard(metrics)
            time.sleep(self.log_interval)  # Add time interval

    def log_to_tensorboard(self, metrics):
        # Now, global_step reflects the actual time progress in seconds
        add_scalar_dict(self.summary_writer, 'resources', metrics, global_step=self.global_step)


def run_nvitop_logger(root_pids=None, summary_writer=None):
    logger = NvitopLogger(root_pids, summary_writer)
    logger.monitor()


if __name__ == "__main__":
    # Assume external_root_pids is either None or a set of pids
    external_root_pids = {os.getpid()}  # or {pid1, pid2, ...}
    nvitop_logger_process = multiprocessing.Process(target=run_nvitop_logger, args=(external_root_pids,))
    nvitop_logger_process.start()

    # ... your main process code
    time.sleep(60)

    # Ensure the nvitop_logger_process is terminated when the main process exits
    nvitop_logger_process.terminate()