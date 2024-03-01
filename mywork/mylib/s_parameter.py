import numpy as np
import matplotlib.pyplot as plt

def load_and_plot_Sparam(date_dir_path, date):
    """Plot S-parameters.
    """
    print('Now plotting...')  # CLI
    # Load data
    D1 = np.loadtxt(
        '{}\\{}_5x.txt'.format(date_dir_path, date), 
        delimiter=',',  skiprows=3
        )
    D2 = np.loadtxt(
        '{}\\{}_10x.txt'.format(date_dir_path, date), 
        delimiter=',',  skiprows=3
        )
    D3 = np.loadtxt(
        '{}\\{}_40x.txt'.format(date_dir_path, date), 
        delimiter=',',  skiprows=3
        )
    
    # ndarray set
    s1_5x = D1[:,0]
    s2_5x = D1[:,1]
    s3_5x = D1[:,2]

    s1_10x = D2[:,0]
    s2_10x = D2[:,1]
    s3_10x = D2[:,2]

    s1_40x = D3[:,0]
    s2_40x = D3[:,1]
    s3_40x = D3[:,2]

    step = np.arange(10, 1, -1)

    # Plot
    fig = plt.figure()

    plt.subplots_adjust(hspace=0.3)

    ax1 = fig.add_subplot(3, 1, 1)
    ax1.invert_xaxis()
    ax1.plot(step, s1_5x, color='green', label='5x')
    ax1.plot(step, s1_10x, color='blue', label='10x')
    ax1.plot(step, s1_40x, color='red', label='40x')
    ax1.set_ylim(-0.2, 0.7)
    # ax1.set_xlabel('Step size [deg]', fontsize=18)
    ax1.set_ylabel('s1', fontsize=18)
    ax1.legend(loc=(0.1, 0.1))

    ax2 = fig.add_subplot(3, 1, 2)
    ax2.invert_xaxis()
    ax2.plot(step, s2_5x, color='green', label='5x')
    ax2.plot(step, s2_10x, color='blue', label='10x')
    ax2.plot(step, s2_40x, color='red', label='40x')
    ax2.set_ylim(0.2, 1.1)
    # ax2.set_xlabel('Step size [deg]', fontsize=18)
    ax2.set_ylabel('s2', fontsize=18)
    ax2.legend(loc=(0.1, 0.1))

    ax3 = fig.add_subplot(3, 1, 3)
    ax3.invert_xaxis()
    ax3.plot(step, s3_5x, color='green', label='5x')
    ax3.plot(step, s3_10x, color='blue', label='10x')
    ax3.plot(step, s3_40x, color='red', label='40x')
    ax3.set_ylim(-0.3, 0.6)
    ax3.set_xlabel('Step size [deg]', fontsize=18)
    ax3.set_ylabel('s3', fontsize=18)
    ax3.legend(loc=(0.1, 0.1))

    ax1.set_title('Stokes Parameter', fontsize=18)

    print('Finished.')  # CLI

    plt.show(block=False)

if __name__ == '__main__':
    load_and_plot_Sparam('C:\\code\\py311\\venv\\mywork\\mywork\\data\\s-parameter\\20230501', '20230501')
