import uuid
from django.db import models, transaction

class ProductionType(models.Model):
    id = models.BinaryField(db_column='_IDRRef', primary_key=True, max_length=16, editable=False, unique=True)
    reproduction = models.BinaryField(db_column='_Fld3203RRef', max_length=16, blank=True, null=True)
    display_name = models.CharField(db_column='_Description', max_length=100)

    class Meta:
        managed = False
        db_table = 'my_type_of_production'
    # def __str__(self):
    #     return self.display_name

class NomencBook(models.Model):
    id = models.BinaryField(db_column='_IDRRef', primary_key=True, max_length=16, editable=False, unique=True)

    name = models.CharField(db_column='_Description', max_length=100, db_collation='Cyrillic_General_CI_AS')
    group = models.BinaryField(db_column='_ParentIDRRef', max_length=16, default=b'\x00' * 16, editable=False) # TODO Тут необходимо реализовать возможность выбора группы номенклатуры из списка! Надо будет убрать "editable=False"
    view = models.BinaryField(db_column='_Fld3204RRef', max_length=16, default=b'\xBA\x80\x0C\xC4\x7A\x22\x9A\x23\x11\xE6\xC8\x40\x91\x63\x13\x34', editable=False)  # TODO Тут необходимо реализовать возможность выбора вида номенклатуры из списка! Надо будет убрать "editable=False"

    # type_of_reproduction = models.BinaryField(db_column='_Fld3203RRef', max_length=16, default=b'\xb7\xe6\xdb!\xb71g\xdfK\xb0\xcdJ}\x149P', blank=True, null=True)  # TODO Реализовать выпадающий список. Вид воспроизводства: покупка, переработка, производство или принятые в переработку
    type_of_reproduction = models.ForeignKey(ProductionType, on_delete=models.CASCADE, db_column='_Fld3203RRef', blank=True, null=True)

    basic_unit = models.TextField(db_column='_Fld3207RRef', blank=True, null=True, editable=False)  # TODO Реализовать выпадающий список. Базовая ед. измерения: перечисление

    field_code = models.CharField(db_column='_Code', max_length=11, db_collation='Cyrillic_General_CI_AS', editable=False)  # Поле содержащее код

    # Поля, которые должны иметь значения для сохранения записи:
    field_marked = models.BinaryField(db_column='_Marked', default=b'\x00', editable=False)
    field_ismetadata = models.BinaryField(db_column='_IsMetadata', default=b'\x00', editable=False)
    field_folder = models.BinaryField(db_column='_Folder', default=b'\x01', editable=False)

    field_Fld3227RRef = models.BinaryField(db_column='_Fld3227RRef', max_length=16, default=b'\x00' * 16, editable=False) # TODO что это такое пока непонятно! Если получиться разобраться - хорошо, по всем записям одинаковая запись "0x00000000000000000000000000000000"

    class Meta:
        managed = False
        db_table = '_Reference175'

    def write(self, *args, **kwargs):
        if not self.id:
            self.id = uuid.UUID(bytes=uuid.uuid4().bytes).bytes

        if not self.field_code:
            # Получаем текущее максимальное значение _Code
            with transaction.atomic():
                last_record = NomencBook.objects.order_by('-field_code').first()
                if last_record and last_record.field_code.strip().isdigit():
                    new_code = int(last_record.field_code.strip()) + 1
                else:
                    new_code = 1  # Начинаем с 1, если таблица пуста или значение не числовое

                # Форматируем новый код как строку длиной 11 символов
                self.field_code = str(new_code).zfill(11)

        if isinstance(self.type_of_reproduction, ProductionType):
            # print(f"Before save, type_of_reproduction value: {self.type_of_reproduction.reproduction}")
            self.type_of_reproduction = self.type_of_reproduction

        super().save(*args, **kwargs)
