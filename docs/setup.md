# Setup Instructions and Requirements for Oasis

Ideally you will have a powerful gpu with a considerable amount of VRAM.
The more VRAM you have the larger the model you can use, I have written and tested this on an RTX 4090 with 24gb of VRAM
and 64gb of system memory.

## Prerequisites

- Python 3.10 is recommended, but 3.7+ should work.
- Visual Studio 2022 may be required for building the wheel, download it
  from [here](https://visualstudio.microsoft.com/vs/). Make sure to select the python workload to download via the gui
  to prevent any issues,
- Visual C++ 14 or later is required. You can get it
  from [here](https://visualstudio.microsoft.com/visual-cpp-build-tools/).
  - Otherwise you can install just the C++ build tools with the command below (_ensure your terminal is in the same
    directory as the executable!_)
  ```shell 
    vs_buildtools.exe --norestart --passive --downloadThenInstall --includeRecommended --add Microsoft.VisualStudio.Workload.NativeDesktop --add Microsoft.VisualStudio.Workload.VCTools --add Microsoft.VisualStudio.Workload.MSBuildTools
    ```

## Requirements

Once the pre-requisites have been fulfilled you can install the requirements.

- Install the correct version of torch for your gpu, see [here](https://pytorch.org/get-started/locally/) for more
  information.
- I used the command below to install with pip
  ```shell
  pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
  ```
- Then install all other requirements with pip
  ```shell
  pip3 install -r requirements.txt
  ```
  - You might want to double check any cuda specific dependencies match the version you installed before.
