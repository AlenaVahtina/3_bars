import json


def load_from_json(filepath):
    with open(filepath, 'r') as data:
        return json.load(data)


def get_biggest_bar(data):
    pass


def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
	try:
    		latitude = float(input('Enter latitude:  '))
	except ValueError:
    		latitude = None

	if latitude is None:
    		print('Sorry, there are no data!')

	try:
    		longitude = float(input('Enter longitude: '))
	except ValueError:
    		latitude = None

	if longitude is None:
    		print('Sorry, there are no data!')



if __name__ == '__main__':
	data = load_from_json('bar.json')
	print(data)
	get_biggest_bar(data)
	get_smallest_bar(data)
	get_closest_bar(data, 0, 0)


    
