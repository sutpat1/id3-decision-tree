# Decision Tree Classifier

A Python implementation of a decision tree classifier that uses information gain to identify the most informative features and make predictions on categorical data.

## 🔍 Overview
This project implements a decision tree learning algorithm from scratch in Python. The classifier analyzes training data to identify patterns, builds a decision tree based on information gain, and uses the resulting model to predict outcomes for new data.

---

## 🚀 Features
- 📊 **Information Gain Calculation**: Uses entropy and information gain to find the most informative features.
- 🌲 **Tree Visualization**: Displays the generated decision tree in a human-readable format.
- 📈 **Model Evaluation**: Calculates and reports accuracy on both training and test data.
- 📊 **Multi-class Support**: Handles features with up to three distinct values (0, 1, and 2).
- 🔄 **Recursive Tree Building**: Creates optimal decision points through recursive partitioning.

---

## 🛠️ Tech Stack
- **Language**: Python
- **Dependencies**: math, sys (standard libraries)

---

## 📁 File Structure
<pre lang="markdown">
├── main.py                 # Core decision tree implementation
├── node.py                 # Node class for the tree structure
├── train.dat               # Training dataset
├── test.dat                # Test dataset
└── README.md               # Project documentation
</pre>

---

## 🚀 Getting Started

### Prerequisites
* Python 3.x

### Running the Classifier

1. Clone the repository

   `git clone https://github.com/yourusername/decision-tree-classifier.git`
   `cd decision-tree-classifier`

2. Run the classifier with training and test data

   `python main.py train.dat test.dat`

3. Review the output
   
   The program will:
   - Display the constructed decision tree
   - Report accuracy on the training set
   - Report accuracy on the test set

---

## 💻 Implementation Details

### Decision Tree Algorithm

The implementation follows these key steps:

1. **Feature Selection**:
   - Calculates entropy for each feature
   - Computes information gain for each potential decision point
   - Selects the feature with the highest information gain

2. **Tree Construction**:
   - Recursively builds the tree by splitting data on the most informative feature
   - Creates branches for each possible feature value (0, 1, 2)
   - Terminates recursion when data is homogeneous or no further splits are possible

3. **Prediction**:
   - Traverses the constructed tree for each data instance
   - Returns the class value at the leaf node

4. **Performance Evaluation**:
   - Computes accuracy on both training and test data
   - Reports results as a percentage

---

## 📊 Dataset Format

The datasets should be structured as follows:
- First line: Space-separated feature names
- Subsequent lines: Space-separated integer values (0, 1, or 2)
- The last column represents the target class

Example:

`feature1 feature2 feature3 class`
`0 1 0 1`
`1 0 1 0`
`2 1 0 1`

---

## 📋 Output Example

`feature3 = 0 : 1`
`feature3 = 1 :`
`| feature1 = 0 : 0`
`| feature1 = 1 : 1`
`| feature1 = 2 : 0`
`Accuracy on training set (800 instances): 85.5%`
`Accuracy on test set (200 instances): 83.2%`

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👥 Contributors

- Sharv Utpat
