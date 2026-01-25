def scale_image(size, scale):
    return "x".join([str(int(int(i)*scale)) for i in size.split("x")])

print(scale_image("800x600", 2))
print(scale_image("100x100", 10))
print(scale_image("1024x768", 0.5))
print(scale_image("300x200", 1.5))