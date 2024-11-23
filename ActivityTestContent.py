from CopyRight import CopyRight
#Activity Test cases:
class ActivityTest:
    def __init__(self):
        print("Activity Test instance created.")
        self.copyRight = CopyRight()
    def generate_activity_test(self, package_name, import_package, activity_name):
        # Generate the content of the activity test case
        original_string = activity_name
        kotlin_code_copyright = self.copyRight.copy_right()
        test_content = f"""package {package_name}

import android.os.Build
import android.os.Bundle
import androidx.test.core.app.ActivityScenario
import org.junit.After
import org.junit.Assert.assertEquals
import org.junit.Before
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.RobolectricTestRunner
import org.robolectric.annotation.Config

@RunWith(RobolectricTestRunner::class)
@Config(sdk = [Build.VERSION_CODES.P]) // Choose the appropriate SDK version
class {activity_name}ActivityTest {{

    private lateinit var activityScenario: ActivityScenario<{activity_name}Activity>

    @Before
    fun setUp() {{
        // Launch the activity scenario
        activityScenario = ActivityScenario.launch({activity_name}Activity::class.java)
    }}

    @After
    fun tearDown() {{
        // Close the activity scenario after each test
        activityScenario.close()
    }}

    @Test
    fun testLifecycle() {{
        // Initialize flags to track if each lifecycle method is called
        var onCreateCalled = false
        var onStartCalled = false
        var onResumeCalled = false
        var onPauseCalled = false
        var onStopCalled = false
        var onDestroyCalled = false

        // Perform actions and assertions on the activity
        activityScenario.onActivity {{ activity ->
            // Test onCreate
            activity.onCreate(Bundle())
            onCreateCalled = true

            // Test onStart
            activity.onStart()
            onStartCalled = true

            // Test onResume
            activity.onResume()
            onResumeCalled = true

            // Test onPause
            activity.onPause()
            onPauseCalled = true

            // Test onStop
            activity.onStop()
            onStopCalled = true

            // Test onDestroy
            activity.onDestroy()
            onDestroyCalled = true
        }}

        // Verify that each lifecycle method was called
        assertEquals(true, onCreateCalled)
        assertEquals(true, onStartCalled)
        assertEquals(true, onResumeCalled)
        assertEquals(true, onPauseCalled)
        assertEquals(true, onStopCalled)
        assertEquals(true, onDestroyCalled)
    }}
}}

"""
        test_content = kotlin_code_copyright + test_content
        return test_content

