import os


# PROFILE VARIABLES
GENDER_OPTIONS = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('trans_male', 'Trans Male'),
    ('trans_female', 'Trans Female'),
    ('non_binary', 'Non-binary'),
    ('genderqueer', 'Genderqueer'),
    ('genderfluid', 'Genderfluid'),
    ('bigender', 'Bigender'),
    ('other', 'Other')
]

HANDLING_MONEY_OPTIONS = [
    ('spender', 'Spender'),
    ('saver', 'Saver'),
    ('investor', 'Investor'),
    ('budgeter', 'Budgeter'),
    ('frugal', 'Frugal'),
    ('extravagant', 'Extravagant'),
    ('debt_averse', 'Debt Averse'),
    ('risk_taker', 'Risk Taker'),
    ('risk_averse', 'Risk Averse'),
    ('charitable', 'Charitable')
]

POLITIC_OPTIONS = [
    ('anarchist', 'Anarchist'),
    ('authoritarian', 'Authoritarian'),
    ('capitalist', 'Capitalist'),
    ('centrist', 'Centrist'),
    ('communist', 'Communist'),
    ('conservative', 'Conservative'),
    ('democratic_socialist', 'Democratic Socialist'),
    ('environmentalist', 'Environmentalist'),
    ('fascist', 'Fascist'),
    ('feminist', 'Feminist'),
    ('liberal', 'Liberal'),
    ('libertarian', 'Libertarian'),
    ('marxist', 'Marxist'),
    ('monarchist', 'Monarchist'),
    ('nationalist', 'Nationalist'),
    ('populist', 'Populist'),
    ('progressive', 'Progressive'),
    ('social_democrat', 'Social Democrat'),
    ('socialist', 'Socialist'),
    ('theocrat', 'Theocrat')
]

RELIGION_OPTIONS = [
    ('agnosticism', 'Agnosticism'),
    ('atheism', 'Atheism'),
    ('bahai', 'Bahá\'í Faith'),
    ('bon', 'Bön'),
    ('buddhism', 'Buddhism'),
    ('caodai', 'Cao Dai'),
    ('christianity', 'Christianity'),
    ('confucianism', 'Confucianism'),
    ('deism', 'Deism'),
    ('druidism', 'Druidism'),
    ('druze', 'Druze'),
    ('eckankar', 'Eckankar'),
    ('falun_gong', 'Falun Gong'),
    ('hinduism', 'Hinduism'),
    ('islam', 'Islam'),
    ('jainism', 'Jainism'),
    ('judaism', 'Judaism'),
    ('native_american_religions', 'Native American Religions'),
    ('neo_paganism', 'Neo-Paganism'),
    ('new_thought', 'New Thought'),
    ('pastafarianism', 'Church of the Flying Spaghetti Monster (Pastafarianism)'),
    ('rastafarianism', 'Rastafarianism'),
    ('scientology', 'Scientology'),
    ('shinto', 'Shinto'),
    ('sikhism', 'Sikhism'),
    ('spiritualism', 'Spiritualism'),
    ('taoism', 'Taoism'),
    ('tenrikyo', 'Tenrikyo'),
    ('traditional_african_religions', 'Traditional African Religions'),
    ('unitarian_universalism', 'Unitarian Universalism'),
    ('wicca', 'Wicca'),
    ('zoroastrianism', 'Zoroastrianism')
]

SHOWERING_FREQUENCY_OPTIONS = [
    ('daily', 'Daily'),
    ('every_other_day', 'Every other day'),
    ('weekly', 'Weekly')
]

ORAL_CARE_OPTIONS = [
    ('brush_twice_a_day', 'Brush twice a day'),
    ('flossing', 'Flossing'),
    ('mouthwash', 'Mouthwash')
]

CIGARETTE_SMOKING_OPTIONS = [
    (True, 'Smoker'),
    (False, 'Non-smoker')
]

LIVING_SPACE_CLEANLINESS_OPTIONS = [
    ('daily_cleaning', 'Daily cleaning'),
    ('weekly_cleaning', 'Weekly cleaning'),
    ('bi_weekly_cleaning', 'Bi-weekly cleaning'),
    ('monthly_cleaning', 'Clean monthly'),
    ('infrequent_cleaning', 'Longer than every month')
]

ALCHOHOL_COMSUMPTION_OPTIONS = [
    ('daily', 'Drink daily'),
    ('other_day', 'Every other day'),
    ('weekend', 'Weekends only'),
    ('sober', 'I don\'t drink')
]

MARIJUANA_CONSUMPTION_OPTIONS = [
    ('daily', 'Blaze daily'),
    ('other_day', 'Every other day'),
    ('weekend', 'Weekends only'),
    ('sober', 'I don\'t blaze')
]

# FLASK CONFIGS
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('DATE_SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATE_DATABASE_URL') or "sqlite:///" + os.path.join(basedir, "app.db")
    UPLOAD_EXTENSIONS = [".jpg", ".png"]
    UPLOAD_PATH = "profile_uploads"