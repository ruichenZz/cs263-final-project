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
conda create -yn vcd python=3.9
conda activate vcd
cd VCD
pip install -r requirements.txt
```