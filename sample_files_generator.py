#!/usr/bin/env python3

'''
* Requires the words file (provided by the wordlist package) located at /usr/share/dict/words
* To add file extensions:
	a) add additional extension to file_extensions list
	b) add a template file for each new extension to ./template_files/ 
'''

import os, sys, argparse, random
from shutil import copyfile

# from https://www.it-swarm.dev/es/python/ruta-un-directorio-como-argumento-argparse/827150818/
def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f'{path} is not a valid path')

def create_directory(dir_list, filename):
	new_directory_path = get_dir_destination(dir_list) + '/' + filename
	os.mkdir(new_directory_path)
	dir_list.append(new_directory_path)
	return dir_list

def create_file(file_type, file_location, filename, max_size):
	source_file = 'template_files/'  + file_type + '.' + file_type
	destination_file = file_location + '/' + filename + '.' + file_type
	copyfile(source_file, destination_file)
	if(max_size):
		grow_file(destination_file, max_size)

def grow_file(destination_file, max_size):
	current_size = os.stat(destination_file).st_size
	potential_bytes_to_add = max_size - current_size
	num_of_bytes_to_add = random.randint(0,potential_bytes_to_add)
	null_byte_array = bytearray(b'\x00') * num_of_bytes_to_add

	file = open(destination_file, 'ab')
	file.write(null_byte_array)
	file.close()

def get_dir_destination(dir_list):
	return random.choice(dir_list)

def open_dictionary(word_file):
	try:
		return open(word_file).read().splitlines()
	except OSError:
		print("Could not open/read file: " + word_file)
		sys.exit()

def main(argv):
	try:
		parser = argparse.ArgumentParser(description='Generate test files.')
		parser.add_argument('destination', help='where to generate the test files.', type=dir_path)
		parser.add_argument('number_of_files', help='how many test files to generate.', type=int)
		parser.add_argument('-d', '--dir', help='create directories.', action="store_true")
		parser.add_argument('--max', help='set the max size in bytes for each file.', type=int, choices=[128,256,512,1024,2048,4096,8192,16384,32768,65536])
		args = parser.parse_args()

		file_destination = args.destination
		dir_list = [args.destination]

		file_extensions = ['txt','pdf','mp3','zip','exe']
		words = open_dictionary("/usr/share/dict/words")

		for x in range(0, args.number_of_files):
			filename = random.choice(words).replace("'", "").lower()
			file_type = random.choice(file_extensions)

			if args.dir and x % 13 == 0:
				dir_list = create_directory(dir_list, filename)
				filename = random.choice(words).replace("'", "").lower()

			new_file = create_file(file_type, get_dir_destination(dir_list), filename, args.max)
		print('Test files created successfully.')
	except Exception as ex:
		print('Exception: ' + ex)

if __name__ == "__main__":
   main(sys.argv[1:])