from app import db
import datetime



class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100))

    def __repr__(self):
        return f'Id: {self.id}, Course Name: {self.course_name}'

    def as_dict(self):
        return {
            "id": self.id,
            "course_name": self.course_name
        }


class Registration:

    def __init__(self, student_image, student_type, full_name, address, country, state, city, email_address
                 , birth_year, birth_month, birth_day, course, comments):
        self.student_image = student_image
        self.student_type = student_type
        self.full_name = full_name
        self.address = address
        self.country = country
        self.state = state
        self.city = city
        self.email_address = email_address
        self.birth_date = datetime.datetime(year=int(birth_year), month=int(birth_month), day=int(birth_day))
        self.course = course
        self.comments = comments

    def as_dict(self):
        return {
            "student_image": self.student_image,
            "student_type": self.student_type,
            "full_name": self.full_name,
            "address": self.address,
            "country": self.country,
            "state": self.state,
            "city": self.city,
            "email_address": self.email_address,
            "birth_date": self.birth_date,
            "course": self.course,
            "comments": self.comments,
        }
