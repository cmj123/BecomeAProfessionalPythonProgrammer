# Import key libraries, function and classes
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

def main():
    fig = plt.figure(figsize=(10,5))
    ax = fig.add_subplot(1,1,1, projection=ccrs.Robinson())

    # make the map global rather than have it zoom in to
    # the extent of any plotted data

    ax.set_global()
    #
    ax.stock_img()
    ax.coastlines()

    ax.plot(-0.08, 51.53, 'o', transform=ccrs.PlateCarree(),color='red')
    # ax.plot([-0.08, 132],[51.53, 43.17], transform=ccrs.PlateCarree())

    plt.show()

if __name__ == '__main__':
    main()
