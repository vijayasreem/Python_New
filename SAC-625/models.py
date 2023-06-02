from django.db import models

class BajajAllianzGroupSampoornaJeevanSurakshaPolicy(models.Model):
    # Minimum and maximum sum assured
    min_sum_assured = models.IntegerField()
    max_sum_assured = models.IntegerField()

    # Minimum and maximum age limits
    min_age_limit = models.IntegerField()
    max_age_limit = models.IntegerField()

    # Annual income of the member
    annual_income = models.IntegerField()

    # Sum assured ranges
    sum_assured_50k = models.BooleanField(default=False)
    sum_assured_1lac = models.BooleanField(default=False)
    sum_assured_1_5lac = models.BooleanField(default=False)
    sum_assured_2lac = models.BooleanField(default=False)

    # Policy tenure ranges
    policy_tenure_12m = models.BooleanField(default=False)
    policy_tenure_15m = models.BooleanField(default=False)
    policy_tenure_18m = models.BooleanField(default=False)
    policy_tenure_24m = models.BooleanField(default=False)

    # Spouse eligibility
    spouse_eligibility = models.BooleanField(default=False)

    # OTP authentication
    otp_authentication = models.BooleanField(default=False)