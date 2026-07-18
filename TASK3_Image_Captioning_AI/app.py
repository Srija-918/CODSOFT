import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import time

# ---------------- Page Config ---------------- #

st.set_page_config(
    page_title="AI Image Captioning",
    page_icon="🖼️",
    layout="wide"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.main{
    background-color:#f8f9fa;
}

h1{
    color:#1f77b4;
    text-align:center;
}

.caption-box{
    background:#E8F4FD;
    padding:20px;
    border-radius:10px;
    font-size:20px;
    font-weight:bold;
    color:#000;
    border-left:8px solid #1f77b4;
}

footer{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Title ---------------- #

st.title("🖼️ AI Image Captioning")

st.markdown(
"""
Generate meaningful captions for your images using
**Salesforce BLIP Image Captioning Model**.
"""
)

# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.header("Project Information")

    st.info("""
AI Image Captioning App

Technologies Used

• Python

• Streamlit

• Hugging Face

• Transformers

• PyTorch

• Pillow
""")

    st.success("Upload an image and click Generate Caption.")

# ---------------- Load Model ---------------- #

@st.cache_resource
def load_model():

    processor = BlipProcessor.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )

    model = BlipForConditionalGeneration.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )

    return processor, model

processor, model = load_model()

# ---------------- Caption History ---------------- #

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- Upload ---------------- #

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")

    col1, col2 = st.columns([1,1])

    with col1:

        st.subheader("Uploaded Image")

        st.image(
            image,
            use_container_width=True
        )

    with col2:

        st.subheader("AI Caption")

        if st.button("Generate Caption"):

            with st.spinner("Analyzing Image..."):

                time.sleep(1)

                inputs = processor(
                    image,
                    return_tensors="pt"
                )

                output = model.generate(
                    **inputs
                )

                caption = processor.decode(
                    output[0],
                    skip_special_tokens=True
                )

            st.markdown(
                f'<div class="caption-box">{caption}</div>',
                unsafe_allow_html=True
            )

            st.session_state.history.append(caption)

            st.download_button(
                "📥 Download Caption",
                caption,
                file_name="caption.txt"
            )

# ---------------- Caption History ---------------- #

if st.session_state.history:

    st.markdown("---")

    st.subheader("📜 Caption History")

    for i, cap in enumerate(reversed(st.session_state.history),1):

        st.write(f"**{i}.** {cap}")

# ---------------- Footer ---------------- #

st.markdown("---")

st.caption(
"Developed with ❤️ using Python, Streamlit and Hugging Face Transformers"
)