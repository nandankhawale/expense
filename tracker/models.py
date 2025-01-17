from django.db import models
import uuid

# Create your models here.
#don't make a model in a database and it can be inherited anywhere by using META ABSTRACT


class BaseModel(models.Model):
    uuid=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)
    created_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now_add=True)
  
    class Meta:
        abstract=True


class Transaction(BaseModel):
    description=models.CharField(max_length=100)
    amount=models.FloatField()

    class Meta:
        ordering=('description',)

    def isNegative(self):
        return self.amount < 0