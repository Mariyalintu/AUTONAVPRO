import xml.etree.ElementTree as ET

#XmlClasses contains content for  fragmnet xmls
class XmlClasses:
    def __init__(self):
        print("XmlClasses instance created.")
        
    def xml_content(self, fragment_name):
        # Create the root element
        #root = ET.Element("FrameLayout")
        buttontext = fragment_name+"_Fragment"
        root= f"""<?xml version='1.0' encoding='utf-8'?>
<androidx.constraintlayout.widget.ConstraintLayout
	xmlns:android="http://schemas.android.com/apk/res/android"
	xmlns:tools="http://schemas.android.com/tools"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	xmlns:app="http://schemas.android.com/apk/res-auto">

	<androidx.recyclerview.widget.RecyclerView
		android:id="@+id/recyclerView"
		android:layout_width="match_parent"
		android:layout_height="0dp"
		android:paddingTop="8dp"
		android:paddingBottom="8dp"
		app:layout_constraintBottom_toBottomOf="parent"
		app:layout_constraintEnd_toEndOf="parent"
		app:layout_constraintStart_toStartOf="parent"
		app:layout_constraintTop_toTopOf="parent" />

<Button 
		android:id="@+id/myButton" 
		android:layout_width="wrap_content" 
		android:layout_height="wrap_content" 
		android:text= "{buttontext}"
		app:layout_constraintBottom_toBottomOf="parent" 
		app:layout_constraintEnd_toEndOf="parent" 
		app:layout_constraintStart_toStartOf="parent" 
		app:layout_constraintTop_toTopOf="parent" />

</androidx.constraintlayout.widget.ConstraintLayout>
"""
        return root
