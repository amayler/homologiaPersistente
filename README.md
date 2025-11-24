# Homologia Persistente
# Supplementary Code: Homología Persistente

This repository contains the code and resources to reproduce the analysis and results from a research tittled **Homogía Persistente** published in **Journal of Basic Sciences**. Two examples are presented of how the Python **Ripser library** is used to calculate Persistent Homology. 
To use Ripser, it is necessary to have Python installed on our computer. Ripser allows calculating the persistent homology of datasets and visualizing persistence diagrams. Originally, the Ripser library was designed to be used in the C programming language, so before installing Ripser, it is necessary to install the Cython library. See **Local Installation** below.

## Contents

*   `notebook_1/0_generadores_1ra_rev.ipynb`: [Breve descripción de lo que hace este notebook, e.g., "Data preprocessing and exploratory analysis"].
*   `notebook_2/1_generadores_1ra_rev.ipynb`: [Breve descripción, e.g., "Training and evaluation of the predictive model"].

## Quick Start in Google Colab

To run the code without any local setup, click the **Open in Colab** badge below for each notebook:

| Notebook | Description | Colab |
|----------|-------------|-------|
| `analisis_datos.ipynb` | Data Preprocessing | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1WLvM9PmGrOfetJXFaarbOeeMJuBmejrD?usp=sharing) |
| `modelo_entrenamiento.ipynb` | Model Training | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1WLvM9PmGrOfetJXFaarbOeeMJuBmejrD?usp=sharing) |


## Local Installation

If you wish to run the code locally, follow these steps:

1.  Clone this repository:
    ```bash
    git clone https://github.com/amayler/Homolog-a_Persistente.git
    ```
2.  Navigate to the project directory.
3.  We recommend creating a virtual environment.
4.  Install the dependencies:
    ```bash
    # Using pip install the Cython library.
    pip install Cython

    # Using pip to install Ripser
    pip install Ripser

    # Using pip to install Persim
    pip install persim
    
5.  Launch Jupyter Notebook or Jupyter Lab:
    ```bash
    jupyter lab
    ```

## Requirements

The main Python packages required are:
- numpy :: Biblioteca fundamental para computación numérica con soporte de arrays multidimensionales y funciones matemáticas. 
- ripser :: Biblioteca para el cálculo eficiente de homología persistente (topología computacional) a partir de datos.
- persim :: Herramientas para visualización, comparación y análisis de diagramas de persistencia generados por Ripser. 

 
## Data

*The data used in this study are generated in running time by the programs. The data set is created randomly and processed by the program.*


## Citation

If you use this code in your research, please cite our article:
> [cite: ]

## Contact

For any questions regarding the code, please open an issue in this repository or contact [jremigio@ujat.mx].
