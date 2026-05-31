import pandas as pd
import numpy as np


class StudentResultAnalyzer:

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def calculate_total(self):
        self.df["Total"] = (
            self.df["Math"] +
            self.df["Science"] +
            self.df["English"]
        )

    def calculate_percentage(self):
        self.df["Percentage"] = (
            self.df["Total"] / 300
        ) * 100

    def assign_grade(self):
        conditions = [
            self.df["Percentage"] >= 90,
            self.df["Percentage"] >= 75,
            self.df["Percentage"] >= 60,
            self.df["Percentage"] >= 40
        ]

        grades = ["A", "B", "C", "D"]

        self.df["Grade"] = np.select(
            conditions,
            grades,
            default="F"
        )

    def class_statistics(self):
        return {
            "Average Score": self.df["Percentage"].mean(),
            "Highest Score": self.df["Percentage"].max(),
            "Lowest Score": self.df["Percentage"].min()
        }

    def topper(self):
        return self.df.loc[
            self.df["Percentage"].idxmax()
        ]

    def process(self):
        self.calculate_total()
        self.calculate_percentage()
        self.assign_grade()

        return self.df