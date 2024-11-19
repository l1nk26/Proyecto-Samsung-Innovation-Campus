
"""
IMPORTANTE:
     1)Esta funcion del programa recibe como parametro el path del pdf y retorna el valor de glucosa en el
    examen o un texto por pantalla si no lo encuentra, aun falta: crear un boton con tkinder que le permita al usuario seleccionar el archivo.
      2) Se uso biblioteca pdfplumber

IDEA PARA EL BOTON: 
    
import tkinter as tk
from tkinter import filedialog

def get_file_path():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        print(f"Selected file path: {file_path}")
        # Puedes hacer algo con el path del archivo aquí
    else:
        print("No file selected")

root = tk.Tk()
root.title("Select PDF File")

button = tk.Button(root, text="Select PDF File", command=get_file_path)
button.pack(pady=20)

root.mainloop()

"""
import pdfplumber
path = r'prueba (1).pdf' 
def pdf_read(pdf_path):
    # Ruta al archivo PDF
 
    # Variable para almacenar el valor de glicemia
    glucosa_value = None

    # Abrir el archivo PDF
    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:
            text = page.extract_text()
            
            # Verificar si el texto fue extraído correctamente
            if text:
                lines = text.split('\n')
                # Buscar la línea que contiene "Glicemia"
                for line in lines:
                    line = line.lower()
                    if "glicemia" in line:
                        # Dividir la línea en palabras
                        words = line.split()
                        if "glicemia" in words:
                            index = words.index("glicemia")
                            if index + 1 < len(words):
                                glucosa_value = words[index + 1]  # Valor de glicemia
                        break 
                    elif "glucosa" in line:
                        # Dividir la línea en palabras
                        words = line.split()
                        if "glucosa" in words:
                            index = words.index("glucosa")
                            if index + 1 < len(words):
                                glucosa_value = words[index + 1]  # Valor de glicemia
                        break    
    # Mostrar el resultado
    if glucosa_value:
        return glucosa_value 
    else:
        print('No se encontró el valor de Glicemia/Glucosa  en el PDF.')


var = pdf_read(path)
print(var)


