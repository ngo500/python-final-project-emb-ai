from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    """
    class for unit testing the emotion_detector function
    of the EmotionDetection package
    """
    def test_emotion_detector(self):
        """
        function for unit testing emotion_detector
        tests for if the dominant emotion is 
        joy, anger, disgust, sadness, or fear
        returns:
        OK or FAILED, the status of the unit tests
        """
        #test for joy dominant statement
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        #test for anger dominant statement
        result_1 = emotion_detector('I am really mad about this')
        self.assertEqual(result_1['dominant_emotion'], 'anger')

        #test for disgust dominant statement
        result_1 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_1['dominant_emotion'], 'disgust')

        #test for sadness dominant statement
        result_1 = emotion_detector('I am so sad about this')
        self.assertEqual(result_1['dominant_emotion'], 'sadness')

        #test for fear dominant statement
        result_1 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_1['dominant_emotion'], 'fear')
#run the unit tests
unittest.main()