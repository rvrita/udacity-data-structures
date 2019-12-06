class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.
    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if type(group) != Group:
        return False

    if user in group.users:
        return True

    for subgroup in group.groups:
        if is_user_in_group(user, subgroup) == True:
            return True

    return False

# Test Cases
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child_without_user = Group("subchild without user")
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
child.add_group(sub_child)
child.add_group(sub_child_without_user)
parent.add_group(child)

print(is_user_in_group("sub_child_user", sub_child))
# True

print(is_user_in_group("nonexistent_user", sub_child))
# False

print(is_user_in_group("sub_child_user", parent))
# True
 
print(is_user_in_group("sub_child_user", sub_child_without_user))
# False

print(is_user_in_group(None, None)) 
# False
