import cx_Freeze

executables = [cx_Freeze.Executable(
    script='Crash.py', icon='assets/CrashIco.ico')]

cx_Freeze.setup(
    name='Crash',
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["assets"]
                           }},
    executables = executables
)