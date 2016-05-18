
# This is how you query a action
# The target_object_id can be whatever object
Action.objects.filter(target_object_id=9240, verb__icontains='received an email')

# Read the Dam docs https://django-activity-stream.readthedocs.io/en/latest/

