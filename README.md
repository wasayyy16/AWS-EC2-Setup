# Cloud MLOps Infrastructure Assignment

This project implements an automated Machine Learning environment on AWS EC2. It features persistent storage (EBS), secure S3 integration via IAM roles, automated environment bootstrapping, and a scheduled training pipeline with auto-shutdown capabilities.

## Infrastructure Configuration

| Component | Specification |
| :--- | :--- |
| **EC2 Instance Type** | t3.micro (Ubuntu 24.04 LTS) |
| **S3 Bucket Name** | assignment11|
| **IAM Role Name** | wasay|
| **EBS Volume** | 11 GB (gp2/gp3) mounted at `/mnt/ml-data` |
| **Python Version** | 3.12 (via Virtualenv) |

---

## Execution Steps

### 1. Storage Setup (EBS Persistence)
*Connect to the instance and configure the additional EBS volume.*

```bash
# Verify attached volume (e.g., xvdf or nvme1n1)
lsblk

# Format volume (ext4)
sudo mkfs -t ext4 /dev/xvdf

# Create mount point and mount
sudo mkdir -p /mnt/ml-data
sudo mount /dev/xvdf /mnt/ml-data
sudo chown -R ubuntu:ubuntu /mnt/ml-data

# Configure auto-mount (Persistence)
# Get UUID
sudo blkid
# Add to /etc/fstab: UUID=YOUR_UUID_HERE /mnt/ml-data ext4 defaults,nofail 0 2

# Create directory structure
mkdir -p /mnt/ml-data/{datasets,features,models,logs}

# Install AWS CLI v2
curl "[https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip](https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip)" -o "awscliv2.zip"
sudo apt install unzip -y
unzip awscliv2.zip
sudo ./aws/install

# Configure (Region only, leave keys blank)
aws configure

# Sync datasets (S3 -> EC2)
aws s3 sync s3://[INSERT YOUR BUCKET NAME HERE] /mnt/ml-data/datasets/

# Make script executable
chmod +x setup_ml_env.sh

# Run setup
./setup_ml_env.sh

# Activate virtual environment
source /mnt/ml-data/venv/bin/activate

# Navigate to data directory
cd /mnt/ml-data

# MLOps Assignment 1 — Training Pipeline and Reproducible Experiments

Lightweight MLOps project containing a reproducible training pipeline, environment setup script, and example experiments used for coursework and demonstrations.

## What this project contains

- `train.py` — example training script and experiment entrypoint.
- `ml_setup_env.sh` — environment and dependency setup helper.
- `screenshots/` — visual outputs and result snapshots.
- `README.md`, `.gitignore`, and `LICENSE` — project metadata and policies.

## Quickstart

1. Create a Python virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies (if you maintain a `requirements.txt`):

```bash
pip install -r requirements.txt || echo "No requirements.txt found; install dependencies manually"
```

3. Run the training example:

```bash
python3 train.py
```

4. Use the included `ml_setup_env.sh` to help provision a local environment (inspect before running):

```bash
bash ml_setup_env.sh
```

## Development notes

- The `train.py` script is intentionally simple for assignment purposes — replace or extend dataset loading, model definition, and hyperparameters to match your experiments.
- Keep experimental outputs in `outputs/` or `runs/` (ignored by `.gitignore`) rather than committing large artifacts.

## Suggested `.gitignore` patterns

Add common Python and environment ignores to avoid committing large or sensitive files (a `.gitignore` is provided).

## License

This project is released under the MIT License. See `LICENSE` for details.

## Contact

Maintainer: Abdul Wasay
Email: (add your email or GitHub profile link)
