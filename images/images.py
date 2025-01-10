import matplotlib.pyplot as plt
import numpy as np
from pypalettes import add_cmap
import seaborn as sns
from pypalettes import load_cmap

plt.rcParams["figure.dpi"] = 300
plt.rcParams["savefig.dpi"] = 300

# plot 1
import matplotlib.pyplot as plt
from pypalettes import load_cmap
import numpy as np

cmap = load_cmap("Sunset2", cmap_type="continuous")

data = np.random.randn(20, 20)

plt.imshow(data, cmap=cmap)
plt.colorbar()
plt.savefig("images/heatmap.png")
plt.close()

# plot 2
cmap = load_cmap("Fun")
palette = cmap.colors
df = sns.load_dataset("penguins")

g = sns.lmplot(
    data=df, x="bill_length_mm", y="bill_depth_mm", hue="species", palette=palette
)
g.set_axis_labels("Snoot length", "Snoot depth")
plt.savefig("images/scatter.png")
plt.close()

# plot 3
import matplotlib.pyplot as plt
from pypalettes import add_cmap
import numpy as np

cmap = add_cmap(
    colors=["#D57A6DFF", "#E8B762FF", "#9CCDDFFF", "#525052FF"],
    name="myCmap",
    cmap_type="continuous",
)

x = np.linspace(0, 20, 1000)
y = np.sin(x)

plt.scatter(x, y, c=y, cmap=cmap)
plt.colorbar()
plt.savefig("images/line.png")
plt.close()
