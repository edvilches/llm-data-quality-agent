import json

def build_prompt(profile):

    prompt = f"""
You are a data quality expert.

Analyze the dataset profile below and identify data quality issues.

Dataset profile:
{json.dumps(profile, indent=2)}

Identify:
- missing values
- logical errors
- inconsistent categories
- duplicates

Provide a list of detected problems and suggested fixes.
"""

    return prompt
