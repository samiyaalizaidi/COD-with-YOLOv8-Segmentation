# Enhanced Camouflaged Object Detection for Agricultural Pest Management

This repository contains the code, data, and resources for the paper:

**"Enhanced Camouflaged Object Detection for Agricultural Pest Management: Insights from Unified Benchmark Dataset Analysis"**

Published in: *2024 21st International Bhurban Conference on Applied Sciences and Technology (IBCAST)*


<p align="center">
 <img src="results/benchmark_Datasets.png" alt="Visual Results">
</p>

## Abstract

In recent decades, the severity of climate change has led to a rise in the frequency of agricultural pest attacks on farms causing significant economic damage and food shortages. Effective management of pests, specifically Camouflaged pests, poses significant challenges in agriculture, requiring accurate automated detection and segmentation.  In this study, we leverage state-of-the-art object detection and segmentation models, specifically the single-stage YOLOv8 model, fine-tuned on a large-scale Unified Benchmark Camouflaged Object Detection Dataset (UBCODD) consisting of 52,447 images. Furthermore, we extend our analysis to benchmark agricultural pest datasets such as IP-102 and the Locust-Mini Dataset, showcasing competitive performance metrics. This integrated approach allows us to capture agricultural camouflaged pests with greater detail and accuracy. Our findings lay the groundwork for the advancement of single-stage object detectors and segmentation models in the field of agriculture. Moreover, we contribute to open-source initiatives in agricultural technology by generating bounding box annotations for the entire IP-102 and binary masks for the Agricultural Pests Image Dataset. This research signifies a significant advancement in agricultural pest recognition and segmentation using cutting-edge computer vision technologies.

## Requirements
Run the command below to install the necessary libraries.
```
pip install -r requirements.txt
```

## Experiments Performed

These metrics were computed using the [COD-ToolBox](https://github.com/DengPingFan/CODToolbox) provided by Deng-Ping Fan et al. The tests were performed on the benchmark ``COD10K`` testing dataset that contains ``2026`` camouflaged images. 

#### Entire Dataset Including MoCA

| Model | $S\alpha$ &#8593; | $\alpha E$ &#8593; | $wF$ &#8593; | $M$ &#8595; | Images |
| --- | --- | --- | --- | --- | --- |
| YOLOv8n | 0.771 | 0.852 | 0.652 | 0.058 | 29,768 |
| YOLOv8m | 0.812 | 0.892 | 0.710 | 0.038 | 29,768 |
| YOLOv8x | 0.834 | 0.906 | 0.746 | 0.033 | 29,768 |

#### Entire Dataset Excluding MoCA

| Model | $S\alpha$ &#8593; | $\alpha E$ &#8593; | $wF$ &#8593; | $M$ &#8595; | Images |
| --- | --- | --- | --- | --- | --- |
| YOLOv8n | 0.794 | 0.879 | 0.692 | 0.048 | 11,447 |
| YOLOv8m | 0.824 | 0.905 | 0.733 | 0.035 | 11,447 |
| YOLOv8x | 0.837 | 0.909 | 0.755 | 0.032 | 11,447 |

#### Equal Datasets
All experiments in the category were performed using ``YOLOv8m``.

- Base dataset has a total of ``1326`` images, out of which ``1250`` images are from ``CAMO`` and ``76`` images are from ``CHAMELEON``.
- Equal dataset has ``1333`` images each from ``COD10K``, ``MoCA``, and ``NC4K``.

| Dataset | $S\alpha$ &#8593; | $\alpha E$ &#8593; | $wF$ &#8593; | $M$ &#8595; | Images |
| --- | --- | --- | --- | --- | --- |
| COD10K + Base | 0.832 | 0.907 | 0.744 | 0.038 | 5,326 |
| NC4K + Base | 0.762 | 0.835 | 0.624 | 0.061 | 5,326 |
| MoCA + Base | 0.664 | 0.725 | 0.480 | 0.120 | 5,326 |
| Equal + Base| 0.778 | 0.852 | 0.653 | 0.056 | 5,326 |

#### Entire Dataset with Filtered MoCA

| Model | $S\alpha$ &#8593; | $\alpha E$ &#8593; | $wF$ &#8593; | $M$ &#8595; | Images |
| --- | --- | --- | --- | --- | --- |
| YOLOv8x | 0.845 | 0.919 | 0.766 | 0.031 | 14,223 |


### Test Dataset Hierarchy

```
../Evaluation Dataset/   
├── CAMO/           
│   ├── GT/
│   │   ├── image01.png
│   │   ├── image02.png
│   │   └── ...
│   ├── Nano_Gts/        
│   │   ├── image01.png
│   │   ├── image02.png
│   │   └── ...
│   ├── Medium_Gts/        
│   │   ├── image01.png
│   │   ├── image02.png
│   │   └── ...
│   ├── Xlarge_Gts/        
│   │   ├── image01.png
│   │   ├── image02.png
│   │   └── ...
├── COD10K/ 
│   ├── GT/
│   │   ├── image01.png
│   │   ├── image02.png
│   │   └── ...
│   ├── Nano_Gts/        
│   │   ├── image01.png
│   │   ├── image02.png
│   │   └── ...
│   ├── Medium_Gts/        
│   │   ├── image01.png
│   │   ├── image02.png
│   │   └── ...
│   ├── Xlarge_Gts/        
│   │   ├── image01.png
│   │   ├── image02.png
│   │   └── ...
├── CHAMELEON/ 
│   ├── GT/
│   │   ├── image01.png
│   │   ├── image02.png
│   │   └── ...
│   ├── Nano_Gts/        
│   │   ├── image01.png
│   │   ├── image02.png
│   │   └── ...
│   ├── Medium_Gts/        
│   │   ├── image01.png
│   │   ├── image02.png
│   │   └── ...
│   ├── Xlarge_Gts/        
│   │   ├── image01.png
│   │   ├── image02.png
│   │   └── ...
└── ...
```


## Citations
If you use this work, please cite:

```bibtex
@inproceedings{UBCODD,
        title = {Enhanced Camouflaged Object Detection for Agricultural Pest Management: Insights from Unified Benchmark Dataset Analysis},
        author = {Hussain, Syed Muhammad and Zaidi, Samiya Ali and Hyder, Afsah and Rizvi, Syed Muhammad Ali and Farhan, Muhammad},
        booktitle = {2024 21st International Bhurban Conference on Applied Sciences and Technology (IBCAST)},
        year = {2024},
        keywords = {Camouflaged Object Detection, YOLOv8, Agricultural Pests, UBCODD, IP-102, Locust-Mini}
      }
```

## Authors
- Syed Muhammad Hussain
- Afsah Hyder
- Samiya Ali Zaidi
- Syed Muhammad Ali Rizvi
- Dr. Muhammad Farhan
