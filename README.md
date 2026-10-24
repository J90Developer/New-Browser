# 🦊 FoxQuantum Browser

Un navegador web profesional inspirado en **Mozilla Firefox (Quantum & Proton UI)** con arquitectura tri-lenguaje ejecutable en **Python**, **C++** y **C# (.NET)**.

---

## 📦 Paquete de Instalación (Setup Package)

Se ha creado un paquete de instalación profesional y autónomo para Windows, ubicado en la carpeta **[`dist/`](file:///c:/Users/JUANDE/Downloads/Navegador/dist/)**:

1. **[`FoxQuantum_Setup.exe`](file:///c:/Users/JUANDE/Downloads/Navegador/dist/FoxQuantum_Setup.exe)**:
   - Instalador ejecutable independiente (Single-File Standalone Wizard) al estilo del instalador oficial de Mozilla Firefox.
   - Permite elegir la ruta de instalación (por defecto: `%LocalAppData%\Programs\FoxQuantum`).
   - Crea automáticamente los accesos directos en el **Escritorio** y en el **Menú Inicio** con su icono oficial.
   - Incluye desinstalador integrado (`Uninstall.exe`).
   - Opción de lanzar FoxQuantum Browser inmediatamente al terminar la instalación.

2. **[`FoxQuantum_Portable.zip`](file:///c:/Users/JUANDE/Downloads/Navegador/dist/FoxQuantum_Portable.zip)**:
   - Versión portable comprimida lista para descomprimir y usar sin necesidad de instalación.

> Para regenerar el instalador en cualquier momento tras hacer cambios en el código, simplemente ejecuta **[`build_installer.bat`](file:///c:/Users/JUANDE/Downloads/Navegador/build_installer.bat)** o `python build_installer.py`.

---

## 🌟 Características Principales

- **Diseño Mozilla Firefox Fiel**:
  - Paleta oficial oscura (`#1C1B22`, `#2B2A33`, acentos en degradado fucsia y naranja).
  - Barra de pestañas superiores con curvatura Proton, pestañas dinámicas con botón de cierre individual.
  - Barra de herramientas con botones de navegación estilizados: **Atrás**, **Adelante**, **Recargar**, **Home**.
  - **AwesomeBar** (Barra de direcciones inteligente): detección de URLs y motor de búsqueda (DuckDuckGo por defecto), badge dinámico de seguridad SSL/TLS (`🔒` HTTPS, `⚠️` HTTP, `🌐` Local).
  - **Página de Nueva Pestaña (New Tab)** idéntica a Firefox con barra de búsqueda central, logo animado y accesos directos (*DuckDuckGo, GitHub, MDN Web Docs, Wikipedia, YouTube, Reddit*).
  - Botón de favoritos (`☆` / `★`) con guardado instantáneo en la barra de marcadores.
  - Menú hamburguesa (`☰`) con acceso a marcadores, historial, descargas, zoom y acerca de.
  - Modo **Navegación Privada** independiente (*Off-The-Record*).
  - Herramientas de desarrollador integradas (**F12 / DevTools**).
  - Gestor de descargas con notificaciones y progreso.

---

## 🏗 Arquitectura Multi-Lenguaje

```
Navegador/
├── dist/                            # Paquetes listos para distribución
│   ├── FoxQuantum_Setup.exe         # Instalador ejecutable GUI independiente
│   └── FoxQuantum_Portable.zip      # Edición portable comprimida
├── installer/                       # Código fuente del instalador
│   ├── FoxQuantum_Setup.cs          # Asistente de instalación estilo Firefox
│   └── Uninstall.cs                 # Desinstalador automático
├── python/                          # Implementación completa en Python WebEngine
│   ├── core/                        # Historial, Marcadores, Descargas
│   │   ├── bookmarks_manager.py
│   │   ├── history_manager.py
│   │   └── download_manager.py
│   ├── ui/                          # Interfaz PyQt6 estilo Firefox Proton
│   │   ├── main_window.py
│   │   ├── navigation_bar.py
│   │   ├── styles.py                # Estilos QSS Firefox oficiales
│   │   └── dialogs.py
│   ├── main.py                      # Punto de entrada WebEngine
│   └── requirements.txt
├── cpp/                             # Implementación Nativa en C++
│   ├── include/BrowserApp.h
│   ├── src/BrowserApp.cpp
│   ├── src/main.cpp
│   ├── CMakeLists.txt
│   └── FoxQuantumBrowser.exe        # Binario compilado nativo Win32
├── csharp/                          # Implementación en C# .NET
│   ├── src/FoxBrowser.cs
│   ├── FoxQuantumBrowser.csproj     # Proyecto .NET 9
│   └── FoxQuantumBrowser_CS.exe     # Binario compilado .NET WinForms
├── shared/                          # Recursos y Datos Compartidos
│   ├── assets/
│   │   ├── newtab.html              # Página de inicio estilo Firefox
│   │   ├── foxquantum.ico           # Icono de alta resolución
│   │   └── foxquantum.png
│   └── data/
│       ├── bookmarks.json           # Marcadores compartidos
│       ├── history.json             # Historial compartido
│       └── preferences.json         # Configuración y preferencias
├── build_installer.py               # Generador automatizado del instalador
├── build_installer.bat              # Acceso directo para construir el instalador
├── launcher.py                      # Lanzador y selector interactivo de motor
├── run.bat                          # Acceso directo al lanzador universal
├── run_python.bat                   # Ejecutar versión Python directamente
├── run_cpp.bat                      # Ejecutar versión C++ directamente
└── run_csharp.bat                   # Ejecutar versión C# directamente
```

---

## 🚀 Cómo Ejecutar

### 1. Lanzador Universal (Recomendado)
Haz doble clic en **[`run.bat`](file:///c:/Users/JUANDE/Downloads/Navegador/run.bat)** o ejecuta en la terminal:
```bash
python launcher.py
```
Aparecerá un menú interactivo para seleccionar si deseas iniciar la versión de **Python (WebEngine)**, **C++** o **C#**, o recompilar los binarios.

---

### 2. Ejecución Directa por Lenguaje

#### 🐍 Versión Python (PyQt6 Quantum WebEngine)
Ofrece soporte completo de HTML5, CSS3, JavaScript moderno, WebGL y aceleración por hardware:
```bash
run_python.bat
# o bien:
python launcher.py --lang python
```

#### ⚡ Versión C++ (Native Win32 High Performance Core)
Ejecutable ultra liviano compilado con MinGW C++17:
```bash
run_cpp.bat
# o bien:
python launcher.py --lang cpp
```

#### 🔷 Versión C# (.NET WinForms & WebView Edition)
Ejecutable de escritorio compilado para Windows:
```bash
run_csharp.bat
# o bien:
python launcher.py --lang csharp
```

---

## ⌨ Atajos de Teclado

| Atajo | Acción |
|---|---|
| `Ctrl + T` | Abrir nueva pestaña |
| `Ctrl + W` | Cerrar pestaña activa |
| `Ctrl + L` | Seleccionar y enfocar barra de direcciones |
| `Ctrl + R` / `F5` | Recargar página actual |
| `Alt + ←` | Retroceder en el historial |
| `Alt + →` | Avanzar en el historial |
| `Ctrl + D` | Añadir página a marcadores |
| `Ctrl + B` | Abrir catálogo de marcadores |
| `Ctrl + H` | Abrir catálogo de historial |
| `Ctrl + Shift + P` | Abrir ventana de navegación privada |
| `Ctrl + +` / `Ctrl + -` | Aumentar / Reducir zoom de lectura |
| `Ctrl + 0` | Restablecer zoom al 100% |
| `F12` | Abrir Herramientas de Desarrollador (DevTools) |
