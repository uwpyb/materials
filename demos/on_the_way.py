# comes with Anaconda/Python
import os
import pandas as pd
import sys

# need to be installed separately
import googlemaps
import tqdm

# need to register with Google to get an API key: https://developers.google.com/maps/documentation/distance-matrix/start
secret_api_key = os.environ.get('GMAPS_API_KEY', '')
gmaps = googlemaps.Client(key=secret_api_key)

# get info from the user
filename = input('Please enter a CSV spreadsheet with a column named "address": ')
spreadsheet = pd.read_csv(filename)

home_addr = input('Please enter your home address: ')
work_addr = input('Please enter your work address: ')

def distance_between(from_addr, to_addr):
    data = gmaps.distance_matrix([from_addr], [to_addr])
    dist = data['rows'][0]['elements'][0]['distance']['value']

    return dist

# build a list of distance from home/work to each place
distances_from_home = []
distances_from_work = []

for addr in tqdm.tqdm(spreadsheet['address'].values):
    distances_from_home.append(distance_between(home_addr, addr))
    distances_from_work.append(distance_between(work_addr, addr))

# copy the lists into table
spreadsheet['distance from home'] = distances_from_home
spreadsheet['distance from work'] = distances_from_work

# add a column for the combined distance
spreadsheet['combined distance'] = spreadsheet['distance from home'] + spreadsheet['distance from work']

# sort by lowest combined distance
spreadsheet = spreadsheet.sort_values('combined distance')

# save the result
out_filename = filename[:-4] + '_sorted.csv'
spreadsheet.to_csv(out_filename, index=False)

print('Done! Please see', out_filename, 'for the results.')
