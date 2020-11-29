#!/usr/bin/env python3

'''
* Requires the words file (provided by the wordlist package) to be located at /usr/share/dict/words
* To add additional file extensions add a template file to ./template_files/ 
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
	max_size = max_size * 1024

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

def get_file_extensions():
	extension_list = []
	template_directory = "./template_files/"

	for template_filename in os.listdir(template_directory):
		if template_filename.endswith("README.md"):
			continue
		else:
			template_file_path = os.path.join(template_directory, template_filename)
			extension = os.path.splitext(template_file_path)[1][1:]
			extension_list.append(extension)

	return extension_list

def main(argv):
	parser = argparse.ArgumentParser(description='Generate sample files.')
	parser.add_argument('destination', help='where to generate the sample files.', type=dir_path)
	parser.add_argument('number_of_files', help='how many test files to generate.', type=int)
	parser.add_argument('-d', '--dir', help='create directories.', action="store_true")
	parser.add_argument('-m', '--max', help='set the max size in kilobytes for each file.', type=int)
	args = parser.parse_args()

	file_destination = args.destination
	dir_list = [args.destination]

	file_extensions = get_file_extensions()
	words = open_dictionary("/usr/share/dict/words")

	for x in range(0, args.number_of_files):
		filename = random.choice(words).replace("'", "").lower()
		file_type = random.choice(file_extensions)

		if args.dir and x % 13 == 0:
			dir_list = create_directory(dir_list, filename)
			filename = random.choice(words).replace("'", "").lower()

		new_file = create_file(file_type, get_dir_destination(dir_list), filename, args.max)
	print('Test files created successfully.')

if __name__ == "__main__":
   main(sys.argv[1:])