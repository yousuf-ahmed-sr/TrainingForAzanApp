_Random_words_ = ['hello', 'nice', 'cool', 'what', 'how', 'the', 'pop', 'make', 'ball', 'super', 'nothing', 'bye', 'buy', 'cost', 'you', 'apple', 'banana', 'cherry', 'date','box','zebra','boxer','vase','quak','jet','jacket','from','fall','vain','fun','scared']
_Letters_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
for i in range(0, 26):
    _Chosen_letter_ = _Letters_[i]
    _Chosen_letter_words_ = []
    for item in _Random_words_:
        if _Chosen_letter_ in item:
            _Chosen_letter_words_.append(item)
    print(f"Words with the letter {_Chosen_letter_}:")
    print(_Chosen_letter_words_)
    print()
    print()