
class CountImage(object):

    IMAGE_EXTENSIONS = ['.png', '.jpg', '.jpeg', '.gif', '.tiff']

    def __init__(self):
        pass

    def get_image_count(self, movie_entries):
        total_count = 0

        for movie_entry in movie_entries:
            total_count += self.__count_images(movie_entry)

        return total_count

    def __count_images(self, movie_entry):
        return self.__count_image_recursive(movie_entry)

    def __count_image_recursive(self, item):
        image_count = 0

        if isinstance(item, dict):
            for key in item.keys():
                image_count += self.__count_image_recursive(item[key])

        elif isinstance(item, tuple) or isinstance(item, list):
            for sub_item in item:
                image_count += self.__count_image_recursive(sub_item)

        else:
            if isinstance(item, basestring):
                for extension in self.IMAGE_EXTENSIONS:
                    try:
                        if item.encode('ascii', 'ignore').lower().endswith(extension):
                            image_count += 1
                            break
                    except:
                        pass

        return image_count
