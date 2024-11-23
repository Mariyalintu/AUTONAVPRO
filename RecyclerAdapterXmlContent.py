import xml.etree.ElementTree as ET

#XmlClasses  contains content for Adapter xmls
class AdapterXmlClasses:
    def __init__(self):
        print("XmlClasses instance created.")
        
    def xml_content(self, imagebutton, textview, textview1):
        # Create the root element
        root = ET.Element("androidx.constraintlayout.widget.ConstraintLayout")

        imagebuttonid = "@+id/"+imagebutton
        textviewid = "@+id/"+textview
        textview1id = "@+id/"+textview1

        # Create the root element
        root = ET.Element("androidx.constraintlayout.widget.ConstraintLayout")
        root.set("\n\txmlns:android", "http://schemas.android.com/apk/res/android")
        root.set("\n\txmlns:app", "http://schemas.android.com/apk/res-auto")
        root.set("\n\tandroid:layout_width", "match_parent")
        root.set("\n\tandroid:layout_height", "wrap_content")
        root.set("\n\tandroid:padding", "16dp")
        root.text = "\n"

        # Create ImageButton element
        image_button = ET.SubElement(root, "ImageButton")
        image_button.set("\n\t\tandroid:id", imagebuttonid)
        image_button.set("\n\t\tandroid:layout_width", "25dp")
        image_button.set("\n\t\tandroid:layout_height", "26dp")
        image_button.set("\n\t\tandroid:background", "@drawable/c")
        image_button.set("\n\t\tapp:layout_constraintStart_toStartOf", "parent")
        image_button.set("\n\t\tapp:layout_constraintTop_toTopOf", "parent")
        image_button.tail = "\n"
        

        # Create nameTextView element
        name_text_view = ET.SubElement(root, "TextView")
        name_text_view.set("\n\t\tandroid:id", textviewid)
        name_text_view.set("\n\t\tandroid:layout_width", "0dp")
        name_text_view.set("\n\t\tandroid:layout_height", "wrap_content")
        name_text_view.set("\n\t\tandroid:layout_marginEnd", "8dp")
        name_text_view.set("\n\t\tandroid:layout_marginStart", "35dp")
        name_text_view.set("\n\t\tapp:layout_constraintEnd_toStartOf", textview1id)
        name_text_view.set("\n\t\tapp:layout_constraintStart_toStartOf", "parent")
        name_text_view.set("\n\t\tapp:layout_constraintTop_toTopOf", "parent")
        name_text_view.set("\n\t\tandroid:textSize", "18sp")
        name_text_view.set("\n\t\tandroid:textColor", "@color/white")
        name_text_view.set("\n\t\tandroid:textStyle", "bold")
        name_text_view.tail = "\n"

        # Create numberTextView element
        number_text_view = ET.SubElement(root, "TextView")
        number_text_view.set("\n\t\tandroid:id", textview1id)
        number_text_view.set("\n\t\tandroid:layout_width", "0dp")
        number_text_view.set("\n\t\tandroid:layout_height", "wrap_content")
        number_text_view.set("\n\t\tapp:layout_constraintEnd_toEndOf", "parent")
        number_text_view.set("\n\t\tapp:layout_constraintStart_toEndOf", textviewid)
        number_text_view.set("\n\t\tapp:layout_constraintTop_toTopOf", "parent")
        number_text_view.set("\n\t\tandroid:textColor", "@color/white")
        number_text_view.set("\n\t\tandroid:textSize", "16sp")
        number_text_view.set("\n\t\tandroid:textStyle", "bold")
        number_text_view.tail = "\n"

        return root
    
    
    

