from django.db import models
from mongoengine import fields, Document

class PollutionDetails(Document):
    index = fields.StringField(max_length=10)
    #timestamp = fields.DateTimeField()
    indexValue = fields.DecimalField(decimal_places=2, max_digits=50)

    '''@property
    def check_index(self):
        return self.index'''

