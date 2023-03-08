import matplotlib.pyplot as pylot

def generate_pie_chart():
    labels = ["a", "b", "c"]
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels)
    plt.savefig("pie.png")
    plt.close()