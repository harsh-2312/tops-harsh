import qrcode as qr

upi_id="lharsh885@okaxis"

Gpay_url=f"upi://pay?pa={upi_id}&pn=recipient%20Name&mc=1234"

upi=qr.make(Gpay_url)
upi.save("googalpay.png")
upi.show()
