import threading
import os
import time
from nvitop import CudaDevice, ResourceMetricCollector
from nvitop.callbacks.tensorboard import add_scalar_dict
# from torch.utils.tensorboard import SummaryWriter
from tensorbaordX import SummaryWriter

class NvitopLogger:
    def __init__(self, root_pids=None, summary_writer=None, log_interval=1):
        self.log_interval = log_interval
        self.summary_writer = summary_writer or SummaryWriter
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
                self.global_step += self.log_interval
                metrics = self.collector.collect()
                self.log_to_tensorboard(metrics)
            time.sleep(self.log_interval)

    def log_to_tensorboard(self, metrics):
        add_scalar_dict(self.summary_writer, 'resources', metrics, global_step=self.global_step)


def run_nvitop_logger(root_pids=None, summary_writer=None):
    nvitop_logger = NvitopLogger(root_pids=root_pids, summary_writer=summary_writer)
    nvitop_thread = threading.Thread(target=nvitop_logger.monitor)
    nvitop_thread.daemon = True
    nvitop_thread.start()

    
if __name__ == "__main__":
    external_root_pids = {os.getpid()}
    writer = SummaryWriter('./runs')

    run_nvitop_logger(external_root_pids, writer)

    # ... your main process code
    time.sleep(60)

    # Exit the program
