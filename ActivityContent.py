from CopyRight import CopyRight
#Activity class contains content for Activities
class Activity:
    def __init__(self):
        print("Activity instance created.")
        self.copyRight = CopyRight() 

    def activity_content(self, package_name, adapter_package, activity_name, fragment_package_name, importdata_binding):
        
        adapter_package = adapter_package+"." + activity_name+"Adapter"
        fragment_package_name = fragment_package_name+"." + activity_name+"Fragment"
        original_string = activity_name
        modified_string = original_string[0] + original_string[1:].lower()
        binding  = "Activity"+modified_string+"Binding"
        importdata_binding = importdata_binding+".databinding."+ binding
    
        kotlin_code_copyright = self.copyRight.copy_right()
        kotlin_content = f"""package {package_name}
import android.os.Bundle
import android.util.Log
import androidx.appcompat.app.AppCompatActivity
import {fragment_package_name}
import {importdata_binding}

class {activity_name}Activity : AppCompatActivity() {{
    private val tag:String = this::class.java.simpleName
    private var binding: {binding}? = null
    
    override fun onCreate(savedInstanceState: Bundle?) {{
        super.onCreate(savedInstanceState)
        Log.d(tag, " onCreate")
        binding = {binding}.inflate(layoutInflater)
        setContentView(binding!!.root)
        binding!!.myButton.setOnClickListener {{
            // Create instance of your fragment
            supportFragmentManager.beginTransaction()
                .replace(binding!!.fragmentContainer.id, {activity_name}Fragment())
                .commit()
        }}
    }}

    override fun onStart() {{
        super.onStart()
        Log.d(tag, " onStart")
    }}

    override fun onResume() {{
        super.onResume()
        Log.d(tag, " onResume")
    }}

    override fun onPause() {{
        super.onPause()
        Log.d(tag, " onPause")
    }}

    override fun onStop() {{
        super.onStop()
        Log.d(tag, " onStop")
    }}

    override fun onDestroy() {{
        super.onDestroy()
        Log.d(tag, " onDestroy")
    }}
}}
"""
        kotlin_code = kotlin_code_copyright + kotlin_content
        return kotlin_code

