# CSIRO - Image2Biomass Prediction
Predict biomass using the provided pasture images


## Overview
Build models that predict pasture biomass from images, ground-truth measurements, and publicly available datasets. Farmers will use these models to determine when and how to graze their livestock.

Competition Host
CSIRO

Prizes & Awards
$75,000



Tags
- Biology
- Agriculture
- R2 Score

## Description
Farmers often walk into a paddock and ask one question: “Is there enough grass here for the herd?” It sounds simple, but the answer is anything but. Pasture biomass - the amount of feed available - shapes when animals can graze, when fields need a break, and how to keep pastures productive season after season.

Estimate incorrectly, and the land suffers; feed goes to waste, and animals struggle. Get it right and everyone wins: better animal welfare, more consistent production, and healthier soils.

Current methods make this assessment more challenging than it could be. The old-school “clip and weigh” method is accurate but slow and impossible at scale. Plate meters and capacitance meters can provide quicker readings, but are unreliable in variable conditions. Remote sensing enables broad-scale monitoring, but it still requires manual validation and can’t separate biomass by species.

This competition challenges you to bring greener solutions to the field: build a model that predicts pasture biomass from images, ground-truth measures, and publicly available datasets. You’ll work with a professionally annotated dataset covering Australian pastures across different seasons, regions, and species mixes, along with NDVI values to enhance your models.

If you succeed, you won’t just improve estimation methods. You’ll help farmers make smarter grazing choices, enable researchers to track pasture health more accurately, and drive the agriculture industry toward more sustainable and productive systems.

## Evaluation
Scoring
The model performance is evaluated using a weighted average of $R^{2}$ scores across the five output dimensions. The final score is calculated as:

```math
\text{Final Score} = \sum_{i=1}^{5} (w_{i} \times R^{2}_{i})
```
Where:

The term 
 represents the coefficient of determination for dimension 
The weights 
 used are as follows:
- Dry_Green_g: 0.1
- Dry_Dead_g: 0.1
- nDry_Clover_g: 0.1
- GDM_g: 0.2
- Dry_Total_g: 0.5

## $R^{2}$ Calculation
For each target, the coefficient of determination $R^{2}$ is:

```math
R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}}
```

Residual Sum of Squares $SS_{\text{res}}$

Measures the total error of the model’s predictions:

```math
SS_{\text{res}} = \sum_{j} (y_j - \hat{y}_j)^2
```


Total Sum of Squares $SS_{\text{tot}}$

Measures the total variance in the data:

```math
SS_{\text{tot}} = \sum_{j} (y_j - \bar{y})^2
```

Terms

- $y_j$: ground-truth value for data point $j$
- $\hat{y}_j$: model prediction for data point $j$
- $\bar{y}$: mean of all ground-truth values

## Submission File
Submit a CSV in long format with exactly two columns:

- sample_id : ID constructed from image ID and target_name pair.
- target: Your predicted biomass value (grams) for that sample_id (float).

The valid target names are: Dry_Green_g, Dry_Dead_g, Dry_Clover_g, GDM_g, Dry_Total_g.

Your file must contain one row per (image, target) pair, i.e., 5 rows for each image in the test set.

Header and example:

```csv
sample_id,target
ID1001187975__Dry_Green_g,0.0
ID1001187975__Dry_Dead_g,0.0
ID1001187975__Dry_Clover_g,0.0
ID1001187975__GDM_g,0.0
ID1001187975__Dry_Total_g,0.0
ID1001187976__Dry_Green_g,0.0
ID1001187976__Dry_Dead_g,0.0
ID1001187976__Dry_Clover_g,0.0
ID1001187976__GDM_g,0.0
ID1001187976__Dry_Total_g,0.0
```

## Acknowledgements

Particular thanks given to our partner the Meat & Livestock Australia (MLA) for the images provided on the competition page. MLA is the declared industry marketing body and the industry research body for the Australian red meat industry. MLA’s mission is to collaborate with stakeholders to invest in research, development and marketing initiatives that contribute to producer profitability, sustainability and global competitiveness. 

This work has also been supported by FrontierSI (previously known as the Cooperative Research Centre for Spatial Information)

## About CSIRO


The Commonwealth Scientific and Industrial Research Organization (CSIRO) is Australia’s national science agency that is responsible for scientific research and its commercial and industrial applications.

At CSIRO, we solve the greatest challenges through innovative science and technology to unlock a better future for everyone. We are thinkers, problem solvers, leaders. We blaze new trails of discovery. We aim to inspire the next generation.

Working with industry, government, universities and research organisations we turn big ideas into disruptive solutions. Turning science into solutions for food security and quality; clean energy and resources; health and wellbeing; resilient and valuable environments; innovative industries; and a secure Australia and region.

## Citation
Qiyu Liao, Dadong Wang, Rhys Pirie, Joshua Whelan, Rebecca Haling, Jiajun Liu, Rizwan Khokher, Xun Li, Martyna Plomecka, and Addison Howard. CSIRO - Image2Biomass Prediction. https://kaggle.com/competitions/csiro-biomass, 2025. Kaggle.

---

