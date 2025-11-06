# AOA Project 1 — Greedy and Divide & Conquer Approaches

**Authors:** Ahmed Rageeb Ahsan, Saiful Islam
**Date:** November 6, 2025
**Course:** Analysis of Algorithms — Project 1
**Instructor:** Alin Dobra

---

## 📘 Overview

This repository contains two algorithmic projects developed for the Analysis of Algorithms course.
Both problems demonstrate advanced applications of algorithm design paradigms — **Divide and Conquer** and **Greedy / Graph Optimization** — in real scientific and medical data contexts.

---

## 🧠 Project 1: Merging Brain Activity Maps using Divide-and-Conquer (Pointwise Maximum Merge)

### Abstract

We present a divide-and-conquer method to fuse multiple overlapping brain activity recordings (EEG/fMRI activation maps) into a single activation contour by computing the pointwise maximum across sensors.
This approach includes:

* A formal problem abstraction
* The recursive algorithm design and pseudocode
* Three complementary correctness proofs
* Tight runtime and optimality analysis
* Numerical and I/O policy details
* Synthetic data verification and usage of the Kaggle EEG dataset

The method demonstrates how algorithmic thinking can efficiently combine spatial neuroimaging data with provable correctness and reproducibility.

---

## 🧩 Project 2: Maximum Probability Disease Progression Path via Log-Transformed Shortest Path

### Abstract

This work addresses the problem of identifying the most probable disease progression path originating from personal habits (e.g., smoking, medication intake) through intermediate health states to diseases in a probabilistic disease progression graph.
By applying a **negative logarithmic transformation**, the problem of maximizing cumulative path probability becomes a **shortest path problem**, efficiently solvable via **Dijkstra’s algorithm**.

The project covers:

* Graph modeling of probabilistic health transitions
* Transformation from multiplicative probabilities to additive weights
* Correctness and runtime proofs
* Domain interpretation and real-world clinical validation

---

### 4. Run Disease Progression Shortest Path

```bash
python greedy_shortest_path/disease_progression.py --graph datasets/disease_graph.csv --source Smoking
```

---

## 📊 Datasets

* **EEG/fMRI Dataset:** Adapted from Kaggle EEG Brainwave Datasets
  [https://www.kaggle.com/datasets/amananandrai/complete-eeg-dataset?resource=download](https://www.kaggle.com/datasets/amananandrai/complete-eeg-dataset?resource=download)
  
  (See LaTeX Appendix B for detailed usage and instructions.)

* **Disease Graph Dataset:** Generated or anonymized clinical progression graphs used for probabilistic pathfinding.
[https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset?select=cardio_train.csv]([https://www.kaggle.com/datasets](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset?select=cardio_train.csv))
---

## 📁 Repository Structure

```
AOA_Project1/
│
├── divide_conquer/                # Divide-and-Conquer implementation
├── greedy_shortest_path/          # Log-transformed Dijkstra implementation
├── reports/
│   ├── D&C.pdf
│   ├── GREEDY.pdf
│   └── Project1_Final.pdf
├── requirements.txt
└── README.md
```

---

## 🔗 External Resources

* **Google Drive Folder (Code + Data):**
  [[https://drive.google.com/drive/folders/1z4sT0gWIyU-71sdMK3_u90aOcTGhf54Q?usp=sharing](drive link)

---

## 🧩 Authors

* **Ahmed Rageeb Ahsan**
* **Saiful Islam**

*Department of Computer Science*
*University of Florida*
*Fall 2025*
