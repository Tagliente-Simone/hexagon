class Configuration:
    def __init__(self, rect_width, rect_height, inter, uuid_length, images_path):
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.start_originx = (rect_width - 1200) / 2
        self.start_originy = (rect_height - 1000) / 2
        self.inter = inter
        self.uuid_length = uuid_length
        self.images_path = images_path



