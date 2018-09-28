import numpy as np
import cv2

# 게임 화면 불러오기, 이미지 가로/세로 비율 원본 이미지의 25%
img = cv2.resize(cv2.imread("./sample/image/1.png"), (0, 0), fx=0.25, fy=0.25)

# 불러온 화면 흑백 이미지로 변환
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# 템플릿 매칭에 사용할 이미지 흑백으로 로드
template_origin = cv2.imread("./sample/image/1_brick.png", cv2.IMREAD_GRAYSCALE)

# 게임화면에 맞추기 위해 원본 이미지 크기의 25%로 변경
template = cv2.resize(template_origin, (0, 0), fx=0.25, fy=0.25)

# 템플릿 매칭에 사용할 이미지의 가로, 세로 길이
w, h = template.shape[::-1]
print(w, h)

# 게임 이미지에 템플릿 매칭
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

# 60% 이상 매칭되는 영역 추출
loc = np.where(res >= 0.6)

# 추출된 영역위치에 사각형 그리기
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255))

# 게임 이미지 출력
cv2.imshow("img", img)

# 템플릿 매칭에 사용한 원본 이미지 출력 (가로/세로 2배 늘리기)
cv2.imshow("Target", cv2.resize(template_origin, (0, 0), fx=2, fy=2))


# 키 입력 대기 및 윈도우 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()