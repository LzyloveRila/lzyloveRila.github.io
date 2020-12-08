import pymongo

print("Connecting to database...")
client = pymongo.MongoClient(
    "mongodb+srv://lzyrila:woaideni1996@rilawebdb.lc25k.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.wish_list
collection = db.wish_list0
print('success')
users = collection.find({'name':'test'})
student2 = {
    'name': 'Mike',
    'item': 21,
    'time': 'male'
}
result = collection.insert_one(student2)
# for user in users:
#     print("test.....:", user)
# print('end...')
