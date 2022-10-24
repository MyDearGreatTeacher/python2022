import matplotlib.pyplot as plt
activities = ["work", "sleep", "Internet", "others"]
hours = [8, 7, 2, 7]
colors = ["lightgreen", "lightblue", "yellow", "pink"]
plt.pie(hours, labels = activities, colors = colors, shadow = True, explode = (0, 0, 0.1, 0), autopct = "%1.1f%%")
plt.axis("equal")
plt.show()
