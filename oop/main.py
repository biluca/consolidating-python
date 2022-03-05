from user import User

my_user = User("biluca@python.com",
               "nice_pwds", "Integration Engineer")
print(my_user)

my_user.change_password("nice_pwd", "great_pwd")
print(my_user)

my_user.change_job_title("Integration Manager")
print(my_user)
