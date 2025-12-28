from emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):


    def test_emotion_detection(self):

        res_joy = emotion_detector('I am glad this happened')
        res_joy_num = res_joy[joy']
        self.assertGreater(res_joy_num, 0.8)

        res_anger = emotion_detector('I am really mad about this')
        res_anger_num = res_anger['anger']
        self.assertGreater(res_anger_num, 0.6)

        res_disgust = emotion_detector('I feel disgusted just hearing about this')
        res_disgust_num = res_disgust['disgust']
        self.assertGreater(res_disgust_num, 0.9)

        res_sadness = emotion_detector('I am so sad about this')
        res_sadness_num = res_sadness['sadness']
        self.assertGreater(res_sadness_num, 0.9)

        res_fear = emotion_detector('I am really afraid that this will happen')
        res_fear_nun = res_fear['fear']
        self.assertGreater(res_fear_nun, 0.9)


unittest.main()