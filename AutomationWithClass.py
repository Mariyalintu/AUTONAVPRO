import os
import xml.etree.ElementTree as ET

from UtilsClassContent import UtilClass
from FragmentxmlClassContent import XmlClasses
from FragmentContent import Fragments
from FragmentContentWithoutAdapter import FragmentsWithoutAdapter
from FolderExistAndParsing import PackageParsing
from ActivityContent import Activity
from ActivityContentwithoutFragment import ActivityWithoutFragment
from ActivityXml import XmlActivity
from RecyclerAdapterContent import AdapterContent
from RecyclerAdapterXmlContent import AdapterXmlClasses
from ViewModelContent import ViewModelContent
from DataClassContent import DataClassContent
from ActivityTestContent import ActivityTest
from FragmentTestContent import FragmentTest
from AdapterTestContent import AdapterTest
from ViewmodelTestContent import ViewmodelTest
from HelperClassTestContent import HelperClassTest

# FragmentAutomation Class Creating fragments and the corresponding xmlfiles,
# Creating Util Classes with Same fragment name.
#creating Activity and corresponding xmlfiles
#Adapter and viewmodel also creating according to user input
class FragmentAutomation:
    def __init__(self, text_file_path, project_path, folder_path, xml_file_folder, test_file_folder, util_class_folder, output_folder, activity_path, viewmodel_path,data_path,imagebutton, imagebutton_type,  textview, textview_type, textview1, textview1_type):
        self.text_file_path = text_file_path
        self.folder_path = folder_path
        self.project_path = project_path
        self.xml_file_folder = xml_file_folder
        self.util_class_folder = util_class_folder
        self.activity_path = activity_path
        self.output_folder = output_folder
        self.test_file_folder = test_file_folder
        self.viewmodel_path = viewmodel_path
        self.data_path = data_path
        self.imagebutton = imagebutton
        self.textview = textview
        self.textview1= textview1
        self.imagebutton_type = imagebutton_type
        self.textview_type = textview_type
        self.textview1_type= textview1_type
        
        # Instantiate AnotherClasses
        self.activity = Activity()
        self.xmlActivity = XmlActivity()
        self.fragments = Fragments()
        self.xmlClasses = XmlClasses()
        self.utilClass = UtilClass()
        self.packageParsing = PackageParsing()
        self.adapterContent = AdapterContent()
        self.adapterXml = AdapterXmlClasses()
        self.viewModelContent = ViewModelContent()
        self.dataClassContent = DataClassContent()
        self.activityContent = ActivityWithoutFragment()
        self.fragmentContent = FragmentsWithoutAdapter()
        self.Actvitytest = ActivityTest()
        self.Fragmenttest = FragmentTest()
        self.Adaptertest = AdapterTest()
        self.viewmodeltest = ViewmodelTest()
        self.helperclasstest = HelperClassTest()

    # Open the text file in read mode ('r'),
    # Read the entire content of the text file etract class names
    def read_from_text(self):
            with open(self.text_file_path, 'r') as file:
            # Read lines from the file
                lines = file.readlines()

            # Initialize lists to store names of fragments and activities
            adapter_available = 'no'
            fragments = []
            activities = []
            adapters = []
            # utils = []
            # dataclasses = []

            # Parse the content of the text file
            for line in lines[1:]:
                parts = line.strip().split('\t')  # Split the line by tab
                if len(parts) < 4:
                    continue  # Skip lines with insufficient parts
                name = parts[0].strip()  # Extract the name
                activity = parts[1].strip().lower()  # Extract the fragment value and convert to lowercase
                fragment = parts[2].strip().lower()  # Extract the activity value and convert to lowercase
                adapter =  parts[3].strip().lower()  # Extract the adapter value and convert to lowercase
                # adapter =  parts[4].strip().lower()  # Extract the util value and convert to lowercase
                # dataclass =parts[5].strip().lower() 
            

                # Check if the fragment value is 'yes', add the name to the fragments list
                if fragment == 'yes':
                    fragments.append(name)
                
                #  # Check if the activity value is 'yes', add the name to the activities list
                # if activity == 'yes':
                #     activities.append(name)
                #     adapter_available = 'no'
                    
                 # Check if the activity value is 'yes', add the name to the activities list
                if activity == 'yes':
                    activities.append(name)
                

                # Check if the activity value is 'yes', add the name to the activities list
                if adapter == 'yes':
                    adapters.append(name)
                
                # # Check if the activity value is 'yes', add the name to the activities list
                # if util == 'yes':
                #     utils.append(name)
               
                # # Check if the activity value is 'yes', add the name to the activities list
                # if dataclass == 'yes':
                #     dataclasses.append(name)
                

            # Generate files based on 'yes' or 'no' values
            for fragment in fragments:
                if fragment in adapters:
                    adapter_available = 'yes'
                else:
                    adapter_available = 'no'
                self.generate_fragment(fragment, adapter_available)
                self.generate_xml(fragment)
                self.generate_util_class(fragment)
                self.generate_fragment_test(fragment)
                self.generate_helperclass_test(fragment)
            
            for activity in activities:
                if activity in fragments:
                    fragment_available = 'yes'
                else:
                    fragment_available = 'no'

                self.generate_activity(activity, fragment_available)
                self.generate_activity_xml(activity)
                self.generate_activity_test(activity)

            for adapter in adapters:
                self.generateAdapter(adapter)
                self.generate_adapter_xml(adapter,self.imagebutton, self.textview, self.textview1)
                self.generate_viewModel(adapter)
                self.generate_adapter_test(adapter)
                self.generate_viewmodel_test(adapter)
        
                
            # Print the activities and fragments
            print("Fragments:", fragments)
            print("Activities:", activities)  
            print("adapters:", adapters)
            # print("utils:", utils)
            # print("dataclasses:", dataclasses)
            


    #function parsing the resoucre file package            
    def packages(self):
        import_r = self.packageParsing.package_name_parsing(self.project_path) 
        import_package = import_r + ".R"
        return import_package

    #function creates a folder or in existing folder,
    #generating fragments and inside fragments with content fragment lifecycles 
    def generate_fragment(self, fragment_name, adapter_available):
        print("adapter_available: ",adapter_available)
        # Ensure the folder exists, create it if it doesn't
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

        # Check if the fragment already exists
        fragment_names = fragment_name+"Fragment.kt"
        if self.packageParsing.file_exists(self.folder_path, fragment_names):
            print(f"Fragment '{fragment_name}Fragment' already exists in {self.folder_path}.")
            return

        #package_name_parsing and import_package function call from PackageParsing Class
        import_package = self.packages()
        package_for_utils = self.packageParsing.package_name_parsing(self.util_class_folder)
        package_name = self.packageParsing.package_name_parsing(self.folder_path)
        importdata_binding = self.packageParsing.package_name_parsing(self.project_path)
        adapter_package = self.packageParsing.package_name_parsing(self.output_folder)
        viewmodel_package_name = self.packageParsing.package_name_parsing(self.viewmodel_path)


        #content fragment lifecycles call from Fragments Class
        print("adapter_available: ",adapter_available)
        if adapter_available == 'yes':
            kotlin_code = self.fragments.fragment_content(package_name, import_package, package_for_utils, fragment_name, importdata_binding, adapter_package, viewmodel_package_name) 
        else:
            kotlin_code = self.fragmentContent.fragment_content(package_name, import_package, package_for_utils, fragment_name, importdata_binding)

        # Write the Kotlin code to a file in the specified folder
        file_path = os.path.join(self.folder_path, f"{fragment_name}Fragment.kt")
        with open(file_path, 'w') as file:
            file.write(kotlin_code)

        print(f"Kotlin fragment class '{fragment_name}Fragment' generated in {file_path}")

    #function generating xml class for fragmnet in existing folder res/layout
    #Content with default Button
    def generate_xml(self, name):
        if not os.path.exists(self.xml_file_folder):
            os.makedirs(self.xml_file_folder)
        
        xml_name = f'fragment_{name.lower()}.xml'
        xml_file_path = os.path.join(self.xml_file_folder, xml_name)

        if self.packageParsing.file_exists(self.xml_file_folder, xml_name):
            print(f"XML '{xml_name}' already exists in {self.xml_file_folder}.")
            return

        root = self.xmlClasses.xml_content(name)
        #tree = ET.ElementTree(root)
        xml_file_path = os.path.join(self.xml_file_folder, xml_name)
        with open(xml_file_path, "w") as file:
            file.write(root)
            print(f"XML file '{xml_file_path}' generated.")



    def generate_fragment_test(self, fragment_name):
        if self.packageParsing.file_exists(self.test_file_folder, fragment_name):
            print(f"TEST '{fragment_name}' already exists in {self.test_file_folder}.")
            return
        fragment_names = fragment_name+"FragmentTest.kt"
        package_name = self.packageParsing.package_name_parsing(self.activity_path)
        import_package = self.packages()
        fragment_package_name = self.packageParsing.package_name_parsing(self.folder_path)
        importdata_binding = self.packageParsing.package_name_parsing(self.project_path)

        test_content = self.Fragmenttest.generate_fragment_test(package_name, import_package, fragment_name)

        # Write the test case content to a file
        test_file_path = os.path.join(self.test_file_folder, f"{fragment_name}FragmentTest.kt")
        with open(test_file_path, 'w') as file:
            file.write(test_content)

        print(f"Fragment test case '{fragment_name}Test' generated in {test_file_path}")

    #function creates a folder or in existing folder,
    #generating utils classes inside fragment with content Button ClickListener
    def generate_util_class(self, fragment_name):
        if not os.path.exists(self.util_class_folder):
            os.makedirs(self.util_class_folder)

        utilclass_name = fragment_name+"Helper.kt"
        if self.packageParsing.file_exists(self.util_class_folder, utilclass_name):
            print(f"Helper class '{fragment_name}Helper' already exists in {self.util_class_folder}.")
            return

        package_name = self.packageParsing.package_name_parsing(self.util_class_folder)
        import_package = self.packages()
        importdata_binding = self.packageParsing.package_name_parsing(self.project_path)


        kotlin_code = self.utilClass.util_class_content(package_name, import_package, fragment_name, importdata_binding)

        file_path = os.path.join(self.util_class_folder, f"{fragment_name}Helper.kt")
        with open(file_path, 'w') as file:
            file.write(kotlin_code)
        print(f"Helper class '{fragment_name}Helper' generated in {self.util_class_folder}")


    def generate_helperclass_test(self, fragment_name):
        if self.packageParsing.file_exists(self.test_file_folder, fragment_name):
            print(f"TEST '{fragment_name}' already exists in {self.test_file_folder}.")
            return
        fragment_names = fragment_name+"HelperTest.kt"
        package_name = self.packageParsing.package_name_parsing(self.activity_path)
        import_package = self.packages()
        fragment_package_name = self.packageParsing.package_name_parsing(self.folder_path)
        importdata_binding = self.packageParsing.package_name_parsing(self.project_path)

        test_content = self.helperclasstest.generate_helperclass_test(package_name, import_package, fragment_name)

        # Write the test case content to a file
        test_file_path = os.path.join(self.test_file_folder, f"{fragment_name}HelperTest.kt")
        with open(test_file_path, 'w') as file:
            file.write(test_content)

        print(f"Helper test case '{fragment_name}Test' generated in {test_file_path}")
    
    #function creates a folder for activity with content lifecycle
    def generate_activity(self, activity_name, fragment_available):
        activity_names = activity_name+"Activity.kt"
        if self.packageParsing.file_exists(self.activity_path, activity_names):
            print(f"Activity '{activity_name}' already exists in {self.activity_path}.")
            return

        package_name = self.packageParsing.package_name_parsing(self.activity_path)
        adapter_package = self.packageParsing.package_name_parsing(self.output_folder)
        fragment_package_name = self.packageParsing.package_name_parsing(self.folder_path)
        importdata_binding = self.packageParsing.package_name_parsing(self.project_path)

        if fragment_available == 'yes':
            kotlin_code = self.activity.activity_content(package_name, adapter_package, activity_name, fragment_package_name, importdata_binding)
        else:
            kotlin_code = self.activityContent.activity_content(package_name, adapter_package, activity_name, fragment_package_name, importdata_binding)

        file_path = os.path.join(self.activity_path, f"{activity_name}Activity.kt")
        with open(file_path, 'w') as file:
            file.write(kotlin_code)
        print(f"Kotlin activity class '{activity_name}' generated in {file_path}")

    #function generating xml class for activity classes in existing folder res/layout
    def generate_activity_xml(self, activity_name):
        xml_name = f'activity_{activity_name.lower()}.xml'

        if self.packageParsing.file_exists(self.xml_file_folder, xml_name):
            print(f"XML '{xml_name}' already exists in {self.xml_file_folder}.")
            return

        # Get XML content for the activity
        xml_content = self.xmlActivity.xml_content(activity_name)

        # Write XML content to a file
        xml_file_path = os.path.join(self.xml_file_folder, xml_name)
        with open(xml_file_path, "w") as file:
            file.write(xml_content)
        print(f"XML file '{xml_file_path}' generated.")
        
    def generate_activity_test(self, activity_name):
        if self.packageParsing.file_exists(self.test_file_folder, activity_name):
            print(f"TEST '{activity_name}' already exists in {self.test_file_folder}.")
            return
        activity_names = activity_name+"ActivityTest.kt"
        package_name = self.packageParsing.package_name_parsing(self.activity_path)
        import_package = self.packages()
        adapter_package = self.packageParsing.package_name_parsing(self.output_folder)
        fragment_package_name = self.packageParsing.package_name_parsing(self.folder_path)
        import_data_binding = self.packageParsing.package_name_parsing(self.project_path)

        
        test_content = self.Actvitytest.generate_activity_test(package_name, import_package, activity_name)

        # Write the test case content to a file
        test_file_path = os.path.join(self.test_file_folder, f"{activity_name}ActivityTest.kt")
        with open(test_file_path, 'w') as file:
            file.write(test_content)

        print(f"Activity test case '{activity_name}Test' generated in {test_file_path}")

    
    

    #function generating dataclass with user input parameter 
    def dataclass(self, data_path, dataclassname, imagebutton, textview, textview1):
        # Ensure the folder exists, create it if it doesn't
        if not os.path.exists(self.data_path):
            os.makedirs(self.data_path)
        
        dataclass_name = dataclassname+"Data.kt"
        if self.packageParsing.file_exists(self.util_class_folder, dataclass_name):
            print(f"data class '{dataclassname}Data' already exists in {self.data_path}.")
            return
         
        package_name = self.packageParsing.package_name_parsing(data_path)
        data_class_content = self.dataClassContent.data_class_content(package_name, dataclassname, imagebutton, textview, textview1)
       
        data_path = os.path.join(self.data_path, f"{dataclassname}.kt")
        with open(data_path, "w") as file:
            file.write(data_class_content)
        print(f" data class {dataclassname} generated successfully!")

    #function creating adapter content
    def generateAdapter(self,adapter_name):
        # Ensure the folder exists, create it if it doesn't
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
        
        # Check if the adapter already exists
        adapter_name1 = adapter_name+"Adapter.kt"
        if self.packageParsing.file_exists(self.output_folder, adapter_name1):
            print(f"adapter_name '{adapter_name}Adapter' already exists in {self.output_folder}.")
            return
        
        package_name = self.packageParsing.package_name_parsing(self.output_folder)
        viewmodel_package_name = self.packageParsing.package_name_parsing(self.viewmodel_path)
        dataclass_package_name = self.packageParsing.package_name_parsing(self.data_path)
        folder_path = self.packageParsing.package_name_parsing(self.folder_path)
        import_package = self.packages()
        importdata_binding = self.packageParsing.package_name_parsing(self.project_path)

        adapter_content = self.adapterContent.generate_recycler_adapter(adapter_name, package_name, import_package, viewmodel_package_name, dataclass_package_name, folder_path, imagebutton, textview, textview1, importdata_binding)
        
        # Write the Kotlin code to a file in the specified folder
        file_path = os.path.join(self.output_folder, f"{adapter_name}Adapter.kt")
        with open(file_path, 'w') as file:
            file.write(adapter_content)

        print(f"RecyclerView Adapter '{adapter_name}' generated in {file_path}")

    #function generating xml class for adapter classes in existing folder res/layout
    def generate_adapter_xml(self, adapter_name, imagebutton, textview, textview1):
        xml_name = f'adapter_{adapter_name.lower()}.xml'

        # Check if the xml for adapter already exists
        if self.packageParsing.file_exists(self.xml_file_folder, xml_name):
            print(f"XML '{xml_name}' already exists in {self.xml_file_folder}.")
            return

        #Content for xml call from xmlClasses
        root = self.adapterXml.xml_content(imagebutton, textview, textview1)

        # Create the ElementTree object
        tree = ET.ElementTree(root)
        xml_file_path = os.path.join(self.xml_file_folder, xml_name)
        with open(xml_file_path, "wb") as file:
            tree.write(file, encoding="utf-8", xml_declaration=True)
        print(f"XML file '{xml_file_path}' generated.")


    def generate_adapter_test(self, adapter_name):
        if self.packageParsing.file_exists(self.test_file_folder, adapter_name):
            print(f"TEST '{adapter_name}' already exists in {self.test_file_folder}.")
            return
        adapter_test_names = adapter_name+"AdapterTest.kt"
        package_name = self.packageParsing.package_name_parsing(self.activity_path)
        import_package = self.packages()
        adapter_package = self.packageParsing.package_name_parsing(self.output_folder)
        import_data_binding = self.packageParsing.package_name_parsing(self.project_path)

        test_content = self.Adaptertest.generate_adapter_test(package_name, import_package, adapter_name)

        # Write the test case content to a file
        test_file_path = os.path.join(self.test_file_folder, f"{adapter_name}AdapterTest.kt")
        with open(test_file_path, 'w') as file:
            file.write(test_content)

        print(f"Adapter test case '{adapter_name}Test' generated in {test_file_path}")

    #function creates a folder or in existing folder,
    #generating viewmodel classes with content list 
    def generate_viewModel(self, adapter_name):
             # Ensure the folder exists, create it if it doesn't
        if not os.path.exists(self.viewmodel_path):
            os.makedirs(self.viewmodel_path)
        
        # Check if the viewmodel already exists
        adapter_name1 = adapter_name+"ViewModel.kt"
        if self.packageParsing.file_exists(self.viewmodel_path, adapter_name1):
            print(f"adapter_name '{adapter_name}ViewModel' already exists in {self.viewmodel_path}.")
            return
        
        package_name = self.packageParsing.package_name_parsing(self.viewmodel_path)
        import_package = self.packages()
        dataclass_package_name = self.packageParsing.package_name_parsing(self.data_path)

        adapter_content = self.viewModelContent.generate_ViewModel_Content(adapter_name, package_name, import_package, dataclass_package_name)
        
        # Write the Kotlin code for viewmodel to a file in the specified folder
        file_path = os.path.join(self.viewmodel_path, f"{adapter_name}ViewModel.kt")
        with open(file_path, 'w') as file:
            file.write(adapter_content)

        print(f"RecyclerView Adapter '{adapter_name}' generated in {file_path}")

    def generate_viewmodel_test(self, adapter_name):
        if self.packageParsing.file_exists(self.test_file_folder, adapter_name):
            print(f"TEST '{adapter_name}' already exists in {self.test_file_folder}.")
            return
        viewmodel_test_names = adapter_name+"ViewModelTest.kt"
        package_name = self.packageParsing.package_name_parsing(self.activity_path)
        adapter_package = self.packageParsing.package_name_parsing(self.output_folder)
        import_package = self.packages()
        import_data_binding = self.packageParsing.package_name_parsing(self.project_path)

        test_content = self.viewmodeltest.generate_viewmodel_test(package_name, import_package, adapter_name)

        # Write the test case content to a file
        test_file_path = os.path.join(self.test_file_folder, f"{adapter_name}ViewModelTest.kt")
        with open(test_file_path, 'w') as file:
            file.write(test_content)

        print(f"ViewModel test case '{adapter_name}Test' generated in {test_file_path}")

if __name__ == "__main__":
    # User input for different paths  Eg:'path/to/your/text/file.txt'
    text_path = input("Enter the text file path: ")
    #Eg:path/to/your/projectname
    project_path = input("Enter the project path: ")
    
    foldername = input("Do you want Folder for this project? (yes/no): ")
    if foldername.lower() == 'yes':
        project_foldername = input("Enter the Foldername: ")
        folder_path = project_path + "/" + project_foldername + "/" + "fragments"
        activity_path = project_path + "/" + project_foldername
        util_class_folder = project_path + "/" + project_foldername + "/" + "helperclass"
        output_folder = project_path + "/" + project_foldername + "/" + "adapters"
        viewmodel_path = project_path + "/" + project_foldername + "/" + "viewmodel"
        data_path = project_path + "/" + project_foldername + "/" + "dataclass"
        dataclass_name = "Data"
    else:
        folder_path = project_path + "/" + "fragments"
        util_class_folder = project_path + "/" + "helperclass"
        activity_path = project_path
        output_folder = project_path + "/" + "adapters"
        viewmodel_path = project_path + "/" + "viewmodel"
        data_path = project_path + "/" + "dataclass"
        dataclass_name = "Data"


    xml_file_folder = input("Enter the xml file folder: ")
    test_file_folder = input("Enter the test file folder: ")
    imagebutton = input("Enter the imagebutton id: ")
    imagebutton_type = input(f"Enter type for {imagebutton}: ")
    textview = input("Enter the textview id: ")
    textview_type = input(f"Enter type for {textview}: ")
    textview1 = input("Enter the textview1 id: ")
    textview1_type = input(f"Enter type for {textview1}: ")

    fragment_automation = FragmentAutomation(text_path, project_path, folder_path, xml_file_folder, test_file_folder, util_class_folder, output_folder, activity_path, viewmodel_path,data_path,imagebutton, imagebutton_type, textview, textview_type, textview1, textview1_type)
    fragment_automation.read_from_text()

    imagebutton = (imagebutton +":"+ imagebutton_type)
    textview =(textview +":"+ textview_type)
    textview1 =(textview1 +":"+ textview1_type)  
    fragment_automation.dataclass(data_path, dataclass_name, imagebutton, textview, textview1)


