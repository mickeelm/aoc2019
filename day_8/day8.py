from io import BytesIO


def assemble_layers(image_data_stream, layer_size):
    layers_list = []
    while layer := image_data_stream.read(layer_size):
        layers_list.append(layer)
    return layers_list


def checksum(image_data_stream, width, height):
    layer_size = width * height
    fewest_zeroes = min(assemble_layers(image_data_stream, layer_size), key=lambda layer: layer.count('0'))
    image_data_stream.close()
    one_digits = fewest_zeroes.count('1')
    two_digits = fewest_zeroes.count('2')
    return one_digits * two_digits


def decode_image(image_data_stream, width, height):
    layer_size = width * height
    flat_image = BytesIO(image_data_stream.read(layer_size))
    while layer_pixel := image_data_stream.read(1):
        image_pixel = flat_image.read(1)
        if image_pixel == b'2':
            flat_image.seek(-1, 1)
            flat_image.write(layer_pixel)
        if flat_image.tell() == layer_size:
            flat_image.seek(0)

    image = []
    while row := flat_image.read(width).decode():
        image.append(row)

    image_data_stream.close()
    flat_image.close()
    return image
