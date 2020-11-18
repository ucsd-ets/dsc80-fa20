
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


plt.style.use('seaborn-white')   # seaborn custom plot style
plt.rc('figure', dpi=100, figsize=(7, 5))   # set default size/resolution
plt.rc('font', size=12)   # font size


def plot_eval_scatter(data, preds, actual, xcol):

    eval_data = (
        pd.concat(
            [data[xcol].rename(xcol), actual, preds.rename('prediction')],
            axis=1
        ).set_index(xcol)
        .unstack()
        .rename(actual.name)
        .reset_index()
        .rename(columns={'level_0': 'type'})
    )

    sns.scatterplot(
        data=eval_data,
        x=xcol, y=actual.name,
        hue='type',
        alpha=0.7
    )

    return


def plot3Dscatter(data, xcol, ycol, mdl, actual):

    # plot the plane of best fit
    # not as useful as one would like!

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    x_surf = np.arange(data[xcol].min() - 1, data[xcol].max() + 1)
    y_surf = np.arange(data[ycol].min() - 1, data[ycol].max() + 1)
    #x_surf = np.arange(50, 80, 5)                # generate a mesh
    #y_surf = np.arange(50, 80, 5)
    x_surf, y_surf = np.meshgrid(x_surf, y_surf)

    zgrid = pd.core.frame.DataFrame(
        {xcol: x_surf.ravel(), ycol: y_surf.ravel()}
    )

    out = mdl.predict(zgrid)

    ax.plot_surface(x_surf, y_surf,
                    out.reshape(x_surf.shape),
                    rstride=1,
                    cstride=1,
                    color='None',
                    alpha=0.4)

    ax.scatter(data[xcol], data[ycol], actual,
               c='blue',
               marker='o',
               alpha=0.7)

    ax.set_xlabel(xcol)
    ax.set_ylabel(ycol)
    ax.set_zlabel('child')

    plt.show()
