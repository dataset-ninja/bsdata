Please visit dataset [homepage](https://github.com/2Obe/BSData) to download the data. 

Afterward, you have the option to download it in the universal supervisely format by utilizing the dataset-tools package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='BSData', dst_dir='~/dtools/datasets/BSData')
```
