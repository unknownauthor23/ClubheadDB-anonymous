<p align="center">
  <img src="https://storage.googleapis.com/gemini-prod/images/5f58359b-137a-4255-b072-46654e9e0325" alt="ClubheadDB Banner" width="80%"/>
</p>

# ClubheadDB: A Video Dataset for Golf Clubhead Tracking

<div align="center">

<!-- These badges will work once you publish to PyPI -->
![PyPI Version](https://img.shields.io/pypi/v/clubheaddb)
![License](https://img.shields.io/pypi/l/clubheaddb)
![Python Versions](https://img.shields.io/pypi/pyversions/clubheaddb)
![Dataset Size](https://img.shields.io/badge/videos-67+-blue)
![Sources](https://img.shields.io/badge/sources-YouTube_|_Reddit-red)

</div>

**ClubheadDB** is an open-source dataset and Python package for computer vision in golf analytics. It provides the metadata and tools to build a curated dataset of over 10,000 annotated frames from diverse, public-domain golf swing videos.

The core philosophy is to provide the **metadata** and **final annotations**, allowing users to download the source video clips directly and reproduce the exact dataset used for our research.

-----

## 🌟 Dataset Highlights

| Feature                | Value                      | Description                                                              |
| :--------------------- | :------------------------- | :----------------------------------------------------------------------- |
| **Total Videos** | 67+                        | Video-level split: 47 Train, 10 Validation, 10 Test.                     |
| **Total Annotated Frames** | 10,847                     | A single bounding box annotation exists for each curated frame.          |
| **Video Sources** | YouTube (51%), Reddit (49%) | Sourced from public posts to ensure a wide variety of conditions.        |
| **Skill Level Mix** | Pros (42%), Amateurs (58%) | Includes a mix of professional and amateur golfers.                      |
| **Club Type Mix** | Irons (67%), Drivers (28%)+ | A diverse set of clubs to ensure model generalization.                   |

-----

## 🚀 Getting the Data

The entire process is managed by the `clubheaddb` command-line tool.

### 1. Prerequisites
- Python 3.8+
- [FFmpeg](https://ffmpeg.org/download.html) (must be installed and available in your system's PATH)

### 2. Installation
Once published, you will be able to install `ClubheadDB` directly from PyPI using pip:
```bash
# For now, you can install it directly from your GitHub repository
pip install git+[https://github.com/sebastianhoefler/ClubheadDB.git](https://github.com/sebastianhoefler/ClubheadDB.git)

# Once published on PyPI, it will be:
# pip install clubheaddb

This command also automatically installs dependencies like Run the download command. This will read the metadata, download all source videos, and extract the raw frames. This is the longest step.yt-dlp`, `pandas`, etc.

### 3. Building the Dataset

The dataset is built in a two-step process.

Run the `download` command. This will read the metadata, download all source videos, and extract the raw frames. This is the longest step.

By default, data is stored in a `.clubheaddb` folder in your home directory. You can see the location by running `clubheaddb locate`.

