import json


def build_prompt(profile):

    return f"""
You are a data quality expert.

Analyze the dataset profile below and identify data quality issues.

Dataset profile:
{json.dumps(profile, indent=2)}

Tasks:
1. Identify data quality issues
2. Explain why they are problematic
3. Suggest cleaning actions

Focus on:
- missing values
- logical errors
- inconsistent categories
- duplicates

Provide a clear and structured answer.
"""
