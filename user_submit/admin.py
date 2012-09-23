from user_submit.models import issue_detail
from django.contrib import admin

class issue_detailAdmin(admin.ModelAdmin):

	list_display = ('user_date_submitted', 'user_request_type', 'user_last_name', 'computed_address', 'geocode_error', 'user_phone', 'user_email', 'user_contact_you')

    	fieldsets = [
    	   ('First Name', {'fields': ['user_first_name']}),
    	   ('Last Name', {'fields': ['user_last_name']}),
    	   ('Address', {'fields': ['user_address']}),
    	   ('Computed Address', {'fields': ['computed_address']}),
    	   ('Lat', {'fields': ['latitude']}),
    	   ('Long', {'fields': ['longitude']}),
    	   ('Error', {'fields': ['geocode_error']}),
    	   ('Phone', {'fields': ['user_phone']}),
    	   ('Email', {'fields': ['user_email']}),
    	   ('Date Submitted', {'fields': ['user_date_submitted']}),
    	   ('Request Type', {'fields': ['user_request_type']}),
    	   ('Issue Details', {'fields': ['user_message']}),
    	   ('Image', {'fields': ['user_submitted_photo']}),
    	   ('Should we contact', {'fields': ['user_contact_you']}),
		]

admin.site.register(issue_detail, issue_detailAdmin)