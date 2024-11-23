from CopyRight import CopyRight
#ViewModel class contains content for ViewModel
class ViewModelContent:

    def __init__(self):
        print("AdapterContent instance created.")
        self.copyRight = CopyRight() 

    def generate_ViewModel_Content(self, adapter_name, package_name, import_package, dataclass_package_name):
        dataclass_package_name = dataclass_package_name+"." + "Data"

        kotlin_code_copyright = self.copyRight.copy_right()
        viewModel_content = f"""package {{package_name}}

import androidx.lifecycle.LiveData
import androidx.lifecycle.ViewModel
import com.example.pythonautomation.automation.dataclass.Data


class {{adapter_name}}ViewModel : ViewModel() {{
    private val data: Data = Data("", "", 0) // Create an instance of Data

    fun getData(): LiveData<Data>  {{
        return getData()
    }}

    // Example function to set data
    fun setDataValues(name: String, number: String, image: Int) {{
        data.setName(name)
        data.setNumber(number)
        data.setImage(image)
    }}
}}
"""
        viewModel_content = kotlin_code_copyright + viewModel_content
        return viewModel_content
