# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]

shelf1_update_tuple = tuple(shelf1_update)

shelf1_concat = shelf1 + shelf1_update_tuple

celery_count = shelf1_concat.count("celery")

celery_index = shelf1_concat.index("celery")

print(F"Updated Shelf #1: {shelf1_concat}")
print(F"Number of Celery: {celery_count}")
print(F"Celery Index: {celery_index}")