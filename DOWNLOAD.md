Dataset **BSData** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/p/0/u6/jdOVZjDKPkEloFwxwC3IT3y6nWhOBpJw7yffzFWmYkABcLHjLzNtZzLVshwpGIWCyf99yWGewRIg74Tviie0BARNTx1Vn9IGeOetVh9XUfGxQCTN4SGZOyo29GWw.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='BSData', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://github.com/2Obe/BSData/archive/refs/heads/main.zip).