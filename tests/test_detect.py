import unittest
from flask_testing import TestCase
from app import create_app
import json


class SettingBase(TestCase):
    def create_app(self):
        return create_app("testing")

      # 在運行測試之前會先被執行
    def setUp(self):
        return

      # 在結束測試時會被執行
    def tearDown(self):
        return

    def detect(self):
        response = self.client.get(
            '/detect?image_url=https://s3.ap-east-1.amazonaws.com/moredeal.org/hk/product_images/adidas_hk/adidas_hk_10478.jpg')
        return response


# 這邊繼承剛剛的寫的 SettingBase class，接下來會把測試都寫在這裡
class CheckObjectDetection(SettingBase):
    def test_object_detection(self):
        response = self.detect()
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'][0]['name'], "footwear")
    
    def test_failure(self):       
        self.assertEqual(True, False)        


if __name__ == '__main__':
    unittest.main()
