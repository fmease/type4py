# Type4Py: Deep Similarity Learning-Based Type Inference for Python
This repository contains the implementation of Type4Py and instructions for re-producing the results of the paper.

- [Dataset](#dataset)
- [Installation Guide](#installation-guide)
- [Usage Guide](#usage-guide)
- [VSCode Extension](#vscode-extension)
- [Citing Type4Py](#citing-type4py)

# Dataset
For Type4Py, we use the **ManyTypes4Py** dataset. You can download the latest version of the dataset [here](https://zenodo.org/record/4719447).
Also, note that the dataset is already de-duplicated.

# Installation Guide
## Requirements
- Linux-based OS
- Python 3.5 or newer
- An NVIDIA GPU with CUDA support

## Quick Install
```
git clone https://github.com/saltudelft/type4py.git && cd type4py
pip install .
```

# Usage Guide
Follow the below steps to train and evaluate the Type4Py model.
## 1. Extraction
**NOTE:** Skip this step if you're using the ManyTypes4Py dataset.
```
$ type4py extract --c $DATA_PATH --o $OUTPUT_DIR --d $DUP_FILES --w $CORES
```
Description:
- `$DATA_PATH`: The path to the Python corpus or dataset.
- `$OUTPUT_DIR`: The path to store processed projects.
- `$DUP_FILES`: The path to the duplicate files. [Optional]
- `$CORES`: Number of CPU cores to use for processing projects.

## 2. Preprocessing
```
$ type4py preprocess --o $OUTPUT_DIR --l $LIMIT
```
Description:
- `$OUTPUT_DIR`: The path that was used in the first step to store processed projects. For the MT4Py dataset, use the directory in which the dataset is extracted.
- `$LIMIT`: The number of projects to be processed. [Optional]

## 3. Vectorizing
```
$ type4py vectorize --o $OUTPUT_DIR
```
Description:
- `$OUTPUT_DIR`: The path that was used in the previous step to store processed projects.

## 4. Learning
```
$ type4py learn --o $OUTPUT_DIR --c --p $PARAM_FILE
```
Description:
- `$OUTPUT_DIR`: The path that was used in the previous step to store processed projects.
- `--c`: Trains the complete model. Use `type4py learn -h` to see other configurations.

- `--p $PARAM_FILE`: The path to user-provided hyper-parameters for the model. See [this](https://github.com/saltudelft/type4py/blob/main/type4py/model_params.json) file as an example. [Optional]

## 5. Testing
```
$ type4py predict --o $OUTPUT_DIR --c
```

Description:
- `$OUTPUT_DIR`: The path that was used in the first step to store processed projects.
- `--c`: Predicts using the complete model. Use `type4py predict -h` to see other configurations.

## 6. Evaluating
```
$ type4py eval --o $OUTPUT_DIR --c --tp 10
```

Description:
- `$OUTPUT_DIR`: The path that was used in the first step to store processed projects.
- `--c`: Evaluates the complete model. Use `type4py eval -h` to see other configurations.
- `--tp 10`: Considers Top-10 predictions for evaluation. For this argument, You can choose a positive integer between 1 and 10. [Optional]

# VSCode Extension
Type4Py can be used in VSCode, which provides ML-based type auto-completion for Python files. The Type4Py's VSCode extension can be installed from the VS Marketplace [here](https://marketplace.visualstudio.com/items?itemName=saltud.type4py).

# Citing Type4Py

```
@article{mir2021type4py,
  title={Type4Py: Deep Similarity Learning-Based Type Inference for Python},
  author={Mir, Amir M and Latoskinas, Evaldas and Proksch, Sebastian and Gousios, Georgios},
  journal={arXiv preprint arXiv:2101.04470},
  year={2021}
}
```