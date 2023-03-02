import subprocess
import os
def main():
    os.chmod("./main", 0o755)

    resultado = subprocess.run(['./main'], capture_output=True)
    if resultado.returncode == 0:
        print("Éxito")
    else:
        print("Error")



if __name__ == "__main__":
    main()