# Sample Files Generator

Generate sample files of type `png`, `exe`, `mp3`, `pdf`, `txt`, and `zip`. These sample files can be useful for software testing such as when testing ransomware.

### Dependencies

* Requires the `/usr/share/dict/words` file which is provided by the `wordlist` package.

### Usage

```
./sample_files_generator.py -h
usage: sample_files_generator.py [-h] [-d] [-m MAX] destination number_of_files

Generate sample files.

positional arguments:
  destination        where to generate the sample files.
  number_of_files    how many test files to generate.

optional arguments:
  -h, --help         show this help message and exit
  -d, --dir          create directories.
  -m MAX, --max MAX  set the max size in kilobytes for each file.
```

### Usage Examples

Generate 2000 sample files:

```
./sample_files_generator.py /home/gforeman/ransomware_sim/samplefiles/ 2000
```

Generate 2000 sample files with a random directory structure and file sizes under 5 MB:

```
./sample_files_generator.py --max 5000 -d /home/gforeman/ransomware_sim/samplefiles/ 2000 
```
