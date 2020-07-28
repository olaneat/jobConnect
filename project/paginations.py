from rest_framework.pagination import LimitOffsetPagination


class CustomizedPagination(LimitOffsetPagination):
	max_limit  = 20
