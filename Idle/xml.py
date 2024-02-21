import os
import xml.etree.ElementTree as ET

def find_button_id_in_xml(xml_file_path, button_id):
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        for button in root.iter('Button'):
            if 'android:id' in button.attrib and button.attrib['android:id'].endswith(button_id):
                return True

        return False

    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return False
# Example usage:
xml_file_path = r"C:\Users\mariy\AndroidStudioProjects\neww\app\src\main\res\layout\activity_main.xml"
button_id_to_find = 'Button'

button_found = find_button_id_in_xml(xml_file_path, button_id_to_find)

if button_found:
    print(f"Button with ID '{button_id_to_find}' found in the XML layout.")
else:
    print(f"Button with ID '{button_id_to_find}' not found in the XML layout.")





