import qrcode
import qrcode.image.svg

from qrcode.image.styledpil import StyledPilImage

def make_the_qr(id: str):

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        image_factory=qrcode.image.svg.SvgPathImage,
        border=0,
        box_size=23
    )

    # agrego data al qr
    qr.add_data(f'ejemplo')

    qr.make(fit=True)

    img = qr.make_image(attrib={'class': 'some-css-class'})

    # convierto la imagen en un string
    qr_string = img.to_string()

    return qr_string.decode("utf-8")