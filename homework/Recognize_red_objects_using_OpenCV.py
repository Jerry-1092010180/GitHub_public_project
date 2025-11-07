import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 红色范围（避免肤色）
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)
    # 检测肤色并去除
    lower_skin = np.array([0, 30, 60])
    upper_skin = np.array([20, 150, 255])
    skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)
    mask = cv2.bitwise_and(mask, cv2.bitwise_not(skin_mask))
    # 去噪 + 合并区域
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,9))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    boxes = []
    for cnt in contours:
        if cv2.contourArea(cnt) < 1500:
            continue
        x, y, w, h = cv2.boundingRect(cnt)
        boxes.append([x, y, x+w, y+h])
    # 合并相邻框
    def merge_boxes(boxes):
        merged = True
        while merged:
            merged = False
            new_boxes = []
            while boxes:
                b1 = boxes.pop()
                bx1, by1, bx2, by2 = b1
                overlap = False
                for b2 in boxes[:]:
                    x1, y1, x2, y2 = b2
                    if not (bx2 < x1-20 or bx1 > x2+20 or by2 < y1-20 or by1 > y2+20):
                        boxes.remove(b2)
                        bx1, by1 = min(bx1, x1), min(by1, y1)
                        bx2, by2 = max(bx2, x2), max(by2, y2)
                        boxes.append([bx1, by1, bx2, by2])
                        overlap = True
                        merged = True
                        break
                if not overlap:
                    new_boxes.append(b1)
            boxes = new_boxes
        return boxes
    boxes = merge_boxes(boxes)
    for x1, y1, x2, y2 in boxes:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
    cv2.imshow("Red Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
