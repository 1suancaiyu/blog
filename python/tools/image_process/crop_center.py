from PIL import Image
im = Image.open('tmp.jpg')


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


image_width, image_height = im.size
im_new = crop_center(im, image_height, int(image_height/16*9))
im_new.save('img_16_9.jpg', quality=95)
im_new = crop_center(im, image_height, int(image_height/4*3))
im_new.save('img_16_9.jpg', quality=95)
im_new = crop_center(im, image_height, int(image_height/3*2))
im_new.save('img_3_2.jpg', quality=95)
im_new = crop_center(im, image_height, int(image_height/1*1))
im_new.save('img_1_1.jpg', quality=95)

