import streamlit as st
import os
from code_for_webui.download_models_openxlab import download 
from code_for_webui.demo_EDTalk_A_using_predefined_exp_weights import Demo as Demo_EDTalk_A_using_predefined_exp_weights
from code_for_webui.demo_lip_pose import Demo as Demo_lip_pose

# Uncomment this line if you haven't downloaded the models yet
download()

# Initialize demo classes
demo_EDTalk_A_using_predefined_exp_weights = Demo_EDTalk_A_using_predefined_exp_weights()
demo_lip_pose = Demo_lip_pose()

st.set_page_config(
    page_title="Expressive Avatar Video Creator",
    page_icon="🎥"
)

# Function to run inference
def run_inference(source_image, audio_file, pose_video, exp_type, face_sr):
    try:
        source_path = source_image if source_image else ""
        audio_driving_path = audio_file if audio_file else ""
        pose_driving_path = pose_video  # Always use the default pose video

        # Process the input data
        if exp_type in ["angry", "contempt", "disgusted", "fear", "happy", "sad", "surprised"]:
            demo_EDTalk_A_using_predefined_exp_weights.process_data(source_path, pose_driving_path, audio_driving_path, exp_type, False, False, face_sr)
            save_path = demo_EDTalk_A_using_predefined_exp_weights.run()
        else:
            demo_lip_pose.process_data(source_path, pose_driving_path, audio_driving_path, False, False, face_sr)
            save_path = demo_lip_pose.run()

        save_512_path = save_path.replace('.mp4', '_512.mp4')

        # Check if the output video file exists
        if not os.path.exists(save_path):
            st.error("Error: Video generation failed. Please check your inputs and try again.")
            return None, None
        
        if not face_sr:
            return save_path, None
        
        if os.path.exists(save_512_path):
            return save_path, save_512_path
        else:
            st.error("Video generation failed for the 512 resolution, please retry.")
            return None, None
    except Exception as e:
        st.error(f"Video generation failed: {str(e)}")
        return None, None

# Streamlit app layout
st.title("Expressive Avatar Video Creator")

# File upload section in the sidebar
st.sidebar.header("Menu:")
source_file = st.sidebar.file_uploader("Select Source Image", type=["jpg", "jpeg", "png"])
driving_audio = st.sidebar.file_uploader("Select Audio File", type=["wav", "mp3"])

# Removed the pose video uploader
pose_video_path = "test_data/pose_source1.mp4"  # Default pose video path

exp_type = st.sidebar.selectbox("Select Expression Type", options=[
    "I don't wanna generate emotional expression", "angry", "contempt", "disgusted", "fear", "happy", "sad", "surprised"
])
face_sr = st.sidebar.checkbox("Use Face Super-Resolution")

if st.sidebar.button("Submit"):
    if not source_file or not driving_audio:
        st.error("Please upload both a source image and an audio file.")
    else:
        with st.spinner("Generating video..."):
            source_image_path = source_file.name  # Save the uploaded image
            with open(source_image_path, "wb") as f:
                f.write(source_file.getbuffer())

            audio_file_path = driving_audio.name  # Save the uploaded audio
            with open(audio_file_path, "wb") as f:
                f.write(driving_audio.getbuffer())

            # Use the default pose video path
            output_256, output_512 = run_inference(source_image_path, audio_file_path, pose_video_path, exp_type, face_sr)

            # Create two columns for video outputs
            col1, col2 = st.columns(2)
            with col1:
                if output_256:
                    st.video(output_256)
                    st.success("Video (256) generated successfully!")
            with col2:
                if output_512:
                    st.video(output_512)
                    st.success("Video (512) generated successfully!")
