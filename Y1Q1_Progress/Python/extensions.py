filename = input("File name: ")
file_extensions = [".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip"]
for a in file_extensions:
    if filename.endswith(a) and (a == ".zip" or a == ".pdf"):
        print(f"application/{a.replace(".", "")}")
        break
    elif filename.endswith(a) and a == ".txt":
        print("text/plain")
        break
    elif filename.endswith(a):
        if a == ".jpg":
            print("image/jpeg")
        else:
            print(f"image/{a.replace(".", "")}")
        break
else:
    print("application/octet-stream")
         
    