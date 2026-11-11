
# Day 6 - Visual Quality Inspection System

FORGE is a computer vision application that analyses component images, identifies potential surface defects and generates inspection reports.

## Features

- Built-in clean and scratched component samples
- Upload custom images
- Grayscale conversion
- Gaussian noise reduction
- Otsu thresholding
- Main object segmentation
- Connected-component analysis
- Dark or bright defect candidate detection
- Minimum defect area filtering
- Defect region annotation
- Affected-area calculation
- Configurable PASS / REVIEW decision
- Downloadable inspection reports
- Annotated image export

## Technology Stack

- Python
- OpenCV
- NumPy
- Pandas
- Pillow
- Streamlit

## Installation

### 1. Create a virtual environment

```powershell
py -3.10 -m venv .venv
```

### 2. Activate it

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip --timeout 600 --retries 10
python -m pip install -r requirements.txt --no-cache-dir --timeout 600 --retries 10
```

### 4. Run the application

```powershell
streamlit run app.py
```

## How to use

1. Open the application.
2. Select Demo component in the sidebar.
3. Test the clean component.
4. Switch to the scratched component.
5. Compare the detected defect regions.
6. Change the defect intensity threshold.
7. Adjust the minimum defect area.
8. Change the allowed affected-area percentage.
9. Inspect the processing stages.
10. Download the inspection report and annotated image.

## Image processing workflow

1. Convert the image to grayscale.
2. Apply Gaussian blur.
3. Use Otsu thresholding to segment the object.
4. Identify the largest connected component.
5. Erode the object mask to reduce edge interference.
6. Identify intensity-based defect candidates.
7. Remove small regions using connected-component analysis.
8. Calculate affected area.
9. Annotate detected regions.

## Important limitation

This project uses classical image processing rather than a trained defect-classification model.

It is best suited to images where the component is distinguishable from its background and defects have a different intensity from the surrounding surface.

The detection result depends on lighting, image quality, object polarity and selected thresholds. A PASS result is not a certified industrial quality decision. Real production use requires validated datasets, calibrated imaging conditions and expert inspection.

## Project Objective

Demonstrate practical skills in computer vision, image preprocessing, segmentation, connected-component analysis, defect localization and interactive application development.
