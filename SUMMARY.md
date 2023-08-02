**BSData: Dataset for Instance Segmentation and Industrial Wear Forecasting** is a dataset for instance segmentation, object detection, and object detection tasks. It is used in the surface defect detection domain. 

The dataset consists of 394 images with 485 labeled objects belonging to 1 single class (*pitting*).

Images in the BSData dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. All images are labeled (i.e. with annotations). There are 2 splits in the dataset: *test* (70 images) and *train* (324 images). Alternatively, the dataset could be split into 2 occurring BSD types: <span style="background-color: #ecdefc; padding: 2px 4px; border-radius: 4px;">type_1</span> (69 images) and <span style="background-color: #ecdefc; padding: 2px 4px; border-radius: 4px;">type_2</span> (325 images); or into the 27 wear developments. The dataset was released in 2021 by the Karlsruhe Institute of Technology, Germany.

<img src="https://github.com/dataset-ninja/bsdata/raw/main/visualizations/poster.png">
