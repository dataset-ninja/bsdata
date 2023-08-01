Dataset **BSData** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/D/B/d1/763hy2c91clyW9LHLU9Z2ja817089MfNFbmwZP0S14raCu09rAa2Nv2OQDKtigA9cZKE6EN78Y2jeSX4aLmNGIcTk6Jsa43ihadVaDRVoZh8qOXoCSpbvS38GPPs.tar)

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

The data in original format can be [downloaded here](https://github.com/2Obe/BSData/archive/refs/heads/main.zip)