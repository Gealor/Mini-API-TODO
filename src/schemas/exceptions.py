class BaseAppException(Exception):
    pass

# Tasks
class TasksBaseException(BaseAppException):
    pass


class TaskNotFoundException(TasksBaseException):
    pass


# InMemory Database
class DatabaseBaseException(BaseAppException):
    pass


class AddRecordException(DatabaseBaseException):
    pass

