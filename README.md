image-object-detection-flask
==================

### Status
![workflow](https://github.com/moredeal-org/image-object-detection-flask/actions/workflows/ci.yml/badge.svg)

Introduction
------------
This flask app detects objects from image by a url. It downloads an image from the url and do inference with mobilenet_v2 by google.

Dependency
------------
tensorflow/tensorflow:latest docker image to setup environment to use tensorflow

Installation
------------
1. virtualenv env
2. & .\env\Scripts\activate
3. pip install -r requirements.txt
4. py main.py
5. curl http://localhost:5000/detect?image_url=https://s3.ap-east-1.amazonaws.com/moredeal.org/hk/product_images/adidas_hk/adidas_hk_10478.jpg<br/>6.1 Exepected output
  { result: { name: "footwear" } }

Reference
------------
https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1
