# Sample Files Generator

Generate sample files of type `exe`, `mp3`, `pdf`, `txt`, and `zip`. These sample files can be useful for software testing such as testing ransomware.

### Usage

```
./sample_files_generator.py --help
usage: sample_files_generator.py [-h] [-d] [--max {128,256,512,1024,2048,4096,8192,16384,32768,65536}] destination number_of_files

Generate test files.

positional arguments:
  destination           where to generate the test files.
  number_of_files       how many test files to generate.

optional arguments:
  -h, --help            show this help message and exit
  -d, --dir             create directories.
  --max {128,256,512,1024,2048,4096,8192,16384,32768,65536}
                        set the max size in bytes for each file.
```

### Usage Examples

Generate 2000 test files:

```
./sample_files_generator.py /home/gforeman/ransomware_sim/testfiles/ 2000
```

Generate 2000 test files with directories and varied file sizes under 2048 bytes:

```
./sample_files_generator.py /home/gforeman/ransomware_sim/testfiles/ 2000 --max 2048 -d
```
