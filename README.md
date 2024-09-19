# Expressive Avatar Video Creator

This repository provides a tool to generate expressive avatar videos from images and audio files using predefined expression weights and lip poses. The project is built using Python, Streamlit, and other libraries to create a web app for generating videos.

## Features

- **Image-to-Video Animation**: Converts a static image into a talking avatar based on audio input.
- **Expression Control**: Select predefined expressions (e.g., happy, angry, sad) for the avatar.
- **Super-Resolution**: Option to use face super-resolution for improved video quality.

---

## Getting Started

### 1. Clone the Repository

Open **Command Prompt** or **PowerShell** and clone the repository:

```bash
git clone https://github.com/tanshuai0219/EDTalk
cd EDTalk
```

### 2. Create a Conda Environment

Open **Command Prompt** or **Anaconda Prompt**, then create a new environment with Python 3.8:

```bash
conda create -n avatar_video_creator python=3.8
conda activate avatar_video_creator
```

### 3. Install Dependencies

#### Install FFmpeg

The project requires **FFmpeg** for video processing. Install it using Conda:

```bash
conda install -c conda-forge ffmpeg
```

#### Install Python Dependencies

The repository includes a `requirements_windows.txt` file for Windows users. You can install all the dependencies with:

```bash
pip install -r requirements_windows.txt
```

Alternatively, you can manually install the main libraries required for the project:

```bash
pip install facexlib==0.3.0
pip install gfpgan==1.3.8
pip install tb-nightly==2.14.0a20230808
pip install google-auth-oauthlib==0.4.6
pip install tensorboard-data-server==0.6.1
pip install streamlit
```

### 4. Install `dlib` (Optional)

Some projects may require `dlib`. Follow these steps if `dlib` is necessary:

1. Install **CMake** via Conda:

    ```bash
    conda install -c conda-forge cmake
    ```

2. Download and install **Visual Studio Build Tools** from [here](https://visualstudio.microsoft.com/visual-cpp-build-tools/) for building `dlib`.

3. Install **dlib** using pip:

    ```bash
    pip install dlib
    ```

### 5. Run the Application

Once everything is installed, download the `app.py` file and place it into the root directory. you can also use the Express_avatar.ipynb(google colab notebook), to run all these commands. Now, you can run the application using Streamlit:

```bash
streamlit run app.py
```

---

## Citation

If you use this code or dataset in your work, please consider citing the repository. Here's an example citation:

```
@inproceedings{tan2024edtalk,
  title = {EDTalk: Efficient Disentanglement for Emotional Talking Head Synthesis},
  author = {Tan, Shuai and Ji, Bin and Bi, Mengxiao and Pan, Ye},
  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},
  year = {2024}
}
```
