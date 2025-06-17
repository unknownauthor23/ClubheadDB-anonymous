# ClubheadDB

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![License](https://img.shields.io/badge/Dataset-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Paper](http://img.shields.io/badge/paper-ICCVW'25-B31B1B.svg)](https://sauafg-workshop.github.io/)

[Dataset Details](#clubheaddb-at-a-glance) •
[Getting the Data](#getting-the-data) •
[Example Use Case](#example-use-case) •
[Citation](#citation)

A public dataset for the fine-grained analysis of golf swings, featuring expert-labeled swing plane classifications.

![Hero Image/GIF of the system in action](https://via.placeholder.com/800x400.png?text=Show+a+GIF+of+swing+plane+analysis!)
*An example of swing plane classification and feedback that can be developed using ClubheadDB.*

---

## ClubheadDB at a Glance

| Feature | Description |
| :--- | :--- |
| **Content** | 100+ video clips of golf swings from a frontal view. |
| **Sources** | Public videos from YouTube and Reddit. |
| **Expert Labels** | Each swing is classified by an expert as `On Plane`, `Over the Top`, or `Underneath`. |
| **Annotations** | Frame-level clubhead coordinates (work in progress). |
| **Goal** | Facilitate research in Action Quality Assessment (AQA) and human feedback systems. |

### Swing Plane Labels

The core contribution of **ClubheadDB** is the expert classification of each swing's plane, a key aspect of golf performance.

* ✅ **On Plane:** The desired, efficient swing path.
* ❌ **Over the Top:** A common fault where the club approaches the ball from outside the target line.
* ❌ **Underneath:** A less common fault where the club approaches from too far inside the target line.

## Getting the Data

This repository provides scripts to download the videos and corresponding labels.

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
* The expert labels are available in `data/labels.csv`.

## Example Use Case

**ClubheadDB** can be used to train models for applications like real-time coaching systems, performance analysis tools, or content recommendation engines for sports e-learning platforms. The included labels are ideal for training a classifier for Action Quality Assessment.

## Citation

If you use ClubheadDB in your research, please cite our work:

```bibtex
@inproceedings{hoefler2025clubheaddb,
  title={{ClubheadDB: A Fine-Grained Dataset for Golf Swing Analysis}},
  author={Höfler, Sebastian and [Your Advisor's Name]},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) Workshops},
  year={2025}
}
```

---
