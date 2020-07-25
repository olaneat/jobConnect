from rest_framework.exceptions import APIException

class ProfileDoesNotExit(APIException):
	status = 400
	default_detail = ' user profile does not exist'