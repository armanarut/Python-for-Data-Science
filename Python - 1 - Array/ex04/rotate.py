import numpy as np
from PIL import Image, ImageDraw, ImageFont
from load_image import ft_load


def main():
    """Load an image and print its dimensions.
Zoom the image by slicing it.
Transpose the image.
Display the scale on the x and y axis on the image.
"""

    im = ft_load("animal.jpeg")
    arr = np.array(im)

    # Print the size in pixel on both X and Y axis
    print("Image size: {} x {}".format(im.size[0], im.size[1]))

    # Print the number of channels
    print("Number of channels:", len(im.getbands()))

    # Print the pixel content of the image.
    print("Pixel content:")
    print(arr)

    # Display the scale on the x and y axis on the image
    cropped = im.crop((450, 100, 850, 500))
    cropped_arr = list(np.array(cropped)[:, :, 0])

    transposed = [[cropped_arr[j][i] for j in range(len(cropped_arr))]
                  for i in range(len(cropped_arr[0]))]
    arr = np.array(transposed)

    print("New shape after slicing :", arr.shape)
    print("Pixel content after slicing:")
    print(arr)

    draw = Image.fromarray(arr)
    draw_obj = ImageDraw.Draw(draw)

    # Draw a scale line
    draw_obj.line([(0, 0), (398, 0)], fill=255, width=2)
    draw_obj.line([(0, 0), (0, 398)], fill=255, width=2)
    draw_obj.line([(0, 398), (398, 398)], fill=255, width=2)
    draw_obj.line([(398, 0), (398, 398)], fill=255, width=2)

    for x in range(0, 400, 50):
        draw_obj.line([(0, x), (10, x)], fill=50, width=2)
        draw_obj.line([(x, 400), (x, 390)], fill=50, width=2)
        draw_obj.text((x-10, 370), str(x), fill=20,
                      font=ImageFont.truetype("arial.ttf", 15))
        draw_obj.text((10, x-10), str(x), fill=20,
                      font=ImageFont.truetype("arial.ttf", 15))

    draw.show()


if __name__ == "__main__":
    main()
