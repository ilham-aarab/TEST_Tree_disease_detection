# preprocessing.py

import cv2

import cv2
import pywt

# Contrast improvement for images
def retinex_transform(img):
    # Apply Retinex transformation
    # Here we apply a simple histogram equalization
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
    return cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

# Edge enhancement for images
def edge_enhancement(img):
    # Apply edge enhancement using Laplacian
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(img_gray, cv2.CV_64F)
    sharpened_img = cv2.addWeighted(img_gray, 1.5, laplacian, -0.5, 0)
    return cv2.cvtColor(sharpened_img, cv2.COLOR_GRAY2BGR)

# Multiresolution Image Fusion using wavelet transform
def wavelet_fusion(images):
    # Apply Multiresolution Image Fusion using wavelet transform
    # Here we use the simplest method, taking the average of corresponding pixels
    coeffs = [pywt.dwt2(img, 'haar') for img in images]
    LL = sum(c[0] for c in coeffs) / len(coeffs)
    return pywt.idwt2((LL, None, None, None), 'haar')

def preprocess_rgb(img):
    # Normalization
    img = cv2.normalize(img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray

def preprocess_multispectral(img):
    # Apply Retinex transformation
    img_retinex = retinex_transform(img)

    # Apply edge enhancement
    img_enhanced = edge_enhancement(img_retinex)

    # Apply Multiresolution Image Fusion
    fused_image = wavelet_fusion([img_retinex, img_enhanced])

    # Example of image processing (resize)
    img_resized = cv2.resize(fused_image, (256, 256))
    return img_resized
