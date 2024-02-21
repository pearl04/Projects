import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Creating a DataFrame from the dummy data
df = pd.DataFrame(data)

def auto_visualize(df, column):
    plt.figure(figsize=(10, 6))
    ax = sns.countplot(x=column, data=df)
    plt.title('Employee Distribution by Department')
    plt.xticks(rotation=45)
    plt.xlabel('Department')
    plt.ylabel('Number of Employees')

    # Adding values on top of each bar
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', 
                    (p.get_x() + p.get_width() /
                     2., p.get_height()),
                    ha='center', va='center', 
                    fontsize=10, 
                    color='black', xytext=(0, 5),
                    textcoords='offset points')

    plt.show()

# Usage
auto_visualize(df, 'Department')
