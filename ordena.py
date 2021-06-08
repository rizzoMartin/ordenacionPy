import sys
import os
import shutil

original = ""
mismo_nombre = []
existe = False

def move(file, folder):
    try:
        global original
        global existe
        dest = original + folder
        if os.path.exists(dest + file):
            os.chdir(dest)
            dest_files = os.listdir()
            os.chdir(original)
            for aux in dest_files:
                if aux == file:
                    mismo_nombre.append(aux)
                    if aux.find("(1)") != -1:
                        aux = aux.replace(str(len(mismo_nombre) - 1), str(len(mismo_nombre)))
                    else:
                        file_no_extension, extension = os.path.splitext(file)
                        aux = file_no_extension + " (" + str(len(mismo_nombre)) + ")" + extension
                    existe = True
                    move(aux, folder)
                    break
        if existe:
            file_no_extension, extension = os.path.splitext(file)
            file_no_extension_aux = file_no_extension.split(" (")
            file_no_extension = file_no_extension_aux[0]
            src = original + file_no_extension + extension
            dst = original + file_no_extension + " (" + str(len(mismo_nombre)) + ")" + extension
            os.renames(src, dst)
            file = file_no_extension + " (" + str(len(mismo_nombre)) + ")" + extension
        original = original + file
        shutil.move(original, dest)
        original = original.replace(file, "")
    except:
        pass

def create_folders():
    if not os.path.exists("ejecutables"):
        os.makedirs("ejecutables")
        print("directorio ejecutables creado")

    if not os.path.exists("comprimidos"):
        os.makedirs("comprimidos")
        print("directorio comprimidos creado")

    if not os.path.exists("pdfs"):
        os.makedirs("pdfs")
        print("directorio pdfs creado")

    if not os.path.exists("imagenes"):
        os.makedirs("imagenes")
        print("directorio imagenes creado")
    
    if not os.path.exists("restos"):
        os.makedirs("restos")
        print("directorio imagenes creado")


def move_files():
    all_files = os.listdir()
    for file in all_files:
        if not os.path.isdir(file):
            if file.find("pdf") != -1:
                move(file, "pdfs\\")
            elif file.find("exe") != -1:
                move(file, "ejecutables\\")
            elif (file.find("zip") != -1) or (file.find("rar") != -1):
                move(file, "comprimidos\\")
            elif (file.find("jpg") != -1) or (file.find("jpeg") != -1) or (file.find("png") != -1):
                move(file, "imagenes\\")
            else:
                move(file, "restos\\")


def start():
    global original

    if(len(sys.argv) == 2):
        original = sys.argv[1] + "\\"
    else:
        original = "C:\\Users\\marti\\Downloads\\"

    os.chdir(original)
    print("Vamos a ordenar la carpeta " + os.getcwd())
    create_folders()
    move_files()


if(__name__ == "__main__"):
    start()