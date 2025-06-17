<p align="center">
  <img src="assets/clubhead_db_banner.png" alt="ClubheadDB Banner"/>
</p>

# ClubheadDB: A Golf Swing Video Dataset

<div align="center">

![Dataset Version](https://img.shields.io/badge/version-1.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Videos](https://img.shields.io/badge/videos-67+-lightgrey)
![Sources](https://img.shields.io/badge/sources-YouTube_|_Reddit-red)

</div>

**ClubheadDB** is an open-source dataset designed for computer vision tasks in golf analytics. It provides metadata for over 67 high-quality video clips of golf swings, sourced from YouTube and Reddit, complete with frame-by-frame bounding box annotations for the golf clubhead.

This repository provides the necessary tools and metadata to download the source videos and reconstruct the full dataset on your local machine.

## 🌟 Dataset Highlights

| Feature | Description |
| :--- | :--- |
| **Total Videos** | 67+ (and growing) |
| **Total Frames** | ~10,800+ (after processing) |
| **Classes** | `clubhead` |
| **Sources** | YouTube, YouTube Shorts, Reddit |
| **Annotations** | Frame-by-frame bounding boxes in YOLO format |
| **Perspectives** | Down-the-line (DTL) |

## 🖼️ Visual Examples

Here are a few examples of the annotated frames you can generate with this dataset.

| DTL View | Face-On View |
| :---: | :---: |
| <img src="assets/example_dtl.jpg" width="400"> | <img src="assets/example_fo.jpg" width="400"> |

## 🚀 Getting Started

Because the video clips are sourced from public platforms, this repository does not contain the video or image files directly. Follow these steps to download and build the dataset locally.

### 1. Prerequisites

You need Python, `yt-dlp`, and `ffmpeg` installed.

- **Python 3.8+**
- **yt-dlp & ffmpeg**: The easiest way to install these on macOS or Linux is with [Homebrew](https://brew.sh):
  ```bash
  brew install yt-dlp ffmpeg


### 2. Clone the Repository

git clone [https://github.com/sebastianhoefler/ClubheadDB.git](https://github.com/sebastianhoefler/ClubheadDB.git)
cd ClubheadDB

### 3. Install Python Dependencies

pip install -r requirements.txt
