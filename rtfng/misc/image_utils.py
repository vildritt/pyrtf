import os


_JPEG_SIGNATURE = b"\xFF\xD8"
_JPEG_MARKER_FF = b"\xFF"
_JPEG_MARKERS = [a for a in b"\xC0\xC1\xC2\xC3\xC5\xC6\xC7\xC9\xCA\xCB\xCD\xCE\xCF"]
_JPEG_MIN_BLOCK_LEN = 2

_PNG_SIGNATURE = "\x89\x50\x4e"
_PNG_W_OFF = 18
_PNG_H_OFF = 22


def bytes2uint16_le(buffer):
    return (ord(buffer[0]) << 8) + ord(buffer[1])


def read_uint16_le(bstream):
    return bytes2uint16_le(bstream.read(2))


def get_png_image_size_from_stream(bstream):
    header = bstream.read(PNG_H_OFF + 2)

    if not header.startswith(_PNG_SIGNATURE):
        raise Exception('PNG image parsing failed')

    width = bytes2uint16_le(header(_PNG_W_OFF : _PNG_W_OFF+1))
    height = bytes2uint16_le(header(_PNG_H_OFF : _PNG_H_OFF+1))

    return width, height


def get_jpg_image_size_from_stream(bstream):
    header = bstream.read(2)
    if header != _JPEG_SIGNATURE:
        raise Exception('JPEG parsing failed')

    while True:
        # try get next marker - find FF then find FF ends
        while bstream.read(1) != _JPEG_MARKER_FF:
            pass

        while True:
            if (block_marker := bstream.read(1)) != _JPEG_MARKER_FF:
                break

        block_length = read_uint16_le(bstream)
        if block_length < _JPEG_MIN_BLOCK_LEN:
            raise Exception("Invalid JPEG marker length")

        if block_marker not in _JPEG_MARKERS:
            bstream.read(block_length - _JPEG_MIN_BLOCK_LEN)
            continue
        
        bstream.read(1) # dummy?
        height = read_uint16_le(bstream)
        width = read_uint16_le(bstream)
        return width, height


def get_image_info_from_file(file_name)
    _, ext = os.path.splitext(file_name)
    ext = ext.lower()

    is_png = (ext == ".png")
    is_jpg = (ext in [".jpg", ".jpeg"])
    if not is_png and not is_jpg:
        return None

    with open(file_name, 'rb') as bstream:
        if is_png:
            return *get_png_image_size_from_stream(bstream), "png"
        if is_jpg:
            return *get_jpg_image_size_from_stream(bstream), "jpg"
    return None