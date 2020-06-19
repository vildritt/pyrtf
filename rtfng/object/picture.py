from binascii import hexlify

from rtfng.document.base import RawCode
import rtfng.misc.image_utils


class Image(RawCode):

    #  Need to add in the width and height in twips as it crashes
    #  word xp with these values.  Still working out the most
    #  efficient way of getting these values.
    # \picscalex100\picscaley100\piccropl0\piccropr0\piccropt0\piccropb0
    # picwgoal900\pichgoal281

    PNG_LIB = 'pngblip'
    JPG_LIB = 'jpegblip'
    PICT_TYPES = {
        'png': PNG_LIB,
        'jpg': JPG_LIB
    }

    def __init__(self, file_name, **kwargs):

        img_info = rtfng.misc.image_utils.get_image_info_from_file(file_name)
        if not img_info:
            pass

        width, height, pict_type = img_info
        pict_type = self.PICT_TYPES[pict_type]

        codes = [
            pict_type,
            'picwgoal%s' % (width * 20),
            'pichgoal%s' % (height * 20)
        ]
        for kwarg, code, default in [
                ('scale_x', 'scalex', '100'), 
                ('scale_y', 'scaley', '100'), 
                ('crop_left', 'cropl', '0'), 
                ('crop_right', 'cropr', '0'), 
                ('crop_top', 'cropt', '0'),
                ('crop_bottom', 'cropb', '0')]:
            codes.append('pic%s%s' % (code, kwargs.pop(kwarg, default)))

        # Reset back to the start of the file to get all of it and now
        # turn it into hex.
        with open(file_name, 'rb') as fin:
            fin.seek(0, 0)
            data = []
            image = hexlify(fin.read()).decode("ascii")
            for i in range(0, len(image), 128):
                data.append(image[i:i + 128])

            data = r'{\pict{\%s}%s}' % ('\\'.join(codes), '\n'.join(data))
            RawCode.__init__(self, data)

    def ToRawCode(self, var_name):
        return '%s = RawCode( """%s""" )' % (var_name, self.Data)
