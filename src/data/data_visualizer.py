import matplotlib.pyplot as plt
import seaborn as sns

def plot_temperature(df):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='timestamp', y='temperature', data=df)
    plt.title('Temperature Over Time')
    plt.show()