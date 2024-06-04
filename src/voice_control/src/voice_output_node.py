#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from gtts import gTTS
import os
from playsound import playsound

def callback_voice(data):
    rospy.loginfo("Playing back: %s", data.data)
    tts = gTTS(text= data.data, lang = 'en')
    tts.save("/tmp/voice_output.mp3")
    playsound("/tmp/voice_output.mp3")
    os.remove("/tmp/voice_output.mp3")


def voice_output_listener():
    rospy.init_node('voice_output_node')
    rospy.loginfo("Node started")
    rospy.Subscriber('voice_text', String, callback = callback_voice)

if __name__ == '__main__':
    try:
        voice_output_listener()
    except rospy.ROSInterruptException:
        pass

