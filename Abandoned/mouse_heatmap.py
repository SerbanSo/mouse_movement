import numpy as np
import cv2


# linear approach
def rgb_generate_linear(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)
    ratio = 2 * (value-minimum) / (maximum - minimum)
    b = 255*(1 - ratio).astype(int)
    b[b < 0] = 0
    r = 255*(ratio - 1).astype(int)
    r[r < 0] = 0
    g = 255 - b - r
    return b, g, r


def generate_image(dim_x, dim_y, matrix, min_value, max_value):
    img = np.zeros((dim_y, dim_x, 3), np.uint8)
    img[:, :, 0], img[:, :, 1], img[:, :, 2] = rgb_generate_linear(min_value, max_value, matrix)

    return img


def increase_adjancent_cells(x, y, dim_x, dim_y, matrix):
    vx = [-1, -1, -1, 0, 0, 1, 1, 1]
    vy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(0, 8):
        if dim_x > x + vx[i] >= 0 and dim_y > y + vy[i] >= 0:
            matrix[y + vy[i]][x + vx[i]] += 1


def main():
    name = "low_data.log"
    progress_total = sum(1 for line in open(name))
    file = open(name, "r")

    line = file.readline().split(" ")

    dim_x = int(line[0])
    dim_y = int(line[1])

    print(dim_x, dim_y)

    matrix = np.zeros((dim_y, dim_x))

    progress = 0

    timestamp = 0

    # video = cv2.VideoWriter('video2.avi', 0, 1, (dim_x, dim_y))
    for lines in file:
        if lines == "Click\n" or lines == "Released\n":
            continue
        line = lines.split(" ")
        x = int(line[0])
        y = int(line[1])
        timestamp += 1
        if timestamp > 1000:
            min_value = matrix.argmin()
            max_value = matrix.argmax()
            img = generate_image(dim_x, dim_y, matrix, min_value, max_value)
            cv2.imshow("image", img)
            cv2.waitKey(1)

            progress += 1
            print("Reading data: " + str("{:0.4f}".format(progress * timestamp * 100/progress_total)) + "% completed")
            # video.write(img)
            timestamp = 0
            continue
        if 0 <= x < dim_x and 0 <= y < dim_y:
            matrix[y][x] += 1
            # increase_adjancent_cells(x, y, dim_x, dim_y, matrix)

    print("Reading data: done!")
    print("Generating Image...")

    file.close()
    min_value = matrix.argmin()
    max_value = matrix.argmax()
    aprox = matrix.mean()
    variance = matrix.var()
    img = generate_image(dim_x, dim_y, matrix, min_value, variance)

    print("Generating Image: done!")

    cv2.imwrite("heatmap2.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
    # cv2.imshow("image", img)
    # cv2.waitKey(0);
    cv2.imshow("image1", img)
    # img = cv2.GaussianBlur(img, (5, 5), 0)
    # cv2.imshow("image2", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(max_value, min_value, aprox, matrix.var())

    # video.release()


main()
