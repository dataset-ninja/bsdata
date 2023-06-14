**BSData** is a dataset for instance segmentation tasks. It is applicable or relevant across various domains.

The dataset consists of 1104 images with 478 labeled objects belonging to 1 single class (*pitting*).

Each image in the BSData dataset has pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 714 (65% of the total) unlabeled images (i.e. without annotations). There is 1 split in the dataset: *ds* (1104 images). The dataset was released in 2021.

Here is the visualized example grid with annotations:

<img src="https://github.com/dataset-ninja/bsdata/raw/main/visualizations/horizontal_grid.png">
