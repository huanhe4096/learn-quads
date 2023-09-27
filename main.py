#%% import libs
import random
import quads
from tqdm import tqdm
from matplotlib import pyplot as plt

print('* loaded packages!')

#%% build tree
tree = quads.QuadTree(
    (0, 0),
    100,
    100
)

n = 1000
X = []
Y = []
for i in tqdm(range(n)):
    x = (0.5 - random.random()) * 100
    y = (0.5 - random.random()) * 100
    X.append(x)
    Y.append(y)
    tree.insert((x, y), {
        "idx": i,
        "uid": '%s'%random.random()
    })
print('* built quadtree with %s points' % (n))

# %% test tree
def find_points_within_r(cx, cy, r):
    pc = quads.Point(cx, cy)
    bb = quads.BoundingBox(min_x=cx-r, min_y=cy-r, max_x=cx+r, max_y=cy+r)
    points = tree.within_bb(bb)
    points_within_r = []
    for p in points:
        d = quads.euclidean_distance(pc, p)
        if d <= r:
            points_within_r.append(p)
    return points_within_r

# %% visualize
cx, cy, r = -10, -10, 20
ps = find_points_within_r(cx, cy, r)
Xr = [ p.x for p in ps ]
Yr = [ p.y for p in ps ]

fig, ax = plt.subplots()
plt.plot(X, Y, 'y.')
plt.plot(Xr, Yr, '.', c='b')
plt.plot([cx], [cy], 'r.')
circle = plt.Circle((cx, cy), r)
ax.add_artist(circle)
ax.set_aspect(1)
ax.text(cx+r, cy, '%sp' % (len(ps)), va='center')
