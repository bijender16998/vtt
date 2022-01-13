'''
import pixellib
from pixellib.tune_bg import alter_bg

change_bg = alter_bg(model_type = "pb")
change_bg.load_pascalvoc_model("xception_pascalvoc.pb")
change_bg.change_bg_img("sample.jpg", "background.jpg", output_image_name="output_img.jpg", detect = "person")
'''

import pixellib
from pixellib.tune_bg import alter_bg
import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,620)

while True:
    change_bg = alter_bg(model_type="pb")
    change_bg.load_pascalvoc_model("xception_pascalvoc.pb")
    change_bg.change_camera_bg(cap, "background.jpg",show_frames=True,frame_name="frame",detect = "person")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

