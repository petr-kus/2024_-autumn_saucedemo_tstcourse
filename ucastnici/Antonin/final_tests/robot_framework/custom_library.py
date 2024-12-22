import random

class custom_library:
    ROBOT_LIBRARY_SCOPE = 'SUITE'

    def random_item_generator(self, AtCs):
        randomAtC = AtCs[random.randrange(0,len(AtCs)-1)] if len(AtCs) > 1 else AtCs[0]
        return randomAtC