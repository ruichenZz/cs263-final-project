# Project Name: LVLM Hallucination Mitigation

This project focuses on mitigating hallucination effects in Large Vision-Language Models (LVLMs) using Visual Contrastive Decoding (VCD) and benchmarking with POPE and AMBER.

## Environment Setup

Follow these steps to set up the environment:

### 1. Install Conda

Ensure you have Conda installed. If not, download and install it from the [official Conda website](https://docs.conda.io/en/latest/miniconda.html).

### 2. Clone the Repository

Clone this repository and navigate to the project directory:
```bash
git clone https://github.com/ruichenZz/cs263-final-project.git
cd cs263-final-project
```

### 3. Create a Conda Environment

Run the following commands to create and activate a Conda environment:

```bash
conda create --name lvlm_env python=3.10 -y
conda activate lvlm_env
```

### 4. Install Dependencies

Install all the required packages listed in the requirements.txt file:

```bash
pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2
pip install -r requirements.txt
```
Use `conda deactivate` to exit the environment when you are done working.

### 5. Download AMBER dataset

```bash
gdown https://drive.google.com/uc?id=1MaCHgtupcZUjf007anNl4_MV0o4DjXvl -O dataset/AMBER.zip
unzip AMBER.zip
rm AMBER.zip
```