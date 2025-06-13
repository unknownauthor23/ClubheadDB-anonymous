# ClubheadDB: A Dataset for Down-the-Line Golf Clubhead Detection

![CVPR 2025 Workshop](https://img.shields.io/badge/Conference-CVPR%202025%20Workshop-blue) ![Dataset Size](https://img.shields.io/badge/Images-5000%2B-orange) ![Annotations](https://img.shields.io/badge/Annotations-Bounding%20Box-green) ![License](https://img.shields.io/badge/License-MIT-lightgrey)

![Hero GIF of the app in action](assets/swing_demo.gif)
*A demonstration of a real-time swing analysis using a model trained on ClubheadDB.*

---

This repository contains the **ClubheadDB** dataset, introduced in our paper:

> **[Your New Paper Title]** <br>
> *[Your Name(s)]* <br>
> *Proceedings of the CVPR 2025 Workshop on Sensing, Art, and Understanding of the Human Form in the Wild for Fine-Grained Analysis.*

**[Link to your paper will go here once it's on arXiv or published]**

## Motivation

The analysis of high-speed human motion on mobile devices is a key challenge in computer vision. For sports like golf, providing fine-grained feedback on form requires robust tracking of small, fast-moving objects. We found that existing public datasets lack the high-quality, densely annotated data needed to train a reliable golf clubhead detector from the critical down-the-line (DTL) perspective. **ClubheadDB was created to fill this specific gap**, enabling researchers to develop and benchmark models for this challenging task.

## Dataset Overview

ClubheadDB is a collection of video frames designed to train and evaluate models for golf clubhead detection. The dataset was collected from 50 diverse videos sourced from public platforms like YouTube and Reddit.

### Key Statistics
* **Total Frames:** ~5,000
* **Source Videos:** 50
* **Perspective:** Down-the-Line (DTL)
* **Annotations:** A single `clubhead` class, manually annotated with tight bounding boxes.
* **Format:** YOLO TXT (`class_id x_center y_center width height`), normalized.

### Dataset Composition

![Data Distribution Charts](assets/distribution_charts.png)
*(Left to right: Recording Mode, Sex, Club Type, Video Source)*

### Sample Images

![Grid of sample images](assets/sample_grid.png)

### Annotation Quality

We focused on creating tight, consistent bounding boxes to ensure high-quality labels for model training.

![Annotation examples](assets/annotation_examples.png)

## Download & Usage

You can download the complete dataset as a single `.zip` file from the [Releases page](https://github.com/your-username/ClubheadDB-Golf-Swing-Dataset/releases).

The dataset is structured for direct use with the Ultralytics YOLO framework but can be easily adapted for other platforms. The data is pre-split at the video level to prevent data leakage.

* **Training Set:** 70%
* **Validation Set:** 17%
* **Test Set:** 13%

## Citation

If you use ClubheadDB in your research, we kindly ask that you cite our paper:

```bibtex
@inproceedings{hoefler2025clubheaddb,
  title={[Your New Paper Title]},
  author={[Your Name(s)]},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops},
  year={2025}
}
```

## License

This dataset is licensed under the [MIT License](LICENSE).

## Contact

For any questions, please contact [your name] at [your email].
