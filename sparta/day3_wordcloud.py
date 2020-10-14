from wordcloud import WordCloud
from PIL import Image
import numpy as np

text = ""
# 파일 이름은 맞게 바꿔주세요!
with open("kakaotalk.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[2:]:
        if '] [' in line \
                and '님이' not in line \
                and '샵검색' not in line \
                and '원 남아있어요!' not in line:
            text += line.split('] ')[2] \
                .replace('ㅋ', '') \
                .replace('ㅠ', '') \
                .replace('ㅜ', '') \
                .replace('ㅇ', '') \
                .replace('ㅎ', '') \
                .replace('ㄴ', '') \
                .replace('ㄱ', '') \
                .replace('#', '') \
                .replace('사진\n', '') \
                .replace('이모티콘\n', '') \
                .replace('삭제된 메시지입니다', '') \
                .replace('빨리 줍줍 하세요!!', '') \
                .replace('(야호!) 다음에 더 낼 기회가 있겠죠~', '') \
                .replace('사다리타기를 요청했어요.', '') \
                .replace('우리 정산해요!', '')

# wc = WordCloud(font_path='C:/Windows/Fonts/NanumGothicBold.ttf', background_color="white", width=600, height=400)
# wc.generate(text)
# wc.to_file("result.png")

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='C:/Windows/Fonts/NanumGothicBold.ttf', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")
