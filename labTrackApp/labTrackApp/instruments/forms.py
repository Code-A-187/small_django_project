from django import forms
from .models import Instrument

class InstrumentBaseForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = ['brand', 'model', 'serial_number', 'description', "status"]


class InstrumentAddForm(InstrumentBaseForm):
    pass

class InstrumentEditForm(InstrumentBaseForm):
    class Meta(InstrumentBaseForm.Meta):
        field = ["status", 'maintenance_date', "cost", "performed_by", "record_type"]

class InstrumentDeleteForm(InstrumentBaseForm):
    pass