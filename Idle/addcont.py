file_path = r"C:\Users\mariy\AndroidStudioProjects\neww\app\src\main\java\com\example\neww\MainActivity.kt"
content_to_append = """\
// Additional content
fun additionalFunction() {
    var Button=findViewById<Button>R.id.Button

    println("This is additional content.")

    
}
"""

try:
    # Open the file in append mode
    with open(file_path, 'a') as file:
        # Append content to the file
        file.write(content_to_append)
    print("Content has been successfully appended to the file.")

    # Open the file in read mode to verify the content
    with open(file_path, 'r') as file:
        file_contents = file.read()
        print("File contents after appending:")
        print(file_contents)


