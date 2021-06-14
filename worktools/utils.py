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

def remove_tools_by_id_list(actual_tools_id, new_tools_id):

    if len(actual_tools_id) == len(new_tools_id):
        return [] # No changes detected

    if len(actual_tools_id) < len(new_tools_id):
        return Exception('Not possible')

    if len(actual_tools_id) > len(new_tools_id): # Excepected case
        removed_tools_id = []
        for current_tool_id in actual_tools_id:
            if current_tool_id not in new_tools_id:
                removed_tools_id.append(current_tool_id)
        return removed_tools_id
