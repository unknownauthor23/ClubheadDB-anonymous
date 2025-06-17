# ClubheadDB: A Dataset for Golf Clubhead Tracking

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![License](https://img.shields.io/badge/Dataset-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Paper](http://img.shields.io/badge/paper-ICCVW'25-B31B1B.svg)](https://sauafg-workshop.github.io/)

[Dataset Details](#clubheaddb-at-a-glance) •
[Annotation Format](#annotation-format) •
[Getting the Data](#getting-the-data) •
[Citation](#citation)

A public dataset of down-the-line golf swings with **bounding box annotations** for tracking the clubhead.

![Hero Image/GIF showing bounding box tracking](https://via.placeholder.com/800x400.png?text=Show+a+GIF+of+a+bounding+box+tracking+the+clubhead!)
*Example of the clubhead tracking possible by training a model on the ClubheadDB dataset.*

---

## ClubheadDB at a Glance

| Feature | Description |
| :--- | :--- |
| **Content** | 100+ video clips of golf swings from a down-the-line view. |
| **Annotations** | **Bounding Boxes (x, y, w, h)** for the golf clubhead in each frame. |
| **Goal** | To provide training data for object detection models (e.g., YOLO) to robustly track a golf clubhead. |


## Annotation Format

The bounding box annotations are provided in `data/annotations.csv`. The format is as follows:

| video_id | frame | x_min | y_min | x_max | y_max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| video_001 | 0 | 642 | 480 | 660 | 498 |
| video_001 | 1 | 645 | 482 | 663 | 500 |
| ... | ... | ... | ... | ... | ... |

***Note to you:*** *Please verify this format matches your actual annotations file and update the description if needed.*

## Getting the Data

This repository contains the video metadata and bounding box annotations.

**1. Prerequisites**
* Python 3.9+
* [FFmpeg](https://ffmpeg.org/download.html) (must be in system's PATH)
* [Git](https://git-scm.com/downloads)

**2. Installation and Download**
```bash
# Clone the repository
git clone [https://github.com/your-username/ClubheadDB.git](https://github.com/your-username/ClubheadDB.git)
cd ClubheadDB

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate # (Use `venv\Scripts\activate` on Windows)

# Install dependencies
pip install -r requirements.txt

# Run the script to download videos listed in data/metadata.csv
python src/download_and_process.py
```
* The video clips will be saved in the `videos/` directory.
* The bounding box annotations are available in `data/annotations.csv`.

## Example Use Case

The primary use case for **ClubheadDB** is to train a custom object detection model for the specific challenge of tracking a small, fast-moving golf clubhead. This is the foundational step for more advanced analysis. Once a model is trained on this data, its tracking output can be used to:

1.  Reconstruct the club's swing path.
2.  Analyze the swing plane for quality and consistency.
3.  Develop an automated coaching system that provides real-time feedback.

## Citation

If you use ClubheadDB in your research, please cite our work:

```bibtex
@inproceedings{hoefler2025clubheaddb,
  title={{ClubheadDB: A Bounding Box Dataset for Golf Clubhead Tracking}},
  author={Höfler, Sebastian and [Your Advisor's Name]},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) Workshops},
  year={2025}
}
```

---
