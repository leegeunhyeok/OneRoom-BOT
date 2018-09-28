# Copyright 2018 Leegeunhyeok. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import cv2
import numpy as np
from enum import Enum



class Type(Enum):
    IMAGE = 0
    VIDEO = 1



class BotInitializeError(Exception):
    """봇 초기화 시 캠, 이미지 경로, 비디오 경로가 없는 경우 예외 발생.

    속성:
        message -- 오류에 대한 설명 메시지
    """
    def __init__(self, message):
        self.message = message



class BotTypeError(Exception):
    """초기화에 사용된 타입이 아닌 다른 타입을 사용할 경우 예외 발생.

    속성:
        message -- 오류에 대한 설명 메시지
    """
    def __init__(self, message):
        self.message = message



class Bot:

    def __init__(self, image: str=None, video: any=None, resize_ratio=0.25):
        self.resize_ratio = resize_ratio
        if image:
            self.image = image
            self.type = Type.IMAGE
        elif video:
            self.video = video
            self.type = Type.VIDEO
        else:
            raise BotInitializeError("이미지 경로, 비디오 경로(캠 번호) 중 하나는 필수입니다.")


    def showImage(self):
        if Type.IMAGE == self.type:
            img = cv2.imread(self.image, cv2.IMREAD_COLOR)
            img = cv2.resize(img, (0, 0), fx=self.resize_ratio, fy=self.resize_ratio)
            cv2.namedWindow("Image")
            cv2.imshow("Image", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            raise BotTypeError("이미지 타입은 사용할 수 없습니다. (초기화된 타입: %s)" % (self.type.name))

    
    def showVideo(self):
        if Type.VIDEO == self.type:
            cap = cv2.VideoCapture(self.video)
            cap.set(3, 540)
            cap.set(4, 980)

            while True:
                _, frame = cap.read()

                if not ret:
                    break

                img = cv2.resize(frame, (0, 0), fx=self.resize_ratio, fy=self.resize_ratio)
                cv2.imshow("Video", img)
                k = cv2.waitKey(1)
                if k == 27:
                    break

            cap.release()
            cv2.destroyAllWindows()
        else:
            raise BotTypeError("비디오 타입은 사용할 수 없습니다. (초기화된 타입: %s)" % (self.type.name))

