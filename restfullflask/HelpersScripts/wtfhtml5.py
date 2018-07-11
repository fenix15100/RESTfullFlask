# -*- coding: UTF-8 -*-

"""
WTForms HTML5 Widgets
~~~~~~~~~~~~~~~~~~~~~
This modul adds HTML5 widgets to WTForms_.
It supports the new INPUT types for fields and also sets some of the
new INPUT attributes automatically (based on widget type and what kind of
validators are set for the field). Also automatically sets the *title*
attribute to *describtion*.

CREDITS :https://gist.github.com/brutus/4038383
"""

from wtforms import TextField as _TextField
from wtforms import IntegerField as _IntegerField
from wtforms import DecimalField as _DecimalField
from wtforms import FloatField as _FloatField
from wtforms import DateField as _DateField
from wtforms.widgets import Input as _Input
from wtforms.validators import Length, NumberRange, StopValidation
from wtforms.compat import string_types


# CUSTOM LOGIC

def get_html5_kwargs(field, kwargs):
    """
  Return *kwargs* for *field*.
  If the field got a *description* but no *title* is set, the *title*
  is set to *description*.
  Generate *kwargs* for the new HTML5 INPUT attributes (`required`, `min` and
  `max`) based on the validators set for *field*.
  Also set (or append) 'invalid' to the fields class, if the *field* got
  errors. 'invalid' is also set by browsers if they detect errors on a field.
  If a key is already in *kwargs* it is left untouched.
  """
    # got description?
    if not 'title' in kwargs and hasattr(field, 'description'):
        kwargs['title'] = u'{}'.format(field.description)
    # is field required?
    if not 'required' in kwargs and field.flags.required:
        kwargs['required'] = u'required'
    # check validators Length or NumberRange
    for vali in field.validators:
        if (
                isinstance(vali, Length) or
                isinstance(vali, NumberRange) or
                isinstance(vali, DateRange)
        ):
            if not 'min' in kwargs and hasattr(vali, 'min'):
                kwargs[u'min'] = vali.min
            if not 'max' in kwargs and hasattr(vali, 'max'):
                kwargs[u'max'] = vali.max
    # check for errors
    if field.errors:
        cls = kwargs.get('class', kwargs.get('class_', ''))
        if cls:
            kwargs[u'class'] = u'invalid {}'.format(cls)
        else:
            kwargs[u'class'] = u'invalid'
    return kwargs


# WIDGETS

class Input(_Input):
    """Base INPUT class. Subclass this."""

    def __call__(self, field, **kwargs):
        kwargs = get_html5_kwargs(field, kwargs)
        return _Input.__call__(self, field, **kwargs)


class TextInput(Input):
    """Creates `<input type=text>` widget with custom *kwargs* parsing."""
    input_type = "text"


class NumberInput(Input):
    """Creates `<input type=number>` widget with custom *kwargs* parsing."""
    input_type = "number"


class DateInput(Input):
    """Creates `<input type=date>` widget with custom *kwargs* parsing."""
    input_type = "date"


class RangeInput(NumberInput):
    """Creates `<input type=range>` widget with custom *kwargs* parsing."""
    input_type = "range"


class URLInput(Input):
    """Creates `<input type=url>` widget with custom *kwargs* parsing."""
    input_type = "url"


class EmailInput(Input):
    """Creates `<input type=email>` widget with custom *kwargs* parsing."""
    input_type = "email"


class SearchInput(Input):
    """Creates `<input type=search>` widget with custom *kwargs* parsing."""
    input_type = "search"


class TelInput(Input):
    """Creates `<input type=tel>` widget with custom *kwargs* parsing."""
    input_type = "tel"


class DecimalInput(NumberInput):
    """Creates `<input type=number>` widget with custom *kwargs* parsing.
  Also adds a *step size* of ``any`` to the field, if not other step
  size is set.
  """

    def __call__(self, field, **kwargs):
        if not u'step' in kwargs:
            kwargs[u'step'] = u'any'
        return NumberInput.__call__(self, field, **kwargs)


class DecimalRangeInput(DecimalInput):
    """Creates `<input type=range>` widget.
  Also adds a *step size* of ``any`` to the field, if not other step
  size is set.
  """
    input_type = "range"


# FIELDS

class TextField(_TextField):
    """**TextField** using **TextInput** by default """
    widget = TextInput()


class SearchField(TextField):
    """**TextField** using **SearchInput** by default """
    widget = SearchInput()


class URLField(TextField):
    """**TextField** using **URLInput** by default """
    widget = URLInput()


class EmailField(TextField):
    """**TextField** using **EmailInput** by default """
    widget = EmailInput()


class TelField(TextField):
    """**TextField** using **TelInput** by default """
    widget = TelInput()


class IntegerField(_IntegerField):
    """**IntegerField** using **NumberInput** by default """
    widget = NumberInput()


class DateField(_DateField):
    """**DateField** using **DateInput** by default """
    widget = DateInput()


class DecimalField(_DecimalField):
    """**DecimalField** using **DecimalInput** by default """
    widget = DecimalInput()


class FloatField(_FloatField):
    """**DecimalField** using **DecimalInput** by default """
    widget = DecimalInput()


class IntegerRangeField(_IntegerField):
    """**IntegerField** using **RangeInput** by default """
    widget = RangeInput()


class DecimalRangeField(_DecimalField):
    """**DecimalField** using **DecimalRangeInput** by default """
    widget = DecimalRangeInput()


class FloatRangeField(_FloatField):
    """**DecimalField** using **DecimalRangeInput** by default """
    widget = DecimalRangeInput()


# VALIDATORS

class DateRange(object):
    """
  Validate that a date is in the *min* and *max* range.
  *message* should be a tuple if you want two different error messages.
  """

    def __init__(self, min=None, max=None, message=None):
        try:
            self.err_min, self.err_max = message
        except TypeError:
            self.err_min = self.err_max = message
        if min:
            self.min = min
        if max:
            self.max = max

    def __call__(self, form, field):
        if self.min and field.data < self.min:
            if not self.err_min:
                self.err_min = field.gettext("Date must be >= {}.").format(self.min)
            field.errors.append(self.err_min)
        if self.max and field.data > self.max:
            if not self.err_max:
                self.err_max = field.gettext("Date must be >= {}.").format(self.max)
            field.errors.append(self.err_max)


class NotEmpty(object):
    """
  No validation, just set the *required* flag.
  Setting the *required* flag along with ``get_html5_kwargs`` prevents
  browsers from sending empty fields.
  """

    field_flags = ('required',)

    def __call__(self, form, field):
        pass


class NotEmptyCheck(object):
    """
  Validate that the field got **any** input.
  Setting the *required* flag along with ``get_html5_kwargs`` prevents
  browsers from sending empty fields.
  """

    field_flags = ('required',)

    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        # check if some data is entered in field
        if field.raw_data is None or (
                isinstance(field.data, string_types)
                and not field.data.strip()
        ):
            # get error message
            if self.message is None:
                self.message = field.gettext('This field is required.')
            # clear all errors for this field
            field.errors[:] = []
            # stop validation and raise this error
            raise StopValidation(self.message)
