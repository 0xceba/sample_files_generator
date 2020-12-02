# Sample Files Generator

Generate sample files of type `png`, `exe`, `mp3`, `pdf`, `txt`, and `zip`. These sample files can be useful for software testing such as when testing ransomware.

### Dependencies

* Requires the `/usr/share/dict/words` file which is provided by the `wordlist` package.

### Usage

```
# python3 sample_files_generator.py -h
usage: sample_files_generator.py [-h] [-d] [-m MAX] destination number_of_files

Generate sample files.

positional arguments:
  destination        where to generate the sample files.
  number_of_files    how many sample files to generate.

optional arguments:
  -h, --help         show this help message and exit
  -d, --dir          create directories.
  -m MAX, --max MAX  set the max size in kilobytes for each file.
```

### Usage Examples

Generate 200 sample files:
```
# python3 sample_files_generator.py ./samplefiles/ 200
Sample files created successfully.

# ls --time-style=+ -lh ./samplefiles/ | head 
total 816K
drwxr-xr-x 2 root root  12K  .
drwxr-xr-x 5 root root 4.0K  ..
-rw-r--r-- 1 root root  130  adjectives.pdf
-rw-r--r-- 1 root root   72  agglomerations.mp3
-rw-r--r-- 1 root root   64  arbitrarinesss.exe
-rw-r--r-- 1 root root    1  assiduousnesss.txt
-rw-r--r-- 1 root root   22  assort.zip
-rw-r--r-- 1 root root   64  asymmetry.exe
-rw-r--r-- 1 root root   64  backbiter.exe
```

Generate 200 sample files with a random directory structure and file sizes under 5 MB:
```
# python3 sample_files_generator.py -d --max 5000 ./samplefiles/ 200
Sample files created successfully.

# ls --time-style=+ -lh ./samplefiles/ | head 
total 77M
drwxr-xr-x 5 root root  4.0K  .
drwxr-xr-x 5 root root  4.0K  ..
-rw-r--r-- 1 root root  2.4M  abstinences.png
-rw-r--r-- 1 root root  4.2M  barmaid.pdf
-rw-r--r-- 1 root root 1014K  berliners.mp3
-rw-r--r-- 1 root root  1.1M  cannoning.exe
-rw-r--r-- 1 root root  283K  climaxed.pdf
-rw-r--r-- 1 root root  739K  coiffuring.txt
drwxr-xr-x 3 root root  4.0K  curlinesss
```

### Adding Additional File Types

Add a file with the desired extension to `./template_files/` to generate files of additional file types. The new file could be an empty text document with the appropriate file extension (ie: `touch /template_files/rar.rar`) or it could be a syntactically valid file. The template files that are shipped with this script come from https://github.com/mathiasbynens/small.