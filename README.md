# image-object-detection-flask

This flask app uses tensorflow/tensorflow:latest docker image to setup environment to use tensorflow

Installation:
1. virtualenv env
2. cd env
3. & .\env\Scripts\activate
4. pip install -r requirements.txt
5. py main.py
6. curl http://localhost:5000/detect?image_url=https://s3.ap-east-1.amazonaws.com/moredeal.org/hk/product_images/adidas_hk/adidas_hk_10478.jpg<br/>6.1 Exepected output
  { result: { name: "footwear" } }

Reference:
https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1
