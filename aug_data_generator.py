import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import random
import time
import uuid
from albumentations import (VerticalFlip, HorizontalFlip, Flip, RandomRotate90, Rotate, ShiftScaleRotate, CenterCrop, OpticalDistortion, GridDistortion, ElasticTransform, JpegCompression, HueSaturationValue,
                            RGBShift, RandomBrightness, RandomContrast, Blur, MotionBlur, MedianBlur, GaussNoise, CLAHE, ChannelShuffle, InvertImg, RandomGamma, ToGray, PadIfNeeded 
                           )

global img_save_path
img_save_path = './generated_images'

def execute_methods(method_list,img):
	for using_method in method_list:
		if using_method == 'VerticalFlip':
			p_value = random.uniform(0,0.6)
			p_value = round(p_value,1)
			transform = VerticalFlip(p=0.5)
			augmented_image = transform(image=img)['image']
			id_value = uuid.uuid4().hex[:8]
			name = id_value + '-' + using_method + '.jpg'
			write_img(augmented_image,name)
			print("[INFO] Saved image " + name + " in generated_images.")
			time.sleep(1)
		
		if using_method == 'HorizontalFlip':
			p_value = random.uniform(0,0.6)
			p_value = round(p_value,1)
			transform = HorizontalFlip(p=0.5)
			augmented_image = transform(image=img)['image']
			id_value = uuid.uuid4().hex[:8]
			name = id_value + '-' + using_method + '.jpg'
			write_img(augmented_image,name)
			print("[INFO] Saved image " + name + " in generated_images.")
			time.sleep(1)

		if using_method == 'RandomRotate90':
			p_value = random.uniform(0,0.6)
			p_value = round(p_value,1)
			transform = RandomRotate90(p=p_value)
			augmented_image = transform(image=img)['image']
			id_value = uuid.uuid4().hex[:8]
			name = id_value + '-' + using_method + '.jpg'
			write_img(augmented_image,name)
			print("[INFO] Saved image " + name + " in generated_images.")
			time.sleep(1)

		if using_method == 'ShiftScaleRotate':
			angle_value = random.randint(180,360)
			shift_value = random.uniform(0.5,1)
			shift_value = round(shift_value,1)
			scale_value = random.uniform(0.8,2)
			scale_value = round(scale_value,1)
			p_value = random.uniform(0,0.6)
			p_value = round(p_value,1)
			transform = ShiftScaleRotate(shift_limit=shift_value, scale_limit=scale_value, rotate_limit=angle_value, p=p_value)
			augmented_image = transform(image=img)['image']
			id_value = uuid.uuid4().hex[:8]
			name = id_value + '-' + using_method + '.jpg'
			write_img(augmented_image,name)
			print("[INFO] Saved image " + name + " in generated_images.")
			time.sleep(1)

		if using_method == 'CenterCrop':
			size = random.randint(250,400)
			p_value = random.uniform(0,0.6)
			p_value = round(p_value,1)
			transform = CenterCrop(height=size, width=size, p=0.5)
			augmented_image = transform(image=img)['image']
			id_value = uuid.uuid4().hex[:8]
			name = id_value + '-' + using_method + '.jpg'
			write_img(augmented_image,name)
			print("[INFO] Saved image " + name + " in generated_images.")
			time.sleep(1)

		if using_method == 'OpticalDistortion':
			shift_value = random.uniform(0.2,0.6)
			shift_value = round(shift_value,1)
			distort_value = random.uniform(0.1,0.5)
			distort_value = round(distort_value,1)
			p_value = random.uniform(0,0.6)
			p_value = round(p_value,1)
			transform = OpticalDistortion(distort_limit=distort_value, shift_limit=shift_value, p=0.5)
			augmented_image = transform(image=img)['image']
			id_value = uuid.uuid4().hex[:8]
			name = id_value + '-' + using_method + '.jpg'
			write_img(augmented_image,name)
			print("[INFO] Saved image " + name + " in generated_images.")
			time.sleep(1)

		if using_method == 'GridDistortion':
			p_value = random.uniform(0,1)
			p_value = round(p_value,1)
			transform = GridDistortion(p=0.8)
			augmented_image = transform(image=img)['image']
			id_value = uuid.uuid4().hex[:8]
			name = id_value + '-' + using_method + '.jpg'
			write_img(augmented_image,name)
			print("[INFO] Saved image " + name + " in generated_images.")
			time.sleep(1)

		if using_method == 'ElasticTransform':
			alpha_value = random.randint(200,255)
			alpha_affine_value = random.randint(105,150)
			sigma_value = random.randint(155,200)
			p_value = random.uniform(0,0.6)
			p_value = round(p_value,1)
			transform = ElasticTransform(alpha=alpha_value, sigma=sigma_value, alpha_affine=alpha_affine_value, p=0.5)
			augmented_image = transform(image=img)['image']
			id_value = uuid.uuid4().hex[:8]
			name = id_value + '-' + using_method + '.jpg'
			write_img(augmented_image,name)
			print("[INFO] Saved image " + name + " in generated_images.")
			time.sleep(1)

		if using_method == 'JpegCompression':
			lower_value = random.randint(1,5)
			p_value = random.uniform(0,0.6)
			p_value = round(p_value,1)
			transform = JpegCompression(quality_lower=lower_value, quality_upper=100, p=0.5)
			augmented_image = transform(image=img)['image']
			id_value = uuid.uuid4().hex[:8]
			name = id_value + '-' + using_method + '.jpg'
			write_img(augmented_image,name)
			print("[INFO] Saved image " + name + " in generated_images.")
			time.sleep(1)
			
		if using_method == 'HueSaturationValue':
			hue_shift = random.randint(160,180)
			sat_shift = random.randint(20,255)
			val_shift = random.randint(25,255)
			p_value = random.uniform(0,0.6)
			p_value = round(p_value,1)
			transform = HueSaturationValue(hue_shift_limit=hue_shift, sat_shift_limit=sat_shift, val_shift_limit=val_shift, p=0.7)
			augmented_image = transform(image=img)['image']
			id_value = uuid.uuid4().hex[:8]
			name = id_value + '-' + using_method + '.jpg'
			write_img(augmented_image,name)
			print("[INFO] Saved image " + name + " in generated_images.")
			time.sleep(1)

		if using_method == 'RGBShift':
			r_shift = random.randint(100,255)
			g_shift = random.randint(30,255)
			b_shift = random.randint(50,255)
			p_value = random.uniform(0,0.6)
			p_value = round(p_value,1)
			transform = RGBShift(r_shift_limit=r_shift, g_shift_limit=g_shift, b_shift_limit=b_shift, p=0.6)
			augmented_image = transform(image=img)['image']
			id_value = uuid.uuid4().hex[:8]
			name = id_value + '-' + using_method + '.jpg'
			write_img(augmented_image,name)
			print("[INFO] Saved image " + name + " in generated_images.")
			time.sleep(1)

		if using_method == 'MotionBlur':
			p_value = random.uniform(0.7,1)
			p_value = round(p_value,1)
			transform = MotionBlur(p=p_value)
			augmented_image = transform(image=img)['image']
			id_value = uuid.uuid4().hex[:8]
			name = id_value + '-' + using_method + '.jpg'
			write_img(augmented_image,name)
			print("[INFO] Saved image " + name + " in generated_images.")
			time.sleep(1)

		if using_method == 'ChannelShuffle':
			p_value = random.uniform(0,1)
			p_value = round(p_value,1)
			transform = ChannelShuffle(p=1)
			augmented_image = transform(image=img)['image']
			id_value = uuid.uuid4().hex[:8]
			name = id_value + '-' + using_method + '.jpg'
			write_img(augmented_image,name)
			print("[INFO] Saved image " + name + " in generated_images.")
			time.sleep(1)

		if using_method == 'RandomGamma':
			p_value = random.uniform(0,1)
			p_value = round(p_value,1)
			transform = RandomGamma(p=0.7)
			augmented_image = transform(image=img)['image']
			id_value = uuid.uuid4().hex[:8]
			name = id_value + '-' + using_method + '.jpg'
			write_img(augmented_image,name)
			print("[INFO] Saved image " + name + " in generated_images.")
			time.sleep(1)

def show_img(img, figsize=(8, 8)):
    fig, ax = plt.subplots(figsize=figsize)
    ax.grid(False)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.imshow(img)
    plt.imshow(img)

def make_folders(path):
	os.makedirs(path, exist_ok=True)

def write_img(img,name):
	make_folders(img_save_path)
	img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
	cv2.imwrite(img_save_path + '/' + name, img)

def main():
	methods = ['VerticalFlip', 'HorizontalFlip', 'RandomRotate90', 'ShiftScaleRotate', 'CenterCrop', 'OpticalDistortion', 'GridDistortion', 'ElasticTransform', 'JpegCompression', 'HueSaturationValue',
              'RGBShift', 'MotionBlur', 'ChannelShuffle', 'RandomGamma']
    
	num = 8
	for imgs in os.listdir("./images"):
		used_methods = []
		used_methods += random.sample(methods, num)
		print("[INFO] Using methods: ", used_methods)
		img_path = os.path.join('./images',imgs)
		img = cv2.imread(img_path)
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		execute_methods(used_methods,img)


if __name__ == '__main__':
	main()