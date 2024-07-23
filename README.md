# MAZRAM Obfuscation

![Screenshot 2024-07-23 174610](https://github.com/user-attachments/assets/67e1765c-5fee-4bec-a463-d1b1418feba8)

MAZRAM Obfuscation is not meant to gaurantee 100% code protection, there are other ways to reverse engineer pythons applications.
This will still make it a challenge for many to reverse engineer.


## How it works
The Mazram obfuscator will take your python file, obfuscate it using zlib, then it will cythonzie it, then run it through pyinstaller
to build an exe file that would make it harder for someone to reverse engineer.

## Setup
Open terminal and run these commands.
```
git clone https://github.com/tr4xnz/mazram
cd mazram
pip install -r requirments.txt
python main.py
```

## Usage
![Screenshot 2024-07-23 174653](https://github.com/user-attachments/assets/4acc25f3-b2bd-45ff-adde-11e59aa42f12)

Enter path of your python file when prompted, if there are modules your code needs to run then create a requirements.txt with listed modules and enter the path of the 
requirements.txt when prompted, if your project doesn't need any modules, leave it blank.

When finished your built exe file will show up in a directory called dist.
