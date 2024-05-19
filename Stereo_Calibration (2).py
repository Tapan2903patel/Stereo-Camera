import numpy as np
import cv2 as cv
import glob

# Set your chessboard and frame sizes
chessboardSize = (9, 6)
frameSize = (640, 480)

# Termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Arrays to store object points and image points from all the images.
objpoints = []  # 3D points in real-world space
imgpointsL = []  # 2D points in the left image plane
imgpointsR = []  # 2D points in the right image plane

# Read stereo image pairs
imagesLeft = glob.glob('images/stereoLeft/*.png')
imagesRight = glob.glob('images/stereoRight/*.png')

for imgLeft, imgRight in zip(imagesLeft, imagesRight):
    imgL = cv.imread(imgLeft)
    imgR = cv.imread(imgRight)
    grayL = cv.cvtColor(imgL, cv.COLOR_BGR2GRAY)
    grayR = cv.cvtColor(imgR, cv.COLOR_BGR2GRAY)

    retL, cornersL = cv.findChessboardCorners(grayL, chessboardSize, None)
    retR, cornersR = cv.findChessboardCorners(grayR, chessboardSize, None)

    if retL and retR:
        objp = np.zeros((np.prod(chessboardSize), 3), np.float32)
        objp[:, :2] = np.mgrid[0:chessboardSize[0], 0:chessboardSize[1]].T.reshape(-1, 2)

        objpoints.append(objp)

        cornersL = cv.cornerSubPix(grayL, cornersL, (11, 11), (-1, -1), criteria)
        imgpointsL.append(cornersL)

        cornersR = cv.cornerSubPix(grayR, cornersR, (11, 11), (-1, -1), criteria)
        imgpointsR.append(cornersR)

# Stereo calibration
flags = 0
flags |= cv.CALIB_FIX_INTRINSIC

criteria_stereo = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

ret, cameraMatrixL, distCoeffsL, cameraMatrixR, distCoeffsR, R, T, E, F = cv.stereoCalibrate(
    objpoints, imgpointsL, imgpointsR,
    (frameSize[1], frameSize[0]), None, None, None, None,
    criteria=criteria_stereo, flags=flags
)

# Stereo rectification
R1, R2, P1, P2, Q, roi1, roi2 = cv.stereoRectify(
    cameraMatrixL, distCoeffsL, cameraMatrixR, distCoeffsR,
    (frameSize[1], frameSize[0]), R, T
)

map1_L, map2_L = cv.initUndistortRectifyMap(
    cameraMatrixL, distCoeffsL, R1, P1, (frameSize[1], frameSize[0]), cv.CV_16SC2
)
map1_R, map2_R = cv.initUndistortRectifyMap(
    cameraMatrixR, distCoeffsR, R2, P2, (frameSize[1], frameSize[0]), cv.CV_16SC2
)

# Save calibration data if needed
np.savez('stereo_calibration.npz', cameraMatrixL=cameraMatrixL, distCoeffsL=distCoeffsL,
         cameraMatrixR=cameraMatrixR, distCoeffsR=distCoeffsR, R=R, T=T,
         R1=R1, R2=R2, P1=P1, P2=P2, Q=Q, roi1=roi1, roi2=roi2,
         map1_L=map1_L, map2_L=map2_L, map1_R=map1_R, map2_R=map2_R)


# Save calibration data to XML file
cv_file = cv.FileStorage('stereo_calibration.xml', cv.FILE_STORAGE_WRITE)

cv_file.write('cameraMatrixL', cameraMatrixL)
cv_file.write('distCoeffsL', distCoeffsL)
cv_file.write('cameraMatrixR', cameraMatrixR)
cv_file.write('distCoeffsR', distCoeffsR)
cv_file.write('R', R)
cv_file.write('T', T)
cv_file.write('R1', R1)
cv_file.write('R2', R2)
cv_file.write('P1', P1)
cv_file.write('P2', P2)
cv_file.write('Q', Q)
cv_file.write('roi1', roi1)
cv_file.write('roi2', roi2)

cv_file.release()