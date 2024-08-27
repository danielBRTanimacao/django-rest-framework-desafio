from django.core.exceptions import ValidationError

def validate_list(item_to_validate: list) -> ValidationError:
    if len(item_to_validate) > 4:
        raise ValidationError("A lista não pode ter mais de 4 valores")
    elif len(item_to_validate) < 4:
        raise ValidationError("A lista não pode ter menos de 4 valores")
    
def sum_return_note_semester(notes: list[float]) -> float:
    validate_list(notes)
    return sum(notes) / 4

print(sum_return_note_semester([10, 10, 10, 10]))