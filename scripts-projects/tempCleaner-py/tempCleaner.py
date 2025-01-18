import os
import shutil
import tempfile
from datetime import datetime
import logging
from pathlib import Path

def setup_logging():
    """Configura el sistema de logging"""
    log_file = f'temp_cleanup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

def get_temp_folders():
    """Obtiene las rutas de las carpetas temporales"""
    temp_folders = []
    
    # Carpeta %temp%
    temp_folders.append(tempfile.gettempdir())
    
    # Carpeta Windows\Temp
    windows_temp = os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'Temp')
    temp_folders.append(windows_temp)
    
    return temp_folders

def clean_temp_folder(folder_path):
    """Limpia una carpeta temporal específica"""
    logging.info(f'Limpiando carpeta: {folder_path}')
    
    try:
        folder = Path(folder_path)
        if not folder.exists():
            logging.warning(f'La carpeta {folder_path} no existe')
            return
        
        # Contador de archivos eliminados
        deleted_files = 0
        failed_files = 0
        
        for item in folder.glob('**/*'):
            try:
                if item.is_file():
                    item.unlink()
                    deleted_files += 1
                elif item.is_dir() and not any(item.iterdir()):
                    item.rmdir()
                    deleted_files += 1
            except PermissionError:
                logging.warning(f'No se pudo eliminar (en uso): {item}')
                failed_files += 1
            except Exception as e:
                logging.error(f'Error al eliminar {item}: {str(e)}')
                failed_files += 1
        
        logging.info(f'Archivos eliminados: {deleted_files}')
        logging.info(f'Archivos no eliminados: {failed_files}')
        
    except Exception as e:
        logging.error(f'Error al limpiar la carpeta {folder_path}: {str(e)}')

def main():
    """Función principal"""
    try:
        # Configurar logging
        setup_logging()
        
        logging.info('Iniciando limpieza de archivos temporales...')
        
        # Obtener carpetas temporales
        temp_folders = get_temp_folders()
        
        # Limpiar cada carpeta
        for folder in temp_folders:
            clean_temp_folder(folder)
            
        logging.info('Limpieza completada')
        
    except Exception as e:
        logging.error(f'Error general: {str(e)}')

if __name__ == "__main__":
    main()