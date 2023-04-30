import qrcode

features = qrcode.QRCode(version=1,box_size=40,border=3)
features.add_data('https://www.youtube.com/watch?v=FJGRl_ht3xI&list=PLpqGPi6G3Jf1efKbzUObp2W-jsF3MGmdT')
features.make(fit=True)

generate_image=features.make_image(fill_color="black",back_color="white")
generate_image.save('image1.png')