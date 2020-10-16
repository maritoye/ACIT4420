import numpy as np


def main():
	file = open("oslomet.bmp", "rb")
	a = np.fromfile(file, dtype=np.uint8)
	file.close()

	header, height, width = read_header(a.copy())
	colour_array = a[54:].reshape(height,width, 3)

	snow(colour_array.copy(),header,height, width)
	yellow(colour_array.copy(), header, height, width)
	small(colour_array, width, height, header)


def read_header(a):
	"""
	Read the header of the file and print the size of the picture
	"""
	header = a[:54]
	width = header[18:22].copy().view("uint32")[0]
	height = header[22:26].copy().view("uint32")[0]

	print(f"The picture has width: {width} and height: {height}")

	return header, height, width


def snow(array, header, height, width):
	"""
	Copy the 3D array and manipulate the pixels in a way that every pixel with higher byte value
	than 150 for each component should be total white.
	Save the new image with the name "oslomet_snow.bmp"
	"""
	snow = array

	for i in range(height):
		for j in range(width):
			if snow[i][j][2] > 150 and snow[i][j][1] > 150 and snow[i][j][0] > 150:
				snow[i][j][0] = 255
				snow[i][j][1] = 255
				snow[i][j][2] = 255

	snow_file = open("oslomet_snow.bmp", "wb")
	header.astype("int8").tofile(snow_file)
	snow.tofile(snow_file)
	snow_file.close()


def yellow(array, header, height, width):
	"""
	Copy the 3D array and manipulate the pixels in a way that every pixel where both the red and the green
	component byte values are higher than 130 and the blue component byte value is less than 110 has to be modified:
	The red and the green value has to be exchanges, the green value has to be increased with 50 (if possible)
	and the red value has to be decreased by 50 (if possible).
	Save the new image with the name "oslomet_yellow.bmp"
	"""
	yellow = array

	for i in range(height):
		for j in range(width):
			if yellow[i][j][0] < 110 and yellow[i][j][1] > 130 and yellow[i][j][2] > 130:
				red = yellow[i][j][2]
				green = yellow[i][j][1]

				yellow[i][j][2] = (green - 50) if (green - 50)>=0 else 0
				yellow[i][j][1] = (red + 50) if (red + 50)<=255 else 255

	yellow_file = open("oslomet_yellow.bmp", "wb")
	header.astype("int8").tofile(yellow_file)
	yellow.tofile(yellow_file)
	yellow_file.close()


def small(array, width, height, header):
	"""
	Cut the upper 200 pixels and 200 pixels from both edges. Modify the header accordingly.
	Save the new bitmap with the name "oslomet_small.bmp"
	"""
	small = array.copy()
	cut = small[:height-200,200:width-200]

	small_width = (width - 200*2)
	small_height = (height - 200)

	header[18] = small_width % 256
	header[19] = small_width / 256
	header[22] = small_height % 256
	header[23] = small_height / 256

	small_file = open("oslomet_small.bmp", "wb")
	header.astype("int8").tofile(small_file)
	cut.astype("int8").tofile(small_file)
	small_file.close()


if __name__ == '__main__':
	main()

