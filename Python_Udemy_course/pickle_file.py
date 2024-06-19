#!/usr/bin/bash
# Generate a pickle file

import pickle
# write to Pickle File
ordering = {"First": 1, "Second": 2, "Third": 3}
order = pickle.dump(ordering, open("new.pkl", "wb"))
print(order)

# Read from Pickle File
reading_pickle = pickle.load(open("new.pkl", "rb"))

print(reading_pickle)
