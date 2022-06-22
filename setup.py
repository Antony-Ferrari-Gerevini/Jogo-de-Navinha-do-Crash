import sys
from cx_Freeze import setup, Executable

build_exe_options = {'packages': ['os']}

executables = [Executable(script='Crash.py', icon='assets/crashIco.ico')]

setup(
    name='Crash',
    version = '1.1',
    #description = 'Registro de jogadores implementado',    
    options={"build_exe": {"packages": ["pygame"],
                               "include_files": ["assets"]}},
    executables = executables
)


#python setup.py build              (vai gerar uma pasta com o executável dentro)
#python setup.py bdist_msi          (vai gerar um instalador de Windows)