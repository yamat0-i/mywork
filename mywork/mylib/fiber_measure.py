import numpy as np
import matplotlib.pyplot as plt


def measure(date_dir_path, date):
    fname = '{}\\{}_FiberDiameter.txt'.format(date_dir_path, date)

    D = np.loadtxt(fname, delimiter=',',  skiprows=3)

    X = D[:,0]  # Absolute position
    y1 = D[:,1]  # Upper edge of fiber
    y2 = D[:,2]  # Lower edge of fiber

    diameter = y2 - y1

    diameter_min = np.nanmin(diameter)
    diameter_min_index = np.argmin(diameter)
    X_min = X[diameter_min_index]
    print('\n(Result)')
    print('X:', X_min, ',', 'diameter:', diameter_min)
    print('\nNow plotting...')

    plt.figure()
    plt.plot(X, diameter)

    plt.xlabel('X absolute position')
    plt.ylabel('diameter[px]')
    plt.title('FiberDiameter_{}'.format(date))

    print('Finished.')

    plt.show(block=False)
