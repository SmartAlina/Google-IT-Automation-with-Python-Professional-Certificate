def groups_per_user(group_dictionary):
	user_groups = {}
	for group_names, list_of_users in group_dictionary.items():
		for user in list_of_users:
			if user not in user_groups:
				nickname = []
				nickname.append(group_names)
				user_groups[user] = nickname
			else:
				user_groups[user].append(group_names)
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
# Should print
# {'admin': ['local', 'public', 'administrator'], 'userA': ['local'], 'userB': ['public']}
