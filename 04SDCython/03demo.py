import win32com.client
# 直接调用操作系统的语音接口
speaker = win32com.client.Dispatch("SAPI.SpVoice")
# 输入你想要说的话，前提是操作系统语音助手要认识。一般中文和英文是没有问题的
speaker.Speak("他能秒我，他能秒杀我？他要是能把我秒了，我当场······")
