#!/usr/bin/env python3
"""
FoxQuantum Browser - Suite Tri-Lenguaje Profesional (Python, C++, C#)
Inspirado en el diseño y arquitectura de Mozilla Firefox Quantum.
"""

import os
import sys
import subprocess
import argparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

BANNER = r"""
  ______            ____                   __                 
 / ____/___  _  __/ __ \__  ______ _____  / /___  ______ ___  
/ /_  / __ \| |/_/ / / / / / / __ `/ __ \/ __/ / / / __ `__ \ 
/ __/ / /_/ />  </ /_/ / /_/ / /_/ / / / / /_/ /_/ / / / / / / 
/_/    \____/_/|_|\___\_\__,_/\__,_/_/ /_/\__/\__,_/_/ /_/ /_/  
                                                               
   * Mozilla Firefox Quantum & Proton Inspired Web Browser *
              [ Python  |  C++  |  C# .NET ]
"""

def print_banner():
    print("\033[95m" + BANNER + "\033[0m")

def run_python_browser():
    print("\n\033[94m[*] Iniciando FoxQuantum Browser [Python + PyQt6 WebEngine]...\033[0m")
    main_script = os.path.join(BASE_DIR, "python", "main.py")
    subprocess.run([sys.executable, main_script])

def run_cpp_browser():
    exe_path = os.path.join(BASE_DIR, "cpp", "FoxQuantumBrowser.exe")
    if not os.path.exists(exe_path):
        print("\n\033[93m[!] Binario C++ no encontrado. Compilando...\033[0m")
        compile_cpp()
    
    if os.path.exists(exe_path):
        print("\n\033[92m[*] Ejecutando FoxQuantum Browser [C++ Native Win32 Core]...\033[0m")
        subprocess.Popen([exe_path], cwd=os.path.join(BASE_DIR, "cpp"))
    else:
        print("\033[91m[X] No se pudo compilar el binario C++.\033[0m")

def run_csharp_browser():
    exe_path = os.path.join(BASE_DIR, "csharp", "FoxQuantumBrowser_CS.exe")
    if not os.path.exists(exe_path):
        print("\n\033[93m[!] Binario C# no encontrado. Compilando...\033[0m")
        compile_csharp()
    
    if os.path.exists(exe_path):
        print("\n\033[92m[*] Ejecutando FoxQuantum Browser [C# .NET Edition]...\033[0m")
        subprocess.Popen([exe_path], cwd=os.path.join(BASE_DIR, "csharp"))
    else:
        print("\033[91m[X] No se pudo compilar el binario C#.\033[0m")

def compile_cpp():
    src_main = os.path.join(BASE_DIR, "cpp", "src", "main.cpp")
    src_app = os.path.join(BASE_DIR, "cpp", "src", "BrowserApp.cpp")
    inc_dir = os.path.join(BASE_DIR, "cpp", "include")
    out_exe = os.path.join(BASE_DIR, "cpp", "FoxQuantumBrowser.exe")

    cmd = [
        "g++", "-O2", "-std=c++17",
        src_main, src_app,
        f"-I{inc_dir}",
        "-mwindows", "-lcomctl32", "-lshell32", "-lole32", "-lgdi32",
        "-o", out_exe
    ]
    print(f"Compilando: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    if result.returncode == 0:
        print("\033[92m[✓] C++ compilado exitosamente.\033[0m")
    else:
        print("\033[91m[X] Error en la compilación C++.\033[0m")

def compile_csharp():
    csc_path = r"C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe"
    src_file = os.path.join(BASE_DIR, "csharp", "src", "FoxBrowser.cs")
    out_exe = os.path.join(BASE_DIR, "csharp", "FoxQuantumBrowser_CS.exe")

    cmd = [
        csc_path,
        "/target:winexe",
        "/optimize+",
        f"/out:{out_exe}",
        "/r:System.Windows.Forms.dll,System.Drawing.dll,System.dll",
        src_file
    ]
    print(f"Compilando C#: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    if result.returncode == 0:
        print("\033[92m[✓] C# compilado exitosamente.\033[0m")
    else:
        print("\033[91m[X] Error en la compilación C#.\033[0m")

def interactive_menu():
    while True:
        print_banner()
        print(" Selecciona el motor de ejecución:")
        print(" --------------------------------------------------")
        print("  [1] Ejecutar en Python (PyQt6 Quantum WebEngine) [Recomendado]")
        print("  [2] Ejecutar en C++ (Native Win32 High-Performance Core)")
        print("  [3] Ejecutar en C# (Desktop .NET WinForms Edition)")
        print("  [4] Recompilar binarios nativos (C++ y C#)")
        print("  [5] Salir")
        print(" --------------------------------------------------")
        
        try:
            choice = input(" Ingresa una opción [1-5]: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nSaliendo...")
            break

        if choice == "1":
            run_python_browser()
            break
        elif choice == "2":
            run_cpp_browser()
            break
        elif choice == "3":
            run_csharp_browser()
            break
        elif choice == "4":
            print("\nRecompilando C++...")
            compile_cpp()
            print("\nRecompilando C#...")
            compile_csharp()
            input("\nPresiona Enter para continuar...")
        elif choice == "5":
            print("\n¡Hasta pronto!")
            break
        else:
            print("\nOpción no válida. Intenta nuevamente.")

def main():
    parser = argparse.ArgumentParser(description="FoxQuantum Browser Launcher")
    parser.add_argument("--lang", choices=["python", "cpp", "csharp", "rebuild"],
                        help="Ejecutar directamente en el lenguaje especificado")
    args = parser.parse_args()

    if args.lang == "python":
        run_python_browser()
    elif args.lang == "cpp":
        run_cpp_browser()
    elif args.lang == "csharp":
        run_csharp_browser()
    elif args.lang == "rebuild":
        compile_cpp()
        compile_csharp()
    else:
        interactive_menu()

if __name__ == "__main__":
    main()
