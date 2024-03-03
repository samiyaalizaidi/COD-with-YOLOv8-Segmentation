# Camouflaged Object Detection using the YOLOv8 Segmentation Architecture

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

## Installations Required
Run the command below to install the necessary libraries.
```
pip install -r requirements.txt
```

## Authors
- Syed Muhammad Hussain
- Afsah Hyder
- Samiya Ali Zaidi
- Syed Muhammad Ali Rizvi
- Dr. Muhammad Farhan
