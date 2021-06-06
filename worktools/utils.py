from datetime import datetime
from .models import WorkTool

def tools_form_validations(form, worktool, actual_tool = None):

    if not form.cleaned_data ['has_been_in_mainteance']:
        worktool.mainteance_date = None

    if not form.cleaned_data['has_tracker']:
        worktool.tracker_id =  None
    
    if actual_tool is not None:
        if actual_tool \
        and not form.cleaned_data ['is_in_maintain']:
            worktool.has_been_in_mainteance = True
            worktool.mainteance_date = datetime.now()
            
    return worktool
