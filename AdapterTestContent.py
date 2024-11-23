from CopyRight import CopyRight
#Adapter Test cases:
class AdapterTest:
    def __init__(self):
        print("Adapter Test instance created. ")
        self.copyRight = CopyRight()


    def generate_adapter_test(self, package_name, import_package, adapter_name):
        original_string = adapter_name
        kotlin_code_copyright = self.copyRight.copy_right()
        Test_content = f"""package {{package_name}}

import android.content.Context
import android.widget.TextView
import androidx.arch.core.executor.testing.InstantTaskExecutorRule
import androidx.lifecycle.MutableLiveData
import com.example.myapplication3.Automation.adapters.FirstAdapter
import com.example.myapplication3.Automation.dataclass.Data
import com.example.myapplication3.Automation.viewmodel.FirstViewModel
import com.example.myapplication3.databinding.AdapterFirstBinding
import org.junit.Before
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith
import org.mockito.Mock
import org.mockito.Mockito.`when`
import org.mockito.MockitoAnnotations
import org.robolectric.RobolectricTestRunner
import org.robolectric.RuntimeEnvironment

@RunWith(RobolectricTestRunner::class)
class {adapter_name}AdapterTest {{

    @get:Rule
    var instantTaskExecutorRule = InstantTaskExecutorRule()

    @Mock
    private lateinit var viewModel: FirstViewModel

    @Mock
    private lateinit var binding: AdapterFirstBinding

    private lateinit var adapter: FirstAdapter

    private lateinit var context: Context

    @Before
    fun setup() {{
        MockitoAnnotations.initMocks(this)
        context = RuntimeEnvironment.systemContext
        adapter = FirstAdapter(viewModel)
    }}

    @Test
    fun testItemCount() {{
        val dataList = listOf(Data("John", "123456", 1), Data("Alice", "789101", 2))
        val liveData = MutableLiveData<List<Data>>()
        liveData.value = dataList

        `when`(viewModel.getContacts()).thenReturn(liveData)

        adapter.notifyDataSetChanged()

        assert(adapter.itemCount == dataList.size)
    }}

    @Test
    fun testItemBinding() {{
        val dataList = listOf(Data("John", "123456", 1))
        val liveData = MutableLiveData<List<Data>>()
        liveData.value = dataList

        `when`(viewModel.getContacts()).thenReturn(liveData)

        adapter.notifyDataSetChanged()

        val parent = androidx.constraintlayout.widget.ConstraintLayout(context)
        val viewHolder = adapter.onCreateViewHolder(parent, 0)
        adapter.onBindViewHolder(viewHolder, 0)

        assert((viewHolder.binding.name as TextView).text == dataList[0].name)
        assert((viewHolder.binding.number as TextView).text == dataList[0].number)
        assert(viewHolder.binding.image.id == dataList[0].image)
    }}
}}

"""
        Test_content = kotlin_code_copyright + Test_content
        return Test_content
