from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
   default_limit = 6
   limit_query_param = 'l'
   offset_query_param = 'off'
   max_limit = 8