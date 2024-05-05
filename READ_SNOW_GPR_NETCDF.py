from netCDF4 import Dataset

def print_point_attributes(ncfile, index):
    print("Point Number:", ncfile.variables['point_number'][index])
    print("Pick Number:", ncfile.variables['pick_number'][index])
    print("Response Time:", ncfile.variables['response_time'][index])
    print("Layer Thickness:", ncfile.variables['layer_thickness'][index])
    print("Bottom Altitude:", ncfile.variables['bottom_altitude'][index])
    print("File Name:", ncfile.variables['file_name'][index])
    print("X UTM:", ncfile.variables['x_utm'][index])
    print("Y UTM:", ncfile.variables['y_utm'][index])
    print("Top Altitude:", ncfile.variables['top_altitude'][index])
    if 'pick_series_number' in ncfile.variables:
        print("Pick Series Number:", ncfile.variables['pick_series_number'][index])

def test_netcdf_file(file_path):
    ncfile = Dataset(file_path, 'r')

    num_points = len(ncfile.dimensions['point'])
    for i in range(num_points):
        print("\nPoint", i+1)
        print_point_attributes(ncfile, i)

    ncfile.close()

test_netcdf_file('SNOW_GPR_DATA_RAW_2024.nc')
