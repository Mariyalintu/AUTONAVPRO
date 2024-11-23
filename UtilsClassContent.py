#UtilClass class contains content for UtilClasses
from CopyRight import CopyRight
class UtilClass:
    def __init__(self):
        print("HelperClass instance created.")
        self.copyRight = CopyRight() 

    def util_class_content(self, package_name, import_package, fragment_name, importdata_binding):
        kotlin_code_copyright = self.copyRight.copy_right()
        original_string = fragment_name
        modified_string = original_string[0] + original_string[1:].lower()
        binding  = "Fragment"+modified_string+"Binding"
        importdata_binding = importdata_binding+".databinding."+ binding

        kotlin_content = f"""package {package_name}

import android.content.Context
import android.widget.Toast
import android.util.Log
import {import_package}
import {importdata_binding}

class {fragment_name}Helper(context: Context, binding: {binding}?) {{
    private val tag:String = this::class.java.simpleName
    private val requireContext = context

    init {{
        Log.d(tag, "{fragment_name}Helper initialized")
          if (binding != null) {{
            clickListener(binding)
        }}
    }}

    private fun clickListener(binding: {binding}) {{
        Log.d(tag, "{fragment_name}Helper clickListener")
        binding.myButton.setOnClickListener {{
            showToast("Button in {fragment_name}Fragment clicked!")
        }}
    }}

    private fun showToast(message: String) {{
        Log.d(tag, "{fragment_name}Helper showToast")
        Toast.makeText(requireContext, message, Toast.LENGTH_SHORT).show()
    }}
}}
"""
        kotlin_code = kotlin_code_copyright + kotlin_content
        return kotlin_code

