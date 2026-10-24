import os
import sys
import subprocess
import zipfile
import shutil

# Asegurar codificación utf-8 para salida
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INSTALLER_DIR = os.path.join(BASE_DIR, "installer")
DIST_DIR = os.path.join(BASE_DIR, "dist")
CSC_PATH = r"C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe"

def log(msg, color="94"):
    print(f"\033[{color}m{msg}\033[0m")

def compile_uninstaller():
    log("\n[1/4] Compilando Desinstalador (Uninstall.exe)...", "94")
    src = os.path.join(INSTALLER_DIR, "Uninstall.cs")
    out = os.path.join(INSTALLER_DIR, "Uninstall.exe")
    ico = os.path.join(BASE_DIR, "shared", "assets", "foxquantum.ico")

    cmd = [
        CSC_PATH,
        "/target:winexe",
        "/optimize+",
        f"/out:{out}",
        f"/win32icon:{ico}",
        "/r:System.Windows.Forms.dll,System.Drawing.dll,System.dll",
        src
    ]
    res = subprocess.run(cmd)
    if res.returncode == 0:
        log("[OK] Uninstall.exe compilado exitosamente.", "92")
    else:
        log("[ERROR] Fallo la compilacion de Uninstall.exe", "91")
        sys.exit(1)

def create_payload_zip():
    log("\n[2/4] Creando paquete comprimido de la aplicacion (payload.zip)...", "94")
    payload_zip = os.path.join(INSTALLER_DIR, "payload.zip")

    if os.path.exists(payload_zip):
        os.remove(payload_zip)

    include_dirs = ["python", "cpp", "csharp", "shared"]
    include_files = [
        "launcher.py", "run.bat", "run_python.bat", "run_cpp.bat", "run_csharp.bat", "README.md"
    ]

    with zipfile.ZipFile(payload_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        # Añadir directorios
        for d in include_dirs:
            full_d = os.path.join(BASE_DIR, d)
            for root, dirs, files in os.walk(full_d):
                # Ignorar caches
                if "__pycache__" in root or ".git" in root:
                    continue
                for f in files:
                    if f.endswith(".pyc"):
                        continue
                    file_path = os.path.join(root, f)
                    arcname = os.path.relpath(file_path, BASE_DIR)
                    zf.write(file_path, arcname)

        # Añadir archivos sueltos de la raíz
        for f in include_files:
            file_path = os.path.join(BASE_DIR, f)
            if os.path.exists(file_path):
                zf.write(file_path, f)

        # Añadir Uninstall.exe
        uninst_exe = os.path.join(INSTALLER_DIR, "Uninstall.exe")
        if os.path.exists(uninst_exe):
            zf.write(uninst_exe, "Uninstall.exe")

    size_mb = os.path.getsize(payload_zip) / (1024 * 1024)
    log(f"[OK] payload.zip generado ({size_mb:.2f} MB).", "92")
    return payload_zip

def compile_installer_exe(payload_zip):
    log("\n[3/4] Compilando Instalador Autonomo (FoxQuantum_Setup.exe)...", "94")
    os.makedirs(DIST_DIR, exist_ok=True)
    src = os.path.join(INSTALLER_DIR, "FoxQuantum_Setup.cs")
    out_exe = os.path.join(DIST_DIR, "FoxQuantum_Setup.exe")
    ico = os.path.join(BASE_DIR, "shared", "assets", "foxquantum.ico")

    cmd = [
        CSC_PATH,
        "/target:winexe",
        "/optimize+",
        f"/out:{out_exe}",
        f"/win32icon:{ico}",
        f"/resource:{payload_zip},payload.zip",
        "/r:System.Windows.Forms.dll,System.Drawing.dll,System.dll,System.IO.Compression.dll,System.IO.Compression.FileSystem.dll",
        src
    ]
    res = subprocess.run(cmd)
    if res.returncode == 0:
        size_mb = os.path.getsize(out_exe) / (1024 * 1024)
        log(f"[OK] FoxQuantum_Setup.exe compilado exitosamente ({size_mb:.2f} MB).", "92")
    else:
        log("[ERROR] Fallo la compilacion de FoxQuantum_Setup.exe", "91")
        sys.exit(1)

def create_portable_zip(payload_zip):
    log("\n[4/4] Generando Edicion Portable (FoxQuantum_Portable.zip)...", "94")
    dest_zip = os.path.join(DIST_DIR, "FoxQuantum_Portable.zip")
    shutil.copy2(payload_zip, dest_zip)
    size_mb = os.path.getsize(dest_zip) / (1024 * 1024)
    log(f"[OK] FoxQuantum_Portable.zip listo ({size_mb:.2f} MB).", "92")

def main():
    log("==================================================", "95")
    log("  GENERADOR DEL PAQUETE DE INSTALACION FOXQUANTUM ", "95")
    log("==================================================", "95")

    compile_uninstaller()
    payload = create_payload_zip()
    compile_installer_exe(payload)
    create_portable_zip(payload)

    log("\n==================================================", "92")
    log("  PAQUETES DE DISTRIBUCION CREADOS CON EXITO!", "92")
    log("==================================================", "92")
    log(f"  * Instalador GUI: {os.path.join(DIST_DIR, 'FoxQuantum_Setup.exe')}")
    log(f"  * Version Portable: {os.path.join(DIST_DIR, 'FoxQuantum_Portable.zip')}")

if __name__ == "__main__":
    main()
