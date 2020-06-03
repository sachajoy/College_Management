import datetimefrom flask.ext.login import UserMixinfrom peewee import *DATABASE = SqliteDatabase('college.db')class Type(Model):    """Table to maintain the diff type of USER in the system        NAME -> type of user"""    name = CharField(unique=True, max_length=20)    class Meta:        database = DATABASE        order_by = ['name', ]class Department(Model):    """ Each faculty and student will belong to one department        NAME -> name of department        CODE -> unique code of the department"""    name = CharField(max_length=255, unique=True)    code = IntegerField(unique=True)    class Meta:        database = DATABASE        order_by = ['code',]class Specialization(Model):    """Each department will have several SPECIALIZATION and each student        in a dept have specific specilization        DEPT -> department they belong to        NAME -> name of specilization        CODE -> code of the specilization in the department"""    dept = ForeignKeyField(Department, backref='specilization')    name = CharField(max_length=255, unique=True)    code = IntegerField(unique=True)    class Meta:        database = DATABASE        order_by = ['code', ]class Subject(Model):    """Each specilization have several subject to study        NAME -> name of subject        SPEC -> specilization it belong to        CODE -> subject code"""    name = CharField(max_length=255)    spec = ForeignKeyField(Specialization, backref='subject')    code = IntegerField(unique=True)    class Meta:        database = DATABASE        order_by = ['code', ]class Faculty(Model):    """Each DEPARTMENT have their faculty to teach        FNAME -> first name        MNAME -> middle name        LNAME -> last name        DOB -> date of birth        MOB -> mobile number        EMAIL -> email addr.        FID -> unique id for faculty for the department        ADDR -> addr        DEPT -> department of the faculty"""    fname = CharField(max_length=255)    mname = CharField(max_length=255)    lname = CharField(max_length=255)    dob = DateField(null=True)    mob = CharField(max_length=11)    email = CharField(max_length=80)    fid = IntegerField(unique=True)    addr = CharField(max_length=255)    dept = ForeignKeyField(Department, backref='faculty')    class Meta:        database = DATABASE        order_by = ['fid', ]class Student(Model):    """Student studing in the college under specilization of the department        FNAME -> first name        MNAME -> middle name        LNAME -> last name        DOB -> date of birth        MOB -> mobile number - unique        EMAIL -> email addr. - unique        ROLL_NO -> roll no - unique        ADDR -> address        SPEC -> specilization they belo    """    fname = CharField(max_length=255)    mname = CharField(max_length=255)    lname = CharField(max_length=255)    dob = DateField(null=True)    mob = CharField(max_length=11, unique=True)    email = CharField(max_length=80, unique=True)    addr = CharField(max_length=255)    roll_no = IntegerField(unique=True)    spec = ForeignKeyField(Specialization, backref='student')    class Meta:        database = DATABASE        order_by = ['roll_no', ]class Attendance(Model):    """Attendance for the student for the subject        DATE -> date        SUBJECT -> charfield        STU_ROLL_NO -> integerfeild        IS_PRESENT -> bool    """    date = DateField(default=datetime.date.today)    subject = ForeignKeyField(Subject, backref='subject')    stu_roll_no = ForeignKeyField(Student, backref='student')    is_present = BooleanField(default=True)    class Meta:        database = DATABASE        order_by = ['-date', 'subject', 'student', ]class Marks(Model):    """Marks for subject of the student        SUBJECT -> subject - foreignkey        MAX_MARKS -> marks - integer        OBT_MARKS -> obt in test - integer        DATE -> date of test - date        STU_ROLL_NO -> student - foreignkey"""    subject = ForeignKeyField(Subject, backref='sub')    max_marks = IntegerField()    obt_marks = IntegerField()    date = DateField(default=datetime.date.today)    stu_roll_no = ForeignKeyField(Student, backref='stu')    class Meta:        database = DATABASE        order_by = ['-date', 'subject', 'student']class Notificaton(Model):    """Notifacation to student from admin and faculty for variou topic        _FROM -> from like type - foreginkey        _TO -> to like type - foreignkey        SUBJECT -> for which subject - foreignkey        SPEC -> for specilization - foreignkey        TIMESTAMP -> time at which published - time"""    _from = ForeignKeyField(Type, backref='from')    _to = ForeignKeyField(Type, backref='to')    subject = ForeignKeyField(Subject, backref='sub')    spec = ForeignKeyField(Specialization, backref='specilization')    timestamp = DateTimeField(default=datetime.datetime.now)    class Meta:        database = DATABASE        order_by = ['-timestamp', 'subject', 'spec', 'from', 'to']class Login(UserMixin, Model):    """Login table for the application for admin, faculty, student        USERNAME -> admin, fid, roll_no - charfeild - unique        PASSWORD -> password - charfield        IS_ADMIN -> for admin - bool        IS_FACULTY -> for faculty - bool        IS_STU -> for stu - bool"""    username = CharField(unique=True)    password = CharField(max_length=15)    is_admin = BooleanField(default=False)    is_faculty = BooleanField(default=False)    is_stu = BooleanField(default=False)    class Meta:        database = DATABASE        order_by = ['username', ]