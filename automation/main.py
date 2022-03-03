from utils import *

KEY_COLUMN = 8
SUM_COLUMN = 10

type_collection = get_unique_collection_by_column(KEY_COLUMN)
homes_per_type = count_items_by_key(KEY_COLUMN, type_collection)
price_per_type = sum_items_by_key(KEY_COLUMN, type_collection, SUM_COLUMN)

print("==Type of Houses")
print("     ", type_collection)
print("==How many houses per Type?")
print("     ", homes_per_type)
print("==How much for each Type?")
print("     ", price_per_type)
