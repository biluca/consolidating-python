from person import Person


class User(Person):

    def __init__(self, email, password, job_title) -> None:
        self.email = email
        self.password = password
        self.job_title = job_title

    def __str__(self) -> str:
        return f"{self.name}, {self.job_title}, {self.password}"

    def change_password(self, current_password, new_password):
        if (self.password == current_password):
            self.password = new_password

    def change_job_title(self, new_job_title):
        self.job_title = new_job_title
