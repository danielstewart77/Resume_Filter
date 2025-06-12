import logging
import fitz  # PyMuPDF for PDF handling

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def extract_text_from_pdf(file_path: str) -> str:
    """
    Extracts text from a PDF file.

    :param file_path: Path to the PDF file.
    :return: Extracted text as a string.
    """
    logger.info(f"Extracting text from PDF: {file_path}")

    try:
        pdf = fitz.open(file_path)  # Open the file directly
        text = ''
        for page in pdf:
            text += page.get_text()
        logger.info("Text extraction completed.")
        return text
    except Exception as e:
        logger.error(f"Error extracting text from {file_path}: {e}")
        return ""
