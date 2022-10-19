class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # sort to  lexicographical order
	    words.sort()
	
	    # make counter using collections package
	    counter = collections.Counter(words)
	
	    # get k most frequent strings
	    k_items = counter.most_common(k)
	
	    # return the result as a list
	    return dict(k_items).keys()