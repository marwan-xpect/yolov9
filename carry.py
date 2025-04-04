import cv2
if hasattr(cv2, "setNumThreads"):
    print("cv2.setNumThreads() is available!")
else:
    print("cv2.setNumThreads() is NOT available.")
    
if hasattr(cv2, 'ximgproc'):
    print("cv2.ximgproc is available.")
else:
    print("cv2.ximgproc is NOT available.")