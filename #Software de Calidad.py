#Software de Calidad
# Rutas de motor OCR y archivos
TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Ruta al ejecutable de Tesseract
LANG_CONFIG = 'spa'  # Modelo de idioma español
DPI_TARGET = 300     # Resolución mínima recomendada para legibilidad

# Parámetros para binarización y reducción de ruido con OpenCV
BLUR_KERNEL_SIZE = (5, 5)  # Tamaño de filtro para suavizado
ADAPTIVE_BLOCK_SIZE = 11  # Umbralización adaptativa para evitar sombras de escaneo
ADAPTIVE_C = 2             # Constante de ajuste de umbral

# Variables de umbral de confianza y calidad de texto
MIN_CONFIDENCE_SCORE = 80.0  # Porcentaje mínimo de confianza global por página
MIN_WORD_CONFIDENCE = 70.0   # Confianza mínima permitida por palabra individual
MAX_SYNTAX_ERROR_RATE = 0.05 # Límite máximo tolerado de palabras mal compuestas (5%)

# Diccionario para almacenar el resultado del análisis de un documento
document_result = {
    "filename": "escritura_publica_102.pdf",
    "total_words": 0,
    "low_confidence_words": [],  # Lista de palabras con bajo score de Tesseract
    "syntax_errors": [],         # Lista de palabras desconocidas u oraciones mal formadas
    "global_confidence": 0.0,
    "is_legible": False
}

#OpenCV	Detectar desenfoque, inclinación, sombras y defectos visuales.

#PyMuPDF	Leer y procesar archivos PDF, contar páginas y extraer texto existente.

#OCR (PaddleOCR o Tesseract)	Reconocer las palabras de documentos escaneados como imágenes.

#RapidFuzz	Comparar textos y detectar posibles diferencias entre minuta y escritura.

#pandas	Calcular indicadores y exportar reportes a Excel.

#Streamlit o Flask	Construir la interfaz para el personal.