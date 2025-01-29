import numpy as np
from PIL import Image

# you will need to pip install pillow and numpy to use this class...
class RifImage:
    """
    RifImage is a custom image file format for educational purposes.
    It has a 9-byte header specifying the image's dimensions, followed by 
    RGB values of the image's pixels. RGB values are each specified as 8-bit 
    unsigned integers.
    """
    def __init__(self, file_path: str, is_jpeg: bool = False) -> None:
        """
        Initializes the RifImage object.

        Args:
            file_path (str): The path to the image file.
            is_jpeg (bool, optional): If the given file is in JPEG format. Defaults to False.
        """  # noqa: E501
        if is_jpeg:
            self._image = Image.open(file_path).convert('RGB')
        else:
            array_data = self._load_rif(file_path)
            self._image = Image.fromarray(array_data)

    @staticmethod
    def _load_rif(rif_file_name: str) -> np.ndarray:
        """
        Loads image data from a RIF file.

        Args:
            rif_file_name (str): The path to the RIF file.

        Returns:
            np.ndarray: The image represented as a NumPy array.
        """
        with open(rif_file_name, 'rb') as file:
            header_w, header_h = file.read(9).decode('utf8').split('x')
            byte_data = file.read(3 * int(header_w) * int(header_h))
        return np.frombuffer(byte_data, dtype=np.uint8).reshape(int(header_w), int(header_h), 3)

    def save_as_jpeg(self, file_path: str) -> None:
        """
        Save the image as a JPEG.

        Args:
            file_path (str): The path to save the JPEG image.
        """
        self._image.save(file_path, format='JPEG')

    def save_as_rif(self, file_path: str) -> None:
        """
        Save the image in RIF format.

        Args:
            file_path (str): The path to save the RIF file.
        """
        array_data = np.array(self._image)
        h, w, _ = array_data.shape
        with open(file_path, "wb") as file:
            file.write(f'{h:04}x{w:04}'.encode('utf8'))
            file.write(bytes(array_data.flatten()))
