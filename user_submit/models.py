from django.conf import settings
from django.db import models
from django.forms import ModelForm
from django.utils.encoding import smart_str
from geopy import geocoders
import datetime
import base64

# Create your models here.
class issue_detail(models.Model):
    issue_types = (
        ('Abandoned Bicycle', 'Abandoned Bicycle'),
        ('Abandoned Vehicle on Private Property', 'Abandoned Vehicle on Private Property'),
        ('Drinking Water Quality & Pressure', 'Drinking Water Quality & Pressure'),
        ('Bikeway Concerns', 'Bikeway Concerns'),
        ('Brush Collection', 'Brush Collection'),
        ('Consumer Complaint', 'Consumer Complaint'),
        ('Dead Animal Collection', 'Dead Animal Collection'),
        ('Erosion Control', 'Erosion Control'),
        ('Exterior Housing', 'Exterior Housing'),
        ('General requests', 'General requests'),
        ('Graffiti', 'Graffiti'),
        ('Interior Housing Problem(s)', 'Interior Housing Problem(s)'),
        ('Mailbox Damaged from a City Snow Plow', 'Mailbox Damaged from a City Snow Plow'),
        ('Metro Transit Feedback Form', 'Metro Transit Feedback Form'),
        ('Parking Enforcement', 'Parking Enforcement'),
        ('Pothole Concern', 'Pothole Concern'),
        ('Recycle Collection', 'Recycle Collection'),
        ('Refuse Collection', 'Refuse Collection'),
        ('Refuse & Recycling Carts', 'Refuse & Recycling Carts'),
        ('Sewer Access Covers (Man Hole Covers)', 'Sewer Access Covers (Man Hole Covers)'),
        ('Sidewalk Concern', 'Sidewalk Concern'),
        ('Sign (Zoning) Violation', 'Sign (Zoning) Violation'),
        ('Snow Removal', 'Snow Removal'),
        ('Traffic Enforcement', 'Traffic Enforcement'),
        ('Traffic Signals, Street Lights and Signs Requests', 'Traffic Signals, Street Lights and Signs Requests'),
        ('Tree Concerns', 'Tree Concerns'),
        ('Weeds and Overgrown Vegetation', 'Weeds and Overgrown Vegetation'),
    )

    user_first_name = models.CharField(max_length=1024, db_index=True, null=True, blank=True)
    user_last_name = models.CharField(max_length=1024, db_index=True, null=True, blank=True)
    user_address = models.CharField(max_length=1024, db_index=True, null=True, blank=True)
    computed_address = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    geocode_error = models.BooleanField(default=False)
    user_phone = models.CharField(max_length=1024, db_index=True, null=True, blank=True)
    user_email = models.CharField(max_length=1024, db_index=True, null=True, blank=True)
    user_submitted_photo = models.ImageField(upload_to = 'tmp', null=True, blank=True)
    user_date_submitted = models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)
    user_request_type = models.CharField(max_length=1024, db_index=True, null=True, blank=True, choices=issue_types)
    user_message = models.TextField(db_index=True, null=True, blank=True)
    user_contact_you = models.NullBooleanField(default=True, db_index=True, null=True, blank=True)

    class Meta:
        ordering = ["-user_date_submitted"]

    # this taken from easy_maps base code for geocoding
    def fill_geocode_data(self):
        if not self.user_address:
            self.geocode_error = True
            return
        try:
            if hasattr(settings, "EASY_MAPS_GOOGLE_KEY") and settings.EASY_MAPS_GOOGLE_KEY:
                g = geocoders.Google(settings.EASY_MAPS_GOOGLE_KEY)
            else:
                g = geocoders.Google(resource='maps')
            address = smart_str(self.user_address)
            self.computed_address, (self.latitude, self.longitude,) = g.geocode(address)
            self.geocode_error = False
        except (UnboundLocalError, ValueError,geocoders.google.GQueryError):
            self.geocode_error = True

    def save(self, *args, **kwargs):
        # fill geocode data if it is unknown
        if (self.longitude is None) or (self.latitude is None):
            self.fill_geocode_data()
        super(issue_detail, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user_first_name

class issue_form(ModelForm):
    """
    Auto generated form to create Server models.
    """
    class Meta:
        model = issue_detail
        exclude = ('computed_address', 'latitude', 'longitude', 'geocode_error', 'user_date_submitted',)