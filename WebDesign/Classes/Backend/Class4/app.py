from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import SelectField, RadioField, StringField, BooleanField, SubmitField, TextAreaField, FileField, PasswordField, DecimalField
from wtforms.validators import InputRequired
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mostImportantSecretKey'

class MyForm(FlaskForm):
  name = StringField('Name', validators=[InputRequired()])
  password = PasswordField('Password', validators=[InputRequired()])
  rememberMe = BooleanField('Remember Me')
  salary = DecimalField('Salary', validators=[InputRequired()])
  gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female')])
  country = SelectField('Country', choices = [
    ('af', 'Afghanistan'), ('al', 'Albania'), ('dz', 'Algeria'), ('as', 'American Samoa'), ('ad', 'Andorra'), ('ao', 'Angola'), 
    ('ai', 'Anguilla'), ('aq', 'Antarctica'), ('ag', 'Antigua and Barbuda'), ('ar', 'Argentina'), ('am', 'Armenia'), ('aw', 'Aruba'), 
    ('au', 'Australia'), ('at', 'Austria'), ('az', 'Azerbaijan'), ('bs', 'Bahamas'), ('bh', 'Bahrain'), ('bd', 'Bangladesh'), 
    ('bb', 'Barbados'), ('by', 'Belarus'), ('be', 'Belgium'), ('bz', 'Belize'), ('bj', 'Benin'), ('bm', 'Bermuda'), ('bt', 'Bhutan'), 
    ('bo', 'Bolivia'), ('ba', 'Bosnia and Herzegovina'), ('bw', 'Botswana'), ('br', 'Brazil'), ('io', 'British Indian Ocean Territory'), 
    ('bn', 'Brunei Darussalam'), ('bg', 'Bulgaria'), ('bf', 'Burkina Faso'), ('bi', 'Burundi'), ('cv', 'Cabo Verde'), ('kh', 'Cambodia'), 
    ('cm', 'Cameroon'), ('ca', 'Canada'), ('ky', 'Cayman Islands'), ('cf', 'Central African Republic'), ('td', 'Chad'), ('cl', 'Chile'), 
    ('cn', 'China'), ('cx', 'Christmas Island'), ('cc', 'Cocos (Keeling) Islands'), ('co', 'Colombia'), ('km', 'Comoros'), 
    ('cg', 'Congo (Brazzaville)'), ('cd', 'Congo (Kinshasa)'), ('ck', 'Cook Islands'), ('cr', 'Costa Rica'), ('hr', 'Croatia'), 
    ('cu', 'Cuba'), ('cw', 'Curaçao'), ('cy', 'Cyprus'), ('cz', 'Czech Republic'), ('dk', 'Denmark'), ('dj', 'Djibouti'), 
    ('dm', 'Dominica'), ('do', 'Dominican Republic'), ('ec', 'Ecuador'), ('eg', 'Egypt'), ('sv', 'El Salvador'), ('gq', 'Equatorial Guinea'), 
    ('er', 'Eritrea'), ('ee', 'Estonia'), ('et', 'Ethiopia'), ('fj', 'Fiji'), ('fi', 'Finland'), ('fr', 'France'), ('gf', 'French Guiana'), 
    ('pf', 'French Polynesia'), ('ga', 'Gabon'), ('gm', 'Gambia'), ('ge', 'Georgia'), ('de', 'Germany'), ('gh', 'Ghana'), ('gi', 'Gibraltar'), 
    ('gr', 'Greece'), ('gl', 'Greenland'), ('gd', 'Grenada'), ('gp', 'Guadeloupe'), ('gu', 'Guam'), ('gt', 'Guatemala'), ('gg', 'Guernsey'), 
    ('gn', 'Guinea'), ('gw', 'Guinea-Bissau'), ('gy', 'Guyana'), ('ht', 'Haiti'), ('va', 'Holy See'), ('hn', 'Honduras'), ('hk', 'Hong Kong'), 
    ('hu', 'Hungary'), ('is', 'Iceland'), ('in', 'India'), ('id', 'Indonesia'), ('ir', 'Iran'), ('iq', 'Iraq'), ('ie', 'Ireland'), 
    ('im', 'Isle of Man'), ('il', 'Israel'), ('it', 'Italy'), ('jm', 'Jamaica'), ('jp', 'Japan'), ('je', 'Jersey'), ('jo', 'Jordan'), 
    ('kz', 'Kazakhstan'), ('ke', 'Kenya'), ('ki', 'Kiribati'), ('kp', 'Korea (North)'), ('kr', 'Korea (South)'), ('kw', 'Kuwait'), 
    ('kg', 'Kyrgyzstan'), ('la', 'Lao PDR'), ('lv', 'Latvia'), ('lb', 'Lebanon'), ('ls', 'Lesotho'), ('lr', 'Liberia'), ('ly', 'Libya'), 
    ('li', 'Liechtenstein'), ('lt', 'Lithuania'), ('lu', 'Luxembourg'), ('mo', 'Macao'), ('mg', 'Madagascar'), ('mw', 'Malawi'), 
    ('my', 'Malaysia'), ('mv', 'Maldives'), ('ml', 'Mali'), ('mt', 'Malta'), ('mh', 'Marshall Islands'), ('mq', 'Martinique'), 
    ('mr', 'Mauritania'), ('mu', 'Mauritius'), ('yt', 'Mayotte'), ('mx', 'Mexico'), ('fm', 'Micronesia'), ('md', 'Moldova'), 
    ('mc', 'Monaco'), ('mn', 'Mongolia'), ('me', 'Montenegro'), ('ms', 'Montserrat'), ('ma', 'Morocco'), ('mz', 'Mozambique'), 
    ('mm', 'Myanmar'), ('na', 'Namibia'), ('nr', 'Nauru'), ('np', 'Nepal'), ('nl', 'Netherlands'), ('nc', 'New Caledonia'), 
    ('nz', 'New Zealand'), ('ni', 'Nicaragua'), ('ne', 'Niger'), ('ng', 'Nigeria'), ('nu', 'Niue'), ('nf', 'Norfolk Island'), 
    ('mk', 'North Macedonia'), ('mp', 'Northern Mariana Islands'), ('no', 'Norway'), ('om', 'Oman'), ('pk', 'Pakistan'), ('pw', 'Palau'), 
    ('ps', 'Palestine, State of'), ('pa', 'Panama'), ('pg', 'Papua New Guinea'), ('py', 'Paraguay'), ('pe', 'Peru'), ('ph', 'Philippines'), 
    ('pn', 'Pitcairn Islands'), ('pl', 'Poland'), ('pt', 'Portugal'), ('pr', 'Puerto Rico'), ('qa', 'Qatar'), ('re', 'Réunion'), 
    ('ro', 'Romania'), ('ru', 'Russian Federation'), ('rw', 'Rwanda'), ('bl', 'Saint Barthélemy'), ('sh', 'Saint Helena'), 
    ('kn', 'Saint Kitts and Nevis'), ('lc', 'Saint Lucia'), ('mf', 'Saint Martin (French part)'), ('pm', 'Saint Pierre and Miquelon'), 
    ('vc', 'Saint Vincent and Grenadines'), ('ws', 'Samoa'), ('sm', 'San Marino'), ('st', 'Sao Tome and Principe'), ('sa', 'Saudi Arabia'), 
    ('sn', 'Senegal'), ('rs', 'Serbia'), ('sc', 'Seychelles'), ('sl', 'Sierra Leone'), ('sg', 'Singapore'), ('sx', 'Sint Maarten (Dutch part)'), 
    ('sk', 'Slovakia'), ('si', 'Slovenia'), ('sb', 'Solomon Islands'), ('so', 'Somalia'), ('za', 'South Africa'), ('ss', 'South Sudan'), 
    ('es', 'Spain'), ('lk', 'Sri Lanka'), ('sd', 'Sudan'), ('sr', 'Suriname'), ('se', 'Sweden'), ('ch', 'Switzerland'), ('sy', 'Syrian Arab Republic'), 
    ('tw', 'Taiwan'), ('tj', 'Tajikistan'), ('tz', 'Tanzania'), ('th', 'Thailand'), ('tl', 'Timor-Leste'), ('tg', 'Togo'), ('tk', 'Tokelau'), 
    ('to', 'Tonga'), ('tt', 'Trinidad and Tobago'), ('tn', 'Tunisia'), ('tr', 'Turkey'), ('tm', 'Turkmenistan'), ('tc', 'Turks and Caicos Islands'), 
    ('tv', 'Tuvalu'), ('ug', 'Uganda'), ('ua', 'Ukraine'), ('ae', 'United Arab Emirates'), ('gb', 'United Kingdom'), ('us', 'United States'), 
    ('uy', 'Uruguay'), ('uz', 'Uzbekistan'), ('vu', 'Vanuatu'), ('ve', 'Venezuela'), ('vn', 'Viet Nam'), ('wf', 'Wallis and Futuna'), 
    ('eh', 'Western Sahara'), ('ye', 'Yemen'), ('zm', 'Zambia'), ('zw', 'Zimbabwe')
]
)
  message = TextAreaField('Message', validators=[InputRequired()])
  photo = FileField('Photo')

@app.route('/', methods=['GET', 'POST'])
def index():
  form = MyForm()
  return render_template('index.html', form=form)

@app.route("/validate", methods=["POST"])
def validateForm():
  form = MyForm()
  if form.validate_on_submit():
    name = form.name.data
    password = form.password.data
    rememberMe = form.rememberMe.data
    salary = form.salary.data
    gender = form.gender.data
    country = form.country.data
    message = form.message.data
    photo = form.photo.data.filename
    mydictionary = {
      "name": name,
      "password": generate_password_hash(password),
      "rememberMe": rememberMe,
      "salary": salary, 
      "gender": gender,
      "country": country,
      "message": message,
      "photo": photo
    }
    return render_template("formOUT.html", details=mydictionary, status="success")



if __name__ == '__main__':
  app.run(debug=True)