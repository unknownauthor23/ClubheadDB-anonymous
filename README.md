# ClubheadDB: A Dataset for Down-the-Line Golf Clubhead Detection

This repository contains the **ClubheadDB** dataset, introduced in our paper:

> [Your Name(s)]. "[Your New Paper Title]." *Proceedings of the CVPR 2025 Workshop on Sensing, Art, and Understanding of the Human Form in the Wild for Fine-Grained Analysis*. 2025.

**[Link to your paper will go here once it's on arXiv or published]**

## About the Dataset

ClubheadDB is a video frame dataset designed to facilitate the training and evaluation of object detection models for a specific, challenging task: locating the golf clubhead from a down-the-line (DTL) camera view throughout the entire swing.

### Key Statistics
* **Total Frames:** ~5,000
* **Source Videos:** 50
* **Perspective:** Down-the-Line (DTL)
* **Annotations:** Manually annotated bounding boxes for a single class: `clubhead`.
* **Format:** YOLO TXT (class_id x_center y_center width height), normalized.

### Data Split
The dataset is pre-split at the video level to prevent data leakage between sets. All frames from a single video belong to only one split.
* **Training:** 70%
* **Validation:** 17%
* **Test:** 13%

## How to Use
Download the `ClubheadDB.zip` file from this repository. The file structure is compatible with the Ultralytics YOLO framework.

## Citation
If you use this dataset in your research, please cite our paper:

```bibtex
@inproceedings{hoefler2025clubheaddb,
  title={[Your New Paper Title]},
  author={[Your Name(s)]},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops},
  year={2025}
}
```
