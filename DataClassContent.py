from CopyRight import CopyRight
class DataClassContent:

    def __init__(self):
        print("AdapterContent instance created.")
        self.copyRight = CopyRight() 

    def data_class_content(self, package_name, dataclass, imagebutton, textview, textview1):
        kotlin_code_copyright = self.copyRight.copy_right()
        
        data_class_content = f"""package {package_name}
import androidx.lifecycle.MutableLiveData

class Data(val name: String, val number: String, val image: Int) {{
    private val _name = MutableLiveData<String>()
    private val _number = MutableLiveData<String>()
    private val _image = MutableLiveData<Int>()

    val liveName: MutableLiveData<String>
        get() = _name

    val liveNumber: MutableLiveData<String>
        get() = _number

    val liveImage: MutableLiveData<Int>
        get() = _image

    fun getNames(): String? {{ // Renamed the method to retrieveName
        return _name.value
    }}

    fun setName(value: String) {{
        _name.value = value
    }}

    fun getNumbers(): String? {{
        return _number.value
    }}

    fun setNumber(value: String) {{
        _number.value = value
    }}

    fun getImages(): Int? {{
        return _image.value
    }}

    fun setImage(value: Int) {{
        _image.value = value
    }}
}}      
"""
        data_class_content = kotlin_code_copyright + data_class_content
        return data_class_content
