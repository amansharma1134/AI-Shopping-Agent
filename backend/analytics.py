import pandas as pd
import matplotlib.pyplot as plt

def plot_user_interest():
    logs = pd.read_csv("data/user_logs.csv")
    logs["category_clicked"].value_counts().plot(kind="bar")
    plt.title("User Interest by Category")
    plt.show()