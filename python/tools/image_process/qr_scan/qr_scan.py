import os
import requests
from io import BytesIO
from pyzbar import pyzbar
from PIL import Image,ImageEnhance
 
import qrcode
 
 
def create_ewm(data, img_file):
	""" 生成二维码 """
	qr = qrcode.QRCode(
		version=1,
		error_correction=qrcode.constants.ERROR_CORRECT_H,
		box_size=10,
		border=4
	)
	# 传入数据
	qr.add_data(data)
	qr.make(fit=True)
	# 生成二维码
	img = qr.make_image()
	# 保存二维码
	img.save(img_file)
	# 显示二维码
	img.show()
 
 
def get_ewm(img_adds):
    """ 读取二维码的内容： img_adds：二维码地址（可以是网址也可是本地地址 """
    if os.path.isfile(img_adds):
        # 从本地加载二维码图片
        img = Image.open(img_adds)
    else:
        # 从网络下载并加载二维码图片
        rq_img = requests.get(img_adds).content
        img = Image.open(BytesIO(rq_img))
 
    # img.show()  # 显示图片，测试用
 
    txt_list = pyzbar.decode(img)
 
    for txt in txt_list:
        barcodeData = txt.data.decode("utf-8")
        print(barcodeData)
 
if __name__ == '__main__':
    get_ewm('qr_code.png')
    #get_ewm('https://gqrcode.alicdn.com/img?type=cs&shop_id=445653319&seller_id=3035998964&w=140&h=140&el=q&v=1')
