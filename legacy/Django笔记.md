# Django 笔记  

## Model  

### Relationships   

1. Many-to-one relationships  

   即ForeignKey，一个必选的位置参数：引用的model，一对多关系按照如下理解：a `Manufacturer` makes multiple cars but each `Car` only has one`Manufacturer`  
   
   ```python
   class Car(models.Model):
       manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
   ```
   
2. Many-to-Many relationships  

   你好

   

### custom django-admin commands  

1. manage

   <https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/>

### ORM  

1. filter.first(). 

   By default, results returned by a `QuerySet` are ordered by the ordering tuple given by the `ordering` option in the model’s `Meta`, In Meta, Options.ordering The default ordering for the object, for use when obtaining lists of objects:  
   
   ```python
   ordering = ['-order_date']
   ```
   
   PS: A particular ordering is guaranteed only when ordering by a set of fields that uniquely identify each object in the results. For example, if a name field isn’t unique, ordering by it won’t guarantee objects with the same name always appear in the same order  
   
### class Meta  

你好  

### def save()  



## Serializers  



   
