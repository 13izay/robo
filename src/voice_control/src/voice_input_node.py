#!/usr/bin/env python3

import rospy
import speech_recognition as sr
from std_msgs.msg import String

def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        rospy.loginfo("Listening.......")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google_cloud(audio)
        rospy.loginfo("Recognized:" + text)
        return text
    
    except sr.UnknownValueError:
        rospy.logwarn("Could not understand audio")
        return ""

    except sr.RequestError as e:
        rospy.logwarn("Could not request results:{0}".format(e))

def voice_input_publisher():
    pub =rospy.Publisher('voice_text', String, queue_size=10)
    rospy.init_node('voice_input_node')
    rate =rospy.Rate(1)

    while not rospy.is_shutdown():
        text = recognize_speech()
        if text:
            pub.publish(text)
        rate.sleep()

if __name__ == '__main__':
    try: 
        voice_input_publisher()
    except rospy.ROSInterruptException:
        pass
