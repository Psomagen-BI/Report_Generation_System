# Report Generation System
## Structure of configuration file
The structure can be found on [this website](https://docs.google.com/document/d/1ZALgdN2HO0FHXR_JpvImAxa6Pl5FnVQKeMt6BZz7nRI/edit).

The keys marked with “<>“ are subject to change depending on a type of a report or information and files needed for a report.
Other keys are fixed.

## Usage
python3 make_report.py "REPORT TYPE"

The body of a report is generated in order of paths in "Contents" key in configuration file.

This version supports "xlsx", "png", "jpg", "jpeg", and "gif", "txt" files.

For xlsx file, a table should be started from A1 index.

To generate text, please use "txt" file extension.

To generate images, please use "png", "jpg", or "jpeg" file extension.

<<<<<<< HEAD
To generate table, please use "xlsx" file extension.
=======
To generate table, please use "xlsx" file extension.
>>>>>>> 73cdb43042d7b52392c6bfe77c8a72cf13293bc8
