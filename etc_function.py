def createHistogram(converted_img):
    grey_level = []
    frequency = []
    histogram = {}
    for i in range(len(converted_img)):
        if converted_img[i] not in grey_level:
            grey_level.append(converted_img[i])
    grey_level.sort()
    for i in range(len(grey_level)):
        frequency.append(converted_img.count(grey_level))
    histogram = dict(zip(grey_level, frequency))
    return histogram