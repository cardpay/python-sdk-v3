# coding: utf-8
import random
import string

from config import EMAILS_DOMAIN
from faker import Faker
from faker.providers import misc, profile, phone_number, date_time

fake = Faker()
fake.add_provider(misc)
fake.add_provider(profile)
fake.add_provider(phone_number)
fake.add_provider(date_time)


def generateMerchantOrderId():
    return randomString(20)


def randomString(stringLength=6):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


def randomBetween(min, max):
    return random.randint(min, max)


def generateAmount(min=10, max=300):
    return randomBetween(min * 100, max * 100) / 100


def generateEmail(mailbox=None):
    return (mailbox if mailbox else randomString(20)) + "@" + EMAILS_DOMAIN


def generateCardExpiration():
    return fake.future_date(end_date="+365d", tzinfo=None)


def generatePhoneNumber():
    return ('+' + fake.msisdn())[:12]
