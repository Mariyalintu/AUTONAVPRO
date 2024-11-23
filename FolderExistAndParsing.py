import os

#PackageParsing Class contains Checking the particular fragment name,
#xml_name and utilclass name existing in the given folder and
#Packages and imports are parsing from the particular Folder for fragments and utilclasses

class PackageParsing:
    def __init__(self):
        print("PackageParsing instance created.")

    # Check if the fragment file already exists in the specified folder
    def file_exists(self, output_folder, adapter_name):
        file_path = os.path.join(output_folder, f"{adapter_name}")
        return os.path.exists(file_path)

    #parsing package name from folder
    def package_name_parsing(self, folder_path):
        folder_path = folder_path.replace('\\', '/')
        package_part = folder_path.split("/java/")[-1]
        package_name = package_part.replace('/', '.')
        return package_name

    #parsing import_package  from package_name
    def import_package_R(self, package_name):
        import_package = '.'.join(package_name.split('.')[:-1])
        import_package = import_package + ".R"
        return import_package
