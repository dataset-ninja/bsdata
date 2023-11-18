**BSData: Industrial Machine Tool Element Surface Defect Dataset** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the surface defect detection domain. 

The dataset consists of 394 images with 485 labeled objects belonging to 1 single class (*pitting*).

Images in the BSData dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. All images are labeled (i.e. with annotations). There are 2 splits in the dataset: *train* (324 images) and *test* (70 images). Alternatively, the dataset could be split into 2 occurring BSD types: ***type_2*** (325 images) and ***type_1*** (69 images). Also, it could be categorized by the 27 wear developments (***wear_dev***). The dataset was released in 2021 by the Karlsruhe Institute of Technology, Germany.

<img src="https://github.com/dataset-ninja/bsdata/raw/main/visualizations/poster.png">
