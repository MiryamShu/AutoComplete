from changes.search_with_changes import SearchWithChanges


class Delete(SearchWithChanges):

    def __init__(self):
        super().__init__()

    def search(self, sentence, size=5):
        res = []
        for i in range(len(sentence) - 1, -1, -1):
            if len(res) == size:
                return res
            try:
                result = super().get_sentence_finder().search(sentence[:i] + sentence[i + 1:])[0]
            except Exception as r:
                continue
            for sent in result:
                if len(res) == size:
                    return res
                sent.set_score(super().get_score(i, sentence))
                res.append(sent)
        return res
