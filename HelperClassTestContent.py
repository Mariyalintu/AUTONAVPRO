from CopyRight import CopyRight
#HelperClass Test cases:
class HelperClassTest:
    def __init__(self):
        print("Fragment Test instance created. ")
        self.copyRight = CopyRight()


    def generate_helperclass_test(self, package_name, import_package, fragment_name):
        original_string = fragment_name
        kotlin_code_copyright = self.copyRight.copy_right()
        Test_content = f"""package {package_name}
import android.content.Context
import android.widget.Toast
import androidx.fragment.app.FragmentActivity
import {package_name}.R
import {package_name}.databinding.Fragment{fragment_name}Binding
import org.junit.Before
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.Robolectric
import org.robolectric.RobolectricTestRunner
import org.robolectric.annotation.Config

@RunWith(RobolectricTestRunner::class)
@Config(sdk = [Build.VERSION_CODES.P]) // Choose the appropriate SDK version
class {fragment_name}HelperTest {{

    private lateinit var context: Context
    private lateinit var binding: Fragment{fragment_name}Binding
    private lateinit var helper: {fragment_name}Helper

    @Before
    fun setUp() {{
        context = Robolectric.buildActivity(FragmentActivity::class.java).create().start().get()
        binding = Fragment{fragment_name}Binding.bind(FragmentActivity())
        helper = {fragment_name}Helper(context, binding)
    }}

    @Test
    fun testClickListener() {{
        val button = binding.myButton
        button.performClick()

        // Verify that showToast() is called
        // Add more assertions or verifications as needed
    }}

    @Test
    fun testShowToast() {{
        helper.showToast("Test Message")

        // Verify that Toast.makeText() is called with the correct parameters
        // Add more assertions or verifications as needed
    }}
}}  

"""
        Test_content = kotlin_code_copyright + Test_content
        return Test_content
