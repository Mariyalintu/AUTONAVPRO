from CopyRight import CopyRight
#Fragments class contains content for fragments
class Fragments:
    def __init__(self):
        print("Fragments instance created.")
        self.copyRight = CopyRight() 

    def fragment_content(self, package_name, import_package, package_for_utils, fragment_name, importdata_binding, adapter_package, viewmodel_package_name):
        import_package_for_utils = package_for_utils + "." + fragment_name + "Helper"
        original_string = fragment_name
        modified_string = original_string[0] + original_string[1:].lower()
        binding  = "Fragment"+modified_string+"Binding"
        importdata_binding = importdata_binding+".databinding."+ binding
        adapter_package = adapter_package+"." + fragment_name+"Adapter"
        viewmodel_package_name = viewmodel_package_name+"." + fragment_name+"ViewModel"

        kotlin_code_copyright = self.copyRight.copy_right()
        kotlin_content = f"""package {package_name}
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import {import_package}
import {import_package_for_utils}
import {importdata_binding}
import {viewmodel_package_name}
import {adapter_package}
import android.util.Log
import androidx.lifecycle.ViewModelProvider
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class {fragment_name}Fragment : Fragment() {{
    private val TAG = this::class.java.simpleName
    private var binding: {binding}? = null
    private var helper: {fragment_name}Helper? = null
    private lateinit var adapter: {fragment_name}Adapter
    private lateinit var viewModel: {fragment_name}ViewModel

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {{
        Log.d(TAG, " onCreate")
        val requireContext = requireContext()
        binding = {binding}.inflate(inflater, container, false)
        helper = {fragment_name}Helper(requireContext, binding!!)
        return binding!!.root
    }}

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {{
        super.onViewCreated(view, savedInstanceState)
        Log.d(TAG, "onViewCreated")
    }}

    override fun onStart() {{
        super.onStart()
        Log.d(TAG, "onStart")
    }}

    override fun onResume() {{
        super.onResume()
        Log.d(TAG, "onResume")
        // Initialize ViewModel
        viewModel = ViewModelProvider(this)[{fragment_name}ViewModel::class.java]
        // Initialize RecyclerViewAdapter
        adapter = {fragment_name}Adapter(viewModel)

        // Initialize RecyclerView and set layout manager
        val recyclerView: RecyclerView = binding!!.recyclerView
        recyclerView.layoutManager = LinearLayoutManager(requireContext())

        // Set adapter to RecyclerView
        recyclerView.adapter = adapter
    }}

    override fun onPause() {{
        super.onPause()
        Log.d(TAG, "onPause")
    }}

    override fun onStop() {{
        super.onStop()
        Log.d(TAG, "onStop")
    }}

    override fun onDestroyView() {{
        super.onDestroyView()
        Log.d(TAG, "onDestroyView")
        binding = null
    }}

    override fun onDestroy() {{
        super.onDestroy()
        Log.d(TAG, "onDestroy")
    }}
}}
"""
        kotlin_code = kotlin_code_copyright + kotlin_content
        return kotlin_code
