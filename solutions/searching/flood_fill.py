#! /usr/bin/env python
"""
Problem

    An 'image' is represented by a 2-D array of integers, each integer
    representing the pixel value of the image (from 0 to 655535).

    Given a coordinate (sr, sc) representing the starting pixel (row and
    column) of the flood fill, and a pixel value 'newColor', "flood fill" the
    image.

    To perform a "flood fill", consider the starting pixel, plus any pixels
    connected 4-directionally to the starting pixel of the same color as the
    starting pixel, plus any pixels connected 4-directionally to those pixels
    (also with the same color as the starting pixel), and so on. Replace the
    color of all of the aforementioned pixels with the 'newColor'.

    At the end, return the modified image.


Example 1

    Input

        image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        sr = 1, sc = 1, newColor = 2

    Output

        [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

    Explanation

        From the center of the image (with position (sr, sc) = (1, 1)), all
        pixels connected by the same color as the starting pixel are colored
        with the new color.

        Note the bottom corner is not colored 2, because it is not
        4-directionally connected to the starting pixel.

Note

    * The length of 'image' and 'image[0]' will be in the range [1, 50]

    * The given starting pixel will satisfy 0 <= sr < image.length and
      0 <= sc <= image[0].length

    * The value of each color in image[i][j] and 'newColor' will be an integer
      in [0, 65535].
"""

from typing import List, Tuple

Image = List[List[int]]
Pixel = Tuple[int, int]
Color = int

ROW = 0
COLUMN = 1
LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)
DIFFERENCES = (LEFT, RIGHT, UP, DOWN)


def _is_valid_pixel(image: Image, pixel: Pixel) -> bool:
    return (
        (pixel[ROW] >= 0) and (pixel[ROW] < len(image)) and
        (pixel[COLUMN] >= 0) and (pixel[COLUMN] < len(image[0]))
    )


def _fill_color(
    image: Image, pixel: Pixel, old_color: Color, new_color: Color
) -> None:
    if old_color == new_color:
        return

    for row_difference, column_difference in DIFFERENCES:
            new_pixel = (
                pixel[ROW] + row_difference, pixel[COLUMN] + column_difference
            )
            if (
                (_is_valid_pixel(image, new_pixel)) and
                (image[new_pixel[ROW]][new_pixel[COLUMN]] == old_color)
            ):
                image[new_pixel[ROW]][new_pixel[COLUMN]] = new_color
                _fill_color(image, new_pixel, old_color, new_color)


def replace(image: Image, pixel: Pixel, color: Color) -> Image:
    """Replaces color of given pixel and adjacent pixels with expected color

    This method will pick color of a pixel received as an argument. Then it
    will replace color of current pixel with a expected color. Then this method
    finds all adjacent pixels having the color we picked earlier and loops by
    changing a current pixel to all adjacent pixel. This method will keep
    replacing colors of adjacent pixels until there are no adjacent pixels left
    which are having the color we picked earlier.

    Adjacent pixel of current pixel

                     Up (-1, 0)

    (0, -1) Left     (0, 0)         Right (0, +1)

                    Down (+1, 0)

    Above four pixels will be considered as an adjacent pixels of a current
    pixel. The braces represent (Row difference, Column Difference). For
    example "Left" adjacent pixel of current pixel will be a previous column of
    same row. The center pixel has no difference thus it is represented as (0,
    0).

    Note

        This method automatically discards pixel values which are going out of
        a image boundaries.

    Strategy

        This method performs an Depth First Search(DFS) for finding all
        adjacent pixels having a same color.

    Example

        >>>flood_fill(
        image=[[0, 0, 0, 0], [1, 5500, 0, 0], [1, 1, 0, 0], [1, 1, 1, 1]],
        pixel=(1, 0)
        color=4500
        ) == [
            [0, 0, 0, 0],
            [4500, 5500, 0, 0],
            [4500, 4500, 0, 0],
            [4500, 4500, 4500, 4500]
        ]

    """
    old_color = image[pixel[ROW]][pixel[COLUMN]]
    image[pixel[ROW]][pixel[COLUMN]] = color
    _fill_color(image, pixel, old_color, color)
    return image
