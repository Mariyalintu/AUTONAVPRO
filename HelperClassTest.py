from CopyRight import CopyRight
#HelperClass Test cases:
class HelperClassTest:
    def __init__(self):
        print("Fragment Test instance created. ")
        self.copyRight = CopyRight()


    def generate_helperclass_test(self, package_name, import_package, package_for_test, fragment_name):

        kotlin_code_copyright = self.copyRight.copy_right()
        Test_content = f"""package {package_name}
 
import android.content.Context
import android.widget.Button
import android.widget.Toast
import {package_name}.helperclass.{fragment_name}Helper
import {package_name}.databinding.Fragment{fragment_name}Binding
import junit.framework.Assert.assertNotNull
import org.junit.Before
import org.junit.Test
import org.junit.runner.RunWith
import org.mockito.Mock
import org.mockito.Mockito.verify
import org.mockito.MockitoAnnotations
import org.robolectric.RobolectricTestRunner
import org.robolectric.annotation.Config

@RunWith(RobolectricTestRunner::class)
@Config(sdk = [Config.OLDEST_SDK]) // Choose the appropriate SDK version
class {fragment_name}HelperTest {

    @Mock
    private lateinit var context: Context

    @Mock
    private lateinit var binding: Fragment{fragment_name}Binding

    @Mock
    private lateinit var button: Button

    private lateinit var helper: {fragment_name}Helper

    @Before
    fun setUp() {
        MockitoAnnotations.initMocks(this)
        helper = FirstHelper(context, binding)
    }

    @Test
    fun testClickListener() {
        assertNotNull(helper)

        // Simulate button click
        helper.showToast("Test Message")

        // Verify that showToast() is called with the correct message
        verify(context).getString(R.string.test_message)
    }

    @Test
    fun testShowToast() {
        assertNotNull(helper)

        // Simulate button click
        helper.showToast("Test Message")

        // Verify that Toast.makeText() is called with the correct parameters
        verify(context).getString(R.string.test_message)
        verify(Toast.makeText(context, "Test Message", Toast.LENGTH_SHORT)).show()
    }
}

"""
        Test_content = kotlin_code_copyright + Test_content
        return Test_content
