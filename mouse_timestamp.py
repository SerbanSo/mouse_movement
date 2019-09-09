import sys
import cv2
import numpy as np

# Used for drawing "click" and "release" circles
CIRCLE = np.arange(0, 360)
CIRCLE = np.pi/180 * CIRCLE
CIRCLE_COS = np.cos(CIRCLE)
CIRCLE_SIN = np.sin(CIRCLE)
# Speed of drawings
SPEED = 50
# number of colors (MAX_VALUE - MIN_VALUE)
MAX_VALUE = 1000
MIN_VALUE = 0
# Determine colors
STEP = 1
value = np.arange(MIN_VALUE, MAX_VALUE, STEP)
value = 2 * (value - MIN_VALUE) / (MAX_VALUE - MIN_VALUE)
R = 255 * (value - 1)
R[R < 0] = 0
B = 255 * (1 - value)
B[B < 0] = 0
G = 255 - R - B


# Colors the pixels in image
def rgb_path(img, index_list):
    y = index_list[0::2]
    x = index_list[1::2]
    z = int(len(index_list)/2)
    img[y, x, 0], img[y, x, 1], img[y, x, 2] = B[0:z], G[0:z], R[0:z]

    return img


# Draw the circle for "Clicks" and "Releases"
def draw_circle(img, x, y, r, g, b, dim_x, dim_y, video, make_video):
    for i in range(0, 15, 2):
        temp_img = np.copy(img)
        index_x = y + (i * CIRCLE_COS).astype(int)
        index_y = x + (i * CIRCLE_SIN).astype(int)
        temp_img[index_x[(index_y < dim_x) & (index_x < dim_y)],
                 index_y[(index_y < dim_x) & (index_x < dim_y)]] = b, g, r
        cv2.imshow("image1", temp_img)
        cv2.waitKey(1)
        cv2.imshow("image1", img)
        if make_video == 1:
            video.write(temp_img)
            video.write(img)


def get_xy(line):
    try:
        x = int(line[0])
        y = int(line[1])
        return x, y
    except ValueError:
        print("Incompatible data, please use another file.")
        sys.exit(1)


def main():
    # File name for the data
    name = ""
    while True:
        try:
            name = input("Insert data file:")
            open(name, "r")
            break
        except KeyboardInterrupt:
            print("Program interrupted")
            sys.exit(1)
        except OSError:
            print("Invalid file. Please try again")
            continue

    make_video = input("Make video file?y/n:")
    if make_video == "y":
        make_video = 1
    else:
        make_video = 0

    total_progress = sum(1 for line in open(name))
    file = open(name, "r")
    line = file.readline().split(" ")

    # Resolution of the screen
    dim_x, dim_y = get_xy(line)

    print(dim_x, dim_y)

    # Image matrix
    img = np.zeros((dim_y, dim_x, 3), np.uint8)

    # Video recording settings
    if make_video == 1:
        video = cv2.VideoWriter('video2.avi', fourcc=cv2.VideoWriter.fourcc('M', 'P', 'E', 'G'),
                            fps=24, frameSize=(dim_x, dim_y), isColor=True)

    # List for the last MAX_VALUE pixels
    index_list = []
    # Count total pixels
    count = 0
    x = 0
    y = 0

    # Reading from file
    for lines in file:
        print("Progress: " + str("{:0.4f}".format(count * 100/total_progress)) + "%", end="\r")
        if lines == "Click\n":
            draw_circle(img, x, y, 255, 0, 0, dim_x, dim_y, video, make_video)
        elif lines == "Released\n":
            draw_circle(img, x, y, 0, 0, 255, dim_x, dim_y, video, make_video)
        else:
            line = lines.split(" ")
            x, y = get_xy(line)

            if 0 <= x < dim_x and 0 <= y < dim_y:
                count += 1
                if count > MAX_VALUE:
                    index_list.pop(0)
                    index_list.pop(0)

                index_list.append(y)
                index_list.append(x)

                # Pixels update speed
                speed = count % SPEED
                if speed == 0:
                    # Update pixels colors
                    img = rgb_path(img, index_list)
                    # Record current image
                    if make_video == 1:
                        video.write(img)
                    cv2.imshow("image1", img)
                    cv2.waitKey(1)

    file.close()
    cv2.destroyAllWindows()
    if make_video == 1:
        video.release()
    print(MAX_VALUE, MIN_VALUE)


main()
