import qrcode
#insert the data you will type in your message
data="I'm the reason why the caged bird sings."

#create the QRCode
img=qrcode.make(data=data)

#Save the qrcode
img.save("SecretMessage.png")

#How can someone view your qr code
#go to this link [https://webqr.com/ ]
#import your code on the field provide