import subprocess

def main():
    resultado = subprocess.run(['envoutput/main'], capture_output=True)
    if resultado.returncode == 0:
        print("Éxito")
    else:
        print("Error")



if __name__ == "__main__":
    main()