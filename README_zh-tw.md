# GPU Monitor

這個項目提供了一個使用 `nvitop` 庫的 Python 腳本，用於監控 GPU 資源。該腳本會定期收集所有可用 CUDA 裝置的資源指標，並將其記錄到 TensorBoard 以便可視化。

## 安裝

要使用此項目，您需要在系統上安裝 Python 3。您可以使用 pip 安裝所需的 Python 套件：

```Shell
pip install nvitop tensorboardX
```

## 使用方式

要運行 GPU 監控器，您需要從 GPU_monitor.py 文件中導入 `run_nvitop_logger`。  
為了避免影響主程序，請使用 `multiprocessing` 來運行 `run_nvitop_logger`。例如：

```Python
# 假設 external_root_pids 是 None 或一組進程 ID
external_root_pids = {os.getpid()}  # 或 {pid1, pid2, ...}
writer = SummaryWriter('runs')
interval = 1 # 秒

nvitop_logger_process = multiprocessing.Process(target=run_nvitop_logger, args=(external_root_pids, writer))
nvitop_logger_process.start()

time.sleep(60)  # ... 你的主進程代碼

# 確保在主進程退出時終止 nvitop_logger_process
nvitop_logger_process.terminate()
```

腳本將開始將 GPU 資源指標記錄到 TensorBoard。您可以通過運行 TensorBoard 並在網頁瀏覽器中導航到相應的 URL 來查看指標：

```Shell
tensorboard --logdir=runs
```

## 鳴謝

特別感謝 [nvitop](https://github.com/XuehaiPan/nvitop) 和 [tensorboardX](https://github.com/lanpa/tensorboardX) 庫的開發者，讓這個項目成為可能。
