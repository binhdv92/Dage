# Convert the Dage Nordson Format (DNF) to the table format project

# info:
this repo used python programming language to compose a small software to intent to convert multiple dage nordson csv files to a single table format file.

# requirement to run this repo:
- >\>= python3.x

# How to use this repo:
the tree folder have organized as below:
root
  PULL_1.csv
  PULL_2.csv
  ...
  SHEAR_1.csv
  SHEAR_2.csv
  SHEAR_xxx.csv
  ...
  
Step1:clone this repo by typing below command on git command prompt
> $ git clone https://github.com/binhdv92/dage_convert.git"=

Step2: open cmd command prompt and navigate to the root project folder and typing the below command
> $ python DAGE_FORMAT_CONVERT_TO_TABLE_REV02.py --path "." --outfile "final_pull_shear.csv"

# Result:
Output file will be is "final_pull_shear.csv"
|FILE_NAME	|DATE	|TIME	|ENTITY	|IPN_CARTRIDGE	|TYPE_FORCE	|WIRE_ID	|FORCE|
| --- | --- | --- | --- | --- | --- | --- | --- |
|PULL_1.csv	|"10/09/19"	|"16:50:08"	|"KWB278"	|"20035517"	|"Wire Pull"	|1	|8.7069|
|PULL_1.csv	|"10/09/19"	|"16:50:08"	|"KWB278"	|"20035517"	|"Wire Pull"	|2	|9.4995|

# Convert *.py file to *.exe file
1. install pyinstaller
> $ pip install PyInstaller
2. use below command to convert to exe file
> pyinstaller /path/to/yourscript.py
# Thanks
