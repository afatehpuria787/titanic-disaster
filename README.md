# 🛳️ Titanic Disaster Survival Analysis

This repository contains Python and R scripts that clean, wrangle, and create a logistic regression model on the famous Kaggle **Titanic dataset** to predict passenger survival.  It demonstrates end-to-end data analysis and modeling in two languages, each with its own Docker environment.

---

## 📊 Dataset

The dataset comes from [Kaggle’s Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic).

### Download Instructions
1. Go to the Kaggle Titanic competition page.
2. Scroll down and click **Download All** to get `train.csv` and `test.csv`.
3. Place both files in:

---

## 🧰 Requirements

You need **Docker** installed on your machine.  
If not installed yet, follow instructions from: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

No local R or Python setup is needed — everything runs inside containers.

---

## 🧑‍💻 Running the repo

As mentioned above, this repo can be run entirely inside **Docker** containers. There are two Docker files, one for Python and one for R. See below for how to build and run the Docker containes for each language.

---

## 🐍 Running the Python Script

```bash
docker build -f Dockerfile-python -t titanic-python .
```

### 2. Build the Docker image

```bash
docker run --rm -it titanic-python
```
---

## 🧮 Running the R Script

### 1. Build the Docker image
From the project root directory:

```bash
docker build -f Dockerfile-r -t titanic-r .
```

### 2. Build the Docker image

```bash
docker run --rm -it titanic-r
```

