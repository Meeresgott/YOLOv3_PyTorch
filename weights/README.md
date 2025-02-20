### 0. Overview
 All of this weights are working for this project with pytorch's format.   
 
 You can use the `download_weight.py` script to download one of the following weights from google drive. 
 If you want to use Baidu Drive you have to download them yourself. 

### 1. YOLO v3 weights base on darknet_53 backbone (mAP=59.66%)   
 * Name: yolov3_weights_pytorch.pth
 * Download: [Google Drive](https://drive.google.com/open?id=1Bm_CLv9hP3mMQ5cyerKRjvt7_t1duvjI) or [Baidu Drive](https://pan.baidu.com/s/1gx-XRUE1NTfIMKkQ1L0awQ)   
 * `python3 download_weight.py -n 1`

### 2. Backbone <darknet53> weights   
 * This is a pretrain model. Use for train yourself data set.   
 * Name: darknet53_weights_pytorch.pth
 * Download: [Google Drive](https://drive.google.com/open?id=1VYwHUznM3jLD7ftmOSCHnpkVpBJcFIOA) or [Baidu Drive](https://pan.baidu.com/s/1axXjz6ct9Rn9GtDTust6DA)   
 * `python3 download_weight.py -n 2`

### 3. Official weigths.    
 * Name: official_yolov3_weights_pytorch.pth
 * Download: [Google Drive](https://drive.google.com/file/d/1SnFAlSvsx37J7MDNs3WWLgeKY0iknikP/view?usp=sharing) or [Baidu Drive](https://pan.baidu.com/s/1YCcRLPWPNhsQfn5f8bs_0g)   
 * `python3 download_weight.py -n 3`
