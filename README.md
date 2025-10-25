# 🛳️ Titanic Disaster Survival Analysis

This repository contains Python and R scripts that clean, wrangle, and create a logistic regression model on the famous Kaggle **Titanic dataset** to predict passenger survival.  It demonstrates end-to-end data analysis and modeling in two languages, each with its own Docker environment. Both scripts output csv files containing the predictions that the logistic regression model makes on the test data. 

---

## 🧰 Requirements

You need **Docker** installed on your machine.  
If not installed yet, follow instructions from [Get Docker](https://docs.docker.com/get-docker/).

No local R or Python setup is needed — everything runs inside containers.

--- 

## 💾 Step 1: Clone the repo onto your machine

---

## 📊 Step 2: Download the dataset

The dataset comes from [Kaggle’s Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic).

### Download Instructions
1. Go to the Kaggle Titanic page above.
2. Scroll down and click **Download All** to get `train.csv` and `test.csv`.
3. Create a data folder under the src folder in the cloned repo on your machine.
4. Save the downloaded datasets in the data folder.

---

## 🧑‍💻 Step 3: Running the repo

As mentioned above, this repo can be run entirely inside **Docker** containers. There are two Docker files, one for Python and one for R. Clone the GitHub repo onto your Desktop and open the files in your preferred text editor. See below for how to build and run the Docker containers for each language in your preferred text editor.

---

## 🐍 Running the Python Script

### A. Build the Docker image

```bash
docker build -f Dockerfile-python -t titanic-python .
```

### B. Build the Docker image

```bash
docker run --rm -it titanic-python
```
---

## 🧮 Running the R Script

### A. Build the Docker image

```bash
docker build -f Dockerfile-r -t titanic-r .
```

### B. Build the Docker image

```bash
docker run --rm -it titanic-r
```

