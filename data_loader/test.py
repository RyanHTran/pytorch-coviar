import cv2
import numpy as np

representations = {'iframe': 0, 'mv': 1, 'residual': 2}

# from coviar_h264 import load, get_num_gops, get_num_frames
# VIDEO_PATH = '/home/ryan/Desktop/val_videos/h264/task_littlegirl-musician-2021_05_01_00_37_21-cvat_for_video_1.1/gop6.mp4'
from coviar import load, get_num_gops, get_num_frames
VIDEO_PATH = '/home/ryan/Desktop/val_videos/mpeg4/littlegirl_musician.mp4'


GOP_INDEX = 7
GOP_POS = 5

print(get_num_gops(VIDEO_PATH))
print(get_num_frames(VIDEO_PATH))

iframe = load(VIDEO_PATH, GOP_INDEX, GOP_POS, representations['iframe'], True)
mv = load(VIDEO_PATH, GOP_INDEX, GOP_POS, representations['mv'], True)
residual = load(VIDEO_PATH, GOP_INDEX, GOP_POS, representations['residual'], True)

cv2.imwrite('viz/iframe.jpg', iframe)
cv2.imwrite('viz/mv.jpg', np.concatenate((mv, np.expand_dims(np.zeros_like(mv[:,:,0]), axis=2)), axis=2))
cv2.imwrite('viz/residual.jpg', residual)

reloaded_mv = cv2.imread('viz/mv.jpg')