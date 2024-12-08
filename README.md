# Project Name: LVLM Hallucination Mitigation

This project focuses on mitigating hallucination effects in Large Vision-Language Models (LVLMs) using Visual Contrastive Decoding (VCD) and benchmarking with POPE and AMBER.

## Environment Setup

Follow these steps to set up the environment:

### 1. Install Conda

Ensure you have Conda installed. If not, download and install it from the [official Conda website](https://docs.conda.io/en/latest/miniconda.html).

### 2. Set up the Repository

Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/ruichenZz/cs263-final-project.git
cd cs263-final-project
```

Clone the AMBER repo into this parent repo and follow the instructions there to set up AMBER pipeline, download data, etc: https://github.com/junyangwang0410/AMBER

### 3. Create a Conda Environment

Run the following commands to create and activate a Conda environment:

```bash
conda create -yn vcd python=3.9
conda activate vcd
cd cs263-final-project
pip install -r requirements.txt
```

### 4. Download LLaVA Model

Under the ./experiments repository, clone LLaVA model from Huggingface:

```bash
git-lfs clone https://huggingface.co/liuhaotian/llava-v1.5-7b ./checkpoints/llava-v1.5-7b
```

### 5. Download MSCOCO

Under the ./experiments repository, download MSCOCO data and unzip it:

```bash
gdown "https://drive.google.com/uc?id=1yHpSt2377usoUah9z-fKCF7mn9rF6Sl7" -O ./data/coco/val2014.zip
unzip val2014.zip
```

### 6. Run Experiments for Discriminative Tasks under POPE metric

Modify ./experiments/cd_scripts/llava1.5_pope.bash with the desired setting, then run the following bash scripts. We made this integrated script so that the execution process and the evaluation process are all included:

```bash
bash pipeline.bash
```

You will then get the POPE metrics for the experiment. You can also check the generated response in ./experiments/output.

### 7. Run Experiments for Generative Tasks under AMBER metric

Modify ./experiments/cd_scripts/llava1.5_pope.bash with the desired setting, then run:

```bash
cd ./experiments/cd_scripts
bash llava1.5_pope.bash
```

After that, you will see outputs at the designated path you set within llava1.5_pope.bash. To evaluate the responses using AMBER, run the following:

```bash
cd ./AMBER
python inference.py --inference_data path/to/your/inference/file --evaluation_type g
```








