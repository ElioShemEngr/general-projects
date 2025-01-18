import os
import shutil
from pathlib import Path
import logging
from datetime import datetime

# Definición de extensiones por tipo de archivo
FILE_TYPES = {
    'Imágenes': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.ico', '.raw'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.mpeg', '.3gp'],
    'Música': ['.mp3', '.wav', '.flac', '.m4a', '.aac', '.ogg', '.wma', '.mid', '.midi'],
    'Documentos': [
        '.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt',
        '.xls', '.xlsx', '.csv', '.ods',
        '.ppt', '.pptx', '.odp'
    ],
    'Comprimidos': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
    'Ejecutables': ['.exe', '.msi', '.bat', '.cmd', '.sh'],
    'Código': [
        '.py', '.java', '.cpp', '.c', '.h', '.cs', '.js', '.html', 
        '.css', '.php', '.rb', '.swift', '.kt', '.go'
    ]
}

def setup_logging():
    """Configura el sistema de logging"""
    log_folder = Path('logs')
    log_folder.mkdir(exist_ok=True)
    
    log_file = log_folder / f'file_organizer_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

def get_file_type(extension):
    """Determina el tipo de archivo basado en su extensión"""
    extension = extension.lower()
    for file_type, extensions in FILE_TYPES.items():
        if extension in extensions:
            return file_type
    return 'Otros'

def create_directory_structure(base_path):
    """Crea la estructura de directorios para organizar los archivos"""
    directories = list(FILE_TYPES.keys()) + ['Otros']
    for directory in directories:
        dir_path = Path(base_path) / directory
        dir_path.mkdir(exist_ok=True)
        logging.info(f'Directorio creado/verificado: {dir_path}')

def organize_files(source_path, dest_path):
    """Organiza los archivos por tipo"""
    source_path = Path(source_path)
    dest_path = Path(dest_path)
    
    # Contadores para estadísticas
    stats = {
        'archivos_movidos': 0,
        'errores': 0,
        'tipos_encontrados': {}
    }
    
    try:
        # Crear estructura de directorios
        create_directory_structure(dest_path)
        
        # Procesar archivos
        for file_path in source_path.rglob('*'):
            if file_path.is_file():
                try:
                    # Obtener tipo de archivo
                    file_type = get_file_type(file_path.suffix)
                    
                    # Actualizar estadísticas
                    stats['tipos_encontrados'][file_type] = stats['tipos_encontrados'].get(file_type, 0) + 1
                    
                    # Crear ruta destino
                    destination = dest_path / file_type / file_path.name
                    
                    # Si ya existe un archivo con el mismo nombre, agregar un número
                    counter = 1
                    while destination.exists():
                        new_name = f"{file_path.stem}_{counter}{file_path.suffix}"
                        destination = dest_path / file_type / new_name
                        counter += 1
                    
                    # Mover archivo
                    shutil.move(str(file_path), str(destination))
                    logging.info(f'Archivo movido: {file_path.name} -> {file_type}/')
                    stats['archivos_movidos'] += 1
                    
                except Exception as e:
                    logging.error(f'Error al mover {file_path}: {str(e)}')
                    stats['errores'] += 1
        
        # Mostrar resumen
        logging.info('\nResumen de organización:')
        logging.info(f'Total de archivos movidos: {stats["archivos_movidos"]}')
        logging.info(f'Errores encontrados: {stats["errores"]}')
        logging.info('\nArchivos por tipo:')
        for tipo, cantidad in stats['tipos_encontrados'].items():
            logging.info(f'{tipo}: {cantidad} archivos')
            
    except Exception as e:
        logging.error(f'Error general: {str(e)}')
        raise

def main():
    """Función principal"""
    setup_logging()
    logging.info('Iniciando organización de archivos...')
    
    try:
        # Obtener rutas de origen y destino
        source_path = input("Ingrese la ruta de la carpeta a organizar: ").strip()
        dest_path = input("Ingrese la ruta de destino (dejar en blanco para usar la misma carpeta): ").strip()
        
        # Si no se especifica destino, usar la misma carpeta
        if not dest_path:
            dest_path = source_path
        
        # Verificar que las rutas existan
        if not os.path.exists(source_path):
            raise ValueError("La carpeta de origen no existe")
        
        # Organizar archivos
        organize_files(source_path, dest_path)
        
        logging.info('Organización completada exitosamente')
        
    except Exception as e:
        logging.error(f'Error en la ejecución: {str(e)}')
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main()