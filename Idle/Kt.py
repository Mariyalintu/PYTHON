import os

def generate_kotlin_file(file_path, package_name, class_name):
    # Write Kotlin code to the file
    with open(file_path, "w") as kt_file:
        kt_file.write(f"package {package_name}\n\n")
        kt_file.write("class " + class_name.capitalize() + " {\n")
        kt_file.write("\tfun greet(name: String) {\n")
        kt_file.write("\t\tprintln(\"Hello,  name!\")\n")
        kt_file.write("\t}\n")
        kt_file.write("}\n")

    print(f"Kotlin file '{class_name}.kt' generated at '{file_path}'.")

directory_path = "C:/Users/mariy/AndroidStudioProjects/AutoNavPro/app/src/main/java/com/example/autonavpro"
package_name = "com.example.autonavpro"
class_name = "MyClass"
file_path = os.path.join(directory_path, class_name + ".kt")

generate_kotlin_file(file_path, package_name, class_name)


