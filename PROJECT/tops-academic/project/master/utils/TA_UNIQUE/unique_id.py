import uuid

def generate_uniq_id(instance):
    unique_id = f"{(uuid.uuid4())}_{instance.SUFFIX_WORD}"

    return unique_id