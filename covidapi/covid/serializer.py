from rest_framework import serializers


class estimatorData(serializers.Serializer):

    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    avgAge = serializers.FloatField(max_value=None, min_value=None, required=True)
    avgDailyIncomeInUSD = serializers.FloatField(max_value=None, min_value=None, required=True)
    avgDailyIncomePopulation = serializers.FloatField(max_value=None, min_value=None, required=True)
    periodType = serializers.CharField(required=True, allow_blank=False, max_length=100)
    timeToElapse = serializers.IntegerField(max_value=None, min_value=None, required=True)
    reportedCases = serializers.IntegerField(max_value=None, min_value=None, required=True)
    population = serializers.IntegerField(max_value=None, min_value=None, required=True)
    totalHospitalBeds = serializers.IntegerField(max_value=None, min_value=None, required=True)
