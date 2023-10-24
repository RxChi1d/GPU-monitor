# GPU Monitor

這個專案提供了一個使用 `nvitop` 库來監控 GPU 資源的 Python 腳本。該腳本會定期收集所有可用 CUDA 裝置的資源指標，並將它們記錄到 TensorBoard 以進行視覺化。

## 安裝

要使用此專案，您需要在系統上安裝 Python 3。您可以使用 pip 安裝所需的 Python 套件：

```shell
pip install nvitop
```

因為它會使用 SummaryWriter，您還需要安裝 tensorboardX 或 torch.utils.tensorboard：

```shell
# 如果您不想安裝 pytorch，可以使用 tensorboardX
pip install tensorboardX
```

## 使用

將存儲庫下載到您的項目目錄中：

```shell
git clone https://github.com/RxChi1d/GPU_monitor.git
```
結構如下：
```
- your_project
    - GPU_monitor
        - monitor.py
    - your_main.py
```


從 GPU_monitor 中導入 `run_nvitop_logger`，如 `sample.py`所示：

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

該腳本將開始將 GPU 資源指標記錄到 TensorBoard，並且不會干擾您的主要進程。當您的主要進程退出時，該腳本將自動停止記錄指標。

您可以運行 TensorBoard 並在網頁瀏覽器中導航到適當的 URL 以查看指標：

```Shell
tensorboard --logdir=runs
```

## 鳴謝

特別感謝 [nvitop](https://github.com/XuehaiPan/nvitop) 和 [tensorboardX](https://github.com/lanpa/tensorboardX) 库的開發人員，使這個專案成為可能。

