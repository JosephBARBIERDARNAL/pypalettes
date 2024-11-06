import matplotlib.pyplot as plt
import numpy as np
import pypalettes
from pypalettes import add_cmap
import seaborn as sns
import pypalettes

plt.rcParams["figure.dpi"] = 300
plt.rcParams["savefig.dpi"] = 300

# plot 1
data = np.random.randn(20, 20)
plt.imshow(data, cmap="Sunset2_c")
plt.colorbar()
plt.savefig("images/heatmap.png")
plt.close()

# plot 2
df = sns.load_dataset("penguins")
g = sns.lmplot(
    data=df, x="bill_length_mm", y="bill_depth_mm", hue="species", palette="Fun"
)
g.set_axis_labels("Snoot length", "Snoot depth")
plt.savefig("images/scatter.png")
plt.close()

# plot 3
add_cmap(
    colors=["#D57A6DFF", "#E8B762FF", "#9CCDDFFF", "#525052FF"],
    name="myOwnCmap",
    cmap_type="continuous",
)

x = np.linspace(0, 20, 1000)
y = np.sin(x)
plt.scatter(x, y, c=y, cmap="myOwnCmap")
plt.colorbar()
plt.savefig("images/line.png")
plt.close()
