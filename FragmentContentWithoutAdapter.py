from CopyRight import CopyRight
#Fragments class contains content for fragments
class FragmentsWithoutAdapter:
    def __init__(self):
        print("Fragments instance created.")
        self.copyRight = CopyRight() 

    def fragment_content(self, package_name, import_package, package_for_utils, fragment_name, importdata_binding):
        import_package_for_utils = package_for_utils + "." + fragment_name + "Helper"
        original_string = fragment_name
        modified_string = original_string[0] + original_string[1:].lower()
        binding  = "Fragment"+modified_string+"Binding"
        importdata_binding = importdata_binding+".databinding."+ binding

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
import android.util.Log

class {fragment_name}Fragment : Fragment() {{
    private val TAG = this::class.java.simpleName
    private var binding: {binding}? = null
    private var helper: {fragment_name}Helper? = null

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
    }}

    override fun onDestroy() {{
        super.onDestroy()
        Log.d(TAG, "onDestroy")
    }}
}}
"""
        kotlin_code = kotlin_code_copyright + kotlin_content
        return kotlin_code
