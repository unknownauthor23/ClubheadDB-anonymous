<p align="center">
  <img src="https://storage.googleapis.com/gemini-prod/images/5f58359b-137a-4255-b072-46654e9e0325" alt="ClubheadDB Banner" width="80%"/>
</p>

# ClubheadDB: A Video Dataset for Golf Clubhead Tracking

<div align="center">

<!-- These badges will work once you publish to PyPI -->
![PyPI Version](https://img.shields.io/pypi/v/clubheaddb)
![License](https://img.shields.io/pypi/l/clubheaddb)
![Python Versions](https://img.shields.io/pypi/pyversions/clubheaddb)
![Dataset Size](https://img.shields.io/badge/Frames-10.000+-blue)
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
```

This command also automatically installs dependencies like `yt-dlp`, `pandas`, etc.

### 3. Building the Dataset

The dataset is built in a two-step process.

Run the `download` command. This will read the metadata, download all source videos, and extract the raw frames. This is the longest step.

By default, data is stored in a `.clubheaddb` folder in your home directory. You can see the location by running `clubheaddb locate`.

3. Building the Dataset

The dataset is built in a two-step process.

Step A: Download and Extract

Run the download command. This will read the metadata, download all source videos, and extract the raw frames. This is the longest step.

clubheaddb download

By default, data is stored in a .clubheaddb folder in your home directory. You can see the location by running clubheaddb locate.

Step B: Finalize the Dataset

Run the finalize command. This script uses the master annotations.parquet file to remove any downloaded frames that were not part of the final, curated dataset. This ensures your local copy is an exact replica.

clubheaddb finalize

You now have the complete, clean ClubheadDB dataset ready for use!
📁 Annotation Format

The primary annotation format is a high-performance Parquet file (annotations.parquet) located inside the package data. This is the fastest way to load labels for model training.

The file contains the following columns:

    image_path: The relative path to the image (e.g., frames/swing_001/images/frame_0001.jpg).

    class_id: The integer ID for the class (always 0 for golf clubhead).

    x_center, y_center, width, height: The normalized bounding box coordinates (YOLO format).

🤝 Contributing

Contributions are welcome! If you would like to add more videos to the dataset, please fork the repository, update metadata.csv, and submit a pull request with your proposed changes.
📜 License

This dataset is released under the MIT License. Please be aware of the Terms of Service of the original video sources (YouTube, Reddit).
✍️ Citation

If you use ClubheadDB in your research, please cite our work:

@inproceedings{hoefler2025clubheaddb,
  title={{ClubheadDB: A Bounding Box Dataset for Golf Clubhead Tracking}},
  author={Höfler, Sebastian and [Your Advisor's Name]},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) Workshops},
  year={2025}
}


