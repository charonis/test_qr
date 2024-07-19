import qrcode


def qr(name: str, first_name: str, pathonimy: str):
    data = f"{name}-{first_name}-{pathonimy}"
    filename = f"{name}_{first_name}-{pathonimy}.png"
    img = qrcode.make(data)
    img.save(f"storage/{filename}")