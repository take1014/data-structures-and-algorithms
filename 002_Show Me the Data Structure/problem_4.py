#%% Imports and function declaration
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
    if user in group.get_users() or user == group.get_name():
        return True
    else:
        if len(group.get_groups()) == 0:  # Keep searching
            return False
        else:
            for sub_group in group.get_groups():
                return is_user_in_group(user, sub_group)
            return False

# Test case
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print("========== Normal case ==========")
print(is_user_in_group(user='parent_user', group=parent))
# False
print(is_user_in_group(user='sub_child_user', group=parent))
# True

print("========== Edge case ==========")
print(is_user_in_group(user='', group=parent))
# False
print(is_user_in_group(user='', group=child))
# False
