from CopyRight import CopyRight
#Adapter class contains content for Adapter
class AdapterContent:

    def __init__(self):
        print("AdapterContent instance created.")
        self.copyRight = CopyRight() 
 
    def generate_recycler_adapter(self, adapter_name, package_name, import_package, viewmodel_package_name,dataclass_package_name, folder_path,
                                 imagebutton, textview, textview1, importdata_binding):
        
        dataclass_package_name = dataclass_package_name+"." + "Data"
        viewmodel_package_name = viewmodel_package_name+"."+adapter_name+"ViewModel"
        folder_path = folder_path+"."+adapter_name+"Fragment"

        original_string = adapter_name
        modified_string = original_string[0] + original_string[1:].lower()
        binding  = "Adapter"+modified_string+"Binding"
        importdata_binding = importdata_binding+".databinding."+ binding

        kotlin_code_copyright = self.copyRight.copy_right()
        adapter_content = f"""package {package_name}

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import android.util.Log
import {import_package}
import {dataclass_package_name}
import {viewmodel_package_name}
import {importdata_binding}

class {adapter_name}Adapter(viewModel: {adapter_name}ViewModel) : RecyclerView.Adapter<{adapter_name}Adapter.ViewHolder>() {{

   private val tag: String = this::class.java.simpleName

    private var dataList: List<{"Data"}> = emptyList()

    init {{
        Log.d(tag, "initialized")
        viewModel.getContacts().observeForever {{ contacts ->
            dataList = contacts
            notifyDataSetChanged()
        }}
    }}

    inner class ViewHolder(private val binding: {binding}) : RecyclerView.ViewHolder(binding.root) {{
     fun bind(contact: {"Data"}) {{
            binding.{textview}.text = contact.{textview}
            binding.{textview1}.text = contact.{textview1}
            binding.{imagebutton}.id = contact.{imagebutton}
        }}
    }}

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder
    {{
        Log.d(tag, "onCreateViewHolder")
        val binding ={binding}.inflate(LayoutInflater.from(parent.context), parent, false)
        return ViewHolder(binding)
    }}

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {{
     Log.d(tag, "onBindViewHolder")
        holder.bind(dataList[position])
    }}

    override fun getItemCount(): Int {{
     Log.d(tag, "getItemCount")
        return dataList.size
    }}
}}
"""
        adapter_content = kotlin_code_copyright + adapter_content
        return adapter_content
        