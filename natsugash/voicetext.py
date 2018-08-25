import natsugash.config as config
import os.path

API_KEY = config.VOICETEXT_API_KEY

def make_voicefile (tweets) :
    for tweet in tweets:
        p = "curl 'https://api.voicetext.jp/v1/tts' \
            -o 'voicefiles/{0}.wav' \
            -u '{1}:' \
            -d 'text={0}' \
            -d 'speaker=hikari'".format(tweet, API_KEY)
        os.system(p)

# API_KEY = "13j7vr127iem66cw"
# text = "斎藤そうまは、良いぞ。"
# p = "curl 'https://api.voicetext.jp/v1/tts' \
#      -o 'test.wav' \
#      -u '％s:' \
#      -d 'text=斎藤そうまは、良いぞ' \
#      -d 'speaker=hikari'" % API_KEY
# os.system(p)
