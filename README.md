# 🧪 Lab 2 – Non-Generalising Machine Intelligence: Pichu vs Pikachu Classifier

Welcome to Ann Mathenge’s Lab 2 assignment for _Icke-Generaliserande Maskinintelligens_!  
This lab demonstrates a classic machine learning technique, k-nearest neighbours (k-NN), applied to a very serious and scientific problem: is your Pokemon a Pichu or a Pikachu?

---

## 📚 About the Assignment

The goal of the lab was to:

- Read and process two datasets: training data with known labels and test data without labels
- Implement a nearest neighbour classifier (k=1)
- Extend the classifier to k-nearest neighbours (default k=10)
- Allow manual classification of new points
- Plot training data
- Randomly split data into training and test sets
- Evaluate and visualise the accuracy of the classifier

---

## 📁 File Structure

- `lab2.py` – Main program file with all functions and logic
- `data/datapoints.txt` – Training data: (width, height, label)
- `data/testpoints.txt` – Test points (width, height)

---

## 🚀 Features & Functionality

### 🧠 Classifiers

- ✅ Nearest Neighbour (k=1) – Finds the closest point in the training data
- ✅ k-Nearest Neighbours (default k=10) – Classifies based on the majority label among k closest points

### 🧪 Modes

- Option 1: Run the 1-NN classifier on predefined test points
- Option 2: Manually input Pokemon dimensions (width & height) to classify using 1-NN
- Option 3: Do the same as above, but using k-NN (k=10)
- Option 4: Plot the training data (Pichus vs Pikachus)
- Option 5: Randomly split the dataset into 50/50 training, 25/25 test, run classification 10 times, and plot accuracies

### 📈 Bonus: Accuracy Evaluation

- Accuracy over 10 randomized runs is calculated and plotted
- True positives, false positives, true negatives, and false negatives are tracked

---

## 🧪 Example Output

```
...
Pikachu predicted, actual Pikachu: 21
Pichu predicted, actual Pichu: 25
Pikachu predicted, actual Pichu: 0
Pichu predicted, actual Pikachu: 4
Run 10: 92.00%

Average accuracy over 10 runs is 96.20%
```

## ⚙️ Tech & Tools

- Python
- `matplotlib` for plotting
- `math` for Euclidean distance
- `random` for shuffling datasets
- `re` for cleaning input with regex
