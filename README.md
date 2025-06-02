# ML-Unsupervised--MH-in-Workplace
Project Overview
This project analyzes survey data from technology employees to assess whether workplace-related questions can predict mental health perception scores. Using linear regression, we evaluated the predictive power of survey responses while accounting for data quality and relevance. The results provide insights into the effectiveness of current survey questions for measuring mental health perceptions in tech workplaces.

Key Findings

    Mean Absolute Error (MAE): 11.47

        Scores range from -36 (very negative) to +36 (very positive)

        The error represents ~1/6th of the total range, making predictions unreliable

        Half of employees score between -10 and 10, meaning the error could misclassify perceptions (e.g., predicting positive instead of negative)

    Survey Limitations

        Current questions do not strongly predict mental health perception scores

        Refinements needed:

            More precise questions

            Better-balanced response options

            Additional factors beyond the survey

Methodology
Data Preparation

    Removed:

        Company-specific questions (to focus on individual experiences)

        Columns used to derive the perception score (avoiding bias)

        Heavily skewed or incomplete questions

    Processed:

        Dummy-encoded categorical variables

        Filled missing values

Modeling

    Algorithm: Linear Regression

    Evaluation Metric: Mean Absolute Error (MAE)
