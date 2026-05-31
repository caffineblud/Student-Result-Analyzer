import matplotlib.pyplot as plt


def show_percentage_chart(df):
    plt.figure(figsize=(8, 5))

    plt.bar(
        df["Name"],
        df["Percentage"]
    )

    plt.title("Student Percentage Analysis")
    plt.xlabel("Students")
    plt.ylabel("Percentage")

    plt.show()