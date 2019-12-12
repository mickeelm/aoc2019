from io import BytesIO, StringIO

from day_8.day8 import checksum, decode_image


def test_checksum():
    assert checksum(StringIO('123456789012'), 3, 2) == 1


def test_answer_1():
    with open('input') as f:
        assert checksum(f, 25, 6) == 1206


def test_decode_image():
    assert decode_image(BytesIO(b'0222112222120000'), 2, 2) == ['01', '10']


def test_answer_2():
    with open('input', 'rb') as f:
        image = decode_image(f, 25, 6)
        assert image == ['1111000110111000110011100', '1000000010100101001010010',
                         '1110000010100101000010010', '1000000010111001011011100',
                         '1000010010101001001010000', '1111001100100100111010000']
        print()
        for row in image:
            for pixel in row:
                print('█', end='') if pixel == '1' else print(' ', end='')
            print()
