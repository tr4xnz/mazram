# ----------------------------------------------------------------------------------- #
# Mazram Obfuscator                                                                   #
# Author: AK                                                                          # 
# Date: 7/23/24                                                                       #
# Version: 1.0                                                                        #
#                                                                                     #
# Created to protect your source code                                                 #
# 100% protection is not garaunteed as it's my first time making something like this. #
# ----------------------------------------------------------------------------------- #

import os
import zlib
import base64
from Cython.Build import cythonize
from distutils.core import setup
from distutils.extension import Extension
import subprocess
import colorama
print(colorama.Fore.MAGENTA+"""

___  ___                                _____ _      __                     _             
|  \/  |                               |  _  | |    / _|                   | |            
| .  . | __ _ _____ __ __ _ _ __ ___   | | | | |__ | |_ _   _ ___  ___ __ _| |_ ___  _ __ 
| |\/| |/ _` |_  / '__/ _` | '_ ` _ \  | | | | '_ \|  _| | | / __|/ __/ _` | __/ _ \| '__|
| |  | | (_| |/ /| | | (_| | | | | | | \ \_/ / |_) | | | |_| \__ \ (_| (_| | || (_) | |   
\_|  |_/\__,_/___|_|  \__,_|_| |_| |_|  \___/|_.__/|_|  \__,_|___/\___\__,_|\__\___/|_|   
                                                                                          
""")
print(colorama.Fore.MAGENTA+"Created by AK")
print("")
print(colorama.Fore.YELLOW+"""
DISCLAIMER: THIS TOOL WAS CREATED TO OBFUSCATE PYTHON CODE TO MAKE IT HARDER FOR PEOPLE TO REVERSE ENGINEER AND EXTRACT SOURCE CODE FOR YOUR PROGRAMS. 
            THIS IS NO WAY MEANT TO BE USED MALICIOUSLY AND THIS IS NOT GARAUNTEED TO PROTECT YOUR CODE A 100%.
      
      """)
def obfuscate_and_compile():
    file_path = input(colorama.Fore.LIGHTCYAN_EX+"Enter path to python file: ")
    if file_path.endswith('.py'): pass
    else: print(colorama.Fore.RED+"[ERROR]: Invalid fily type, only support python files")
    print("")
    requirements_file = input(colorama.Fore.LIGHTGREEN_EX+"Please provide the path to your requirements.txt file (leave blank to skip): ")
    with open(file_path, 'r') as file:
        code = file.read()
    compressed_code = zlib.compress(code.encode('utf-8'))

    encoded_code = base64.b64encode(compressed_code).decode('utf-8')

    temp_file_path = file_path.replace('.py', '_obfuscated.py')
    with open(temp_file_path, 'w') as temp_file:
        temp_file.write(f"""
import zlib
import base64

encoded_code = '{encoded_code}'

# Decode and decompress the code
compressed_code = base64.b64decode(encoded_code)
original_code = zlib.decompress(compressed_code).decode('utf-8')

# Execute the original code
exec(original_code)
""")

    extensions = [Extension(temp_file_path.replace('.py', ''), [temp_file_path])]
    setup(
        ext_modules=cythonize(extensions, compiler_directives={'language_level': '3'}),
        script_args=['build_ext', '--inplace']
    )

    run_script_path = 'build.py'
    module_name = temp_file_path.replace('.py', '')
    with open(run_script_path, 'w') as run_script:
        run_script.write(f"""
import importlib

# Import the compiled module
module_name = '{module_name}'
compiled_module = importlib.import_module(module_name)

# Execute the module's main function if it exists
if hasattr(compiled_module, 'main'):
    compiled_module.main()
""")

    

    hidden_imports = ['zlib', 'base64', 'Cython', 'importlib']
    if requirements_file:
        with open(requirements_file, 'r') as req_file:
            for line in req_file:
                package = line.strip()
                if package:
                    hidden_imports.append(package)

    hidden_imports_args = []
    for hidden_import in hidden_imports:
        hidden_imports_args.extend(['--hidden-import', hidden_import])

    subprocess.run(['pyinstaller', '--onefile', '--add-data', f'{module_name}.cp310-win_amd64.pyd;.', *hidden_imports_args, run_script_path])

    os.remove(temp_file_path)
    os.remove(run_script_path)
    build_dir = 'build'
    dist_dir = 'dist'
    spec_file = run_script_path.replace('.py', '.spec')

try:
    obfuscate_and_compile()
    print(colorama.Fore.CYAN+f"It looks like your executable was successfully created navigate to {os.getcwd()}/dist to see your executable.")
    print(colorama.Fore.CYAN+"Executable might take a while to run")
except:
    pass