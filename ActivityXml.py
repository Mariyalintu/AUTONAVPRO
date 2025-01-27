#XmlClasses  contains content for Activities
class XmlActivity:
    def __init__(self):
        print("XmlActivity instance created.")
        
    def xml_content(self,activity_name):
        buttontext = activity_name+"_Activity"
        xml_content = f"""<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <FrameLayout
        android:id="@+id/fragment_container"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:text= "{buttontext}"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintEnd_toEndOf="parent" >
    </FrameLayout>

    <Button 
        android:id="@+id/myButton" 
        android:layout_width="wrap_content" 
        android:layout_height="wrap_content" 
        app:layout_constraintBottom_toBottomOf="parent" 
        app:layout_constraintEnd_toEndOf="parent" 
        app:layout_constraintStart_toStartOf="parent" 
        app:layout_constraintTop_toTopOf="parent"
        android:visibility="visible"/>

</androidx.constraintlayout.widget.ConstraintLayout>
"""

        return xml_content 
 
