# openEO Platform User Oriented Example Notebooks

<img src="https://raw.githubusercontent.com/openEOPlatform/SRR1_notebooks/main/data/images/openEO-platform.png"
     alt="OpenEO Platform logo"
     />

This repository contains Python Jupyter Notebooks and R Notebooks, showing interactive examples of Earth Observation tasks using openEO Platform.

## Become an Early Adopter

**Important: You need to be an early adopter to run the code provided here, please follow this link for the instructions: https://openeo.cloud/early-adopters/**

**After becoming an Early Adopter, please use the forum https://discuss.eodc.eu/t to ask us any question related to the usage of the platform.**
## Python
### openEO Platform Jupyter Hub

You can run the Jupyter Notebooks in the openEO Platform Jupyter Hub instance accessible here: https://lab.openeo.cloud/

If you have any issue, please let us know on the forum (if you also don't have access to the forum, feel free to open a GitHub issue here!).

### Local Installation Instructions
Alternatively, you can run them locally (please note: the Anaconda Python enviornment has been tested on Linux Ubuntu 18.04, on Windows please use in step 3 the runtime optimized trimmed version `environment_windows.yml`):

1. Install Anaconda to manage virtual environments. You can follow the instructions [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
2. Clone the repository and get into the repo folder:
 ```
        git clone https://github.com/openEOPlatform/sample-notebooks.git
        cd sample-notebooks
```
3. Create a new conda environment with the following command:
```
        conda env create -f environment.yml
        conda env create -f environment_windows.yml (use this line on Windows)
```
4. Once the process is complete, you can activate the environment:
```
        conda activate openeo_platform
```
5. Now you can start the Jupyter Notebook Server and use the notebooks, just typing:
```
        jupyter notebook
```
6. This should open up a new window in your default web browser, where you can select the notebook you prefer.
