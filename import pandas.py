import pandas as pd

def show_module_version(module_name, version):
    print(f"The version of {module_name} is {version}")

if __name__ == "__main__":
    try:
        pandas_version = pd.__version__
        show_module_version("Pandas", pandas_version)
    except ImportError:
        print("Pandas is not installed.")


