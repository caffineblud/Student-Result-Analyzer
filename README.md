# 🎓 Student Result Analyzer

A Python-based application that analyzes student academic performance using **NumPy**, **Pandas**, **Matplotlib**, and a modern **Tkinter Dark GUI**.

## 📌 Features

* Load student data from a CSV file
* Calculate total marks
* Calculate percentage scores
* Assign grades automatically
* Display class statistics

  * Average Score
  * Highest Score
  * Lowest Score
* Identify the class topper
* Interactive Dark-Themed GUI
* Data visualization using Matplotlib

---

## 🛠 Technologies Used

* Python 3.x
* NumPy
* Pandas
* Matplotlib
* Tkinter

---

## 📂 Project Structure

```text
student_result_analyzer/
│
├── data/
│   └── students.csv
│
├── src/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── gui.py
│   └── visualization.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 📋 Sample CSV Format

```csv
Name,Math,Science,English
Alice,85,90,88
Bob,78,82,80
Charlie,92,88,95
David,65,70,68
Eva,89,91,87
```

---

## ⚙ Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd student_result_analyzer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Application

Run the following command from the project root directory:

```bash
python main.py
```

---

## 📊 Grade Criteria

| Percentage    | Grade |
| ------------- | ----- |
| 90% and above | A     |
| 75% - 89%     | B     |
| 60% - 74%     | C     |
| 40% - 59%     | D     |
| Below 40%     | F     |

---

## 📈 Analysis Performed

The application performs the following calculations:

### Total Marks

```python
Total = Math + Science + English
```

### Percentage

```python
Percentage = (Total / 300) * 100
```

### Statistics

* Average Percentage
* Highest Percentage
* Lowest Percentage
* Top Performer

---

## 🖥 GUI Features

* Dark Mode Interface
* CSV File Upload
* Analyze Results Button
* Student Results Table
* Statistics Dashboard
* Error Handling and Notifications

---

## 📸 Expected Output

After loading a CSV file and clicking Analyze:

* Student marks are displayed in a table.
* Total marks and percentages are calculated.
* Grades are assigned automatically.
* Class statistics are shown.
* Top-performing student can be identified.

---

## 🚀 Future Enhancements

* Export results to Excel
* Generate PDF reports
* Search and filter students
* Grade distribution charts
* Student ranking system
* Subject-wise analytics dashboard

---

## 👨‍💻 Author

***Yash Kumar Singh***
 Student Result Analyzer

---

## 📄 License

This project is developed for educational and learning purposes.
