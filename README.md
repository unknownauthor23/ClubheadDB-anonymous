<h1 align="center">ClubheadDB: A Video Dataset for Golf Clubhead Tracking</h1>

<p align="center">
  <img src="https://img.shields.io/pypi/v/clubhead-db" alt="PyPI Version">
  <img src="https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg" alt="License">
  <img src="https://img.shields.io/pypi/pyversions/clubhead-db" alt="Python Versions">
  <img src="https://img.shields.io/badge/Frames-10,000+-blue" alt="Dataset Size">
  <img src="https://img.shields.io/badge/sources-YouTube_%7C_Reddit-red" alt="Sources">
</p>

**ClubheadDB** is a web-sourced dataset for computer vision research in golf swing analysis, with a focus on clubhead detection. It contains over 10,000 “down-the-line” frames from public golf swing videos, each hand-annotated with precise clubhead locations. The dataset is fully reproducible: we provide the metadata (video URLs, timestamps) and final annotations, along with scripts to download and extract the exact set of frames used in our study.

-----

## 🌟 Dataset Highlights

| Feature                | Value                      | Description                                                              |
| :--------------------- | :------------------------- | :----------------------------------------------------------------------- |
| **Unique Golfers** | 67+                        | Video-level split: 47 Train, 10 Validation, 10 Test.                     |
| **Total Annotated Frames** | 10,180                     | A single bounding box annotation exists for each frame (zero for null examples).          |
| **Video Sources** | YouTube (46%), Reddit (54%) | Sourced from public posts to ensure a wide variety of conditions.        |
| **Skill Level Mix** | Pros (42%), Amateurs (58%) | Includes a mix of professional and amateur golfers.                      |
| **Club Type Mix** | Irons (70%), Drivers (27%) and Woods (3%) | A diverse set of clubs to ensure model generalization.                   |

-----

## 🚀 Getting the Data

The entire process is managed by the `clubhead-build` command-line tool.

### Prerequisites

Before you begin, you must have the following command-line tools installed and available in your system's `PATH`:
-   **Python** (3.8 or higher)
-   **yt-dlp**: For downloading video clips from YouTube and Reddit. ([Installation Guide](https://github.com/yt-dlp/yt-dlp#installation))
-   **ffmpeg**: For extracting frames from videos. ([Installation Guide](https://ffmpeg.org/download.html))

### Installation and Usage

#### Step 1: Install the Package

The easiest way to get the dataset is to install the package directly from PyPI:

```bash
pip install clubhead-db
```

#### Step 2: Run the Build Command

Now, you can build the entire dataset by running a single command in your terminal:
```plaintext
clubhead-build
```
This command will execute the full pipeline:

1.  It reads `metadata/metadata.csv` to find the video clips.
2.  It downloads the clips into a local `videos/` directory.
3.  It extracts frames from the videos into the `frames/swing_xxx/images/` structure.
4.  It reads `annotations.parquet` and creates the corresponding `.txt` label files in the `frames/swing_xxx/labels/` structure.

The process may take a significant amount of time depending on your internet connection and the number of videos.

### Final Data Structure

After running the pipeline, you will have a `frames/` directory organized as follows. This structure is designed to be easy to parse, view, and use for further processing.
```plaintext
frames/
└── swing_001/
    ├── images/
    │   ├── frame_0001.jpg
    │   ├── frame_0002.jpg
    │   └── ...
    └── labels/
        ├── frame_0001.txt
        ├── frame_0002.txt
        └── ...
```
Each `.txt` file contains the bounding box annotations for the corresponding image in YOLO format. Images with no clubhead present will have an empty `.txt` file.

### Citation

If you use ClubheadDB or the tools in this repository in your research, please cite our paper:

(Placeholder until paper gets accepted or rejected:)
```plaintext 
@inproceedings{unknownauthor23_2025clubheaddb,
  title={ClubheadDB: A Video Dataset for Golf Clubhead Tracking},
  author={unknownauthor23},
  booktitle={Workshop}
}
```

