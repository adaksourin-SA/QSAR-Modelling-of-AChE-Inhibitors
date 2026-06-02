# Knowledge Base

# Computational Drug Discovery using QSAR and Machine Learning

---

# 1. Project Overview

This project demonstrates an end-to-end **Computational Drug Discovery** workflow using **Quantitative Structure–Activity Relationship (QSAR)** modeling.

The objective is to build a machine learning model capable of predicting the biological activity of chemical compounds against a target protein, **Acetylcholinesterase (AChE)**, using molecular descriptors and fingerprints.

The workflow consists of:

1. Retrieving bioactivity data from ChEMBL.
2. Cleaning and preprocessing the dataset.
3. Calculating molecular descriptors.
4. Converting biological activity values into a machine-learning friendly format.
5. Generating molecular fingerprints.
6. Feature selection.
7. Building regression models.
8. Optimizing the best model.
9. Deploying the model as a predictive application.

---

# 2. What is Drug Discovery?

Drug discovery is the process of identifying chemical compounds that can interact with biological targets and potentially become medicines.

Traditional drug discovery involves:

- Target identification
- Compound screening
- Lead optimization
- Preclinical testing
- Clinical trials

This process is extremely expensive and may take more than 10 years.

Computational approaches help reduce:

- Time
- Cost
- Experimental effort

by predicting promising compounds before laboratory testing.

---

# 3. What is Bioinformatics?

**Bioinformatics** is an interdisciplinary field combining:

- Biology
- Computer Science
- Statistics
- Mathematics

to analyze biological data.

Applications include:

- Genomics
- Proteomics
- Drug Discovery
- Molecular Modeling
- Systems Biology

---

# 4. What is Computational Drug Discovery?

Computational Drug Discovery uses algorithms, statistics, and machine learning to predict how molecules behave biologically.

Major applications include:

- Virtual Screening
- QSAR Modeling
- Molecular Docking
- Molecular Dynamics
- ADMET Prediction

The present project focuses on **QSAR Modeling**.

---

# 5. What is QSAR?

## Full Form

**QSAR = Quantitative Structure–Activity Relationship**

QSAR assumes that:

> Molecules with similar structures tend to exhibit similar biological activities.

The goal is to establish a mathematical relationship between:

- Molecular structure
- Biological activity

General representation:

```math
Activity = f(Descriptors)
```

where descriptors numerically represent molecular properties.

---

# 6. Target Protein: Acetylcholinesterase

## Full Form

**AChE = Acetylcholinesterase**

Acetylcholinesterase is an enzyme responsible for breaking down the neurotransmitter **Acetylcholine**.

Reaction:

```math
Acetylcholine + H_2O \rightarrow Choline + Acetate
```

## Importance

In Alzheimer's disease:

- Acetylcholine levels decrease.
- Memory and cognitive functions deteriorate.

By inhibiting AChE:

- Acetylcholine remains available longer.
- Cognitive symptoms may improve.

Therefore, AChE inhibitors are important therapeutic candidates.

Examples:

- Donepezil
- Rivastigmine
- Galantamine

---

# 7. ChEMBL Database

## What is ChEMBL?

ChEMBL is a manually curated bioactivity database maintained by EMBL-EBI.

It contains:

- Bioactive molecules
- Drug-like compounds
- Assay information
- Target information
- Experimental bioactivity values

## Why ChEMBL?

It provides:

- High-quality experimental data
- Standardized activity measurements
- Drug-target interaction information

making it ideal for QSAR studies.

---

# 8. Important ChEMBL Terminology

## Target

A biological entity against which compounds are tested.

Examples:

- Proteins
- Enzymes
- Receptors

In this project:

**Acetylcholinesterase**

### Assay

An experimental procedure used to measure biological activity.

Examples:

- Enzyme inhibition assay
- Cell viability assay

### Bioactivity

A measurable biological response produced by a compound.

Examples:

- IC50
- EC50
- Ki
- Kd

---

# 9. Molecular Representation

Computers cannot directly understand chemical structures.

Therefore molecules must be represented numerically.

## SMILES

### Full Form

**SMILES = Simplified Molecular Input Line Entry System**

A text-based representation of molecules.

Example:

```text
CCO
```

(Ethanol)

Advantages:

- Human readable
- Machine readable
- Compact

---

# 10. Molecular Descriptors

Descriptors are numerical values describing chemical structures.

They transform molecules into numbers that machine learning algorithms can understand.

## Why are descriptors needed?

Machine learning algorithms require numerical input.

Chemical structures must therefore be converted into measurable properties.

---

# 11. Lipinski Descriptors

The project calculates several descriptors derived from Lipinski's Rule of Five.

## Molecular Weight (MW)

### Definition

Mass of one molecule.

### Unit

- Dalton (Da)
- g/mol

### Importance

Larger molecules generally:

- Diffuse more slowly
- Have poorer absorption

---

## LogP

### Definition

Partition coefficient between:

- Octanol
- Water

```math
LogP = \log_{10}
\left(
\frac{Concentration_{octanol}}
{Concentration_{water}}
\right)
```

### Interpretation

High LogP:

- More hydrophobic

Low LogP:

- More hydrophilic

---

## Hydrogen Bond Donors (HBD)

Atoms capable of donating hydrogen atoms.

Examples:

- OH
- NH

---

## Hydrogen Bond Acceptors (HBA)

Atoms capable of accepting hydrogen bonds.

Examples:

- Oxygen
- Nitrogen

---

# 12. Lipinski's Rule of Five

Proposed by Christopher Lipinski.

Guidelines suggesting good oral drug-likeness:

| Property | Rule |
|-----------|--------|
| Molecular Weight | ≤ 500 |
| LogP | ≤ 5 |
| HBD | ≤ 5 |
| HBA | ≤ 10 |

---

# 13. Bioactivity Measurements

## IC50

### Full Form

**Half Maximal Inhibitory Concentration**

Concentration required to inhibit 50% of biological activity.

### Common Units

| Unit | Value |
|--------|--------|
| M | \(10^0\) M |
| mM | \(10^{-3}\) M |
| μM | \(10^{-6}\) M |
| nM | \(10^{-9}\) M |
| pM | \(10^{-12}\) M |

### Interpretation

Lower IC50 means higher potency.

---

# 14. Why Convert IC50 to pIC50?

Raw IC50 values span several orders of magnitude.

Machine learning models generally perform better with transformed data.

## Definition

```math
pIC50 = -\log_{10}(IC50)
```

where IC50 is expressed in molar concentration.

### Interpretation

Higher pIC50 = More potent compound

| IC50 | pIC50 |
|--------|--------|
| 1 nM | 9 |
| 10 nM | 8 |
| 100 nM | 7 |

---

# 15. Molecular Fingerprints

Fingerprints convert molecular structures into binary vectors.

Example:

```text
[1,0,1,0,0,1,...]
```

Each bit indicates presence or absence of a structural feature.

## Why use fingerprints?

- Numerical representation
- Structural information
- Fast computation
- Suitable for machine learning

---

# 16. PubChem Fingerprints

This project uses **PubChem Fingerprints**.

These encode:

- Functional groups
- Ring systems
- Atomic environments
- Structural fragments

Each bit answers:

> Does this structural feature exist?

Yes → 1

No → 0

---

# 17. PaDEL Descriptor

## Full Form

**PaDEL = Pharmaceutical Data Exploration Laboratory**

PaDEL Descriptor is software used to calculate:

- Molecular descriptors
- Molecular fingerprints

from SMILES strings.

## Why use PaDEL?

- Thousands of descriptors
- Standardized calculations
- Free and widely used
- Supports PubChem fingerprints

---

# 18. Feature Selection

Not every descriptor contributes useful information.

Many features have little or no variation.

## Variance

Variance measures spread in data.

```math
Variance = \frac{\sum (x-\bar{x})^2}{N}
```

### Low Variance Features

Example:

```text
1
1
1
1
1
```

Variance = 0

Such features provide little information and are removed.

### Benefits

- Faster training
- Less overfitting
- Lower memory usage
- Better generalization

---

# 19. Machine Learning Task

The project predicts pIC50 values.

Since pIC50 is continuous, this is a:

## Regression Problem

### Classification vs Regression

Classification:

```text
Active / Inactive
```

Regression:

```text
pIC50 = 7.45
```

---

# 20. Training and Testing Sets

Datasets are split into:

- Training Set
- Testing Set

Common split:

- 80% Training
- 20% Testing

### Purpose

Training Set:

- Learn patterns

Testing Set:

- Evaluate performance on unseen data

---

# 21. Random Forest Regression

Random Forest is an ensemble learning algorithm.

It combines predictions from multiple decision trees.

### Advantages

- Handles nonlinear relationships
- Robust to noise
- Reduces overfitting
- Performs well on QSAR data

---

# 22. Hyperparameter Tuning

Hyperparameters are settings chosen before training.

Examples:

- Number of trees
- Tree depth
- Minimum samples per split

## Grid Search

Grid Search systematically evaluates multiple combinations to find the best configuration.

---

# 23. Model Evaluation Metrics

## R² Score

Coefficient of Determination.

Measures how much variance is explained by the model.

Range:

```text
(-∞, 1]
```

Perfect model:

```text
R² = 1
```

---

## MAE

Mean Absolute Error

```math
MAE=\frac{1}{N}\sum |y-\hat y|
```

Lower is better.

---

## MSE

Mean Squared Error

```math
MSE=\frac{1}{N}\sum (y-\hat y)^2
```

Lower is better.

---

## RMSE

Root Mean Squared Error

```math
RMSE=\sqrt{MSE}
```

Lower is better.

---

# 24. Why Machine Learning Helps Drug Discovery

Machine learning can:

- Screen millions of molecules rapidly
- Reduce experimental costs
- Prioritize promising candidates
- Accelerate lead optimization

---

# 25. End-to-End Workflow Summary

```text
ChEMBL Database
       │
       ▼
Retrieve Bioactivity Data
       │
       ▼
Data Cleaning
       │
       ▼
SMILES Structures
       │
       ▼
Descriptor Calculation
       │
       ▼
IC50 → pIC50 Conversion
       │
       ▼
PubChem Fingerprints
       │
       ▼
Feature Selection
       │
       ▼
Train/Test Split
       │
       ▼
Machine Learning Models
       │
       ▼
Hyperparameter Optimization
       │
       ▼
Final QSAR Model
       │
       ▼
Predict Activity of New Molecules
```

---

# 26. Key Full Forms

| Abbreviation | Full Form |
|-------------|------------|
| QSAR | Quantitative Structure–Activity Relationship |
| AChE | Acetylcholinesterase |
| SMILES | Simplified Molecular Input Line Entry System |
| IC50 | Half Maximal Inhibitory Concentration |
| pIC50 | Negative Logarithm of IC50 |
| MW | Molecular Weight |
| LogP | Octanol-Water Partition Coefficient |
| HBD | Hydrogen Bond Donor |
| HBA | Hydrogen Bond Acceptor |
| ML | Machine Learning |
| MAE | Mean Absolute Error |
| MSE | Mean Squared Error |
| RMSE | Root Mean Squared Error |
| R² | Coefficient of Determination |
| PaDEL | Pharmaceutical Data Exploration Laboratory |

---

# 27. Final Takeaway

This project demonstrates how experimental bioactivity data from ChEMBL can be transformed into molecular descriptors and fingerprints, enabling machine learning models to learn structure–activity relationships. The final QSAR model predicts the inhibitory activity (pIC50) of compounds against Acetylcholinesterase, helping accelerate early-stage drug discovery through computational methods.