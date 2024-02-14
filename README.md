# Camouflaged Object Detection using the YOLOv8 Segmentation Architecture

### Experiments Performed

| Dataset | $S\alpha$ &#8593; | $\alpha E$ &#8593; | $wF$ &#8593; | $M$ &#8595; | Images |
| --- | --- | --- | --- | --- | --- |
| YOLOv8n with MoCA | 0.771 | 0.852 | 0.652 | 0.058 | 29,768 |
| YOLOv8m with MoCA | 0.812 | 0.892 | 0.710 | 0.038 | 29,768 |
| YOLOv8x with MoCA | 0.834 | 0.906 | 0.746 | 0.033 | 29,768 |
| YOLOv8n without MoCA | 0.794 | 0.879 | 0.692 | 0.048 | 11,447 |
| YOLOv8m without MoCA | 0.824 | 0.905 | 0.733 | 0.035 | 11,447 |
| YOLOv8x without MoCA | 0.837 | 0.909 | 0.755 | 0.032 | 11,447 |
| COD10K + Base &#8594; YOLOv8m| 0.832 | 0.907 | 0.744 | 0.038 | 5,326 |
| NC4K + Base &#8594; YOLOv8m| 0.762 | 0.835 | 0.624 | 0.061 | 5,326 |
| MoCA + Base &#8594; YOLOv8m| 0.664 | 0.725 | 0.480 | 0.120 | 5,326 |
| Equal + Base &#8594; YOLOv8m| 0.778 | 0.852 | 0.653 | 0.056 | 5,326 |

All of these results were obtained by testing the models on the benchmark COD10K testing dataset that contains 2026 camouflaged images.

### Test Dataset Hierarchy

```
|Evaluation Dataset

|-- CAMO
|   |-- GT
|   |-- Nano_Gts
|   |-- Medium_Gts
|   |-- Xlarge_Gts

|-- CHAMELEON
|   |-- GT
|   |-- Nano_Gts
|   |-- Medium_Gts
|   |-- Xlarge_Gts

|-- COD10k
|   |-- GT
|   |-- Nano_Gts
|   |-- Medium_Gts
|   |-- Xlarge_Gts

```

### Installations Required
Run the command below to install the necessary libraries.
```
pip install -r requirements.txt
```


