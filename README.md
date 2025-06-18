Here's the markdown text for your GitHub repository:

# ClubheadDB: A Video Database for Golf Clubhead Tracking

A public dataset of 67 diverse, down-the-line golf swings with frame-by-frame bounding box annotations for training and evaluating clubhead trackers.

**[Dataset Statistics](https://www.google.com/search?q=%23dataset-statistics)** • **[Data & Annotations](https://www.google.com/search?q=%23data--annotation-details)** • **[Baselines](https://www.google.com/search?q=%23performance-baselines)** • **[Getting the Data](https://www.google.com/search?q=%23getting-the-data)** • **[Citation](https://www.google.com/search?q=%23citation)**

-----


![Alt Text](banner.gif)
-----

## Dataset Statistics

The dataset is designed to provide a diverse set of scenarios for robust model training. All videos are filmed from a down-the-line (DTL) perspective.

| Feature               | Value           | Description                                                                 |
| :-------------------- | :-------------- | :-------------------------------------------------------------------------- |
| **Total Videos** | 67              | Video-level split: 44 Train, 10 Validation, 13 Test.                        |
| **Total Annotated Frames** | 10,847          | A single bounding box annotation exists for each frame.                     |
| **Video Sources** | YouTube (51%), Reddit (49%) | Sourced from public channels, providing a mix of camera qualities.          |
| **Unique Golfers** | 67             | Includes a mix of male and female golfers.                                  |
| **Skill Level Mix** | Pros (42%), Amateurs (58%) | Professional golfer swings are identified by name; amateur swings are anonymized. |
| **Club Type Mix** | Irons (67%), Drivers (28%), Woods (5%) | Provides variation in clubhead shape and speed.                             |
| **Frame Rate** | 15 or 30 FPS    | Videos are processed to a target FPS for consistency.                       |
| **Resolution** | $\\ge$ 720p       | All source videos are at least 720p to ensure annotation quality.           |

-----

## Data & Annotation Details

### Provenance

The video clips were sourced from public posts on YouTube and Reddit. The selection criteria focused on a clear "Down-The-Line" (DTL) view with minimal obstructions. The dataset includes a wide variety of lighting conditions, backgrounds, and camera qualities inherent to these public sources.

### Annotation Format

The bounding box annotations are provided in `data/annotations.csv`. The format is a standard `[x_min, y_min, x_max, y_max]` representation of the clubhead in pixel coordinates.

| `video_id`  | `frame` | `x_min` | `y_min` | `x_max` | `y_max` |
| :---------- | :------ | :------ | :------ | :------ | :------ |
| `swing_001` | 0       | 642     | 480     | 660     | 498     |
| `swing_001` | 1       | 645     | 482     | 663     | 500     |

We also provide a simple script to convert these annotations to the YOLO format (`<class_id> <x_center> <y_center> <width> <height>`) for direct use with popular detection frameworks.

-----

## Performance Baselines

To verify the quality of the dataset and establish a performance benchmark, we trained a YOLOv8s model on ClubheadDB. The results demonstrate the utility of the dataset for training accurate, real-time clubhead trackers.

| Model   | Precision | Recall | mAP@0.5 | mAP@.5:.95 |
| :------ | :-------- | :----- | :------ | :-------- |
| YOLOv8s | 0.94      | 0.83   | 0.87    | 0.53      |

This baseline provides a strong starting point for future research in trajectory analysis, swing plane reconstruction, and automated golf coaching systems.

-----

## Getting the Data

This repository contains the video metadata and bounding box annotations. The video files are downloaded via the provided script.

### 1\. Prerequisites

  * Python 3.9+
  * FFmpeg (must be in system's `PATH`)
  * `yt-dlp` (can be installed via pip)
  * Git

### 2\. Installation and Download

```bash
# Clone the repository
git clone https://github.com/your-username/ClubheadDB.git
cd ClubheadDB

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate # (Use `venv\Scripts\activate` on Windows)

# Install dependencies from the requirements file
pip install -r requirements.txt

# Run the script to download videos and extract frames
python src/download_and_process.py
```

The `download_and_process.py` script will:

  * Read the video list from `data/metadata.csv`.
  * Download the specified clip for each video into the `videos/` directory using `yt-dlp`.
  * Extract frames at the target FPS into the `frames/` directory using FFmpeg.

### Limitations

  * **Handedness Imbalance**: The dataset is overwhelmingly composed of right-handed golfers, with only two left-handed examples. Models trained on this data may not generalize well to left-handed swings without augmentation or further data collection.
  * **Viewpoint Consistency**: While all videos are from a DTL perspective, there are minor variations in camera placement and angle inherent to the public data sources.

-----

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
