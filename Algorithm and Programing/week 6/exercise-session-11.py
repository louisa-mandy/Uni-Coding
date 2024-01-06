#exercise session 11, sir jude 

inventory = {
'gold' : 500,
'pouch' : ['flint', 'twine', 'gemstone'],
'backpack' : ['xylophone','dagger', 'bedroll','bread loaf'],
'pocket' : ['seashell', 'strange berry','lint']
}
sort = list(inventory['backpack'])  # make the dict in to a list, sort the list 
sort.sort() # sorting  'sort' list 
print(sort)

sort.remove("dagger") #removing 'dagger' from backpack
print(sort)

inventory['gold']+=50 # additioning 50 

print(inventory)


# add a key to inventory 'pocket'
# sort the items 