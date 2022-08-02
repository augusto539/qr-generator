import qrcode
import qrcode.image.svg

from qrcode.image.styledpil import StyledPilImage

def make_the_qr(id: str):

    qr = qrcode.QRCode(
        image_factory=qrcode.image.svg.SvgPathImage,
        box_size=8
    )

    # agrego data al qr
    qr.add_data(f'ejemplo')

    qr.make(fit=True)

    img = qr.make_image(attrib={'class': 'some-css-class'})

    # convierto la imagen en un string
    qr_string = img.to_string()

    return qr_string.decode("utf-8")