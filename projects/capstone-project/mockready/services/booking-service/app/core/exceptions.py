"""
core/exceptions.py

Booking Service Custom Exceptions
Raised inside service layer.
Routers or global handlers convert them
into proper API responses.
"""


class MockReadyException(Exception):
    def __init__(self, message: str, code: str = "ERROR"):
        self.message = message
        self.code = code
        super().__init__(message)

class BookingAlreadyExistsException(MockReadyException):
    def __init__(self):
        super().__init__(
            message="Booking already exists",
            code="BOOKING_ALREADY_EXISTS"
        )


class BookingNotFoundException(MockReadyException):
    def __init__(self):
        super().__init__(
            message="Booking not found",
            code="BOOKING_NOT_FOUND"
        )


class SlotAlreadyBookedException(MockReadyException):
    def __init__(self):
        super().__init__(
            message="Selected slot is already booked",
            code="SLOT_ALREADY_BOOKED"
        )


class TrainerUnavailableException(MockReadyException):
    def __init__(self):
        super().__init__(
            message="Trainer is unavailable for selected slot",
            code="TRAINER_UNAVAILABLE"
        )


class InvalidBookingStatusException(MockReadyException):
    def __init__(self):
        super().__init__(
            message="Invalid booking status",
            code="INVALID_BOOKING_STATUS"
        )


class BookingCancellationException(MockReadyException):
    def __init__(self):
        super().__init__(
            message="Booking cannot be cancelled",
            code="BOOKING_CANCELLATION_FAILED"
        )