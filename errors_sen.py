import changes


def sort(array):
    for i,obj in enumerate(array):
        temp_score = obj.get_score()
        array[i] = (obj, temp_score)
    array.sort(key=lambda tup: tup[1])
    return [arr[0] for arr in array]


class ErrorsSentence:
    def __init__(self):
        self.__swap = changes.Swap()
        self.__delete = changes.Delete()
        self.__add = changes.Add()

    def search(self, sentence, size):
        changes_arr = self.__swap.search(sentence, size)
        deletes_arr = self.__delete.search(sentence, size)
        add_arr = self.__add.search(sentence, size)

        merge_arr = sort(changes_arr + deletes_arr + add_arr)[::-1]


        return merge_arr[0:min(size, len(merge_arr))]
