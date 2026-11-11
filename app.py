
import streamlit as st
import numpy as np
import pandas as pd
import cv2
from PIL import Image, ImageDraw
from datetime import datetime
from io import BytesIO


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="FORGE | Visual Inspection System",
    page_icon="⬡",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# INDUSTRIAL DESIGN SYSTEM
# ============================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&family=Inter:wght@400;500;600;700&display=swap');

:root {
    --bg: #111416;
    --panel: #1b2023;
    --panel2: #242b2f;
    --line: #343d42;
    --text: #e8edef;
    --muted: #8d999e;
    --orange: #ff8a36;
    --green: #9bdb73;
    --red: #ff6262;
}

.stApp {
    background: var(--bg);
    color: var(--text);
    font-family: 'Inter', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1550px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

h1, h2, h3, h4, p, label {
    color: var(--text);
    font-family: 'Inter', sans-serif;
}

h1, h2 {
    font-family: 'Barlow Condensed', sans-serif !important;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

h1 {
    font-size: 48px !important;
    font-weight: 800 !important;
}

h2 {
    font-size: 29px !important;
    font-weight: 700 !important;
}

h3 {
    font-size: 18px !important;
    font-weight: 700 !important;
}

[data-testid="stSidebar"] {
    background: #191e21;
    border-right: 1px solid var(--line);
}

[data-testid="stSidebar"] * {
    color: var(--text);
}

[data-testid="stMetric"] {
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: 5px;
    padding: 15px;
}

[data-testid="stMetricLabel"] {
    color: var(--muted) !important;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px !important;
    letter-spacing: 1px;
    text-transform: uppercase;
}

[data-testid="stMetricValue"] {
    color: var(--orange) !important;
    font-weight: 800;
}

.stButton > button,
.stDownloadButton > button {
    background: var(--orange);
    color: #17191a;
    border: 1px solid var(--orange);
    border-radius: 4px;
    font-weight: 800;
    min-height: 42px;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    background: #ffa45e;
    color: #17191a;
    border-color: #ffa45e;
}

.stTextInput input,
.stSelectbox div[data-baseweb="select"],
.stNumberInput input {
    background: var(--panel);
    border-color: var(--line);
    color: var(--text);
}

.stTabs [data-baseweb="tab-list"] {
    gap: 12px;
    border-bottom: 1px solid var(--line);
}

.stTabs [data-baseweb="tab"] {
    color: var(--muted);
    font-family: 'IBM Plex Mono', monospace;
    font-size: 12px;
}

.stTabs [aria-selected="true"] {
    color: var(--orange) !important;
}

hr {
    border-color: var(--line);
}

[data-testid="stFileUploader"] {
    background: var(--panel);
    border: 1px dashed #59656b;
    border-radius: 5px;
    padding: 10px;
}

.machine-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--line);
    margin-bottom: 28px;
}

.machine-brand {
    font-family: 'IBM Plex Mono', monospace;
    color: var(--orange);
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 3px;
}

.machine-meta {
    color: var(--muted);
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    letter-spacing: 1px;
}

.hero-kicker {
    color: var(--orange);
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    letter-spacing: 3px;
    margin-bottom: 10px;
}

.hero-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: clamp(45px, 7vw, 76px);
    font-weight: 800;
    line-height: 0.98;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.hero-title span {
    color: var(--orange);
}

.hero-description {
    color: var(--muted);
    font-size: 14px;
    line-height: 1.8;
    max-width: 680px;
    margin-top: 15px;
}

.section-kicker {
    font-family: 'IBM Plex Mono', monospace;
    color: var(--orange);
    font-size: 10px;
    letter-spacing: 2px;
    margin-bottom: 8px;
}

.section-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 29px;
    font-weight: 700;
    text-transform: uppercase;
    margin-bottom: 5px;
}

.section-copy {
    color: var(--muted);
    font-size: 12px;
    margin-bottom: 20px;
}

.machine-panel {
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: 5px;
    padding: 18px;
    height: 100%;
}

.panel-label {
    color: var(--muted);
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    letter-spacing: 1.5px;
}

.panel-value {
    font-family: 'Barlow Condensed', sans-serif;
    color: var(--orange);
    font-size: 35px;
    font-weight: 700;
    margin-top: 7px;
}

.panel-note {
    color: var(--muted);
    font-size: 11px;
    margin-top: 4px;
}

.status-pass {
    background: #193322;
    border: 1px solid #3f8652;
    color: var(--green);
    padding: 20px;
    border-radius: 5px;
    font-family: 'IBM Plex Mono', monospace;
    font-weight: 600;
    letter-spacing: 2px;
    text-align: center;
    font-size: 22px;
}

.status-review {
    background: #3b2020;
    border: 1px solid #a84c4c;
    color: var(--red);
    padding: 20px;
    border-radius: 5px;
    font-family: 'IBM Plex Mono', monospace;
    font-weight: 600;
    letter-spacing: 2px;
    text-align: center;
    font-size: 22px;
}

.stage-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    color: var(--muted);
    letter-spacing: 1.5px;
    margin-bottom: 8px;
}

.footer {
    border-top: 1px solid var(--line);
    margin-top: 40px;
    padding-top: 18px;
    color: var(--muted);
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    letter-spacing: 1px;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# DEMO IMAGE GENERATOR
# ============================================================

def generate_component(defective=False, seed=42):

    rng = np.random.default_rng(seed)

    width = 640
    height = 480

    image = np.full(
        (height, width, 3),
        35,
        dtype=np.uint8
    )

    center = (width // 2, height // 2)

    # Metallic component
    cv2.circle(
        image,
        center,
        165,
        (185, 185, 185),
        -1,
        cv2.LINE_AA
    )

    # Subtle metallic texture
    noise = rng.normal(
        0,
        4,
        (height, width)
    )

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    ).astype(np.float32)

    gray += noise

    gray = np.clip(
        gray,
        0,
        255
    ).astype(np.uint8)

    image = cv2.cvtColor(
        gray,
        cv2.COLOR_GRAY2BGR
    )

    # Inner opening
    cv2.circle(
        image,
        center,
        55,
        (35, 35, 35),
        -1,
        cv2.LINE_AA
    )

    # Outer and inner edge details
    cv2.circle(
        image,
        center,
        165,
        (220, 220, 220),
        3,
        cv2.LINE_AA
    )

    cv2.circle(
        image,
        center,
        55,
        (105, 105, 105),
        2,
        cv2.LINE_AA
    )

    if defective:

        # Scratch marks
        cv2.line(
            image,
            (245, 165),
            (350, 235),
            (42, 42, 42),
            7,
            cv2.LINE_AA
        )

        cv2.line(
            image,
            (370, 295),
            (430, 330),
            (48, 48, 48),
            5,
            cv2.LINE_AA
        )

        # Dark defect spots
        cv2.circle(
            image,
            (265, 290),
            12,
            (35, 35, 35),
            -1
        )

        cv2.circle(
            image,
            (395, 165),
            9,
            (42, 42, 42),
            -1
        )

    return image


# ============================================================
# INSPECTION ENGINE
# ============================================================

def inspect_component(
    image,
    polarity="Bright object",
    defect_threshold=110,
    minimum_area=12,
    blur_size=5
):

    # Convert image to grayscale
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # Noise reduction
    blur = cv2.GaussianBlur(
        gray,
        (blur_size, blur_size),
        0
    )

    # Automatic thresholding for object segmentation
    threshold_type = (
        cv2.THRESH_BINARY
        if polarity == "Bright object"
        else cv2.THRESH_BINARY_INV
    )

    _, object_mask = cv2.threshold(
        blur,
        0,
        255,
        threshold_type + cv2.THRESH_OTSU
    )

    # Keep the largest connected component
    count, labels, stats, _ = (
        cv2.connectedComponentsWithStats(
            object_mask,
            connectivity=8
        )
    )

    if count <= 1:
        raise ValueError(
            "Could not identify the main object. "
            "Try changing object polarity or image background."
        )

    component_areas = stats[1:, cv2.CC_STAT_AREA]

    largest_label = int(
        np.argmax(component_areas) + 1
    )

    object_region = np.uint8(
        labels == largest_label
    ) * 255

    object_area = int(
        np.count_nonzero(object_region)
    )

    image_area = image.shape[0] * image.shape[1]

    if object_area < image_area * 0.01:
        raise ValueError(
            "The detected object region is too small. "
            "Try a clearer image with a more contrasting background."
        )

    # Erode edges to avoid counting normal boundaries
    kernel = np.ones((7, 7), np.uint8)

    interior_mask = cv2.erode(
        object_region,
        kernel,
        iterations=1
    )

    # Find dark irregular regions inside the object
    if polarity == "Bright object":
        candidate_mask = np.uint8(
            (blur < defect_threshold) &
            (interior_mask > 0)
        ) * 255
    else:
        candidate_mask = np.uint8(
            (blur > defect_threshold) &
            (interior_mask > 0)
        ) * 255

    # Remove small noise
    candidate_mask = cv2.morphologyEx(
        candidate_mask,
        cv2.MORPH_OPEN,
        np.ones((3, 3), np.uint8)
    )

    # Connected components for defect candidates
    defect_count, defect_labels, defect_stats, _ = (
        cv2.connectedComponentsWithStats(
            candidate_mask,
            connectivity=8
        )
    )

    final_defect_mask = np.zeros_like(
        candidate_mask
    )

    defects = []

    for i in range(1, defect_count):

        area = int(
            defect_stats[i, cv2.CC_STAT_AREA]
        )

        if area < minimum_area:
            continue

        x = int(defect_stats[i, cv2.CC_STAT_LEFT])
        y = int(defect_stats[i, cv2.CC_STAT_TOP])
        w = int(defect_stats[i, cv2.CC_STAT_WIDTH])
        h = int(defect_stats[i, cv2.CC_STAT_HEIGHT])

        final_defect_mask[
            defect_labels == i
        ] = 255

        defects.append({
            "Defect ID": len(defects) + 1,
            "X": x,
            "Y": y,
            "Width": w,
            "Height": h,
            "Area (pixels)": area
        })

    total_defect_area = int(
        np.count_nonzero(final_defect_mask)
    )

    defect_percentage = (
        total_defect_area / max(object_area, 1)
    ) * 100

    # Create annotated image
    annotated = image.copy()

    contours, _ = cv2.findContours(
        final_defect_mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:

        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(
            annotated,
            (x, y),
            (x + w, y + h),
            (0, 100, 255),
            2
        )

        cv2.putText(
            annotated,
            "DEFECT",
            (x, max(y - 7, 15)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            (0, 100, 255),
            1,
            cv2.LINE_AA
        )

    # Overlay defect pixels
    overlay = annotated.copy()

    overlay[final_defect_mask > 0] = (
        0,
        60,
        255
    )

    annotated = cv2.addWeighted(
        overlay,
        0.45,
        annotated,
        0.55,
        0
    )

    defect_table = pd.DataFrame(
        defects,
        columns=[
            "Defect ID",
            "X",
            "Y",
            "Width",
            "Height",
            "Area (pixels)"
        ]
    )

    return {
        "gray": gray,
        "blur": blur,
        "object_mask": object_region,
        "defect_mask": final_defect_mask,
        "annotated": annotated,
        "object_area": object_area,
        "defect_area": total_defect_area,
        "defect_percentage": defect_percentage,
        "defect_count": len(defects),
        "defects": defect_table
    }


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="machine-header">
    <div class="machine-brand">⬡ FORGE / VISION SYSTEMS</div>
    <div class="machine-meta">
        STATION 06 &nbsp; | &nbsp; COMPUTER VISION &nbsp; | &nbsp; ONLINE
    </div>
</div>

<div class="hero-kicker">
    INDUSTRIAL AUTOMATION / VISUAL QUALITY CONTROL
</div>

<div class="hero-title">
    Inspect. Detect.<br>
    <span>Decide.</span>
</div>

<div class="hero-description">
    A computer vision inspection workstation for identifying
    visible surface irregularities, measuring defect regions
    and generating quality-control results.
</div>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR — MACHINE CONTROLS
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="machine-brand">MACHINE CONTROLS</div>',
        unsafe_allow_html=True
    )

    st.divider()

    input_mode = st.radio(
        "Inspection input",
        [
            "Demo component",
            "Upload image"
        ]
    )

    uploaded_file = None
    demo_choice = None

    if input_mode == "Demo component":

        demo_choice = st.selectbox(
            "Select test component",
            [
                "Clean component",
                "Scratched component"
            ]
        )

    else:

        uploaded_file = st.file_uploader(
            "Upload inspection image",
            type=["png", "jpg", "jpeg", "bmp"]
        )

    st.divider()

    st.markdown("### Inspection parameters")

    polarity = st.selectbox(
        "Object appearance",
        [
            "Bright object",
            "Dark object"
        ],
        help=(
            "Choose Bright object when the component is lighter "
            "than its background."
        )
    )

    defect_threshold = st.slider(
        "Defect intensity threshold",
        min_value=20,
        max_value=220,
        value=110,
        step=5
    )

    minimum_area = st.slider(
        "Minimum defect area (pixels)",
        min_value=3,
        max_value=300,
        value=12,
        step=1
    )

    blur_size = st.selectbox(
        "Noise reduction",
        [3, 5, 7, 9],
        index=1
    )

    st.divider()

    st.markdown("### Quality standard")

    max_defect_percentage = st.slider(
        "Maximum affected area (%)",
        min_value=0.1,
        max_value=5.0,
        value=0.8,
        step=0.1
    )

    st.caption(
        "Components exceeding this affected-area threshold "
        "are marked REVIEW."
    )


# ============================================================
# LOAD IMAGE
# ============================================================

image_bgr = None
image_name = "Demo component"

if input_mode == "Demo component":

    defective = (
        demo_choice == "Scratched component"
    )

    image_bgr = generate_component(
        defective=defective
    )

    image_name = demo_choice

elif uploaded_file is not None:

    try:

        pil_image = Image.open(
            uploaded_file
        ).convert("RGB")

        image_rgb = np.array(pil_image)

        image_bgr = cv2.cvtColor(
            image_rgb,
            cv2.COLOR_RGB2BGR
        )

        image_name = uploaded_file.name

    except Exception as error:

        st.error(
            f"Could not open image: {error}"
        )
        st.stop()

else:

    st.info(
        "Upload an image using the machine controls in the sidebar."
    )
    st.stop()


# ============================================================
# RUN INSPECTION
# ============================================================

try:

    result = inspect_component(
        image_bgr,
        polarity=polarity,
        defect_threshold=defect_threshold,
        minimum_area=minimum_area,
        blur_size=blur_size
    )

except Exception as error:

    st.error(
        f"Inspection could not be completed: {error}"
    )
    st.stop()


# ============================================================
# INSPECTION STATUS
# ============================================================

inspection_status = (
    "PASS"
    if result["defect_percentage"] <= max_defect_percentage
    else "REVIEW"
)

inspection_time = datetime.now().strftime(
    "%d %b %Y, %H:%M:%S"
)


# ============================================================
# WORKSPACE NAVIGATION
# ============================================================

page = st.radio(
    "Inspection workspace",
    [
        "01  Live Inspection",
        "02  Image Processing",
        "03  Defect Analysis",
        "04  Inspection Report"
    ],
    horizontal=True,
    label_visibility="collapsed"
)

st.divider()


# ============================================================
# PAGE 1 — LIVE INSPECTION
# ============================================================

if page == "01  Live Inspection":

    st.markdown("""
    <div class="section-kicker">01 / INSPECTION WORKSTATION</div>
    <div class="section-title">Component inspection</div>
    <div class="section-copy">
        Inspect the component and review detected surface irregularities.
    </div>
    """, unsafe_allow_html=True)

    if inspection_status == "PASS":

        st.markdown(
            '<div class="status-pass">● QUALITY STATUS: PASS</div>',
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            '<div class="status-review">● QUALITY STATUS: REVIEW REQUIRED</div>',
            unsafe_allow_html=True
        )

    st.write("")

    left, right = st.columns([1.7, 1])

    with left:

        st.markdown(
            '<div class="stage-label">CAMERA FEED / ANNOTATED OUTPUT</div>',
            unsafe_allow_html=True
        )

        st.image(
            cv2.cvtColor(
                result["annotated"],
                cv2.COLOR_BGR2RGB
            ),
            use_container_width=True
        )

        st.caption(
            f"Inspection target: {image_name}"
        )

    with right:

        st.markdown("### Inspection telemetry")

        st.metric(
            "DEFECT CANDIDATES",
            result["defect_count"]
        )

        st.metric(
            "DEFECT AREA",
            f"{result['defect_area']:,} px"
        )

        st.metric(
            "AFFECTED AREA",
            f"{result['defect_percentage']:.3f}%"
        )

        st.metric(
            "OBJECT AREA",
            f"{result['object_area']:,} px"
        )

        st.divider()

        st.markdown("### Machine settings")

        st.write(f"**Input:** {image_name}")
        st.write(f"**Threshold:** {defect_threshold}")
        st.write(f"**Minimum area:** {minimum_area} px")
        st.write(f"**Noise filter:** {blur_size} × {blur_size}")
        st.write(
            f"**Quality limit:** {max_defect_percentage:.1f}%"
        )


# ============================================================
# PAGE 2 — IMAGE PROCESSING
# ============================================================

elif page == "02  Image Processing":

    st.markdown("""
    <div class="section-kicker">02 / IMAGE PIPELINE</div>
    <div class="section-title">Processing stages</div>
    <div class="section-copy">
        Examine how the image is transformed before defect detection.
    </div>
    """, unsafe_allow_html=True)

    stages = [
        (
            "01 / ORIGINAL IMAGE",
            cv2.cvtColor(
                image_bgr,
                cv2.COLOR_BGR2RGB
            )
        ),
        (
            "02 / GRAYSCALE",
            result["gray"]
        ),
        (
            "03 / NOISE REDUCTION",
            result["blur"]
        ),
        (
            "04 / OBJECT MASK",
            result["object_mask"]
        ),
        (
            "05 / DEFECT MASK",
            result["defect_mask"]
        ),
        (
            "06 / ANNOTATED OUTPUT",
            cv2.cvtColor(
                result["annotated"],
                cv2.COLOR_BGR2RGB
            )
        )
    ]

    col1, col2 = st.columns(2)

    for index, (name, image) in enumerate(stages):

        target = col1 if index % 2 == 0 else col2

        with target:

            st.markdown(
                f'<div class="stage-label">{name}</div>',
                unsafe_allow_html=True
            )

            st.image(
                image,
                use_container_width=True
            )

    st.divider()

    st.markdown("### Pipeline explanation")

    st.write(
        "1. Grayscale: removes colour information and simplifies analysis."
    )

    st.write(
        "2. Gaussian blur: reduces small image variations and noise."
    )

    st.write(
        "3. Otsu thresholding: separates the component from its background."
    )

    st.write(
        "4. Connected components: isolates the largest detected object."
    )

    st.write(
        "5. Defect segmentation: identifies sufficiently dark or bright "
        "regions inside the component's interior."
    )

    st.write(
        "6. Contour annotation: draws boxes around detected defect regions."
    )


# ============================================================
# PAGE 3 — DEFECT ANALYSIS
# ============================================================

elif page == "03  Defect Analysis":

    st.markdown("""
    <div class="section-kicker">03 / QUALITY ANALYTICS</div>
    <div class="section-title">Defect analysis</div>
    <div class="section-copy">
        Investigate detected regions and their impact on the component.
    </div>
    """, unsafe_allow_html=True)

    a, b, c = st.columns(3)

    a.metric(
        "DEFECT COUNT",
        result["defect_count"]
    )

    b.metric(
        "TOTAL DEFECT AREA",
        f"{result['defect_area']:,} px"
    )

    c.metric(
        "AFFECTED AREA",
        f"{result['defect_percentage']:.3f}%"
    )

    st.divider()

    st.markdown("### Defect region map")

    st.image(
        cv2.cvtColor(
            result["annotated"],
            cv2.COLOR_BGR2RGB
        ),
        use_container_width=True
    )

    st.divider()

    st.markdown("### Detected defect coordinates")

    if result["defects"].empty:

        st.success(
            "No defect regions passed the selected detection filters."
        )

    else:

        st.dataframe(
            result["defects"],
            use_container_width=True,
            hide_index=True
        )

        st.download_button(
            "Download defect coordinates",
            result["defects"].to_csv(
                index=False
            ).encode("utf-8"),
            file_name="defect_coordinates.csv",
            mime="text/csv"
        )

    st.divider()

    st.markdown("### Inspection configuration")

    st.write(
        f"Intensity threshold: {defect_threshold}"
    )

    st.write(
        f"Minimum defect area: {minimum_area} pixels"
    )

    st.write(
        f"Maximum allowed affected area: "
        f"{max_defect_percentage:.1f}%"
    )


# ============================================================
# PAGE 4 — INSPECTION REPORT
# ============================================================

elif page == "04  Inspection Report":

    st.markdown("""
    <div class="section-kicker">04 / QUALITY CONTROL RECORD</div>
    <div class="section-title">Inspection report</div>
    <div class="section-copy">
        Review and export the current component inspection.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Inspection record")

    report = pd.DataFrame([{
        "Inspection Date": inspection_time,
        "Component": image_name,
        "Status": inspection_status,
        "Defect Count": result["defect_count"],
        "Object Area (px)": result["object_area"],
        "Defect Area (px)": result["defect_area"],
        "Affected Area (%)": round(
            result["defect_percentage"],
            4
        ),
        "Intensity Threshold": defect_threshold,
        "Minimum Defect Area": minimum_area,
        "Allowed Affected Area (%)": max_defect_percentage
    }])

    st.dataframe(
        report,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.markdown("### Annotated inspection image")

    st.image(
        cv2.cvtColor(
            result["annotated"],
            cv2.COLOR_BGR2RGB
        ),
        use_container_width=True
    )

    st.divider()

    st.markdown("### Export records")

    st.download_button(
        "Download inspection report CSV",
        report.to_csv(index=False).encode("utf-8"),
        file_name="inspection_report.csv",
        mime="text/csv"
    )

    output_rgb = cv2.cvtColor(
        result["annotated"],
        cv2.COLOR_BGR2RGB
    )

    output_image = Image.fromarray(output_rgb)

    image_buffer = BytesIO()

    output_image.save(
        image_buffer,
        format="PNG"
    )

    st.download_button(
        "Download annotated inspection image",
        image_buffer.getvalue(),
        file_name="annotated_inspection.png",
        mime="image/png"
    )

    if inspection_status == "PASS":

        st.success(
            "The component is within the configured affected-area limit."
        )

    else:

        st.error(
            "The component exceeds the configured affected-area limit "
            "and requires manual review."
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
    FORGE / VISION SYSTEMS
    <br><br>
    COMPUTER VISION &nbsp; • &nbsp;
    INDUSTRIAL INSPECTION &nbsp; • &nbsp;
    IMAGE PROCESSING
    <br><br>
    PROJECT MARATHON / DAY 06 OF 60
</div>
""", unsafe_allow_html=True)
