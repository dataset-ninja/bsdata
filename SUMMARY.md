**BSData: Dataset for Instance Segmentation and Industrial Wear Forecasting** is a dataset for instance segmentation, object detection, and object detection tasks. It is used in the industrial and computer aided quality control domains, and surface defect detection research. 

The dataset consists of 1104 images with 478 labeled objects belonging to 1 single class (*pitting*).

Images in the BSData dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 714 (65% of the total) unlabeled images (i.e. without annotations). There are no pre-defined <i>train/val/test</i> splits in the dataset. The dataset was released in 2021 by the [Karlsruhe Institute of Technology, Germany](https://www.kit.edu/english/).

<img src="https://github.com/dataset-ninja/bsdata/raw/main/visualizations/poster.png">
