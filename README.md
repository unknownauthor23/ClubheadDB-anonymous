# ClubheadDB: A Dataset for Golf Swingplane Analysis

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![License](https://img.shields.io/badge/Dataset-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Paper](http://img.shields.io/badge/paper-ICCVW'25-B31B1B.svg)](https://sauafg-workshop.github.io/) This repository introduces **ClubheadDB**, a new public dataset for the fine-grained analysis of golf swings. It is designed to facilitate research in areas such as Action Quality Assessment (AQA), human motion analysis, and corrective feedback generation, aligning with the core themes of the ICCV 2025 Workshop on AI-driven Skilled Activity Understanding, Assessment & Feedback Generation (SAU&FG).

---

## ⛳ About ClubheadDB

The study of skilled human motion in sports is often hampered by the lack of specialized, publicly available datasets. **ClubheadDB** aims to address this gap by providing a focused collection of golf swing videos with detailed annotations, enabling researchers to develop and benchmark models for fine-grained analysis.

* **Content**: 100+ video clips of golf swings, sourced from public platforms like YouTube and Reddit.
* **Frame-Level Annotations**: The dataset will include frame-by-frame coordinates of the clubhead position (coming soon).
* **Expert Labels**: Each swing in the dataset is expertly classified as belonging to one of three categories based on its swing plane:
    1.  **On Plane**
    2.  **Over the Top** (a common fault)
    3.  **Underneath** (a less common fault)

The labels are provided in `data/labels.csv` and correspond to the videos downloaded via the provided script.

## 🚀 Getting the Data

### 1. Prerequisites

* Python 3.9+
* [FFmpeg](https://ffmpeg.org/download.html) (must be installed and accessible in your system's PATH)
* [Git](https://git-scm.com/downloads)

### 2. Installation and Download

Clone this repository, set up the environment, and run the download script.

```bash
git clone [https://github.com/your-username/ClubheadDB.git](https://github.com/your-username/ClubheadDB.git)
cd ClubheadDB

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate # (Use `venv\Scripts\activate` on Windows)

# Install dependencies
pip install -r requirements.txt

# Run the script to download videos from data/metadata.csv
python src/download_and_process.py
```
This will download all source videos into a `videos/` directory.

## 🎯 Example Use Case: Real-Time Swing Plane Feedback

To demonstrate the utility of **ClubheadDB**, we trained a mobile-optimized deep learning pipeline for real-time swing plane assessment and feedback. By training on this data, a system can learn to identify the swing plane and provide immediate visual guidance to an athlete.

***Note to you:*** *This is now the perfect place for your visual. It powerfully demonstrates the dataset's value.*

![Hero Image/GIF of the system in action](https://via.placeholder.com/800x400.png?text=Show+a+GIF+of+a+feedback+system+built+with+this+data!)
*An example of a real-time feedback application built using the ClubheadDB dataset.*

This application is a proof-of-concept for how **ClubheadDB** can directly facilitate the development of systems for **Skilled Activity Understanding, Assessment, and Feedback Generation.**

## 🙏 Citation

If you use the ClubheadDB dataset in your research, please cite our paper:

```bibtex
@inproceedings{hoefler2025clubheaddb,
  title={{ClubheadDB: A Fine-Grained Dataset for Golf Swing Analysis}},
  author={Höfler, Sebastian and [Your Advisor's Name]},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) Workshops},
  year={2025}
}
```

## 📜 License

The **ClubheadDB** dataset (annotations and labels) is licensed under the [Creative Commons BY-NC-SA 4.0 License](https://creativecommons.org/licenses/by-nc-sa/4.0/). The code provided in this repository is licensed under the MIT License.

---
